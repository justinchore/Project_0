import uuid
import json
import re
import os
# from colorama import Fore, Back, Style
from time import sleep

from output_functions import format_account_dict, line_generator

from CustomExceptions import InvalidCharactersError, InvalidNumbersError, InvalidEmailError, DuplicateEmailError, InvalidPasswordError, InvalidCurrencyFormatError, InitDepositNotMetError, EmailNotRegisteredError, PasswordAuthenticationError

from validation_functions import special_chars_validation, no_numbers_validation, currency_validation, email_validation, duplicate_email, password_check, hash_password, check_password_bcrypt

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
        line_generator()
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
                    line_generator(10)
                    raise InvalidCharactersError(result)
                if len(result2) != 0:
                    line_generator(10)
                    raise InvalidNumbersError(result2)

            except InvalidCharactersError as ice:
                print(ice.message, end="\n\n")
                    
            except InvalidNumbersError as ine:
                print(ine.message, end="\n\n")
                    
            else:
                break
        #place into account_info
        account_info["first_name"] = first_name.capitalize()
        line_generator()
        while True: 
            try:
                print('Last Name: ', end='')
                last_name = input().strip()
                if last_name == '/q' or last_name == 'q':
                    print('Exiting...')
                    return None
                result = special_chars_validation(last_name)
                result2 = no_numbers_validation(last_name)
               
                if len(result) != 0:
                    line_generator(10)
                    raise InvalidCharactersError(result)
                if len(result2) != 0:
                    line_generator(10)
                    raise InvalidNumbersError(result2)

            except InvalidCharactersError as ice:
                print(ice.message, end="\n\n")
            except InvalidNumbersError as ine:
                print(ine.message, end="\n\n")
            else:
                break
        #place into account_info
        account_info["last_name"] = last_name.capitalize()
        #Email validation:
        line_generator()
        while True:
            try:
               
                print('Email: ', end='')
                email = input().strip()
                if email == '/q' or email == 'q':
                    print('Exiting...')
                    return None
                result = email_validation(email)
                if result == None:
                    line_generator(10)
                    raise InvalidEmailError
                
                if duplicate_email(email, accounts_list) == True:
                    line_generator(10)
                    raise DuplicateEmailError
             
            except InvalidEmailError as iee:
                print(iee.message, end="\n\n")
            except DuplicateEmailError as dee:
                print(dee.message, end="\n\n")
                return None
            else: 
                break
        
        #place into account_info
        account_info["email"] = email.lower()
        line_generator()
        while True:
            try:
                print('Please enter a password with the following: \n - At least 6 characters long\n - Contains a lowercase letter\n - Contains an uppercase letter\n - Contains a number\n Enter password: ', end='\n\n')
                password = input()
                if password == '/q' or password == 'q':
                    print('Exiting...')
                    return None

                if password_check(password) == None:
                    line_generator(10)
                    raise InvalidPasswordError
                
            except InvalidPasswordError as ipe:
                
                print(ipe.message, end="\n\n")
            else: 
                break
        #place into account_info
        account_info["password"] = password
        line_generator()
        while True:
            try: 
                print('Initial Balance Deposit: $', end='')
                balance = input().strip()
                if balance == '/q' or balance == 'q':
                    print('Exiting...')
                    return None
                validation_result = currency_validation(balance)
                # print(validation_result)
                if validation_result == None:
                    line_generator(10)
                    raise InvalidCurrencyFormatError
                if float(balance) < 25:
                    line_generator(10)
                    raise InitDepositNotMetError
                
            except InvalidCurrencyFormatError as icf:
                print(icf.message, end="\n\n")
            except InitDepositNotMetError as ednme:
                print(ednme.message, end="\n\n")
            else:
                break
        
        #validation/normalize here
        #place into account_info
        account_info["balance"] = float("{:.2f}".format(float(balance)))
        #show user information, ask for confirmation
        print('Outputting New Account Information....')
        line_generator()
        while True:
            try:
                format_account_dict(account_info)
                save_confirm = input("Does everything look correct? /y to confirm, /n to exit: ")
                if (save_confirm.lower() == 'n' or save_confirm == '/n') :
                    return None
                elif (save_confirm.lower() == 'y' or save_confirm == '/y'):
                    return account_info
                else:
                    raise ValueError
            except ValueError as ve:
                print("Invalid input. Please enter 'y' to create account or 'n' to exit.")
                
    
    def log_in(self, accounts_list):
        #[{}, {}, {}]
        print('Accounts List: ', accounts_list)
        print("Log in to your account or enter '/q' to exit")
        line_generator()
        while True:
            try:
                print('Email: ', end='' )
                input_email = input().strip().lower()
                if input_email == '/q' or input_email == 'q':
                    print('Exiting...')
                    return False
                print('Password: ', end='')
                input_password = input()
                if input_password.lower() == '/q' or input_password.lower() == 'q':
                    print('Exiting...')
                    return False 
                
                email_authentication_result = self.is_email_registered(input_email, accounts_list)
                
                if email_authentication_result == False:
                    raise EmailNotRegisteredError
                
                if email_authentication_result['password'] == input_password:
                    first_name_str = email_authentication_result.get('first_name')
                    last_name_str = email_authentication_result.get('last_name')
                    print(f'Welcome {first_name_str} {last_name_str}!')
                    return email_authentication_result
                else:
                    raise PasswordAuthenticationError
                
                       
            except EmailNotRegisteredError as ere:
                print(ere.message, end="\n\n")
            except PasswordAuthenticationError as pae:
                print(pae.message, end="\n\n")     
    
    def is_email_registered(self, email, accounts_list):
        for acc in accounts_list:
            if email.lower() in acc.values():
                return acc
            
        return False
        
        

        
            
        
        
        
        
        
        
        
        
#iterate through the list of accounts
# #if email is not in account ->print user does not exist
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
    
    

