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
        """
        Creates a new Match object and inserts it into the repository
        :param player_1: A Player object for one of the players in the match
        :param player_2: Another Player object for the other player in the match
        :param expected_outcome: Float values for both players indicating their odds of winning the match
        """
        match_id: int = self._get_new_id()
        match_game: str = "pool"
        match: Match = Match(match_id, player_1, player_2, match_game, "time", expected_outcome)

        self._data[match_id] = match
        self.write()

    def update(self):
        pass

    def retrieve(self, match_id: int) -> Match:
        """
        Retrieves a Match object from the repository
        :param match_id: The id of the match to be retrieved
        :return: A Match object containing player data and the odds of them winning
        """
        return self._data[match_id]

    def delete(self, match_id: int):
        """
        Remove a Match object from the repository
        :param match_id: The id of the match to be deleted
        """
        del self._data[match_id]
        self.write()

    def _get_new_id(self) -> int:
        """
        Creates a new id for a key value pair entry to the repository
        :return: An unused id from the existing repository
        """
        if self._data.__len__() == 0:
            last_id = 0
        else:
            last_id: int = sorted(self._data.keys())[-1]

        new_id: int = last_id + 1

        return new_id

    def load(self):
        """
        Reads data from the database and stores it in the data attribute
        """
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
        """
        Writes to the database the data in the data attribute
        """
        dir_caller = os.path.dirname(__file__)
        file_name = os.path.join(dir_caller, DB_FILE_PATH)

        data_dict: dict[int, dict] = {}

        for k, v in self._data.items():
            data_dict[k] = v.to_dict

        CSVReaderWriter.write_csv(file_name, data_dict)
