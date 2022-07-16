from Account import Account
from Bank import Bank


# accounts = [] #Get Data here
accounts =  {'accounts': [{'first_name': 'Justin', 'last_name': 'Cho', 'email': 'justin@justin.com', 'password': 'password123', 'balance': '100'}]}


def main():
    bank = Bank()
    current_account_class = None
    print(bank.is_running, bank.logged_in)
    while bank.is_running and not bank.logged_in:
        print('Welcome to Foundation Bank!')
        print('Please select an option from the menu')
        print('1: Log in to your account')
        print('2: Create a Foundation Bank account')
        print('3: Exit')

        user_selection = int(input())

        match user_selection:
            case 1:
                print(bank.logged_in)
                login_result = bank.log_in(accounts) #returns an account if successful
                if login_result != False:
                    current_account_class = Account(login_result)
                    bank.set_logged_in()
                    bank.set_logged_in_account = login_result
                print(bank.logged_in)

            case 2:
                print('Create an account. Minimum initial deposit amount: $25')
                #call create_account:
                # account_info_dict = create_account()

                #Create user class
                # new_account = Account(account_info_dict)
                #Save User
                new_account_dict = bank.create_account()
                new_account_class = Account(new_account_dict)
                accounts.append(new_account_dict)
                print('Account successfully created. You are now logged in!')                
                bank.set_logged_in()
                bank.logged_in_account = new_account_dict
                # print(bank.logged_in)
            case 3: 
                print('exit')
                bank.set_is_running()
                return None

    while bank.is_running == True and bank.logged_in == True:
        print('What would you like to do?')
        print('1.Deposit')
        print('2.Withdraw')
        print('3.Log out and Exit Program')
        
        user_selection = int(input())

        match user_selection:
            case 1:
                print(bank.logged_in_account)
                print('You have chosen to deposit')
                print(f'You currently have ${(current_account_class.balance)}')
            case 2: 
                print(bank.logged_in_account)
                print('You have chosen to withdraw')
            case 3: 
                print('You have chosen to log out and exit')
                #sets logged in to False
                bank.set_logged_in()
                #sets the logged in user dictionary value to none
                bank.set_logged_in_account = None
                #terminates program
                bank.set_is_running()
        
            

    return None
    

if __name__ == "__main__":
    main()
        