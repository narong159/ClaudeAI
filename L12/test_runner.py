import helpers
from helpers import assert_status_code, assert_field
from test_data import BASE_URL, post_body

import requests

response = requests.post(f"{BASE_URL}/post", json=post_body)

assert_status_code(response.status_code, 200)
assert_field(response.json()["json"], "name", "Ma")

print(f"----- Test Report -----")
print (f"Total: {helpers.passed+helpers.failed}")
print (f"✅ Passed: {helpers.passed}")
print (f"❌ Failed: {helpers.failed}")