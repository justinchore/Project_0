import re
import bcrypt

# def password_check(input):
#     pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
#     match = re.search(pattern, input)
#     if match == None:
#         print('password requirements not met.')
#     else:
#         print(match)
#         print('password requirements met')
    
# password_check('password123') #nope
# password_check('password')#nope
# password_check('Password1')#yup
# password_check('P@ssword!')#nope
# password_check('123password')#nope
# password_check('123Password')#yup
# password_check('Password')#nope
# password_check('PASSWORD123')#nope
# password_check('p2aS')#nope

# def currency_validation(input):
#     #Allows $.
#     # pattern = re.compile(r'^\$?(\d*(\d\.?|\.\d{1,2}))$')
#     pattern = re.compile(r'[1-9]\d*(\.\d\d)?(?![\d.])')
#     match =  re.fullmatch(pattern, input)
#     return match

# print(currency_validation('10.45235345345345'))
# print(currency_validation('1.45235345345345'))
# print(currency_validation('10.45'))
# print(currency_validation('10.4'))
# print(currency_validation('10.04'))
# print(currency_validation('.56'))

def hash_password(input):
    bytes = input.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)

def check_password(pass_attempt, correct_hashed):
    return correct_hashed == bcrypt.hashpw(pass_attempt.encode('utf-8'), correct_hashed)
       
   
   

# print(hash_password('Password123'))
print(check_password('Password123', b'$2b$12$gvqAu2TRqK8qOZLhSWtL2OhdPdxUryjJ6hhvIgckp4R7/rcHBDzzC'))
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