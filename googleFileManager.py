from apiclient.http import MediaFileUpload
from googleAuth import get_creds
from apiclient.discovery import build


class GoogleFileManager():
    def __init__(self):
        self.service = build('drive', 'v3', credentials=get_creds())
    
    def list_files_in(self, id):
        # 17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy => ApuntesDriveBot
        #folders = path.split("/")
        #folders = [] if not folders else folders
        current_folder_id = '"17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy"'
        
        #for folder in folders:
        #    current_folder_id = self.get_file_id(current_folder_id, folder)
        #print("hola")
        files = []
        results = self.service.files().list(q='"'+id+'" in parents and trashed = false').execute()
        items = results.get('files', [])
        #print(items)
        
        if items:
            #print('Files:')
            for item in items:
                # print(u'{0} ({1})'.format(item['name'], item['id']))
                print(item)
                files.append({'name':item['name'],
                              'id':item['id'],
                              'type':'folder' if item['mimeType'] == "application/vnd.google-apps.folder" else 'file'})
            return files
        return files

    def get_file_id(self, parent_id, folder_name):
        results = self.service.files().list(q=parent_id+' in parents and trashed = false').execute()
        items = results.get('files', [])
        for item in items:
            if item['name'] == folder_name:
                return '"{}"'.format(item['id'])

    def upload_file(self, file_name, file_paht, mime_type):

        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_paht, mime_type)
        file = self.service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
        print("File ID: " + file.get('id'))
