results = []
case_counter = 0
def record_test(method,
                url,
                request_header,
                request_body,
                response_time,
                response_body,
                e_code,
                a_code,
                e_http,
                a_http
                ):
    global case_counter
    case_counter +=1
    case_id = f"TC{str(case_counter).zfill(3)}"
    passed = e_http == a_http

    results.append({
        "case_id": case_id,
        "method": method,
        "url": url,
        "request_header": request_header,
        "request_body": request_body,
        "response_time": round(response_time, 3),
        "response": response_body,
        "e_code": e_code,
        "a_code": a_code,
        "e_http": e_http,
        "a_http": a_http,
        "result": "✅ Pass" if passed else "❌ Fail"
    })

