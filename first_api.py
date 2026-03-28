import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/")

print(response.status_code)
print(response.json())

data = response.json()
for user in data:
    print (f"Name: {user["name"]} | Email: {user["email"]}")