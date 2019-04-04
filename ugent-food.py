#!/usr/bin/env python3

import datetime
import requests
import sys
from urllib.error import HTTPError


def header(text, fillchar='-', width=40):
    tofill = max(width - 4 - len(text), 0)
    leftpad = tofill // 2

    print('{}[ {} ]{}'.format(
        fillchar * leftpad,
        text,
        fillchar * (tofill - leftpad),
    ))


# What day
weekdagen = ('ma', 'di', 'wo', 'do', 'vr', 'za', 'zo')
deltas = {'morgen': 1,
          'overmorgen': 2,
          'volgende': 7}

d = datetime.date.today()

sys.argv.pop(0)

if sys.argv:
    if sys.argv[0] in deltas:
        d += datetime.timedelta(deltas[sys.argv[0]])
        sys.argv.pop(0)

    if sys.argv and sys.argv[0][0:2] in weekdagen:
        while d.weekday() != weekdagen.index(sys.argv[0][0:2]):
            d += datetime.timedelta(1)

# Fetch from API
try:
    menu = requests.get("http://zeus.ugent.be/hydra/api/2.0/resto/menu/nl/{}/{}/{}.json".format(d.year, d.month, d.day)).json()
    # Print menu
    header(str(d), fillchar='=')

    header('SOEP')
    for s in menu["meals"]:
        if s["kind"] == "soup":
            print("* {}".format(s["name"]))

    header('HOOFDGERECHTEN')
    for m in menu["meals"]:
        if m["kind"] == "meat":
            print("* Vlees: {}".format(m["name"]))
        elif m["kind"] == "fish":
            print("* Vis: {}".format(m["name"]))
        elif m["kind"] == "vegetarian":
            print("* Vegetarisch: {}".format(m["name"]))
        elif m["kind"] == "vegan":
            print("* Vegan: {}".format(m["name"]))

    header('GROENTEN')
    for v in menu["vegetables"]:
        print("* {}".format(v))
except HTTPError:
    exit("Restaurant gesloten")
