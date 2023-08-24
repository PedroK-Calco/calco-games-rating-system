import os

from popo import Match
from popo import Player

from data import PlayerRepository

from utilities import CSVReaderWriter

DB_FILE_PATH = "database/pool_match_db.csv"


class MatchRepository:
    def __init__(self, player_rep: PlayerRepository):
        self._data: dict[int, Match] = {}
        self._player_repo: PlayerRepository = player_rep

    def create(self, player_1: Player, player_2: Player, expected_outcome: dict[int, float]):
        match_id: int = self._get_new_id()
        match_game: str = "pool"
        match: Match = Match(match_id, player_1, player_2, match_game, "time", expected_outcome)

        self._data[match_id] = match
        self.write()

    def update(self):
        pass

    def retrieve(self, match_id: int) -> Match:
        return self._data[match_id]

    def delete(self, match_id: int):
        del self._data[match_id]
        self.write()

    def _get_new_id(self) -> int:
        if self._data.__len__() == 0:
            last_id = 0
        else:
            last_id: int = sorted(self._data.keys())[-1]

        new_id: int = last_id + 1

        return new_id

    def load(self):
        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH)

        data: dict[int, dict] = CSVReaderWriter.read_csv(file_name)

        for k, v in data.items():
            player_1: Player = self._player_repo.retrieve(v["player_1"])
            player_2: Player = self._player_repo.retrieve(v["player_2"])

            self.create(player_1, player_2, {
                v["player_1"]: v["expected_outcome_p1"],
                v["player_2"]: v["expected_outcome_p2"]
            })

    def write(self):
        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH)

        data_dict: dict[int, dict] = {}

        for k, v in self._data.items():
            data_dict[k] = v.to_dict

        CSVReaderWriter.write_csv(file_name, data_dict)
