from __future__ import print_function
import pyexcel
import pyexcel_io
from pyexcel_io import get_data
from webfns import get_credentials
from oauth2client import tools
import httplib2
from apiclient import discovery, errors
from emailmgmt import get_messages

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

CSV_FILE = None
USER_ID = 'me'

def main():
    global CSV_FILE
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    CSV_FILE = sys.argv[1]    
    
def process_email(message):
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

if __name__ == '__main__':
    main()