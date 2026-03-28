def check_result(result):
    if result == "pass":
        return "✅ Test passed"
    else:
        return "❌ Test failed"

results = ["pass", "fail", "pass", "pass", "fail"]
messages = []

for result in results:
    message = check_result(result)
    messages.append(message)

print (messages)