# This script takes input from a list of email addresses
# It then makes an http request for the google calendar associated with the address
# If status code 200 is returned, then the email address is at least partially public
# and should be investigated. The address to the calendar is provided to assist investigation.
# If 404 is returned, the calendar is not public.
# All addresses with a 200 code are saved to a text file.

import requests

directory = open('directory.txt')
public_calendars_file = open("public_calendars.txt", "w")
public_calendars_list = []

for address in directory:
    r = requests.get('https://calendar.google.com/calendar/u/0/htmlembed?src=' + address.strip())

    if r.status_code == 200:
        print(address + " is public")
        public_calendars_file.write(address)
        public_calendars_file.write('https://calendar.google.com/calendar/u/0/htmlembed?src=' + address + '\n')
