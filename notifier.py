# -*- coding: utf-8 -*-
import http.client
import sys
import urllib

from enums.emoji import Emoji
def push_notification(notification_msg):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": "TOKEN",
                     "user": "USER",
                     "message": notification_msg,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()

def main(stdin):
    available_site_strings = generate_availability_strings(stdin)

    if available_site_strings:
        tweet = generate_notification_str(available_site_strings)
        push_notification(tweet)
        sys.exit(0)
    else:
        print("No campsites available, not tweeting 😞")
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
        if Emoji.SUCCESS.value in line:
            park_name_and_id = " ".join(line.split(":")[0].split(" ")[1:])
            num_available = line.split(":")[1][1].split(" ")[0]
            s = "{} site(s) available in {}".format(
                num_available, park_name_and_id
            )
            available_site_strings.append(s)
    return available_site_strings


if __name__ == "__main__":
    main(sys.stdin)
