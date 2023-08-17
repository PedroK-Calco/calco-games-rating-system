from popo import Player
from utilities import CSVReaderWriter

DB_FILE_PATH = "data/database/pool_player_db.csv"
DB_FILE_PATH_TEST = "data/database/pool_player_db_new.csv"


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
        data: dict[int, dict] = CSVReaderWriter.read_csv("data/database/pool_player_db.csv")

        for k, v in data.items():
            temp_player = Player("Pool", v["rating"], v["rd"], v["g(rd)"], k, v["name"], v["email"])
            self.create(k, temp_player)

    def write(self):
        data_dict: dict[int, dict] = {}

        for k, v in self._data.items():
            data_dict[k] = {
                "name": v.name,
                "email": v.email,
                "rating": v.rating,
                "rd": v.deviation,
                "g(rd)": v.g_of_rd
            }

        CSVReaderWriter.write_csv(DB_FILE_PATH_TEST, data_dict)
