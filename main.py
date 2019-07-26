from modules import deluge
import base64
import asyncio

async def test():
    delugeObj = deluge.deluge()

    #version_number = await delugeObj.send_request_async('webapi.get_api_version')

    version_number = await delugeObj.send_request_async('web.get_hosts')
    assert version_number

    print('WebAPI version: %s' % version_number)

    hostId = version_number[0][0]

    version_number = await delugeObj.send_request_async('web.connect',[hostId])

    await asyncio.sleep(10)
    version_number = await delugeObj.send_request_async('web.connected')
    assert version_number

    print('WebAPI version: %s' % version_number)

    #print(await delugeObj.send_request_async('web.update_ui', [["label"], {"label":"tv-sonarr"}]))
    #fileSave("torrentsList.txt",delugeObj.send_request('web.update_ui', [["label"], {}]))


    #[["tracker", "label"], {}]

    # version_number = await delugeObj.send_request_async('webapi.get_torrents')
    # assert version_number

    #"core.add_torrent_magnet"

    # version_number = await delugeObj.send_request_async('core.add_torrent_magnet', ["magnet:?xt=urn:btih:d344c074850d158f501b012a9018e98fe97a23be&dn=archlinux-2019.07.01-x86_64.iso&tr=udp://tracker.archlinux.org:6969&tr=http://tracker.archlinux.org:6969/announce",{"add_paused":False,"remove_at_ratio":False}])

    # print('WebAPI version: %s' % version_number)

    data = base64.b64encode(open('archlinux.torrent','rb').read()).decode('utf-8')

    print(type(data))

    version_number = await delugeObj.send_request_async('core.add_torrent_file', ["archlinux.torrent",data,{"add_paused":False,"remove_at_ratio":False}])

    print('WebAPI version: %s' % version_number)


    print('Success')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())