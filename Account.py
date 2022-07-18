import json

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
        print(f'You currently have ${self.balance} in your balance. Enter the amount for deposit: ', end="")
        deposit_amount = float("{:.2f}".format(float(input())))
        #validate
        self.set_balance(deposit_amount)
        #add time thing here "...depositing to your account.."
        print(f'Deposit successful. Your new balance is {self.balance}')
    
    def withdraw(self):
        print(f'You currently have ${self.balance} in your balance. Enter the amount for withdrawl: ', end="")
        withdrawl_amount = float("{:.2f}".format(float(input())))
        #validate
        self.set_balance(withdrawl_amount * -1)
        #add timing thing here "...withdrawing from your account.."
        print(f'Withdrawl successful. Your new balance is {self.balance}')



    def __str__(self):
        return (f'Account Information:\nName: {self._first_name} {self._last_name}\nEmail: {self._email}\nBalance:{self._balance}')
        
        
   