class PersonalInfo:
    def __init__(self, name: str, id: int, phoneNumber: int, emailadress: str):
        self._name = name
        self._id = id
        self._phoneNum = phoneNumber
        self._emailAdd = emailadress

    def __str__(self):
        return f"Name: {self._name}, id: {self._id}, phone number: {self._phoneNum}, email address: {self._emailAdd}"