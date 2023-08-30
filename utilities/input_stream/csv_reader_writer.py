import pandas


class CSVReaderWriter:
    """
    Read and writer IO for .csv files containing player data.
    The methods will format the data to and from a dictionary nested with dictionaries of user data
    """
    @staticmethod
    def read_csv(file_path: str) -> dict[int, dict]:
        """
        Reads the player data csv file and converts the data to a dictionary nested with dictionaries structure
        :param file_path: Path of csv file to be read
        :return: Formatted data read from the csv file
        """
        data = pandas.read_csv(file_path, sep=";")

        dict_index = data.columns.values[0]

        data = data.set_index(dict_index)

        data = data.to_dict("index")

        return data

    @staticmethod
    def write_csv(file_path: str, data: dict[int, dict], columns: list):
        # Will have to be changed at a later date to only write context player's data
        """
        Writes the entire data set to a csv file at a target file path.
        The data is transformed into a legible format for the red_csv() method.
        :param columns:
        :param file_path: Path and name of file to write to / create
        :param data: Data set to be written to the csv
        :return:
        """
        columns: list = columns

        df = pandas.DataFrame.from_dict(data, orient="index", columns=columns[1:])
        df = df.reset_index()
        df = df.rename(columns={'index': columns[0]})

        df.to_csv(file_path, sep=";", index=False)

