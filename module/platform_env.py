import os
def env_variable(os_name, token, id):
    options = {
        'Darwin': darwin(token, id),
        'Linux': linux(token, id),
        'Windows': windows(token, id),
    }
    options[os_name]
def darwin(token, id):
    os.environ['token'] = token
    print(id)
    os.environ['user_id'] = str(id)
def linux(token, id):
    os.environ['token'] = token
    os.environ['user_id'] = str(id)
def windows(token, id):
    os.environ['token'] = token
    os.environ['user_id'] = str(id)
