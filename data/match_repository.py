from popo import Match


class MatchRepository:
    def __init__(self):
        self._data: dict[int, Match] = {}

    def create(self, player_1_id: int, player_2_id: int, expected_outcome: dict[int, float]):
        match_id: int = self._get_new_id()
        match_game: str = "pool"
        match: Match = Match(match_id, player_1_id, player_2_id, match_game, "time", expected_outcome)

        self._data[match_id] = match

    def update(self):
        pass

    def retrieve(self, match_id: int) -> Match:
        return self._data[match_id]

    def delete(self, match_id: int):
        self._data.pop(match_id)

    def _get_new_id(self) -> int:
        last_id: int = sorted(self._data.keys())[-1]

        new_id: int = last_id + 1

        return new_id
