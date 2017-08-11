import urllib2 as request
import urllib
from module import initialize
from module import platform_env
from module import menu
import os
import json

def get_users_list():
    base_url = "http://localhost:8000"
    print(verify_token())
    result = request.urlopen(base_url).read()
    return initialize.encap_model(json.loads(result))

def register():
    base_url = "http://localhost:8000/register"

def login():
    email = raw_input('Email: ')
    password = raw_input('Password: ')
    base_url = "http://localhost:8000/login"
    data = urllib.urlencode({ 'email': email, 'password': password})
    req = request.Request(base_url, data)
    response = request.urlopen(req).read()
    response = json.loads(response)
    initialize.set_platform_env_var(response)
    menu.SubMenu(get_users_list(), response)

def verify_token():
    base_url = "http://localhost:8000/api-token-verify/"
    data = urllib.urlencode({ 'token': os.environ['token'] })
    req = request.urlopen(base_url, data)
    req.request('POST',base_url,data)
    result = request.urlopen(base_url).read()

def initialize_conversation(recipient_email):
    sender_email = "AlecksJohanssen@gmail.com"
    base_url = "http://localhost:8000/conversation?sender_email=" + sender_email + "&" + recipient_email
    result = request.urlopen(base_url).read()


