class NotCurrencyFormatError(Exception):
    def __init__(self, message="Not a valid format for currency. EXAMPLES"):
        self.message = message
    pass




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