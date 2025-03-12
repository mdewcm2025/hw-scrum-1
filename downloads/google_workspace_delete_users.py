import csv
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Setup API client with service account
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']
SERVICE_ACCOUNT_FILE = 'path_to_your_service_account_credentials.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('admin', 'directory_v1', credentials=credentials)

# Open the CSV file
with open('users_to_delete.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        email = row[0]
        try:
            # Delete the user by email
            service.users().delete(userKey=email).execute()
            print(f"Deleted user: {email}")
        except Exception as e:
            print(f"Error deleting user {email}: {e}")

'''
users_to_delete.csv

user1@example.com
user2@example.com
user3@example.com

'''