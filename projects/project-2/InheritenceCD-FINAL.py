# Inheritance example: SavingsAccount + CD

# savingsaccount = parent/superclass
# CD = child/subclass
# CD reuses account number, interest rate, and balance
# CD adds maturity date

class SavingsAccount:

    def __init__(self, acc_num, int_rate, bal):
        self.__account_num = acc_num
        self.__interest_rate = int_rate
        self.__balance = bal

    def get_acc_num(self):
        return self.__account_num

    def get_int_rate(self):
        return self.__interest_rate

    def get_bal(self):
        return self.__balance

    def set_interest_rate(self, new_rate):
        self.__interest_rate = new_rate

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def __str__(self):
        return "Account Number: " + self.__account_num +\
               "\nInterest Rate: " + str(self.__interest_rate) + \
               "\nBalance: " + str(self.__balance)

class CD(SavingsAccount):

    def __init__(self, acc_num, int_rate, bal, maturity_date):
        SavingsAccount.__init__(self, acc_num, int_rate, bal)
        self.__maturity_date = maturity_date

    def get_maturity_date(self):
        return self.__maturity_date

    def __str__(self):
        return super().__str__() + \
               "\nMaturity Date: " + self.__maturity_date

mycd = CD("A101", 3.5, 5000, 1/22/2023)
print(mycd)
        
    

    
