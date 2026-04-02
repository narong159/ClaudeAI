import json

def load_schema(api, ref):
    schema_name = ref.split("/")[-1]
    return api["components"]["schemas"][schema_name]

def generate_name_cases(schema):
    max_len = schema.get("maximum", 100)
    return[
        {"value": "", "expect": "fail"},
        {"value": "y", "expect": "pass"},
        {"value": "y" * (max_len // 2), "expect": "pass"},
        {"value": "y" * max_len, "expect": "pass"},
        {"value": "y" * (max_len + 1), "expect": "fail"},
    ]

def generate_inputaeskey_cases(schema):
    min_len = schema.get("minLength", 16)
    max_len = schema.get("minLength", 32)
    return[
        {"value": "", "expect": "fail"},
        {"value": "y" * (min_len - 1), "expect": "fail"},
        {"value": "y" * (min_len), "expect": "pass"},
        {"value": "y" * ((min_len+max_len) // 2), "expect": "pass"},
        {"value": "y" * (max_len), "expect": "pass"},
        {"value": "y" * (max_len + 1), "expect": "fail"},
    ]

def generate_rsakeysize_cases(schema):
    enum_values = schema.get("enum", [])
    cases = [{"value": v, "expect": "pass"} for v in enum_values]
    cases.append({"value": 0, "expect": "fail"})
    cases.append({"value": 9999, "expect": "fail"})    
    return cases

with open ("D:/ClaudeAI/Work/API_systemsetting/openapi.json", "r", encoding="utf-8") as f:
    api = json.load(f)

name_schema = load_schema(api, "#/components/schemas/AESName")
inputaeskey_schema = load_schema(api, "#/components/schemas/InputAESKey")
rsakeysize_schema = load_schema(api, "#/components/schemas/RSAKeySize")

name_cases = generate_name_cases(name_schema)
inputaeskey_cases = generate_inputaeskey_cases(inputaeskey_schema)
rsakeysize_cases = generate_rsakeysize_cases(rsakeysize_schema)

# print (f"name cases: {len(name_cases)}")
# print (f"inputaeskey cases: {len(inputaeskey_cases)}")
# print (f"rsakeysize cases: {len(rsakeysize_cases)}")