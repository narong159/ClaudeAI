results = []

def record_test(case_id, method, url, request_body, response_body, expected, actual, status_code, response_time):
    passed = expected == actual

    results.append({
        "case_id": case_id,
        "method": method,
        "url": url,
        "request": request_body,
        "status_code": status_code,
        "response_time": round(response_time, 3),
        "response": response_body,
        "expected": expected,
        "actual": actual,
        "result": "✅ Pass" if passed else "❌ Fail"
    })