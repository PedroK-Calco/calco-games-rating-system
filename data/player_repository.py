import os

from popo import Player
from utilities import CSVReaderWriter

DB_FILE_PATH = "database/pool_player_db.csv"
DB_FILE_PATH_TEST = "database/pool_player_db_new.csv"


class PlayerRepository:
    def __init__(self):
        self._data: dict[int, Player] = {}

    def create(self, key: int, value: Player):
        if key not in self._data:
            self._data[key] = value.clone
        else:
            raise ValueError(f"key: {key} already exists")

    def retrieve(self, index: int) -> Player:
        return self._data[index]

    def update(self, index: int, value: Player):
        self._data[index] = value.clone

    def load(self):
        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH)

        data: dict[int, dict] = CSVReaderWriter.read_csv(file_name)

        for k, v in data.items():
            temp_player = Player("Pool", v["rating"], v["rd"], v["g(rd)"], k, v["name"], v["email"])
            self.create(k, temp_player)

    def write(self):
        if len(self._data) == 0:
            raise ValueError("Repository is empty")

        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH_TEST)

        data_dict: dict[int, dict] = {}

        for k, v in self._data.items():
            data_dict[k] = v.to_dict

        CSVReaderWriter.write_csv(file_name, data_dict)
