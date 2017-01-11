from __future__ import print_function
import pyexcel
from webfns import get_credentials
from oauth2client import tools
import httplib2
from apiclient import discovery

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
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
      print('Labels:')
      for label in labels:
        print(label['name'])




def outputmain():
    import pandas as pd
    spreadsheet = pd.read_csv(csv_file)

    balance = get_balance(spreadsheet)
    percentages = get_percentages(spreadsheet)

    send_email(balance,percentages)


def send_email(x,y):

def get_balance(spreadsheet):

    grouped = spreadsheet.groupby([])

    return balance

def get_percentages(spreadsheet):

    grouped = spreadsheet.groupby(["Food","Entertainment","Travel","Clothing","Rent","Income","Housing","Miscellaneous"])

    return spreadsheet

if __name__ == '__main__':
    main()
