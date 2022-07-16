class Bank:
    def __init__(self):
        self._is_running = True
        self._logged_in = False
    
    @property
    def is_running(self):
        return self._is_running
    
    def set_is_running(self):
       self._is_running = not self._is_running
    
    @property
    def logged_in(self):
        return self._logged_in
    
    def set_logged_in(self):
        self._logged_in = not self._logged_in 
    
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
    
    def log_in(self, accounts_list, email, password):
        #[{}, {}, {}]
        for acc in accounts_list:

        #iterate through the list of accounts
        #if email is not in account ->print user does not exist
        #if email is in account, check password of that dictionary! 
        #if password == password, then toggle logged in, set current_account to the dictionary.
