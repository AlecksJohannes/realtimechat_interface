import urllib2 as request
import sys
import os
sys.path.append(os.path.abspath("../ChatInterface/module"))
import initialize
import json

def get_users_list():
    print("haha")
    base_url = "http://localhost:8000"
    result = request.urlopen(base_url).read()
    return initialize.encap_model(json.loads(result))

