passed = 0
failed = 0
test_cases = [
    {"name": "Login Correct user and password", "url": "google.com", "expected": "pass"},
    {"name": "Login Correct user but wrong password", "url": "google.com", "expected": "fail"},
    {"name": "Login Wrong user but correct password", "url": "google.com", "expected": "fail"},
    {"name": "Login Wrong user and password", "url": "google.com", "expected": "fail"},
    {"name": "Login with user that expired", "url": "google.com", "expected": "fail"}
]

def check_test(test):
    if test["expected"] == "pass":
        return "✅ Passed"
    else:
        return "❌ Failed"
    
for cases in test_cases:
    print(f"Test: {cases['name']} | URL: {cases['url']} | Result: {check_test(cases)}")
    if cases["expected"] == "pass":
        passed = passed+1
    else:
        failed = failed+1
    
print (f"Total tests: {len(test_cases)}")
print (f"Passed: {passed}")
print (f"Failed: {failed}")