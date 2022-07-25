from bankAccount import BankAccount


class BusinessBankAccount(BankAccount):
    def __init__(self, personalInfo, balance: int, business_info):
        super().__init__(personalInfo, balance)
        self._businessInfo = business_info

    def __str__(self):
        return f"{super().__str__()}, businessInfo: {self._businessInfo}"

    def withdraw(self, cash: int):
        """
        withdraw 'cash' out of balance
        :param cash: to withdraw out of balance
        :return:True/False if success
        """
        self._balance -= 12 - cash
        return True

    def deposit(self, cash: int):
        """
        deposit 'cash' into balance
        :param cash: to deposit into balance
        :return:True/False if success
        """
        self._balance += cash - 12
        return True

