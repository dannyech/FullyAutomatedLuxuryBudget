from __future__ import print_function
import pyexcel
import pyexcel_io
from pyexcel_io import get_data
from webfns import get_credentials
from oauth2client import tools
import httplib2

import time
from apiclient import discovery
import sys
from emailmgmt import get_messages

CSV_FILE = None
USER_ID = 'me'

def main():
    global CSV_FILE
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    CSV_FILE = sys.argv[1]

    for message in get_messages(service, USER_ID):
        process_email(message.decode("utf8"))
    
def process_email(message):
    global CSV_FILE
    print(type(message))
    data = pyexcel_io.get_data(CSV_FILE)
    print(data)
    if len(data[0])!=6:
        print("Invalid file!")
        #Prompt for new
        #data = newFile()
        return
    try:
        [int(item) for item in data[len(data)-1][1:5]]
    except ValueError:
        print("Invalid file!2")
        #Prompt for new
        #data = newFile()
        return
    if "," not in message:
        return
    split = message.split(",")
    split[:len(split)-1] = [item.lower() for item in split[:len(split)-1]]
    curdate = time.strftime("%d/%m/%Y")
    init_checking = int(data[len(data)-1][1])
    init_savings = int(data[len(data)-1][2]) 
    init_total = init_checking+init_savings
    if len(split)==3:
        if "c:" in split[0] and "s:" in split[1]:
            break1 = "c:"
            break2 = "s:"
        elif "s:" in split[0] and "c:" in split[1]:
            break1 = "s:"
            break2 = "c:"
        else:
            return
        try:
            first = int(split[0].split(break1)[1])
            second = int(split[1].split(break2)[1])
            note = str(split[2])
        except ValueError:
            return
        change = first+second
    elif len(split)==2:
        try:
            if "s:" in split[0]:
                second = int(split[0].split("s:")[1])
                first = 0
            elif "c:" in split[0]:
                first = int(split[0].split("c:")[1])
                second = 0
            else: 
                first = int(split[0])
                second = 0
            note = str(split[1])
        except ValueError:
            return
        change = first+second
    else:
        return

    data.append([curdate, str(first+init_checking), str(second+init_savings),str(change+init_total),str(first+second),note])
    pyexcel_io.save_data(CSV_FILE,data)

if __name__ == '__main__':
    main()