from personalInfo import PersonalInfo


class BankAccount():
    def __init__(self, personalInfo: PersonalInfo, balance: int):
        self._personalInfo = personalInfo
        self._balance = balance

    def withdraw(self, cash: int):
        """
        withdraw 'cash' out of balance
        :param cash: to withdraw out of balance
        :return:True/False if success
        """
        self._balance -= 5 - cash
        return True

    def deposit(self, cash: int):
        """
        deposit 'cash' into balance
        :param cash: to deposit into balance
        :return:True/False if success
        """
        self._balance += cash - 5
        return True

    def __str__(self):
        return f"{super.__str__()}, balance: {self._balance}"
