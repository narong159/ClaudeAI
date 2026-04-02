from allpairspy import AllPairs
from generate_cases_aes_post import name_cases, inputaeskey_cases, rsakeysize_cases

parameters = [name_cases, inputaeskey_cases, rsakeysize_cases]

test_cases = []
for i, name in enumerate(name_cases):
    inputaeskey = inputaeskey_cases[i % len(inputaeskey_cases)]
    rsakeysize = rsakeysize_cases[i % len(rsakeysize_cases)]

    if name["expect"] == "pass" and inputaeskey["expect"] == "pass" and rsakeysize["expect"] == "pass":
        expected = 200
    else:
        excepted = 400

    test_cases.append({
        "name": name["value"],
        "inputaeskey": inputaeskey["value"],
        "rsakeysize": rsakeysize["value"],
        "expected": excepted
    })

print(f"Total test cases generated: {len(test_cases)}")