import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

# Check status code
assert response.status_code == 201, "❌ Status code is not 200!"

# Check response time (in seconds)
assert response.elapsed.total_seconds() < 2, "❌ Response too slow!"

# Check data
data = response.json()
assert data["name"] == "Leanne Graham", "❌ Name is wrong!"

print("✅ All checks passed!")