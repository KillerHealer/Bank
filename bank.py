import bankAccount


class Bank:
    def __init__(self, accounts: []):
        self._accounts = accounts

    def __str__(self):
        s= ""
        for item in self._accounts:
            s = item.__str__()
        return s

    def load_and_parse_init_data(self):
        f = open("init.xml")
        self._accounts = f

    def add_new_account(self, bankacc):
        self._accounts.append(bankacc)

    def delete_by_userID(self, pid: int):
        bullseye = bankAccount.BankAccount
        for item in self._accounts:
            if item._personalInfo._id == pid:
                bullseye = item
                break
        self._accounts.remove(bullseye)
        if bullseye in self._accounts:
            return False
        else:
            return True

    def Withdraw_by_user_id(self, pid: int, cash: int):
        bullseye = bankAccount.BankAccount
        for item in self._accounts:
            if item._personalInfo._id == pid:
                bullseye = item
                break
        if bullseye.withdraw(cash):
            return True
        else:
            return False

    def Deposit_by_user_id(self, pid: int, cash: int):
        bullseye = bankAccount.BankAccount
        for item in self._accounts:
            if item._personalInfo._id == pid:
                bullseye = item
                break
        if bullseye.deposit(cash):
            return True
        else:
            return False

    def calc_balance_statistics(self):
        pass

