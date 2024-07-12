import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/cake/Downloads/snappy-byte-429200-k4-e80a0e97bc19.json'

# Create credentials
credentials = service_account.Credentials.from_service_account_file(
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=[
        'https://www.googleapis.com/auth/documents',
        'https://www.googleapis.com/auth/drive.file'
    ]
)

# Create a Google Docs API client instance
docs_service = build('docs', 'v1', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)

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

update_request = {
    'requests': [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': 'Your new text here'
            }
        }
    ]
}

update_response = docs_service.documents().batchUpdate(
    documentId=document_id,
    body=update_request
).execute()


# Read a document
document_id = document_id
response = docs_service.documents().get(documentId=document_id).execute()
print(response.get('body'))

def share_document(document_id, email):
    permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': email
    }
    drive_service.permissions().create(
        fileId=document_id,
        body=permission,
        fields='id'
    ).execute()

# Use the function
share_document(document_id, 'codeforupwork@gmail.com')