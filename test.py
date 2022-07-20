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


'''
TODO: 
 - Check for the existence of account when creating (DONE)
 - Text input -> special characters (DONE)  
 - number check(cast into float with decimal) (DONE)
 - password check: length, numbers, special char (DONE)
 - email format check (DONE)
 - capitalize name (DONE)
 
 - Exit out whenever! Not logged in.(WORKING - Deposit, Withdrawl)
 - Create custom error class for homemade exceptions (WORKING, Deposit, Withdrawl)
 - Withdrawl/Deposit Validations (WORKING)
 - Datetime -> field for account created at (Maybe)
 - hash password -> hashlib or bcrypt (Maybe)
 - Colorama (No)

'''