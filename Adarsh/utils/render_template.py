from Adarsh.vars import Var
from Adarsh.bot import StreamBot
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.file_properties import get_file_ids
from Adarsh.server.exceptions import InvalidHash
import urllib.parse
import aiofiles
import logging
import aiohttp


async def render_page(id, secure_hash):
    file_data = await get_file_ids(StreamBot, int(Var.BIN_CHANNEL), int(id))
    if file_data.unique_id[:6] != secure_hash:
        logging.debug(f'link hash: {secure_hash} - {file_data.unique_id[:6]}')
        logging.debug(f"Invalid hash for message with - ID {id}")
        raise InvalidHash
    src = urllib.parse.urljoin(Var.URL, f'{secure_hash}{str(id)}')
    
    if str(file_data.mime_type.split('/')[0].strip()) == 'video':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Watch {}'.format(file_data.file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)
    elif str(file_data.mime_type.split('/')[0].strip()) == 'audio':
        async with aiofiles.open('Adarsh/template/req.html') as r:
            heading = 'Listen {}'.format(file_data.file_name)
            tag = file_data.mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_data.file_name, src)
    else:
        async with aiofiles.open('Adarsh/template/dl.html') as r:
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u:
                    heading = 'Download {}'.format(file_data.file_name)
                    file_size = humanbytes(int(u.headers.get('Content-Length')))
                    html = (await r.read()) % (heading, file_data.file_name, src, file_size)
    current_url = f'{Var.URL}/{str(id)}/{file_data.file_name}?hash={secure_hash}'
    html_code = f'''
   <p>
    <center><h5>Click on 👇 button to watch/download in your favorite player</h5></center>
    <center>
        <button style="font-size: 20px; background-color: skyblue; border-radius: 10px;" onclick="window.location.href = 'intent:{current_url}#Intent;package=com.mxtech.videoplayer.ad;S.title={file_data.file_name};end'">MX player</button> &nbsp
        <button style="font-size: 20px; background-color: orange; border-radius: 10px;" onclick="window.location.href = 'vlc://{current_url}'">VLC player</button> &nbsp <br>
        <p>&nbsp</p>
        <button style="font-size: 20px; background-color: red; border-radius: 10px;" onclick="window.location.href = 'playit://playerv2/video?url={current_url}&amp;title={file_data.file_name}'">Playit player</button> &nbsp <br>
        <p>&nbsp</p>
        <button style="font-size: 20px; background-color: yellow; border-radius: 10px;" onclick="window.location.href = '{current_url}'">Save in your gallery</button> &nbsp
    </center>
</p>
</p>
<center>
    <h2>
        <a href="https://telegram.me/BotszList">
            <img src="https://graph.org/file/b57cdba982191a25db535.jpg" alt="BotszList" width="150" height="75">
        </a>
    </h2>
</center>

'''

    html += html_code    
    return html
