from ..abstract_classes.schedule import Schedule
from pandas.core.frame import DataFrame
from pandas.core.series import Series
from math import trunc
import sys


class Schedule_Standard(Schedule):
    """
    Inherits the Schedule AbstractClass.
    This implementation uses the get_schedule method to parse
    the vesting events DataFrame, extracting unique identifiers
    (composed by Employee ID, Employee Name and Award ID) and
    calculating the quantity of vesting to each one up to and
    including the given arg Date

    ...

    Methods
    -------
    get_schedule(events, args) : DataFrame
        Parses the events DataFrame into a Schedule DataFrame.
        args should include 'Date' and 'Precision'

    """
    def get_schedule(self, events: DataFrame, args: dict) -> DataFrame:
        """
        get_schedule(events, args)
            Parses the events into a Schedule.

        Parameters
        ----------
        events : DataFrame
            A pandas DataFrame of the vesting events to be parsed. This
            implementation requires the DataFrame to be composed of the
            columns:
                'VEST'
                'EMPLOYEE ID'
                'EMPLOYEE NAME'
                'AWARD ID',
                'DATE'
                'QUANTITY'

        args : dict
            Args that are used to calculate the Schedule. This
            implementation requires that it should include
            'Date' and 'Precision'

        Returns
        -------
        DataFrame
            A DataFrame of the vesting Schedule
        """
        self.__validate_headers(events, args)

        row_id_separator = '|'
        tmp_schedule = {}
        for index, row in events.iterrows():
            row_id = self.__get_row_id(row, row_id_separator)
            tmp_schedule[row_id] = self.__calculate_row(row, tmp_schedule,
                                                        row_id, args)

        schedule_df = self.__schedule_dict_to_dataframe(tmp_schedule,
                                                        row_id_separator)
        return schedule_df

    def __validate_headers(self, events_df: DataFrame, args: dict) -> bool:
        cols = ['VEST', 'EMPLOYEE ID', 'EMPLOYEE NAME', 'AWARD ID',
                'DATE', 'QUANTITY']
        columns_check = all(item in events_df.columns for item in cols)

        if not columns_check:
            raise Exception('Events Dataframe received doesn\'t have '
                            'compatible column headers')
        return True

    def __get_row_id(self, row: Series, separator: str) -> str:
        """
        Returns a string composed of the unique
        identifier of the given row, in the format:

        "<EMPLOYEE ID><S><EMPLOYEE NAME><S><AWARD ID>"

        where the <s> is a symbol, usually a '|' used as separator
        """
        row_id = (f'{row["EMPLOYEE ID"]}{separator}'
                  f'{row["EMPLOYEE NAME"]}{separator}'
                  f'{row["AWARD ID"]}')
        return row_id

    def __calculate_row(self, row, schedule_dict: dict,
                        row_id: str, args: dict):
        """
        Returns the value of the unique row identifier based on
        a series of verifications, like the existence of the
        identifier in the schedule_dict, the target date of the
        schedule and the type of event (Vest or Cancel)
        """
        try:
            identifier_exists = row_id in schedule_dict
            inside_schedule_date = row['DATE'] <= args['Date']
            is_vest = row['VEST'] == 'VEST'
            is_cancel = row['VEST'] == 'CANCEL'

            result = 0

            if (not identifier_exists) and (not inside_schedule_date):
                result = 0
            elif (not identifier_exists) and (inside_schedule_date):
                result = row['QUANTITY']
            elif identifier_exists and (not inside_schedule_date):
                result = float(schedule_dict[row_id])
            elif identifier_exists and inside_schedule_date:
                if is_vest:
                    result = float(schedule_dict[row_id]) + row['QUANTITY']
                elif is_cancel:
                    result = float(schedule_dict[row_id]) - row['QUANTITY']
                    result = result if result > 0 else 0

            result = self.__set_precision(result, args['Precision'])
            return result
        except TypeError:
            sys.exit('Error during Events Row Calculation: Events Dataframe '
                     'seems to have an incompatible structure')

    def __schedule_dict_to_dataframe(self, schedule_dict: dict,
                                     row_id_separator: str):
        """
        Converts the temporary dict used to store the unique
        vesting identifiers and their values into a pandas
        DataFrame
        """
        df_row = 1
        tmp_dict = {}
        for k, v in schedule_dict.items():
            tmp_list = k.split(row_id_separator)
            tmp_list.append(str(v))
            tmp_dict[df_row] = tmp_list
            df_row += 1
        schedule_df = DataFrame.from_dict(data=tmp_dict, orient='index')
        return schedule_df

    def __set_precision(self, number, precision: int) -> str:
        """
        Sets the decimal precision of the number and adds trailling
        zeros
        """
        if precision > 0:
            return '%.{0}f'.format(precision) % number
        else:
            return str(trunc(number))
