import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import helpers_upgrade

BASE_URL = "https://httpbin.org"

def test_login_valid():
    body = {"username": "student", "password": "Password123"}
    response = requests.post(f"{BASE_URL}/post", json=body)
    helpers_upgrade.record_test(
        case_id = "TC001",
        method = "POST",
        url = f"{BASE_URL}/post",
        request_body = body,
        status_code = response.status_code,
        response_time = response.elapsed.total_seconds(),
        response_body = response.json(),
        expected = 200,
        actual = response.status_code
    )

def test_login_wrong_password():
    body = {"username": "student", "password": "wrongpass"}
    response = requests.post(f"{BASE_URL}/post", json=body)
    helpers_upgrade.record_test(
        case_id = "TC002",
        method = "POST",
        url = f"{BASE_URL}/post",
        request_body = body,
        status_code = response.status_code,
        response_time = response.elapsed.total_seconds(),
        response_body = response.json(),
        expected = 200,
        actual = response.status_code
    )

# test_login_valid()
# test_login_wrong_password()

# print (helpers_upgrade.results)