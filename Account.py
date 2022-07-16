class Account:
    #Create constructor for attributes:
    def __init__(self, account_info):

        self._first_name, self._last_name, self._email,self._password, self._balance = account_info.values()
   