from apiclient.http import MediaFileUpload
from googleAuth import get_creds
from apiclient.discovery import build


class GoogleFileManager():
    def __init__(self):
        self.service = build('drive', 'v3', credentials=get_creds())
    
    def list_files(self):
        # 17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy => ApuntesDriveBot
        results = self.service.files().list(q='"17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy" in parents and trashed = false').execute()
        items = results.get('files', [])
        files = []

        if not items:
            #print('No files found.')
            # TODO: dry this
            return file_names
        else:
            #print('Files:')
            for item in items:
                # print(u'{0} ({1})'.format(item['name'], item['id']))
                print(item)
                files.append({'name':item['name'], 'id':item['id']})
            return files


    def upload_file(self, file_name, file_paht, mime_type):

        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_paht, mime_type)
        file = self.service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
        print("File ID: " + file.get('id'))
