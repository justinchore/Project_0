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
    
    def create_account(self):
        account_info = {}
        print('First Name: ', end='')
        first_name = input()
        #validation here
        #place into account_info
        account_info["first_name"] = first_name
        print('Last Name: ', end='')
        last_name = input()
        #validation here
        #place into account_info
        account_info["last_name"] = last_name
        print('Email: ', end='')
        email = input()
        #validation here
        #place into account_info
        account_info["email"] = email
        print('Password: ', end='')
        password = input()
        #validation here
        #place into account_info
        account_info["password"] = password
        print('Initial Balance Deposit: ', end='')
        balance = input()
        #validation/normalize here
        #place into account_info
        account_info["balance"] = balance
        #show user information, ask for confirmation
        #save account! (Here or main?)
        print(account_info)
        return account_info
    
    def log_in(self, accounts_list):
        #[{}, {}, {}]
        print('Log in to your account')
        print('Email: ', end='' )
        input_email = input()
        print('Password: ', end='')
        input_password = input()

        for acc in accounts_list:
            if input_email in acc.values():
                if acc["password"] == input_password:
                    print('You have successfully logged in to your account.')
                    return acc
                else:
                    print('Log in failed. Check your credentials and try again')
                    return False
            else:
                print('Log in failed. Check your credentials and try again')
                return False
        
            
        #iterate through the list of accounts
        #if email is not in account ->print user does not exist
        #if email is in account, check password of that dictionary! 
        #if password == password, then toggle logged in, set current_account to the dictionary.







'''
TODO: 
Deposit
Withdraw
Check for the existence of account when creating
Validations
Datetime -> field for account created at
JSON
Hash Password/Hide Password -> token? 
Colorama
'''