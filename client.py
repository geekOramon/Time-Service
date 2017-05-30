#! usr/bin/env Python 2.7
"""This is an early implementation client \n to retrieve Configuration from a centralized server \n pip prerequisites: requests, yaml by doing pip install requests"""
import requests
import yaml


def perform_request_to_config_server(config_server_url, microservice, environment, branch, uname, upass):
    r = requests.get(
        'http://' + uname + ':' + upass + '@' + config_server_url + '/' + microservice + '-' + environment + '.yml')
    return yaml.load(r.text)
