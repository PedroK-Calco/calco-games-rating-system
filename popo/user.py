from utilities.validation import *


class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id: int = user_id
        self._name: str = name
        self._email: str = email

    @property
    def user_id(self) -> int:
        return self._id

    @user_id.setter
    @int_validator
    def user_id(self, user_id: int):
        self._id = user_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @str_validator
    def name(self, name: str):
        self._name = name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    @str_validator
    def email(self, email: str):
        self._email = email
