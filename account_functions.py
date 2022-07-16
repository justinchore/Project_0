#str(first_name)
#str(last_name)
#str(email)
#str(password)
#float(balance)
def create_account():
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
