import os
def env_variable(os_name, token):
    options = {
        'Darwin': darwin(token),
        'Linux': linux(token),
        'Windows': windows(token),
    }
    options[os_name]
def darwin(token):
    os.environ['token'] = token
def linux(token):
    os.environ['token'] = token
def windows(token):
    os.environ['token'] = token
