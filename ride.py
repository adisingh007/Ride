#!/usr/bin/python

import json
import requests


# Loading drop details
drop_details = json.load(open('drop-details.json'))

# Getting the session ID
index_page = "http://drops/index.php"
index_page_response = requests.get(index_page)
cookies = index_page_response.headers['Set-Cookie'].split(';')  # Getting the session ID
session_id = ""
for cookie in cookies:
    if cookie.startswith('PHPSESSID'):
        session_id = cookie
        break

if session_id != "":
    # Creating a header dictionary that will be used throughout the app.
    headers = {
        'Cookie': session_id
    }

    # Logging in
    login_page = "http://drops/login.php"
    login_params = {
        'src': drop_details['src'],  # 1: Mumbai-Plex, 2: Mumbai-Seepz
        'uname': drop_details['uname'],
        'pwd': drop_details['pwd']
    }
    login_response = requests.post(login_page, data=login_params, headers=headers)

    if login_response.text == '1':  # Successful login
        # Getting the home page
        home_page = "http://drops/home.php"
        home_page_response = requests.get(home_page, headers=headers)

        # Get location ID
        location_url = "http://172.16.185.58:5001/locations?filter=enabled"
        locations = requests.get(location_url, headers=headers)
        locations_text = json.loads(locations.text)
        my_location_id = -1
        for location in locations_text['message']:
            if location['location'] == drop_details['location']:
                my_location_id = location['id']
                break

        # Get timings list
        timings_url = "http://172.16.185.58:5001/time?filter=available&sid=" + str(drop_details['src'])
        timings = requests.get(timings_url, headers=headers)
        timings_text = json.loads(timings.text)
        tid = -1
        epoch = -1
        timestamp = ''
        for timing in timings_text['message']:
            if timing['timestamp'].endswith(drop_details['time']):
                tid = timing['tid']
                epoch = timing['epoch']
                timestamp = timing['timestamp']
                break

        # Book drop finally
        booking_url = "http://drops/setdrop.php"
        booking_params = {
            'lid': my_location_id,
            'tid': tid,
            'epoch': epoch,
            'sid': drop_details['src']
        }
        booking_response = requests.post(booking_url, data=booking_params, headers=headers)
        if booking_response.text == '1':
            print(drop_details['booking_success_text'])
        else:
            print(drop_details['booking_error_text'].replace('%base_url%', drop_details['base_url']))
    else:
        print(drop_details['could_not_log_in_text'])
else:
    print(drop_details['session_not_initialized_text'])
