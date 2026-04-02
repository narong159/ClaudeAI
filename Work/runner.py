import requests
import urllib3
import sys
import os
sys.path.append ("D:/ClaudeAI/learning_with_AI")
sys.path.append ("D:/ClaudeAI/*")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers_upgrade
import report
from API_systemsetting.combine_cases import test_cases

kc_mad_URL = "https://uat-auth.sooksanonline.com/realms/mad/protocol/openid-connect/token"
systemsetting_url = "https://uat-api.sooksanonline.com/mad/api/systemsetting/security/v1"

def login_keycloak():
    headers = {
    "Accept": "*/*",
    "Authorization": "Basic bWFkLXN5c3RlbS1zZXR0aW5nOmFncFNBYTUxS0lJUTR6eW9EamdQZ25GUUNFbmhWOHJ3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded"
    }
    
    body = {
    "grant_type": "password",
    "code": "4d61f5f2-e156-3ef8-6426-b950c4fa1fd0.073981a0-7b2f-c297-0c9e-ef8f5f67fefa.f8f8ccef-0163-4b09-8dd8-ad64b14b63fb",
    "redirect_uri": "https://oauth.pstmn.io/v1/callback",
    "code_verifier": "alAk4Cbi1gWazrRxxsS9psd1QT1xwIDJlN01V7OMYsE",
    "username": "abc_test",
    "password": "12345",
    "scope": "mad-system-setting"
    }

    response = requests.post(kc_mad_URL, headers=headers, data=body, verify=False)
    helpers_upgrade.record_test(
        method = "GET",
        url = kc_mad_URL,
        request_header = headers,
        request_body = body,
        response_time = response.elapsed.total_seconds(),
        response_body = response.json(),
        e_code = "",
        a_code = "",
        e_http = 200,
        a_http = response.status_code
    )

    # print (response.json())
    global access_token    
    access_token = response.json()["access_token"]

def aes_create():
    headers = {
    "Accept": "text/plain",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}",
    }

    for case in test_cases:
        body = {
            "name": case["name"],
            "inputaeskey": case["inputaeskey"],
            "rsakeysize": case["rsakeysize"]
        }

        response = requests.post((f"{systemsetting_url}/aes"), headers=headers, json=body, verify=False)
        helpers_upgrade.record_test(
            method = "POST",
            url = f"{systemsetting_url}/aes",
            request_header = headers,
            request_body = body,
            response_time = response.elapsed.total_seconds(),
            response_body = response.json(),
            e_code = 000000,
            a_code = response.json()["responseCode"],
            e_http = 200,
            a_http = response.status_code
        )

#runner here
login_keycloak()
aes_create()

report.generate_report()