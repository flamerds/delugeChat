from modules import deluge
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

    # 

   


    print('Success')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())