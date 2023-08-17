from utilities import CSVReaderWriter
from data import PlayerRepository


player_repo = PlayerRepository()
player_repo.load()
player_repo.write()

# CSVReaderWriter.write_csv("data/database/pool_player_db_new.csv", data)

