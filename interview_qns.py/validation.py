#16. Validation Rules (Regex)
import re

def valid_email(email):
    return bool(re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email))

def valid_mobile(num):
    return bool(re.match(r'^[6-9]\d{9}$', num))