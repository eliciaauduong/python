class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

def password(pss):
    if len(pss) < 8:
        raise InvalidPasswordException("Your password needs to be 8 characters")
try:
    pwd = input("Enter your password: ")
    password(pwd)
except InvalidPasswordException as obj:
    print(obj)