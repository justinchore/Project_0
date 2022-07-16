from Account import Account
from account_functions import create_account


accounts = [] #Get Data here

def main():
    run_program = True
    while run_program:
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
                #str(first_name)
                #str(last_name)
                #str(email)
                #str(password)
                #float(balance)
                account_info_dict = create_account()
                #Create user class
                new_account = Account(account_info_dict)
                print('Account successfully created. Please log in!')                
                user_selection = 1
            case 3: 
                print('exit')
                run_program = False


    return None
    

if __name__ == "__main__":
    main()
        