import uuid
import json
import re

class Bank:
    def __init__(self):
        self._is_running = True
        self._logged_in = False
        self._logged_in_account = None
    
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
    
    def create_account(self, accounts_list):
        account_info = {}
        account_info["id"] = str(uuid.uuid4())
        #validation here
        while True:
            try:
                print('First Name: ', end='')
                first_name = input().strip()
                result = special_chars_validation(first_name)
               
                if len(result) != 0:
                    raise ValueError

            except ValueError as ve:
                print(f'Invalid characters detected: {result}. Please try again')
            else:
                break
        #place into account_info
        account_info["first_name"] = first_name.capitalize()
        while True: 
            try:
                print('Last Name: ', end='')
                last_name = input().strip()
                result = special_chars_validation(last_name)
               
                if len(result) != 0:
                    raise ValueError

            except ValueError as ve:
                print(f'Invalid characters detected: {result}. Please try again')
            else:
                break
        #place into account_info
        account_info["last_name"] = last_name.capitalize()
        #Email validation:
        while True:
            try:
                print('Email: ', end='')
                email = input()
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
        print('Password: ', end='')
        password = input()
        #validation here
        #place into account_info
        account_info["password"] = password
        print('Initial Balance Deposit: ', end='')
        balance = float("{:.2f}".format(float(input())))
        #validation/normalize here
        #place into account_info
        account_info["balance"] = balance
        
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


def special_chars_validation(input):
     pattern = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")
     return pattern.findall(input)

def email_validation(input):
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    match = re.fullmatch(pattern, input)
    print(match)
    return match

def duplicate_email(input, accounts_list):
    print(accounts_list)
    for acc in accounts_list:
        if input.lower() == acc['email']:
            return True
    return False

'''
TODO: 
Check for the existence of account when creating
Validations
- Text input -> special characters  
 - number check(cast into float with decimal)
 - withdraw check
 - email format check
 - capitalize name 
Datetime -> field for account created at
JSON
Generate IDs with uuid4()
Hash Password/Hide Password -> token? 
Colorama
'''