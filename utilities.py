from email_validator import validate_email


 
def check_email(testEmail):
    s = validate_email(testEmail,check_deliverability=False)
    return testEmail.lower() == s.ascii_email.lower()

def is_even(i) -> bool:
    return (i%2 == 0)

def is_odd(i) -> bool:
    return ( i%2 != 0)

def sign(num):
    if num > 0:
        return "+"
    elif num < 0:
        return "-"
    else:
        return "0"


