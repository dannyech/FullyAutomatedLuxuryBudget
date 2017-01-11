from __future__ import print_function
import pyexcel
import pyexcel_io
from pyexcel_io import get_data
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
CSV_FILE = None

def main():
    global CSV_FILE
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    CSV_FILE = sys.argv[1]


def process_email(message)
    global CSV_FILE
    data = pyexcel_io.get_data(CSV_FILE)
    if "," not in message:
        return
    split = message.split(",")
    split[:len(split)-1] = [item.lower() for item in split[:len(split)-1]]
    if len(split)==3:
        if "c:" in split[0] and "s:" in split[1]:
            try:
                first = int(split[0].split("c:")[0])
                second = int(split[1].split("s:")[1])
            except ValueError:
                return

        elif "s:" in split[0] and "c:" in split[1]:

    elif len(split)==2:
        if "c:" in split[:0]:

        elif "s:" in split[:0]

        else:

    else:
        return







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
