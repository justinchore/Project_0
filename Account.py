import json
from CustomExceptions import InvalidCurrencyFormatError, WithdrawlAmountError
from output_functions import line_generator
from validation_functions import currency_validation, withdrawl_amount_check

class Account:
    #Create constructor for attributes:
    def __init__(self, account_info):

        self._id, self._first_name, self._last_name, self._email,self._password, self._balance = account_info.values()
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def id(self):
        return self._id
    
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password
    

    def set_balance(self, amount):
        self._balance += amount

    def deposit(self):
        line_generator()
        try:
            print(f'You currently have ${self.balance} in your balance. Enter the amount for deposit or /q to exit: $ ', end="")
            deposit_amount = input().strip()
            if deposit_amount == '/q' or deposit_amount == 'q':
                print('Exiting...')
                return None
            validation_result = currency_validation(deposit_amount)
            print(validation_result)
            if validation_result == None:
                line_generator(10)
                raise InvalidCurrencyFormatError
            # deposit_amount = float("{:.2f}".format(float(input())))
            #validate
            float_balance = float("{:.2f}".format(float(deposit_amount)))
            self.set_balance(float_balance)
             #add time thing here "...depositing to your account.."
            print(f'Deposit successful. Your new balance is {self.balance}')
        except InvalidCurrencyFormatError as icfe:
            print(icfe.message)
    
    def withdraw(self):
        try:
            print(f'You currently have ${self.balance} in your balance. Enter the amount for withdrawl or /q to exit: $ ', end="")
            # withdrawl_amount = float("{:.2f}".format(float(input())))
            withdrawl_amount = input().strip()
            if withdrawl_amount == '/q' or withdrawl_amount == 'q':
                print('Exiting....')
                return None
            validation_result = currency_validation(withdrawl_amount)
            print(validation_result)
            if validation_result == None:
                raise InvalidCurrencyFormatError
            if float(withdrawl_amount) <= 0:
                raise WithdrawlAmountError
            if withdrawl_amount_check(float(withdrawl_amount), self.balance) == False:
                raise WithdrawlAmountError
            
            withdrawl_amount = float("{:.2f}".format(float(withdrawl_amount)))
            self.set_balance(withdrawl_amount * -1)
            line_generator()
            print(f'Withdrawl successful. Your new balance is {self.balance}')
            
            return None
        except InvalidCurrencyFormatError as icfe:
            print(icfe.message)
        except WithdrawlAmountError as wae:
            print(wae.message)

    def __str__(self):
        return (f'Account Information:\nName: {self._first_name} {self._last_name}\nEmail: {self._email}\nBalance:{self._balance}')
        
        
   