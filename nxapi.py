#!/usr/bin/env python3

# Requires Python3 and requests

# imports
import json
import requests
from requests.auth import HTTPBasicAuth

# import creds
import creds
username = creds.username
password = creds.password
nxip = creds.nxip

if __name__ == "__main__":

    auth = HTTPBasicAuth(username, password)
    requests.packages.urllib3.disable_warnings()
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'https://'+nxip+'/ins'

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "sh ver",
            "output_format": "json"
        }
    }

    response =  requests.post(url, data=json.dumps(payload), headers=headers, auth=auth, verify=False)

    print (response)
    result = response.text
    result_dict = json.loads(result)

    print (result_dict['ins_api']['outputs']['output']['body']['host_name'])
