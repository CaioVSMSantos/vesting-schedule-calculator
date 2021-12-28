from ..abstract_classes.schedule_presenter import SchedulePresenter
from pandas.core.frame import DataFrame


class SchedulePresenter_Standard(SchedulePresenter):
    """
    Inherits the SchedulePresenter AbstractClass.
    This implementation sorts the rows of the Schedule DataFrame by
    Employee ID and Award ID and prints them to the console

    ...

    Methods
    -------
    present(schedule_dataframe) : DataFrame
        Parses and sorts the Schedule DataFrame and prints it to
        the console

    """
    def present(self, schedule_dataframe: DataFrame):
        """
        present(schedule_dataframe)
            Parses and sorts the Schedule DataFrame by Employee ID
            and Award ID and prints it to the console

        Parameters
        ----------
        schedule_dataframe : DataFrame
            A pandas DataFrame of the Schedule to be presented
        """
        schedule_dataframe.columns = ['EMPLOYEE ID', 'EMPLOYEE NAME',
                                      'AWARD ID', 'QUANTITY']
        schedule_dataframe = schedule_dataframe.sort_values(
            by=['EMPLOYEE ID', 'AWARD ID'])

        for index, row in schedule_dataframe.iterrows():
            formated_line = ','.join(row.values)
            print(formated_line)
