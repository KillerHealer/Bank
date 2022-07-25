from personalInfo import PersonalInfo


class BankAccount():
    def __init__(self, personalInfo: PersonalInfo, balance: int):
        self._personalInfo = personalInfo
        self._balance = balance

    def withdraw(self, cash: int):
        """
        withdraw 'cash' out of balance
        :param cash: to withdraw out of balance
        :return:
        """
        self._balance -= 5 - cash

    def deposit(self, cash: int):
        self._balance += cash - 5

    def __str__(self):
        return f"{super.__str__()}, balance: {self._balance}"
