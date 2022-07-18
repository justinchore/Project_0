import re

def password_check(input):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
    match = re.search(pattern, input)
    if match == None:
        print('password requirements not met.')
    else:
        print(match)
        print('password requirements met')
    
password_check('password123') #nope
password_check('password')#nope
password_check('Password1')#yup
password_check('P@ssword!')#nope
password_check('123password')#nope
password_check('123Password')#yup
password_check('Password')#nope
password_check('PASSWORD123')#nope
password_check('p2aS')#nope
