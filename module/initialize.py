import sys
import os
import user
sys.path.append(os.path.abspath("../models"))
sys.path.append(os.path.abspath("../network"))

def encap_model(result):
    list = []
    for attr in result:
        user.first_name = attr['first_name']
        user.id = attr['id']
        list.append(user)
    return list
