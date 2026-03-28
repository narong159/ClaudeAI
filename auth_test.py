import requests
passed = 0
failed = 0

def record_result(value):
    global passed
    global failed
    if value == "pass":
        passed += 1
        return passed
    else:
        failed += 1
        return failed

def assert_status_code(reponse, expected):
    if reponse == expected:
        record_result("pass")
        print (f"✅ Status code correct: {reponse}")
    else:
        record_result("failed")
        print (f"❌ Wrong status code: got {reponse} expected {expected}")

def assert_response_time(response, max_seconds):
    
    if response <= max_seconds:
        record_result("pass")
        print (f"✅ {response} is expected time")
    else:
        record_result("failed")
        print (f"❌ Response too slow!")

def assert_field(data, field, expected_value):
    if data[field] == expected_value:
        record_result("pass")
        print (f"✅ {data[field]} is expected")
    else:
        record_result("failed")
        print (f"❌ {data[field]} is not expected")

headers = {
    "x-api-key": "testkey123"
}

headers2 = {
    "Authorization": "Bearer mytoken123"
}
response = requests.get(
    # "https://httpbin.org/basic-auth/myuser/mypassword",
    "https://httpbin.org/headers",
    headers=headers2
    )

# assert_status_code(response.status_code, 200)
# assert_field(response.json(), "authenticated", True)
# assert_field(response.json(), "user", "myuser")
print (f"{response.json()}")
print (f"----- Test Report -----")
print (f"Total: {passed+failed}")
print (f"✅ Passed: {passed}")
print (f"❌ Failed: {failed}")