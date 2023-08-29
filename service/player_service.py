from popo import Player
from data import PlayerRepository
from service import glicko


class PlayerService:
    def __init__(self, repo: PlayerRepository):
        self._repository: PlayerRepository = repo

        self._repository.load()

    def get_player(self, user_id: int) -> Player:
        """
        Retrieves a Player object from the player repository based on its id
        :param user_id: The id of the player to retrieve
        :return: A Player object of the player
        """
        return self._repository.retrieve(user_id)

    def update_player(self, user_id: int, player: Player):
        """
        Updates a player's data in the repository based on the new data of a Player object
        :param user_id: The id of the player to update the values
        :param player: The Player object with new player data
        """
        self._repository.update(user_id, player)

    def save_player_data(self):
        """
        Writes the player repository to a .csv file
        """
        self._repository.write()

    def update_time_player(self, player: Player):
        player.deviation = glicko.calculate_rd_time(player.deviation)

        self.update_player(player.user_id, player)
