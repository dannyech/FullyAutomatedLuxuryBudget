from __future__ import print_function
import pyexcel
from webfns import get_credentials
from oauth2client import tools
import httplib2
from apiclient import discovery, errors
import emailmgmt

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'FullyAutomatedLuxuryBudget'

def main():
    credentials = get_credentials()
    user_info = get_user_info(credentials)
    user_id = user_info.get('id')
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    messages = get_newest_messages(service, user_id)
    print(messages)

if __name__ == '__main__':
    main()