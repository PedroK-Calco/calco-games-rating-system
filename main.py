from utilities import CSVReaderWriter

data = CSVReaderWriter.read_csv("data/database/pool_player_db.csv")
CSVReaderWriter.write_csv("data/database/pool_player_db_new.csv", data)

