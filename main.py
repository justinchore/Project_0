from Account import Account
from Bank import Bank
import json


# # accounts = [] #Get Data here
# accounts =  ['id'first_name': 'Justin', 'last_name': 'Cho', 'email': 'justin@justin.com', 'password': 'password123', 'balance': 100}]

def read_parse_json(): #returns a list of accounts
    with open("bank.json", "r") as myfile:
        return json.load(myfile)


def write_to_json(account_dict, list):
    with open("bank.json", "w") as myfile:
        list.append(account_dict)
        print(list)
        myfile.write(json.dumps(list))

def get_image_from_txt(filename):
    with open(filename, "r") as mytextimage:
        for line in mytextimage:
            print(line, end='')


def main():

    print(get_image_from_txt('bank-banner.txt'))
    bank = Bank()
    current_account_class = None
    accounts_list = read_parse_json()
    print(bank.is_running, bank.logged_in)
    while bank.is_running and not bank.logged_in:
        print('Welcome to Foundation Bank!')
        print('Please select an option from the menu')
        print('1: Log in to your account')
        print('2: Create a Foundation Bank account')
        print('3: Exit')

        user_selection = input()

        match user_selection:
            case '1':
                print(bank.logged_in)
                login_result = bank.log_in(accounts_list) #returns an account if successful
                if login_result != False:
                    current_account_class = Account(login_result)
                    bank.set_logged_in()
                    bank.set_logged_in_account (current_account_class)
                print(bank.logged_in)

            case '2':
                print('Create an account. Minimum initial deposit amount: $25')
                new_account_dict = bank.create_account()
                current_account_class = Account(new_account_dict)
                write_to_json(new_account_dict, accounts_list)
                print('Account successfully created. You are now logged in!')                
                bank.set_logged_in()
                bank.set_logged_in_account(new_account_dict)
            case '3': 
                print('exit')

                bank.set_is_running()
                return None
            case default:
                print('Unrecognized input. Enter a number 1-3.')

    while bank.is_running == True and bank.logged_in == True:
        accounts_list = read_parse_json()
        print('What would you like to do?')
        print('1) Deposit')
        print('2) Withdraw')
        print('3) Account Overview')
        print('4) Log out and Exit Program')
        
        user_selection = input()

        match user_selection:
            case '1':
                print(current_account_class)
                current_account_class.deposit()
                #save file
                write_to_json(current_account_class.__dict__, accounts_list)
               
            case '2': 
                print(bank.logged_in_account)
                print('You have chosen to withdraw')
            case '3':
                print(current_account_class)
            case '4': 
                print('You have chosen to log out and exit')
                #sets logged in to False
                bank.set_logged_in()
                #sets the logged in user dictionary value to none
                bank.set_logged_in_account = None
                #terminates program
                bank.set_is_running()
            case default:
                print('Unrecognized input. Enter a number 1-4.')
        
            

    return None






    

if __name__ == "__main__":
    main()
        