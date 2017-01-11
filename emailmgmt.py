from __future__ import print_function
import pyexcel
from webfns import get_credentials
from oauth2client import tools
import httplib2
from apiclient import discovery, errors

NEW_MESSAGES = 'is:unread' 

def get_messages(service, user_id):
    messages = get_newest_messages(service, user_id)
    message_texts = []
    for message in messages:
        message_texts.append(get_message_text(service, user_id, message['id']))
        mark_message_old(service, user_id, message['id'])

    return message_texts

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

def mark_message_old(service, user_id, message_id):
    try:
        service.users().messages().modify(userId=user_id, id=message_id, 
            body={ 'removeLabelIds': ['UNREAD']}).execute()
    except errors.HttpError, error:
        print('An error occurred: %s' % error)

def get_message_text(service, user_id, message_id):
  try:
    message = service.users().messages().get(userId=user_id, 
        id=message_id).execute()
    text = message['snippet']
    return text
  except errors.HttpError, error:
    print('An error occurred: %s' % error)

