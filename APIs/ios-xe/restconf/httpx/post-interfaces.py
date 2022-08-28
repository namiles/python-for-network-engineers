import json
from urllib import response
import httpx
from routers import lab_routers

url = f"https://{lab_routers['r1']['HOST']}:{lab_routers['r1']['PORT']}/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
    "Authorization": "Basic bm1pbGVzOmNpc2Nv",
}

payload = json.dumps(
    {
        "ietf-interfaces:interface": {
            "name": f"Loopback100",
            "description": "Added using RESTCONF and Python - devnet",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [{"ip": f"100.100.100.1", "netmask": "255.255.255.255"}]
            },
        }
    }
)

with httpx.Client(verify=False) as client:
    response = client.post(url=url, headers=headers, data=payload)
    print(response.status_code)
