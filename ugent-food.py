import json
import urllib2
import datetime
import sys


__author__ = 'thepieterdc'

def getMenu(weekNo,todayForm):
    url = "http://zeus.ugent.be/hydra/api/1.0/resto/week/%d.json" %weekNo
    response = urllib2.urlopen(url)
    jsonData = json.load(response)

    if dict.has_key(jsonData, todayForm):
        return dict.get(jsonData, todayForm)
    else:
        print 'Restaurant gesloten'

def main():

    if len(sys.argv) == 2:
        argument = sys.argv[1]

        if argument == 'morgen':
            day = datetime.date.today() + datetime.timedelta(days=1)
        elif argument == 'overmorgen':
            day = datetime.date.today() + datetime.timedelta(days=2)
        elif argument == 'maandag':
            day = datetime.date.today()
            while day.weekday() != 0:
                day += datetime.timedelta(1)
        elif argument == 'dinsdag':
            day = datetime.date.today()
            while day.weekday() != 1:
                day += datetime.timedelta(1)
        elif argument == 'woensdag':
            day = datetime.date.today()
            while day.weekday() != 2:
                day += datetime.timedelta(1)
        elif argument == 'donderdag':
            day = datetime.date.today()
            while day.weekday() != 3:
                day += datetime.timedelta(1)
        elif argument == 'vrijdag':
            day = datetime.date.today()
            while day.weekday() != 4:
                day += datetime.timedelta(1)
        else:
            day = datetime.date.today()
    else:
        day = datetime.date.today()

    weekNumber = day.isocalendar()[1]
    todayFormatted = day.strftime('%Y-%m-%d')
    menu = getMenu(weekNumber, todayFormatted)

    print "==================[%s]====================" %day

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