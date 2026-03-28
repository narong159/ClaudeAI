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
        print (f"✅ {data[field]} is expected email")
    else:
        record_result("failed")
        print (f"❌ {data[field]} is not expected email")

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

assert_status_code(response.status_code, 200)
assert_response_time(response.elapsed.total_seconds(), 2)
# assert response.status_code == 200, "❌ Status code is not 200!"
# assert response.elapsed.total_seconds() < 2, "❌ Response too slow!"
assert_field(response.json(), "email", "Sincere@april.biz")
# assert data["email"] == "Sincere@april.biz", "❌ Email is wrong"

print ("✅ All checks passed!")
print (f"----- Test Report -----")
print (f"Total: {passed+failed}")
print (f"✅ Passed: {passed}")
print (f"❌ Failed: {failed}")
# assert data["email"] == "wrong@email.com", "❌ Email is wrong"