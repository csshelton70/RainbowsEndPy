from email_validator import validate_email


 
def check_email(testEmail):
    s = validate_email(testEmail,check_deliverability=False)
    return testEmail.lower() == s.ascii_email.lower()
