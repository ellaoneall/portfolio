# BankAccount Class Example

# goal: to write a class that stores account ID and balance
# and can deposit, withdraw money, return balance, display object info with __str__


class BankAccount:

    def __init__(self, myid, mybal):
        self.__id = myid
        self.__balance = mybal

    def deposit(self, myamount):
        self.__balance += myamount

    def withdraw(self, my_amount):
        if self.__balance >= my_amount:
            self.__balance -= my_amount

        else:
            print("insufficient balance!")

    def get_balance(self):
        return self.__balance

    def set_balance(self, my_amount):
        self.__balance = my_amount

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def __str__(self):
        return "The balance is $" + format(self.__balance, ',.2f') + "\nMy ID: " + self.__id

def main():

    mysaving = BankAccount(my_id, start_bal)

    depositamount = float(input("Please eneter deposit amount: "))
    mysaving.desposit(depositamount)

    withdraw_amount = float(input("Please enter withdraw amount: "))
    mysaving.withdraw(withdraw_amount)

    print(mysaving)

main()


# REMEMBER THIS PATTERN

class Classname:

    def __init__(self, inputs):
        self.__attribute = input

    def set_attribtue(self, value):
        self.__attribute = value

    def get_attribute(self):
        return self.__attribute

    def __str__(self):
        return "formatted object info"


def main():

    object = Classname(arguments)
    object.method()
    print(obj)

main()
