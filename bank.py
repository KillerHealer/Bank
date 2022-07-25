import xml.etree.ElementTree as et
from statistics import median
import numpy as np
import xml.dom.minidom as MD
import bankAccount
import personalInfo
import studentBankAccount
import businessBankAccount


class Bank:
    def __init__(self, accounts: []):
        self._accounts = accounts

    def __str__(self):
        s = ""
        for item in self._accounts:
            s += item.__str__() + "\n"
        return s

    def load_and_parse_init_data(self):
        """
        loads and parses data from init.xml
        :return: True/False for success
        """
        f = open("init.xml")
        tree = et.parse(f)
        root = tree.getroot()
        for item in root.findall('account'):
            if item.attrib['type'] == "StudentBankAccount":
                a1 = studentBankAccount.StudentBankAccount(
                    personalInfo.PersonalInfo(item[0][0].text, int(item[0][1].text),
                                              item[0][2].text, item[0][3].text),
                    int(item[1].text), item[2].text)
                self.add_new_account(a1)
            if item.attrib['type'] == "BankAccount":
                a2 = bankAccount.BankAccount(personalInfo.PersonalInfo(item[0][0].text, int(item[0][1].text),
                                                                       item[0][2].text, item[0][3].text),
                                             int(item[1].text))
                self.add_new_account(a2)
            if item.attrib['type'] == "BusinessBankAccount":
                a3 = businessBankAccount.BusinessBankAccount(
                    personalInfo.PersonalInfo(item[0][0].text, int(item[0][1].text),
                                              item[0][2].text, item[0][3].text),
                    int(item[1].text), item[2])
                self.add_new_account(a3)

    def add_new_account(self, bankacc):
        """
        adds a new account to the bank (but not to the file)
        :param bankacc: the account to add to the bank
        :return: True/False for success
        """
        if isinstance(bankacc, bankAccount.BankAccount):
            self._accounts.append(bankacc)
            return True
        else:
            return False

    def delete_by_userID(self, pid: int):
        """
        searches for the account with the id provided and deletes it from the bank
        (but not from the file)
        :param pid: the personal id to search for in the bank
        :return: True/False for success
        """
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
        """
        searches for the account with the id provided and withdraws the amount provided
        (doesn't update in file)
        :param pid: the personal id to search for in the bank
        :param cash: the amount to withdraw from the bank account
        :return: True/False for success
        """
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
        """
        searches for the account with the id provided and deposits the amount provided
        (doesn't update in file)
        :param pid: the personal id to search for in the bank
        :param cash: the amount to deposit to the bank account
        :return: True/False for success
        """
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
        """
        this function returns the average,
        the median,  90th percentile and 10th percentile of balances
        of all already added clients of the bank
        :return:a dictionary that has: average, median,
         90th percentile and 10th percentile of the balances
        """
        balances = []
        cnt = 0
        isum = 0
        for item in self._accounts:
            balances[cnt] = item._balance
            cnt += 1
            isum += item._balance
        ave = isum / len(balances)
        medi = median(balances)
        nine = np.percentile(balances, 90)
        one = np.percentile(balances, 10)
        result = {"average": ave, "median": medi, "90 percentile": nine, "10 percentile": one}
        return result


b1 = Bank([])
b1.load_and_parse_init_data()
print(b1)
