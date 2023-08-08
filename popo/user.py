from validation import validator


class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id: int = user_id
        self._name: str = name
        self._email: str = email

    @property
    def user_id(self) -> int:
        return self._id

    @user_id.setter
    @validator(lambda n: n < 0, ValueError("User ID can't be less than 0"))
    def user_id(self, user_id: int):
        self._id = user_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @validator(lambda n: [n == "", n is None], ValueError("Name can't be blank or None"))
    def name(self, name: str):
        self._name = name

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    @validator(lambda n: [n == "", n is None], ValueError("Name can't be blank or None"))
    def email(self, email: str):
        self._email = email
