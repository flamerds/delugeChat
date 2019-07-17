from modules import deluge
import asyncio

async def test():
    delugeObj = deluge.deluge()


    version_number = await delugeObj.send_request_async('webapi.get_api_version')
    assert version_number

    print('WebAPI version: %s' % version_number)


    print(await delugeObj.send_request_async('web.update_ui', [["label"], {"label":"tv-sonarr"}]))
    #fileSave("torrentsList.txt",delugeObj.send_request('web.update_ui', [["label"], {}]))


    #[["tracker", "label"], {}]

    version_number = await delugeObj.send_request_async('webapi.get_torrents')
    assert version_number

    #print('WebAPI version: %s' % version_number)



    print('Success')

loop = asyncio.get_event_loop()
loop.run_until_complete(test())