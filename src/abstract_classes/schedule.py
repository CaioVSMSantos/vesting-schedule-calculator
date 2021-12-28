from pandas.core.frame import DataFrame
from abc import ABC, abstractmethod


class Schedule(ABC):
    """
    Abstract class.
    A Concrete Class that inherits it should implement a get_schedule
    method, responsible to parse a vesting events pandas DataFrame and
    calculate the Schedule using the implemented logic.

    ...

    Methods
    -------
    get_schedule(events, args=None) : DataFrame, abstract
        Parses the events DataFrame into a Schedule DataFrame

    """
    @abstractmethod
    def get_schedule(self, events: DataFrame, args: dict = None) -> DataFrame:
        """
        get_schedule(events, args)
            Abstract Method.
            Parses the events into a Schedule

        Parameters
        ----------
        events : DataFrame
            A pandas DataFrame of the vesting events to be parsed
        args : dict, optional
            Args that can be used to calculate the Schedule, like dates
            and decimal Precision of quantities

        Returns
        -------
        DataFrame
            A DataFrame of the vesting Schedule
        """
        pass
