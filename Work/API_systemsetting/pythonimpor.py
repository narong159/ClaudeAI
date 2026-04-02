import json

with open("D:/ClaudeAI/Work/API_systemsetting/openapi.json", "r", encoding="utf-8") as f:
    api = json.load(f)

print(api.keys())

for path, details in api["paths"].items():
    print(f"Path: {path}")
    for method, info in details.items():
        print (f" Method: {method.upper()}")
        print (f" Summary: {info.get('summary', 'no summary')}")
    print ("---")

path = "/security/v1/aes" 
details = api["paths"][path]["post"]
print (f"Summary: {details.get('summary', '')}")
print (f"Request body: {json.dumps(details.get('requestBody', {}), indent = 2)}")


# Extract schema name from $ref
ref = details["requestBody"]["content"]["application/json"]["schema"]["$ref"]
schema_name = ref.split("/")[-1]  # gets "xxxyyyy" from "#/components/schemas/xxxyyyy"

# Follow the pointer
schema = api["components"]["schemas"][schema_name]
print(json.dumps(schema, indent=2))

# Follow param1's ref
name_schema = api["components"]["schemas"]["AESName"]
print(json.dumps(name_schema, indent=2))

description_schema = api["components"]["schemas"]["Description"]
print(json.dumps(description_schema, indent=2))

inputaeskey_schema = api["components"]["schemas"]["InputAESKey"]
print(json.dumps(inputaeskey_schema, indent=2))

rsakeysize_schema = api["components"]["schemas"]["RSAKeySize"]
print(json.dumps(rsakeysize_schema, indent=2))

isactive_schema = api["components"]["schemas"]["IsActive"]
print(json.dumps(isactive_schema, indent=2))

# name boundaries
name_cases = ["", "x", "x" * 50, "x" * 100, "x" * 101]

# inputaeskey boundaries  
inputaeskey_cases = ["", "x" * 15, "x" * 16, "x" * 24, "x" * 32, "x" * 33]

# rsakeysize enum values
rsakeysize_cases = [1024, 2048, 3072, 4096, 0, ""]