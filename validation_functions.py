import re
import bcrypt

def special_chars_validation(input):
     pattern = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")
     return pattern.findall(input)
 
def no_numbers_validation(input):
     match = re.findall('[0-9]+', input)
     return match
 
def currency_validation(input):
    #Allows $.
    # pattern = re.compile(r'^\$?(\d*(\d\.?|\.\d{1,2}))$')
    pattern = re.compile(r'[1-9]\d*(\.\d\d)?(?![\d.])')
    match =  re.fullmatch(pattern, input)
    return match
     
def email_validation(input):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    match = re.fullmatch(pattern, input)
    return match

def duplicate_email(input, accounts_list):
    #print(accounts_list)
    for acc in accounts_list:
        if input.lower() == acc['email']:
            return True
    return False

def password_check(input):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    match = re.search(pattern, input)
    return match
    
def withdrawl_amount_check(withdrawl_amount, account_balance):
    converted_withdrawl_amount = withdrawl_amount * -1
    if account_balance + converted_withdrawl_amount < 0:
        return False
    return True

def hash_password(input):
    bytes = input.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt)


def check_password_bcrypt(attempt, password_string):
    password_str_byte = password_string.encode('utf-8')
    return bcrypt.checkpw(attempt.encode('utf-8'), password_str_byte)
    