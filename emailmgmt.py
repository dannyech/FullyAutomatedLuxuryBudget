from __future__ import print_function
import pyexcel
from webfns import get_credentials
from oauth2client import tools
import httplib2
from apiclient import discovery, errors

NEW_MESSAGES = 'is:unread' 

def get_newest_messages(service, user_id):
    try:
        response = service.users().messages().list(userId=user_id, 
            q=NEW_MESSAGES).execute()

        if 'messages' in response:
            messages = response['messages']
            while 'nextPageToken' in response:
                page_toke = response['nextPageToken']
                response = service.users().messages().list(userId=user_id, 
                    q=NEW_MESSAGES, pageToken=page_token).execute()
                messages.extend(response['messages'])
        else:
            messages = []

        return messages
    except errors.HttpError, error:
        print('An error occurred: %s' % error)
