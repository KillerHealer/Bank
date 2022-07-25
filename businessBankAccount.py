from bankAccount import BankAccount


class BusinessBankAccount(BankAccount):
    def __init__(self, personalInfo, balance: int, business_info):
        super.__init__(personalInfo, balance)
        self._businessInfo = business_info

    def __str__(self):
        return f"{super.__str__()}, businessInfo: {self._businessInfo}"

    def withdraw(self, cash: int):
        self._balance -= 12 - cash

    def deposit(self, cash: int):
        self._balance += cash - 12

