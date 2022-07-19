import uuid
import json
import re
from CustomExceptions import InvalidCharactersError, InvalidNumbersError, InvalidEmailError, DuplicateEmailError, InvalidPasswordError, InvalidCurrencyFormatError, InitDepositNotMetError

from validation_functions import special_chars_validation, no_numbers_validation, currency_validation, email_validation, duplicate_email, password_check

class Bank:
    def __init__(self):
        self._is_running = True
        self._logged_in = False
        self._logged_in_account = None
        self._minimum_deposit_amount = 25
    
    @property
    def is_running(self):
        return self._is_running
    
    def set_is_running(self):
       self._is_running = not self._is_running
    
    @property
    def logged_in(self):
        return self._logged_in
    
    @property
    def logged_in_account(self):
        return self._logged_in_account
    
    def set_logged_in_account(self, account):
        self._logged_in_account = account

    
    def set_logged_in(self):
        # self._logged_in = not self._logged_in 
        if self.logged_in == True:
            self._logged_in = False
        else:
            self._logged_in = True
    
    @property
    def minimum_deposit_amount(self):
        return self._minimum_deposit_amount
    
    
    def create_account(self, accounts_list):
        account_info = {}
        account_info["id"] = str(uuid.uuid4())
        #validation here
        while True:
            try:
                print('First Name: ', end='')
                first_name = input().strip()
                if first_name == '/q' or first_name == 'q':
                    print('Exiting...')
                    return None
                result = special_chars_validation(first_name)
                result2 = no_numbers_validation(first_name)
               
                if len(result) != 0:
                    raise InvalidCharactersError(result)
                if len(result2) != 0:
                    raise InvalidNumbersError(result2)

            except InvalidCharactersError as ice:
                    print(ice.message)
            except InvalidNumbersError as ine:
                    print(ine.message)
            else:
                break
        #place into account_info
        account_info["first_name"] = first_name.capitalize()
        while True: 
            try:
                print('Last Name: ', end='')
                last_name = input().strip()
                result = special_chars_validation(last_name)
                result2 = no_numbers_validation(last_name)
               
                if len(result) != 0:
                    raise ValueError
                if len(result2) != 0:
                    raise SyntaxError

            except ValueError as ve:
                print(f'Invalid characters detected: {result}. Please try again')
            except SyntaxError as se:
                print(f'Numbers detected: {result2}. Please try again')
            else:
                break
        #place into account_info
        account_info["last_name"] = last_name.capitalize()
        #Email validation:
        while True:
            try:
                print('Email: ', end='')
                email = input().strip()
                result = email_validation(email)
                if result == None:
                    raise ValueError
                
                if duplicate_email(email, accounts_list) == True:
                    raise SyntaxError
             
            except SyntaxError as se:
                print(f'Email already registered to an account. Please log in.')
                return None
            except ValueError as ve:
                print(f'Invalid Email. Please Try again.')
            else: 
                break
        
        #place into account_info
        account_info["email"] = email.lower()
        while True:
            try:
                print('Please enter a password with the following: \n - At least 6 characters long\n - Contains a lowercase letter\n - Contains an uppercase letter\n - Contains a number\n Enter password: ', end='')
                password = input()

                if password_check(password) == None:
                    raise ValueError
                
            except ValueError as ve:
                print(f'Password requirements not met. Please try again.')
            else: 
                break
        #place into account_info
        account_info["password"] = password
        while True:
            try: 
                print('Initial Balance Deposit: $', end='')
                balance = input().strip()
                validation_result = currency_validation(balance)
                print(validation_result)
                if validation_result == None:
                    raise ValueError
                if float(balance) < 25:
                    raise SyntaxError
                
            except ValueError as ve:
                print(f'Invalid currency format. Examples: [25, 25.50, 25.05]')
            except SyntaxError as se:
                print(f'Initial deposit amount must be at least {self.minimum_deposit_amount}.')
            else:
                break
        
        #validation/normalize here
        #place into account_info
        account_info["balance"] = float("{:.2f}".format(float(balance)))
        #show user information, ask for confirmation 
        #save account! (Here or main?)
        print(account_info)
        return account_info
    
    def log_in(self, accounts_list):
        #[{}, {}, {}]
        print('Accounts List: ', accounts_list)
        print('Log in to your account')
        print('Email: ', end='' )
        input_email = input()
        print('Password: ', end='')
        input_password = input()

        for acc in accounts_list:
            print(acc.values())
            if input_email in acc.values():
                print(acc)
                if acc["password"] == input_password:
                    print('You have successfully logged in to your account.')
                    return acc
                else:
                    print('Log in failed. Check your credentials and try again')
                    return False
            
        print('Log in failed. Check your credentials and try again')
        return False
        
            
        #iterate through the list of accounts
        #if email is not in account ->print user does not exist
        #if email is in account, check password of that dictionary! 
        #if password == password, then toggle logged in, set current_account to the dictionary.


# def special_chars_validation(input):
#      pattern = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")
#      return pattern.findall(input)
 
# def no_numbers_validation(input):
#      match = re.findall('[0-9]+', input)
#      return match
 
# def currency_validation(input):
#     #Allows $.
#     # pattern = re.compile(r'^\$?(\d*(\d\.?|\.\d{1,2}))$')
#     pattern = re.compile(r'[1-9]\d*(\.\d\d)?(?![\d.])')
#     match =  re.fullmatch(pattern, input)
#     return match
     
# def email_validation(input):
#     pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
#     match = re.fullmatch(pattern, input)
#     print(match)
#     return match

# def duplicate_email(input, accounts_list):
#     print(accounts_list)
#     for acc in accounts_list:
#         if input.lower() == acc['email']:
#             return True
#     return False

# def password_check(input):
#     pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
#     match = re.search(pattern, input)
#     return match
    
    

