import requests, json, pprint
from flask import Flask, jsonify, render_template

def tickgen():
    url = "https://sandboxapic.cisco.com/api/v1/ticket"
    payload = {"username":"devnetuser", "password":"Cisco123!"}
    header = {"content-type":"application/json"}

    r = requests.post(url, json.dumps(payload), headers=header, verify=False)

    return r.json()["response"]["serviceTicket"]

tick = tickgen()

controller = "devnetapi.cisco.com/sandbox/apic_em"
url = "https://" + controller + "/api/v1/topology/physical-topology"
header = {"content-type": "application/json", "X-Auth-Token":tick}

resp = requests.get(url, headers=header, verify=False)

top = resp.json()["response"]

print(top)

confapp = Flask(__name__)

@confapp.route("/")
@confapp.route("/index")
def index():
    return render_template("topology.html")

@confapp.route("/api/<name>")
def api(name):
    if name == "topology":
        return jsonify(top)
    else:
        return "No such page found"


if __name__ == '__main__':
    confapp.run(debug=True)