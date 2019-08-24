from googleapiclient.discovery import build, MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools
import requests



def text_to_docs_upload(output_text):
    try :
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()

    if not creds or creds.invalid:
        print("make new storage data file ")
        flow = client.flow_from_clientsecrets('client_secret_drive.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)

    DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

    FILES = (
        (output_text),
    )

    for file_title in FILES :
        media = MediaFileUpload(file_title,
                                mimetype="application/vnd.google-apps.document")
        metadata = {'name': file_title,
                    'mimeType': "application/vnd.google-apps.document"
                    }
        print(metadata)
        res = DRIVE.files().create(body=metadata, media_body=media, fields = 'id').execute()
        print(res)
        URL = 'https://www.googleapis.com/drive/v3/files/'+ str(res.get('id')) +'/permissions?key=[your_google_api_key_here]'
        data = {'role': 'reader', 'type': 'anyone'}
        response = requests.post(URL, data=data)
        print(response)


        print(res)

        if res:
            print('Uploaded "%s" (%s)' % (file_title, res.get('id')))
    doc_url = "https://docs.google.com/document/d/"+ str(res.get('id'))
    return doc_url

text_to_docs_upload("output.txt")
