import requests
import urllib3
import sys
import os
sys.path.append ("D:/ClaudeAI/learning_with_AI")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers_upgrade

BASE_URL = "https://172.235.199.28:9248/realms/touchpoint/protocol/openid-connect/token"

def login_keycloak():
    headers = {
    "Accept": "*/*",
    "Host": "172.235.199.28:9248",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "125"
    }
    
    body = {
        "username": "testuser@email.com", "password": "1234", "client_id": "sad-frontend", "grant_type": "password", "scope": "openid api-terminal-profile-2j"
    }
    response = requests.post(BASE_URL, headers=headers, data=body, verify=False)
    helpers_upgrade.record_test(
        case_id = "TC001",
        method = "POST",
        url = f"{BASE_URL}/post",
        request_header = headers,
        request_body = body,
        status_code = response.status_code,
        response_time = response.elapsed.total_seconds(),
        response_body = response.json(),
        expected = 200,
        actual = response.status_code
    )
    # response = requests.post("xxx", headers=headers)

    # print (response.json())
    global access_token
    global id_token
    
    access_token = response.json()["access_token"]
    id_token = response.json()["id_token"]
    # print (f"access token = {access_token} \nid token = {id_token}")