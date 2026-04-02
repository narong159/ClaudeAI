results = []
case_counter = 0
def record_test(method, 
                url, 
                request_header, 
                request_body, 
                response_body, 
                expected, 
                actual, 
                status_code, 
                response_time, 
                response_code):
    global case_counter
    case_counter +=1
    case_id = f"TC{str(case_counter).zfill(3)}"
    passed = expected == actual

    results.append({
        "case_id": case_id,
        "method": method,
        "url": url,
        "request_header": request_header,
        "request_body": request_body,
        "status_code": status_code,
        "response_time": round(response_time, 3),
        "response_code": response_code,
        "response": response_body,
        "expected": expected,
        "actual": actual,
        "result": "✅ Pass" if passed else "❌ Fail"
    })

