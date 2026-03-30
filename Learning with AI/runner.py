import os
from tests.test_login import test_login_valid, test_login_wrong_password
from terminalProfile_TerminalManagement import login_keycloak
from report import generate_report

#Run all tests
# test_login_valid()
# test_login_wrong_password()
login_keycloak()

# Generate report
generate_report()
print(os.getcwd())  # prints current working directory