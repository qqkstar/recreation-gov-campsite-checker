# -*- coding: utf-8 -*-
import http.client
import sys
import urllib
import json
import datetime

from enums.emoji import Emoji

def push_notification(notification_msg):
    pushover_creds = load_credentials('pushover_creds.json')
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": pushover_creds['token'],
                     "user": pushover_creds['user_key'],
                     "message": notification_msg,
                     "priority": 1,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()

def main(stdin):
    available_site_strings = generate_availability_strings(stdin)
    current_time = datetime.datetime.now()

    if available_site_strings:
        tweet = generate_notification_str(available_site_strings)
        push_notification(tweet)
        custom_string = "Pushed notification at time:"
        # Print the custom string followed by the formatted current time
        print(f"{custom_string} {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        sys.exit(0)
    else:
        custom_string = "Could not find available sites at time:"
        # Print the custom string followed by the formatted current time
        print(f"{custom_string} {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        sys.exit(1)


def generate_notification_str(available_site_strings):
    tweet = "Hurry up!!! "
    tweet += " 🏕🏕🏕\n"
    tweet += "\n".join(available_site_strings)
    tweet += "\n" + "🏕"
    return tweet


def generate_availability_strings(stdin):
    available_site_strings = []
    for line in stdin:
        line = line.strip()
        print(line)
        if Emoji.SUCCESS.value in line:
            park_name_and_id = " ".join(line.split(":")[0].split(" ")[1:])
            num_available = line.split(":")[1][1].split(" ")[0]
            s = "{} site(s) available in {}".format(
                num_available, park_name_and_id
            )
            available_site_strings.append(s)
    return available_site_strings

def load_credentials(filename):
    with open(filename, 'r') as file:
        credentials = json.load(file)
    return credentials

if __name__ == "__main__":
    main(sys.stdin)
