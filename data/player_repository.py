import os

from popo import Player
from utilities import CSVReaderWriter, SQLReaderWriter

DB_FILE_PATH = "database/pool_player_db.csv"
DB_FILE_PATH_TEST = "database/pool_player_db_new.csv"
DB_FILE_PATH_TESTCASE = "database/pool_player_test_db.csv"


class PlayerRepository:
    def __init__(self):
        self._data: dict[int, Player] = {}
        self._data_columns: list = []

    def create(self, key: int, value: Player):
        """
        Creates a new Player class element in the repository
        :param key: The user_id of the new player
        :param value: The Player object with that player's data
        """
        if key not in self._data:
            self._data[key] = value.clone
            self._data_columns = list(value.to_dict.keys())
        else:
            raise ValueError(f"key: {key} already exists")

    def retrieve(self, index: int) -> Player:
        """
        Retrieves a Player object with a player's data from the repository
        :param index: The user_id of the player to retrieve
        :return: A Player object associated to the user_id
        """
        return self._data[index]

    def update(self, index: int, value: Player):
        """
        Updates the values of a player in the repository
        :param index: The user_id of the player to be updated
        :param value: The Player object with the new values
        """
        self._data[index] = value.clone

    def load(self):
        """
        Reads data from the database and stores it in the data attribute
        """
        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH_TESTCASE)

        data: dict[int, dict] = CSVReaderWriter.read_csv(file_name)

        for k, v in data.items():
            temp_player = Player("Pool", v["rating"], v["rd"], v["g(rd)"], k, v["name"], v["email"])
            self.create(k, temp_player)

    def load_test(self):
        query = "SELECT * FROM players_pool p JOIN users u ON p.user_id = u.id"

        data = SQLReaderWriter.retrieve(query)

        for x in data:
            print(x)

    def write(self):
        """
        Writes to the database the data in the data attribute
        """
        if len(self._data) == 0:
            raise ValueError("Repository is empty")

        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH_TESTCASE)

        data_dict: dict[int, dict] = {}

        for k, v in self._data.items():
            data_dict[k] = v.to_dict

        CSVReaderWriter.write_csv(file_name, data_dict, self._data_columns)
