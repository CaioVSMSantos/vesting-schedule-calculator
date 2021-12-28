from ..abstract_classes.arg_parser import ArgParser
import argparse as ap
from datetime import datetime
from ..utils.file_utils import exists


class ArgParser_Standard(ArgParser):
    """
    Inherits the ArgParser Abstract Class.
    Uses the argparse module.

    ...

    Methods
    -------
    parse_args(args) : dict, abstract
        parses the args using the parser defined in the constructor

    """
    def __init__(self):
        """
        Defines an ArgumentParser object and add three arguments. They
        can be checked with the -h command upon running the main script

        """
        self.__arg_parser = ap.ArgumentParser(
            description='Generates a Vesting Schedule up to and including a '
                        'specified date, from a structured events file')
        self.__arg_parser.add_argument('File',
                                       metavar='file',
                                       type=self.__validate_file,
                                       help='the file with vesting entries')

        self.__arg_parser.add_argument('Date',
                                       metavar='date',
                                       type=self.__validate_string_date,
                                       help=('the date which vesting '
                                             'will be calculated'))

        self.__arg_parser.add_argument('Precision',
                                       metavar='precision',
                                       type=int,
                                       default=0,
                                       choices=range(0, 7),
                                       nargs='?',
                                       help=('Optional. the number of '
                                             'precision digits of vesting '
                                             'quantities'))

    def __validate_string_date(self, date_arg) -> str:
        try:
            datetime.strptime(date_arg, '%Y-%m-%d')
            return date_arg
        except ValueError:
            raise ValueError(f'Invalid Date Value: {date_arg}. '
                             'Format should be yyyy-MM-dd')

    def __validate_file(self, file_arg) -> str:
        if exists(file_arg):
            return file_arg
        else:
            raise FileNotFoundError(f'Invalid File {file_arg}. '
                                    'File doesn\'t exist')

    def parse_args(self, args) -> dict:
        """
        parse_args(args)

        Parses the args passed as arguments using the ArgumentParser
        defined in the constructor.

        Parameters
        ----------
        args
            An object, usually a list or Namespace, with the args to
            be parsed

        Returns
        -------
        dict
            A dictionary of arguments
        """
        return vars(self.__arg_parser.parse_args(args))
