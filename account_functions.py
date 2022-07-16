#str(first_name)
#str(last_name)
#str(email)
#str(password)
#float(balance)
def create_account():
    account_info = {}
    print('First Name: ')
    first_name = input()
    #validation here
    #place into account_info
    account_info[first_name] = first_name
    print('Last Name: ')
    last_name = input()
    #validation here
    #place into account_info
    account_info[last_name] = first_name
    print('Email Address: ')
    email = input()
    #validation here
    #place into account_info
    account_info[email] = first_name
    print('Password: ')
    password = input()
    #validation here
    #place into account_info
    account_info[password] = first_name
    print('Initial Balance Deposit: ')
    balance = input()
    #validation here
    #place into account_info
    account_info[balance] = first_name
    #show user information, ask for confirmation
    #save account! (Here or main?)
    return account_info
