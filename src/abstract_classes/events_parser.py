from abc import ABC, abstractmethod
from pandas.core.frame import DataFrame


class EventsParser(ABC):
    """
    Abstract class.
    A Concrete Class that inherits it should implement a parse
    method, responsible to parse the file received as a parameter
    and return a pandas DataFrame

    ...

    Methods
    -------
    parse(file_path) : DataFrame, abstract
        Parses the file into a DataFrame

    """
    @abstractmethod
    def parse(self, file_path) -> DataFrame:
        """
        parse(file_path)
            Abstract Method.
            Parses the file into a DataFrame

        Parameters
        ----------
        file_path
            A path to a vesting events file to be parsed

        Returns
        -------
        DataFrame
            A DataFrame of the vesting events file
        """
        pass
