import urllib2 as request
import urllib
from module import initialize
from module import platform_env
from module import menu
from network import protocol
from django.http import JsonResponse
import os
import json

def get_users_list():
    base_url = "http://localhost:8000"
    result = request.urlopen(base_url).read()
    return initialize.encap_model(json.loads(result))

def register():
    password = raw_input('Password: ')
    username = raw_input('Username: ')
    base_url = "http://localhost:8000/register"
    data = urllib.urlencode({ 'password': password, 'username': username })
    req = request.urlopen(base_url, data)
    response = req.read()
    response = json.loads(response)
    initialize.set_platform_env_var(response)
    menu.SubMenu().create(get_users_list(), response)


def login():
    username = raw_input('Username: ')
    password = raw_input('Password: ')
    base_url = "http://localhost:8000/login"
    data = urllib.urlencode({ 'username': username, 'password': password})
    req = request.Request(base_url, data)
    response = request.urlopen(req).read()
    response = json.loads(response)
    initialize.set_platform_env_var(response)
    menu.SubMenu().create(get_users_list(), response)

def verify_token():
    base_url = "http://localhost:8000/api-activate/"
    req = request.Request(base_url, headers={"Authorization" : "JWT " + os.environ['token']})
    response = request.urlopen(req).read()
    return json.loads(response)

def initialize_conversation(recipient_email):
    if verify_token()['code'] == 302:
        base_url = "http://localhost:8000/conversation"
        data = urllib.urlencode({ 'sender_email': verify_token()['current_user'], 'recipient_email': recipient_email })
        req = request.urlopen(base_url, data)
        result = req.read()
        result = json.loads(result)
        protocol.init_protocal(result['conversation'])
    else:
        menu.SubMenu().create(get_users_list())


