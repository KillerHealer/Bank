import bankAccount


class Bank:
    def __init__(self, accounts = []):
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

    def delete_by_userID(self):
        pass

    def Withdraw_by_user_id(self, id: int):
        bulseye = 0
        for item in self._accounts:
            if item._personalInfo._id == id:
                pass

    def Deposit_by_user_id(self):
        pass

    def calc_balance_statistics(self):
        pass

