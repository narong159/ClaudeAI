import os
import sys
sys.path.append ("D:/ClaudeAI/Work")
from tests.test_login import test_login_valid, test_login_wrong_password
import terminalProfile_TerminalManagement
import systemsetting_aes
from report import generate_report

#Run all tests
systemsetting_aes.login_keycloak()
systemsetting_aes.aes_listAll()
systemsetting_aes.aes_listNames()
systemsetting_aes.aes_create()

# Generate report
generate_report()

