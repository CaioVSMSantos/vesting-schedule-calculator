""" Vesting Schedule Calculator

This script allows the user to print to the console a vesting schedule
up to and including a given date.

The Standard implementation accepts a .csv file without headers and
the following columns:
    VEST
        An Identifier if the value of the event is Vested `VEST` or
        Cancelled `CANCEL`
    EMPLOYEE ID
        A Unique Identifier for the Employee
    EMPLOYEE NAME
        Name of the Employee
    AWARD ID
        Unique Identifier of the equity
    QUANTITY
        The amount to be vested/cancelled

The output is a list of calculated quantities per employee and per
award. Example:
    E001,Alice Smith,ISO-001,2000.0
    E001,Alice Smith,ISO-002,800.0
    E002,Bobby Jones,NSO-001,600.0
    E003,Cat Helms,NSO-002,0.0

This script's requirements are included in the `requirements.txt`
file. It also requires the packages `abstract_classes`, `classes` and
`utils` inside the `src` directory

"""

import sys
from src.classes.arg_parser_standard import ArgParser, ArgParser_Standard
from src.classes.events_parser_csv import EventsParser, EventsParser_CSV
from src.classes.schedule_standard import Schedule, Schedule_Standard
from src.classes.schedule_presenter_standard import \
    SchedulePresenter, SchedulePresenter_Standard


class VestingScheduleCalculator():
    """
    Performs the calculation of a vesting schedule

    ...

    Methods
    -------
    execute()
        Executes the Calculator, using the objects passed during
        instantiation

    """
    def __init__(self, arg_parser: ArgParser,
                 events_parser: EventsParser,
                 schedule: Schedule,
                 presenter: SchedulePresenter):
        """
        Parameters
        ----------
        arg_parser : ArgParser
            It should be able to parse two
            positional args `File` and `Date`
        events_parser : EventsParser
            Parses the vesting events file into a pandas DataFrame
        schedule : Schedule
            Parses a vesting events pandas DataFrame into a schedule
            DataFrame
        presenter : SchedulePresenter
            Used to present the schedule in a pandas DataFrame into
            console or other appropriate format

        """
        self.__arg_parser = arg_parser
        self.__events_parser = events_parser
        self.__schedule = schedule
        self.__presenter = presenter

    def execute(self):
        """
        execute()

        Executes the Calculator, using the objects passed during
        instantiation

        """
        args = self.__arg_parser.parse_args(sys.argv[1:])
        self.__validate_positional_args(args)
        events_df = self.__events_parser.parse(args['File'])
        schedule_df = self.__schedule.get_schedule(events_df, args)
        self.__presenter.present(schedule_df)

    def __validate_positional_args(self, args: dict):
        is_file_existant = 'File' in args
        is_date_existant = 'Date' in args

        if not is_file_existant:
            raise Exception('Required Positional Arg '
                            '`File` couldn\'t be found')
        if not is_date_existant:
            raise Exception('Required Positional Arg '
                            '`Date` couldn\'t be found')


def main():
    arg_parser = ArgParser_Standard()
    file_parser = EventsParser_CSV()
    schedule = Schedule_Standard()
    presenter = SchedulePresenter_Standard()

    calculator = VestingScheduleCalculator(arg_parser,
                                           file_parser,
                                           schedule,
                                           presenter)
    try:
        calculator.execute()
    except Exception as error:
        sys.exit(f'An error ocurred: {error}')


if __name__ == '__main__':
    main()
