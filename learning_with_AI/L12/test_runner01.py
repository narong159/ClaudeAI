import requests
import test_data01
import helpers

for test_case in test_data01.test_cases:
    post_body = {
        "username": test_case["username"],
        "password": test_case["password"]
    }
    response = requests.post("https://httpbin.org/post", json=post_body)
    print (f"Test case name: {test_case["name"]}")
    helpers.assert_status_code(response.status_code, 200)
    helpers.assert_field(response.json()["json"], "username", test_case["username"])
    helpers.assert_field(response.json()["json"], "password", test_case["password"])
    
print(f"----- Test Report -----")
print (f"Total: {helpers.passed+helpers.failed}")
print (f"✅ Passed: {helpers.passed}")
print (f"❌ Failed: {helpers.failed}")