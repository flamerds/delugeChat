from modules import deluge

delugeObj = deluge.deluge()


version_number = delugeObj.send_request('webapi.get_api_version')
assert version_number

print('WebAPI version: %s' % version_number)


print(delugeObj.send_request('web.update_ui', [["label"], {"label":"tv-sonarr"}]))
#fileSave("torrentsList.txt",delugeObj.send_request('web.update_ui', [["label"], {}]))


#[["tracker", "label"], {}]

version_number = delugeObj.send_request('webapi.get_torrents')
assert version_number

#print('WebAPI version: %s' % version_number)



print('Success')