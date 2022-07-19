class InvalidCurrencyFormatError(Exception):
    def __init__(self):
        self.message = "Not a valid format for currency. Accepted formats: [25, 25.50, 25.05"
    pass

class InvalidEmailError(Exception):
    def __init__(self):
        self.message = "Invalid email. Please try again or enter '/q' to exit"
    pass

class InvalidCharactersError(Exception):
    def __init__(self, list):
        def generate_message(): 
            return f"Invalid characters detected: {list} Please try again or enter '/q' to exit"
        self.message = generate_message()
        
class DuplicateEmailError(Exception):
    def __init__(self):
        self.message = 'There is already an account registered to this email. Please log in.'

class InvalidPasswordError(Exception):
    def __init__(self):
        self.message = 'Password requirements not met. Please try again.'
        
            




'''
class NotCurrencyFormatError(Exception):
    def __init__(self, lst="Not a currency!!"):
        self.lst = lst
        def generateMessage(lst):
            return "modified message"
        self.message = generateMessage()

currency = False

try:
    if currency == False:
        lst = retListOfBadChar()
        raise NotCurrencyFormatError(str(lst) + " is not a currency")
except NotCurrencyFormatError as ncf:
    print(ncf.message)



'''