from bankAccount import BankAccount


class StudentBankAccount(BankAccount):
    def __init__(self, personalInfo, balance: int, college_name: str):
        super.__init__(personalInfo, balance)
        self._collegeName = college_name

    def __str__(self):
        return f"{super.__str__()}, college name: {self._collegeName}"

    def withdraw(self, cash: int):
        if self._balance - 5 - cash <= 0:
            print("The balance of this student will be bellow 0 so please choose a different amount")
        else:
            self._balance -= 5 - cash
