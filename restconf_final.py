import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback64070106"


# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback64070106",
        "description": "Sasithorn RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.30.106.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

    resp = requests.put(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 203):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070106 is created successfully"
    elif(resp.status_code >= 204 and resp.status_code <= 400):
        print("STATUS ERROR: {}".format(resp.status_code))
        return "Cannot create: Interface loopback 64070106"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))

def delete():
    resp = requests.delete(
        api_url, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070106 is deleted successfully"
    elif(resp.status_code   >= 400 and resp.status_code <= 500):
        print("STATUS ERROR: {}".format(resp.status_code))
        return("Cannot delete: Interface loopback 64070106")
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def enable():

    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback64070106",
            "enabled": True
        }
    }

    resp = requests.patch(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070106 is enabled successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def disable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback64070106",
            "enabled": False
        }
    }

    resp = requests.patch(
        api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 64070106 is shutdowned successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))


def status():
    api_url_status = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback64070106"

    resp = requests.get(
        api_url_status, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        print(response_json)
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        print(admin_status)
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback 64070106 is enabled"
        elif admin_status == 'down' and oper_status == 'down':
            return "Interface loopback 64070106 is disabled"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback 64070106"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))