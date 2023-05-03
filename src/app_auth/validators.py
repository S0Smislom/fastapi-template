def validate_password(cls, values):
    password, password_1 = values.get("password"), values.get("password2")
    if password != password_1:
        raise ValueError("Passwords not matched")
    return values
