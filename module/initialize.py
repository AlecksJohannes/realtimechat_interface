from module import platform_env
import platform
def encap_model(result):
    user_array = []
    for attr in result:
        user_array.append(attr['username'])
    return user_array

def set_platform_env_var(response):
    if response['code'] == 302:
        platform_env.env_variable(platform.system(), response['token'], response['id'])
