#!/usr/bin/env python3

import json
import datetime
import os

import requests
import sys
from urllib.error import HTTPError


d = datetime.date.today()

# Fetch from API
try:
    menu = requests.get("http://zeus.ugent.be/hydra/api/2.0/resto/menu/nl/{}/{}/{}.json".format(d.year, d.month, d.day)).json()

    soups = set()
    mains = set()

    for s in menu["meals"]:
        if s["kind"] == "soup":
            soups.add(s["name"].replace(" klein", "").replace(" groot", ""))
        if s["type"] == "main" and s["kind"] != "soup":
            mains.add(s["name"])

    os.system("notify-send -i restaurant --urgency=critical \"Soep\" \"{}\"".format(" en ".join(soups)))
    os.system("notify-send -i restaurant --urgency=critical \"Hoofdgerechten\" \"{}\"".format(", ".join(mains)))
except HTTPError:
    # don't do anything
    pass
