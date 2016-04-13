#!/usr/bin/env python3

import json
import datetime
import sys
import urllib.request

def header(text, fillchar='-', width=40):
    tofill = max(width - 4 - len(text), 0)
    leftpad = tofill // 2

    print('{}[ {} ]{}'.format(
        fillchar * leftpad,
        text,
        fillchar * (tofill - leftpad),
    ))

# What day
weekdagen = ('ma', 'di', 'wo', 'do', 'vr')
deltas = {'morgen': 1,
          'overmorgen': 2}

d = datetime.date.today()
if len(sys.argv) == 2:
    d += datetime.timedelta(deltas.get(sys.argv[1], 0))

    if sys.argv[1][0:2] in weekdagen:
        while d.weekday() != weekdagen.index(sys.argv[1][0:2]):
            d += datetime.timedelta(1)

# Fetch from API
menu = json.loads(urllib.request.urlopen(
    "http://zeus.ugent.be/hydra/api/1.0/resto/week/{}.json".format(d.isocalendar()[1])).read().decode('utf-8'))

# Get wanted day in API response
if str(d) not in menu:
    exit("Restaurant gesloten")
today = menu[str(d)]

# Print menu
header(str(d), fillchar='=')

header('SOEP')
print("* {}".format(today["soup"]["name"]))

header('HOOFDGERECHTEN')
for g in today["meat"]:
    print("* {}".format(g["name"]))

header('GROENTEN')
for v in today["vegetables"]:
    print("* {}".format(v))
