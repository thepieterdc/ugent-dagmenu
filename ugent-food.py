import json
import datetime
import sys
import urllib.request

d = datetime.date.today()
if len(sys.argv) == 2:
    d += datetime.timedelta(1 if sys.argv[1] == 'morgen' else 2 if sys.argv[1] == 'overmorgen' else 0)

    if sys.argv[1][0:2] in ['ma', 'di', 'wo', 'do', 'vr']:
        while d.weekday() != ['ma', 'di', 'wo', 'do', 'vr'].index(sys.argv[1][0:2]):
            d += datetime.timedelta(1)

menu = json.loads(urllib.request.urlopen(
    "http://zeus.ugent.be/hydra/api/1.0/resto/week/{}.json".format(d.isocalendar()[1])).read().decode('utf-8'))

if str(d) not in menu:
    exit("Restaurant gesloten")

print("{}[{}]{}".format("=" * 19, d, "=" * 19))
print("{}[ SOEP ]{}".format("=" * 21, "=" * 21))
print("* {}".format(menu[str(d)]["soup"]["name"]))
print("{}[ HOOFDGERECHTEN ]{}".format("=" * 16, "=" * 16))
[print("* {}".format(g["name"])) for g in menu[str(d)]["meat"]]
print("{}[ GROENTEN ]{}".format("=" * 21, "=" * 21))
[print("* {}".format(v)) for v in menu[str(d)]["vegetables"]]
