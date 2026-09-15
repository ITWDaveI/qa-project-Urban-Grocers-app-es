import requests
from configuration import KITS_PATH
from configuration import CREATE_USER_PATH

def create_user(URL_SERVICE, user_data):
    response = requests.post(f"{URL_SERVICE}{CREATE_USER_PATH}", json=user_data)
    return response

def get_new_user_token(URL_SERVICE, user_data):
    response = create_user(URL_SERVICE, user_data)
    body = response.json()
    user_authToken = body["authToken"]
    return user_authToken

def create_kit_for_user(URL_SERVICE, user_data, user_authToken):
    headers = {"Authorization": 'Bearer ' + user_authToken}
    response = requests.post(f"{URL_SERVICE}{KITS_PATH}", headers=headers, json=user_data)
    return response