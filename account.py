class Account():
    # set up the class
    def __init__(self, number:int, open_amt:float):
        self.__account_number = number
        self.__balance = open_amt

 # adds money to the current balance
    def deposit(self, amt:float)->float:
        self.__balance = self.__balance + amt

 # removes money from account money but doesnt let acount total be less than 5
    def withdraw(self,amt:float)-> float:
        amount = self.__balance - amt
        if amount <= 4.99:
            print('couldn\'t complete transaction, balance drops bellow $5.00'),
            return 0.00
        else:
            self.__balance = amount
            return amt

 # gives user balance of their account
    def getBalance(self)->float:
        return self.__balance

 # returns accounts number
    def getAccountNumber(self)->int:
        return self.__account_number
