# from allpairspy import allpairs
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_cases_aes_post import name_cases, inputaeskey_cases, rsakeysize_cases

test_cases = []

for name in name_cases:
    for inputaeskey in inputaeskey_cases:
        for rsakeysize in rsakeysize_cases:

            # determine overall expected result
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