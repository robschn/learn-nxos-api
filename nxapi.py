#!/usr/bin/env python3

# Requires Python3 and requests

# imports
import json
import requests
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings

# import creds
import sys
import creds

# change file path to use creds.py
sys.path.append("..")

# definitions
username = creds.username
password = creds.password
ip_address = creds.ip_address

if __name__ == "__main__":

    auth = HTTPBasicAuth(username, password)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    url = 'https://'+ip_address+'/ins'

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


    disable_warnings()
    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth, verify=False)

    result = json.loads(response.text)
    result_body = result['ins_api']['outputs']['output']['body']

    print(result_body['host_name'])
