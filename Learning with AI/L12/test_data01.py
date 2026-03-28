test_cases = [
    {"name": "Valid login", "username": "admin", "password": "admin123", "expected_status": 200},
    {"name": "Wrong password", "username": "admin", "password": "wrongpass", "expected_status": 200},
    {"name": "Empty username", "username": "", "password": "admin123", "expected_status": 200},
]