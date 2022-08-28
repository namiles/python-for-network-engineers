import httpx
from routers import lab_routers

# https://www.python-httpx.org/

url = f"https://{lab_routers['r1']['HOST']}:{lab_routers['r1']['PORT']}/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Authorization": "Basic bm1pbGVzOmNpc2Nv",
}

with httpx.Client(verify=False) as client:
    response = client.get(url=url, headers=headers)
    print(response.text)
