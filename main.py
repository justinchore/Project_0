from Account import Account
from Bank import Bank


accounts = [] #Get Data here
# [{}, {}, {}, {}]

def main():
    bank = Bank()
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
                print('Log in to your account')

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
                print(bank.logged_in)
            case 3: 
                print('exit')
                bank.set_is_running()
                return None

    # while run_program and logged_in:
    #     print('What would you like to do?')
    #     print('Deposit Money')



    return None
    

if __name__ == "__main__":
    main()
        