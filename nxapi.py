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

    auth = HTTPBasicAuth()
