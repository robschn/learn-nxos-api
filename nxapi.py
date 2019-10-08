#!/usr/bin/env python3

# Requires Python3 and requests

# imports
import json
import requests
from requests.auth import HTTPBasicAuth
from urllib3 import disable_warnings

# import creds
import creds
username = creds.username
password = creds.password
api_ip = creds.api_ip

if __name__ == "__main__":

    auth = HTTPBasicAuth(username, password)

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    url = 'https://'+api_ip+'/ins'

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

    print("Test")