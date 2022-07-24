# Jinja2 Templates   

### Variable Substitution
Variables are surrounded by double curly braces = {{ variable }}   

As a general rule of thumb, any piece of information that needs to be replaced with some peice of data should be surrounded by curly braces.   

In the below example, we are subsititing **BGP.ASN** with a variable from the Python module.
```
router bgp {{ BGP.ASN }}
```

### Loops   
Jinja2 supports using loops for when you need to generate the same bit of information with slight differences.

In the below example, we loop through each peer in the BGP YAML configuration data, and create a neighbor config line for each one using the variables **peer.neighbor** and **peer.asn_path**. We are able to use a loop here because BGP.peers is a list of peers.
```
  {% for peer in BGP.peers %}
  neighbor {{ peer.neighbor }} remote-as {{ peer.peer_asn }}
  {% endfor %}
```

### Conditional Logic   
Jinja2 also supports the use of conditional logic for even more intricate templates.

For example, if we wanted to exclude 10.0.0.4 from being configured as a neighbor, we can use conditional logic to make sure it is excluded. In the below example, if peer.neighbor is **NOT** 10.0.0.4, then create a neigbor configuration line. This will leave out 10.0.0.4.
```
{% if peer.neighbor != "10.0.0.4" %}
  neighbor {{ peer.neighbor }} remote-as {{ peer.peer_asn }}
{% endif %}
```

### Filters
Jinja2 filters can be used to modify variables. There are an assortment of [built-in](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters) Jinja2 filters, though custom filters can also be created.

In the below example, we use the built-in capitalize filter to capitalize a variable.
```
snmp-community {{ SNMP.community | capitalize }}
```


## Complete Example
Example Configuration Data:
```
---
BGP:
  ASN: "65001"
  peers:
    - neighbor: "10.0.0.2"
      peer_asn: "65002"
    - neighbor: "10.0.0.3"
      peer_asn: "65003"
    - neighbor: "10.0.0.4"
      peer_asn: "65004"
    - neighbor: "10.0.0.5"
      peer_asn: "65005"
```
Or, as a Python Object:
```
{
    "BGP": {
        "ASN": "65001",
        "peers": [
            {
                "neighbor": "10.0.0.2",
                "peer_asn": "65002"
            },
            {
                "neighbor": "10.0.0.3",
                "peer_asn": "65003"
            },
            {
                "neighbor": "10.0.0.4",
                "peer_asn": "65004"
            },
            {
                "neighbor": "10.0.0.5",
                "peer_asn": "65005"
            }
        ]
    }
}
```

Example Template:
```
router bgp {{ BGP.ASN }}
  {% for peer in BGP.peers %}
  {% if peer.neighbor != "10.0.0.4" %}
  neighbor {{ peer.neighbor }} remote-as {{ peer.peer_asn }}
  {% endif %}
  {% endfor %}
```

Renders to:
```
router bgp 65001
  neighbor 10.0.0.2 remote-as 65002
  neighbor 10.0.0.3 remote-as 65003
  neighbor 10.0.0.5 remote-as 65005
```
