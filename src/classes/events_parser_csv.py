from pandas.core.frame import DataFrame
from ..abstract_classes.events_parser import EventsParser
import pandas as pd
from ..utils.file_utils import exists, validate_extension


class EventsParser_CSV(EventsParser):
    """
    Inherits the EventsParser AbstractClass.
    This implementation parses a .csv vesting events file, adding
    headers for ease of use and returns it as a pandas DataFrame object.

    ...

    Methods
    -------
    parse(file_path) : DataFrame
        Parses the file_path into a DataFrame

    """
    def parse(self, file_path) -> DataFrame:
        """
        parse(file_path)
            Parses the vesting events file_path into a DataFrame

        Parameters
        ----------
        file_path
            A path to a .csv vesting events file to be parsed

        Returns
        -------
        DataFrame
            A DataFrame of the vesting events file with headers
        """
        self.__validate_file_path(file_path)
        column_names = ['VEST', 'EMPLOYEE ID', 'EMPLOYEE NAME', 'AWARD ID',
                        'DATE', 'QUANTITY']
        return pd.read_csv(file_path, names=column_names)

    def __validate_file_path(self, file_path):
        if exists(file_path) and validate_extension(file_path, '.csv'):
            return file_path
        else:
            raise FileNotFoundError(f'Invalid File {file_path}. '
                                    'File doesn\'t exist or is not a .csv')
