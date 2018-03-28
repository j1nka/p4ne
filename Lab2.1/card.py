import requests
import pprint
import json

res = []

#cardnum = "5404367554185185"
#r = requests.get("https://lookup.binlist.net/"+cardnum)

js = json.load(open("card1.json"))

for i in js:
    #print(i["CreditCard"]["CardNumber"])
    r = requests.get("https://lookup.binlist.net/"+str(i["CreditCard"]["CardNumber"])).json()
    if r["bank"] != {}:
        if r["bank"]["name"] != "":
            res.append(r["bank"]["name"])

res = list(set(res))

print(sorted(res))

