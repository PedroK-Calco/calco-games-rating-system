import pandas


class CSVReaderWriter:
    """
    Read and writer IO for .csv files containing player data.
    The methods will format the data to and from a dictionary nested with dictionaries of user data
    """
    @staticmethod
    def read_csv(file_path: str) -> dict[dict]:
        """
        Reads the player data csv file and converts the data to a dictionary nested with dictionaries structure
        :param file_path: Path of csv file to be read
        :return: Formatted data read from the csv file
        """
        data = pandas.read_csv(file_path, sep=";")

        data = data.set_index('user_id')

        data = data.to_dict("index")

        return data

    @staticmethod
    def write_csv(file_path: str, data: dict):
        # Will have to be changed at a later date to only write context player's data
        """
        Writes the entire data set to a csv file at a target file path.
        The data is transformed into a legible format for the red_csv() method.
        :param file_path: Path and name of file to write to / create
        :param data: Data set to be written to the csv
        :return:
        """
        df = pandas.DataFrame.from_dict(data, orient="index", columns=["name", "email", "rating", "rd", "g(rd)"])
        df = df.reset_index()
        df = df.rename(columns={'index': 'user_id'})

        df.to_csv(file_path, sep=";", index=False)
