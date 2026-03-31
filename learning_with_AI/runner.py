import os
import sys
sys.path.append ("D:/ClaudeAI/Work")
from tests.test_login import test_login_valid, test_login_wrong_password
import terminalProfile_TerminalManagement
from report import generate_report

#Run all tests
# test_login_valid()
# test_login_wrong_password()
terminalProfile_TerminalManagement.login_keycloak()

# Generate report
generate_report()