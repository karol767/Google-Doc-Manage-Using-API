import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/cake/Downloads/snappy-byte-429200-k4-e80a0e97bc19.json'

# Create credentials
credentials = service_account.Credentials.from_service_account_file(
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=['https://www.googleapis.com/auth/documents']
)

# Create a Google Docs API client instance
docs_service = build('docs', 'v1', credentials=credentials)

# Create a new document
# Create a new document
document = {
    'title': 'Example Document',
    'body': {
        'content': [{
            'paragraph': {
                'elements': [{
                    'textRun': {
                        'content': 'Hello, world!'
                    }
                }]
            }
        }]
    }
}
response = docs_service.documents().create(body=document).execute()
print(response.get('documentId'))


# Update an existing document
document_id = response.get('documentId')
document = docs_service.documents().get(documentId=document_id).execute()

document_id = '1aeNsn06ZdzgUcIpVCP3K4OPSY9gH6pbmJOMs-7roGsg'
document = docs_service.documents().get(documentId=document_id).execute()

# This will give you the full document content
print(document)

# If you want to print just the body content
print(document.get('body'))

# update_request = {
#     'requests': [
#         {
#             'insertText': {
#                 'location': {
#                     'index': 1,
#                 },
#                 'text': 'Your new text here'
#             }
#         }
#     ]
# }

# update_response = docs_service.documents().batchUpdate(
#     documentId=document_id,
#     body=update_request
# ).execute()


# # Read a document
# document_id = document_id
# response = docs_service.documents().get(documentId=document_id).execute()
# print(response.get('body'))
