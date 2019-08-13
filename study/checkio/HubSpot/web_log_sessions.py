#!/usr/bin/env checkio --domain=py run web-log-sessions

# https://py.checkio.org/mission/web-log-sessions/

# pre {        border: solid #696969 1px;        background-color: white;        padding: 2px;        font-family: Consolas, 'Bitstream Vera Sans Mono', 'Courier New', Courier, monospace;        overflow: auto;    }For this task, we have logs from various web sites. These logs contain information about user http and https requests.    To analyse this data we need to parse and collect the information contained in these logs.
#
# A log file is a text file, where each request is represented as a string.    The strings are separated by a newline "\n".    Requests contain a timestamp, username and URL.    These fields are separated by";;".
# Timestamps are represented in the following format:
# YYYY-MM-DD-hh-mm-ss, where YYYY-MM-DD is the date, hh-mm-ss is the time.
# Usernames contain only letters, digits and an underscore.
# A URL is given in the normalized form (for example: http://checkio.org).
# All fields are case-insensitive and must be converted in the lowercase.
#
# You should collect information about user sessions from the given logs.    A session is a sequence of the user requests at the same site (second-level domain),    where each request is no more than 30 minutes older than the previous request from that user at the same site.    We compare URL by second-level domain name, so admin.checkio.org and www.checkio.org are the same site.    The requests are sorted by timestamps.
#
# For example:
# 2013-01-01-01-00-00;;Name;;http://checkio.org/task
# 2013-01-01-01-02-00;;name;;http://checkio.org/task2
# 2013-01-01-01-31-00;;Name;;https://admin.checkio.org
# 2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
# 2013-01-01-03-00-01;;Name;;http://example.com
# 2013-01-01-03-11-00;;Name;;http://checkio.org/task
# 2013-02-03-04-00-00;;user2;;http://checkio.org/task
#
# This log contains 4 sessions. The first three requests (1-3) are created by "Name" ("name") at the same site,checkio.orgwith no more than 30 minutes between "neighbour" requests.    The second session contains two requests (4, 6) from "Name" atcheckio.org(more than 30 minutes from    01:31:00 request).    The next is the request (5) atexample.com.    The last session is the request (7) from "user2" atcheckio.org.
#
# The results should contain information about sessions in the next format:
# username;;site;;duration;;quantity_of_requests
# where each string is a session.
#
# usernameis a username from logs.siteis a second-level domain.durationis a time from first to last requests in seconds. The seconds are calculated inclusively.        If there's only one request in the session, then it has 1 second duration.        For example: two requests at 00:00:00 and 00:00:02 -- 3 seconds duration.quantity_of_requestsis a quantity of request in the session.The sessions strings should be separated by newline ("\n") and sorted in the ascending order by next priorities:usernames, sites, durations and quantity_of_requests
#
# The previous log text will be processed in:
# name;;checkio.org;;661;;2
# name;;checkio.org;;1861;;3
# name;;example.com;;1;;1
# user2;;checkio.org;;1;;1
# Input:A log text, a multilines string (unicode).
#
# Output:Sessions data, a multilines string.
#
#
# END_DESC

import re
from datetime import datetime
from operator import itemgetter, attrgetter


def checkio(log_text):

    sessions = []

    log = [x.lower().split(';;') for x in log_text.split('\n')]

    for l in log:

        l[0] = datetime.strptime(l[0], '%Y-%m-%d-%H-%M-%S')
        l[2] = re.search('(?<=\/|\.)[a-z]+\.[a-z]{2,4}(?=\/|$)', l[2]).group(0)

    sessions.append(log[0]+[1, 1])

    for l in log[1:]:

        for s in sessions:

            delta = int((l[0]-s[0]).total_seconds())
            if delta//60 < 30:
                if l[1] == s[1] and l[2] == s[2]:
                    s[0] = l[0]
                    s[3] += delta
                    s[4] += 1
                    break
        else:
            sessions.append(l+[1, 1])

    sessions = sorted([x[1:] for x in sessions], key=itemgetter(0, 1, 2, 3))

    sessions = '\n'.join([';;'.join([str(y) for y in x]) for x in sessions])

    return sessions


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(
        """2013-01-01-01-00-00;;name;;http://checkio.org/task2
2013-02-01-01-00-00;;Name;;https://admin.checkio.org""")
        ==
        """name;;checkio.org;;1;;1
name;;checkio.org;;1;;1"""), "Example"
