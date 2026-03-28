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