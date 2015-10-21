import json
import urllib2

__author__ = 'thepieterdc'

from datetime import date

def getMenu(weekNo,todayForm):
    url = "http://zeus.ugent.be/hydra/api/1.0/resto/week/%d.json" %weekNo
    response = urllib2.urlopen(url)
    jsonData = json.load(response)

    if dict.has_key(jsonData, todayForm):
        return dict.get(jsonData, todayForm)
    else:
        print 'Restaurant gesloten'

def main():

    weekNumber = date.today().isocalendar()[1]
    todayFormatted  = date.today().strftime('%Y-%m-%d')
    menu = getMenu(weekNumber,todayFormatted)

    print "==================[SOEP]=================="
    print dict(menu)["soup"]["name"]

    print "==================[GERECHTEN]=================="
    print dict(menu)["meat"][0]["name"]
    print dict(menu)["meat"][1]["name"]
    print dict(menu)["meat"][2]["name"]
    print dict(menu)["meat"][3]["name"]

    print "==================[GROENTEN]=================="
    print dict(menu)["vegetables"][0]
    print dict(menu)["vegetables"][1]

if __name__ == '__main__':
    main()