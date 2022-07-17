class Account:
    #Create constructor for attributes:
    def __init__(self, account_info):

        self._first_name, self._last_name, self._email,self._password, self._balance = account_info.values()
    
    @property
    def balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance += amount

    def deposit(self):
        print(f'You currently have ${self.balance} in your balance. Enter the amount for depost: ', end="")
        deposit_amount = int(input())
        #validate
        self.set_balance(deposit_amount)
        #add time thing here "...depositing to your account.."
        print(f'Deposit successful. Your new balance is {self.balance}')



    def __str__(self):
        return (f'Account Information:\nName: {self._first_name} {self._last_name}\nEmail: {self._email}\nBalance:{self._balance}')
        
        
   