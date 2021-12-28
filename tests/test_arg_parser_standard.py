import directory_setup as tds
import unittest
from io import StringIO
from unittest.mock import patch
from src.classes.arg_parser_standard import ArgParser_Standard


class ArgParser_Standard_TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.arg_parser = ArgParser_Standard()

    def test_positional_args(self):
        args = self.arg_parser.parse_args(['data\\example1.csv', '2021-01-01'])
        self.assertEqual(args['File'], 'data\\example1.csv',
                         'File Arg should be data\\example1.csv')
        self.assertEqual(args['Date'], '2021-01-01',
                         'Date Arg should be 2021-01-01')

    @patch('sys.stderr', new_callable=StringIO)
    def test_incomplete_positional_args(self, mock_stderr):
        with self.assertRaises(SystemExit):
            self.arg_parser.parse_args(['data\\example1.csv'])
        self.assertRegexpMatches(mock_stderr.getvalue(),
                                 r"arguments are required")

    def test_precision_arg(self):
        args = self.arg_parser.parse_args(['data\\example1.csv',
                                           '2021-01-01', '5'])
        self.assertEqual(args['Precision'], 5, 'Precision should be 5')

    @patch('sys.stderr', new_callable=StringIO)
    def test_wrong_precision_arg(self, mock_stderr):
        with self.assertRaises(SystemExit):
            self.arg_parser.parse_args(['data\\example1.csv',
                                        '2021-01-01', '7'])
        self.assertRegexpMatches(mock_stderr.getvalue(),
                                 r"invalid choice")


if __name__ == '__main__':
    tds.tests_setup_confirm()
    unittest.main()
