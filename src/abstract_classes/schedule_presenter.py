from abc import ABC, abstractmethod
from pandas.core.frame import DataFrame


class SchedulePresenter(ABC):
    """
    Abstract class.
    A Concrete Class that inherits it should implement a present
    method, responsible to parse a vesting Schedule pandas DataFrame
    and present it into a desired format, like console or a file

    ...

    Methods
    -------
    present(schedule_dataframe) : DataFrame, abstract
        Parses the DataFrame into a desired format like console or a file

    """
    @abstractmethod
    def present(self, schedule_dataframe: DataFrame):
        """
        present(schedule_dataframe)
            Abstract Method.
            Parses the DataFrame into a desired
            format like console or a file

        Parameters
        ----------
        schedule_dataframe : DataFrame
            A pandas DataFrame of the Schedule to be presented
        """
        pass
