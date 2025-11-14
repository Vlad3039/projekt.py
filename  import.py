from email_validator import validate_email, EmailNotValidError

def check_email(email):
    try:
        result = validate_email(email)
        return True
    except EmailNotValidError:
        return False
