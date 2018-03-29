import re
import glob
from flask import Flask, jsonify


def getdatafromconfigs(fname):
    result = {}
    for fname in glob.glob(fname):
        ipinfo =[]
        for line in open(fname):
            pat = "(ip address) ((?:[0-9]{1,3}[\.]){1,3}[0-9]{1,3}) ((?:[0-9]{1,3}[\.]){3}[0-9]{1,3})"
            m = re.match(pat, line.strip().lower())
            if m:
                ipaddr = m.group(2) + "/" + m.group(3)
                ipinfo.append(ipaddr)
            if re.match("(hostname)", line.strip().lower()):
                hname = line.strip().lower().split(" ")[1]
        result[hname] = list(set(ipinfo))
    return result

res = getdatafromconfigs("config_files\*.txt")
#print(res)
#print (res.keys())

confapp = Flask(__name__)

@confapp.route("/")
@confapp.route("/index")
def index():
    return "Go to /configs to see the hostnames; " \
           "Go to /config/[name] to see [name] config. Thanks!"

@confapp.route("/configs")
def configs():
    return jsonify(list(res.keys()))

''''@confapp.route("/config/<name>")
def config(name):
    if name == "hostname":
        return jsonify(res)
    else:
        return "No such page found"'''

@confapp.route("/config/<name>")
def config(name):
    try:
        return jsonify(res[name])
    except:
        return "No such page found"

if __name__ == '__main__':
    confapp.run(debug=True)



