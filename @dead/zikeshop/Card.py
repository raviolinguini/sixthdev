"""
(credit) Card object for zikeshop
"""
__ver__="$Id$"

import time
import zikeshop
from strongbox import attr
from strongbox import Strongbox

class Card(Strongbox):
    expMonth = attr(int)
    expYear = attr(int)
    number = attr(str)

    def getEditableAttrs(self):
        return super(Card, self).getEditableAttrs() + ["masked","issuer"]
    
    def _new(self):
        super(Card,self)._new()
        nowYear, nowMonth = time.localtime(time.time())[0:2]
        self.expYear  = nowYear
        self.expMonth = nowMonth
        self.customerID = 0
        
    def get_issuer(self):
        return issuer(self.number)

    def get_masked(self):
        return ("x" * (len(self.number)-4)) + self.number[-4:]


    def checkdigits(self, digits):
        return validate(digits)

    def isExpired(self):
        import time
        # @TODO: does a card expire on the first or last of expiration month?
        nowYear, nowMonth = time.localtime(time.time())[0:2]
        return (nowYear, nowMonth) > (self.expYear, self.expMonth)

    def set_number(self, value):
        # Strip dashes and spaces..
        # I'm leaving letters and other characters in
        # so that they generate an error.
        num = ""
        for ch in str(value):
            if ch not in "- ":
                num = num + ch

        # validate the card:
        if (issuer(num) != "unknown") and checkLength(issuer(num), len(num)) \
           and self.checkdigits(num):
            self.__values__['number']=num
        else:
            raise ValueError, "Invalid credit card number."

##### @TODO: THIS CAME FROM THE PAYMENT MODULE. PUT IT BACK THERE! #######

def issuer(number):
    """
    issuer(number) -> who issued the card?
    """
    res = "unknown"
    num = str(number)
    if num[:1]=="4":
        res = "Visa"
    elif num[:2] in ("34","37"):
        res = "American Express"
    elif num[:2] in ("51","55"):
        res = "MasterCard"
    elif num[:4]=="6011":
        res = "Discover/Novus"
    return res
            

def checkLength(ish, length):
    """
    checkLength(ish,length) -> is length okay for issuer 'ish'?
    """
    if ish == "Visa":
        ok = (13,16)
    elif ish == "American Express":
        ok = (15,)
    elif ish == "MasterCard":
        ok = (16,)
    elif ish == "Discover/Novus":
        ok = (16,)
    else:
        raise TypeError, "unknown issuer"
    return length in ok
    

def validate(number):
    """
    validate the format of a credit card number..
    this is tested extensively against perl's Business::CreditCard
    in the zike payment module (outside zikeshop)

    I'm just sticking this in here for now, until the payment
    library is ready to go..

    If there's a bug, put it right in payment first!!!
    (but i don't think there's any bugs, since I tested it against
    all kinds of card #'s and compared to perl)
    """
    # numbers only:
    try:
        long(number)
    except:
        return 0

    # must be at least 13 digits:
    if len(str(number)) < 13:
        return 0

    # can't be all zeros, even though this passes the check below
    if long(number) == 0:
        return 0
    
    ### check the digits: ###########
    # see http://www.beachnet.com/~hstiles/cardtype.html

    # digits, from right to left...
    digits = list(str(number))
    digits.reverse()

    doubles = ""
    sum = 0
    # Step 1: Double the value of alternate digits of the primary
    # account number beginning with the second digit from the right
    # (the first right--hand digit is the check digit.)
    for i in range(len(digits)):
        if i % 2:
            # note that this does NOT fire for the rightmost digit,
            # because 0 % 2 is 0... :)
            doubles = doubles + str(int(digits[i]) * 2)

    # Step 2: Add the individual digits comprising the products
    # obtained in Step 1 to each of the unaffected digits in the
    # original number.
        else:
            sum = sum + int(digits[i])

    for ch in doubles:
        sum = sum + int(ch)

    # Step 3: The total obtained in Step 2 must be a number ending in
    # zero (30, 40, 50, etc.) for the account number to be validated.
    if (sum % 10) != 0:
        return 0

    return 1
