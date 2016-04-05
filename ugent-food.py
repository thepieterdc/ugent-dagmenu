import json
import datetime
import sys
import urllib.request


def getmenu(d: datetime) -> dict:
    """
    Gets the menu for a given date.
    :param d: the date
    :return: the menu for a given date
    """
    jsonData = json.loads(urllib.request.urlopen(
        "http://zeus.ugent.be/hydra/api/1.0/resto/week/{}.json".format(d.isocalendar()[1])).read().decode('utf-8'))

    if str(d) in jsonData:
        return jsonData[str(d)]
    exit("Restaurant gesloten.")


def printmenu(d: datetime):
    """
    Prints the menu for a given date.
    :param d: the date
    """
    menu = getmenu(d)
    print("{}[{}]{}".format("=" * 19, d, "=" * 19))
    print("{}[ SOEP ]{}".format("=" * 21, "=" * 21))
    print("* {}".format(menu["soup"]["name"]))
    print("{}[ HOOFDGERECHTEN ]{}".format("=" * 16, "=" * 16))
    [print("* {}".format(g["name"])) for g in menu["meat"]]
    print("{}[ GROENTEN ]{}".format("=" * 21, "=" * 21))
    [print("* {}".format(v)) for v in menu["vegetables"]]


if len(sys.argv) == 2:
    o = str(sys.argv[1])

    day = datetime.date.today() + datetime.timedelta(1 if o == 'morgen' else 2 if o == 'overmorgen' else 0)

    if o[0:2] in ['ma', 'di', 'wo', 'do', 'vr']:
        while day.weekday() != ['ma', 'di', 'wo', 'do', 'vr'].index(o[0:2]):
            day += datetime.timedelta(1)
else:
    day = datetime.date.today()

printmenu(day)
