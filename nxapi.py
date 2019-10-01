#!/usr/bin/env python3

# Requires Python3 and requests

# imports
import json
import requests
from requests.auth import HTTPBasicAuth
from requests.packages import urllib3

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


    urllib3.disable_warnings()
    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth, verify=False)

    print (response)
    result = response.text
    result_dict = json.loads(result)
    result_body = result_dict['ins_api']['outputs']['output']['body']

    print (result_body['host_name'])
