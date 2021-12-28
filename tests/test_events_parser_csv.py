from pandas.core.frame import DataFrame
import directory_setup as tds
import unittest
from src.classes.events_parser_csv import EventsParser_CSV


class EventParser_CSV_TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.event_parser = EventsParser_CSV()

    def test_existent_csv_file(self):
        dataframe = self.event_parser.parse('data\\example1.csv')
        self.assertEqual(type(dataframe), DataFrame,
                         'Should return a DataFrame')

    def test_existent_not_csv_file(self):
        with self.assertRaises(FileNotFoundError):
            self.event_parser.parse('data\\wrong_file.txt')

    def test_not_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.event_parser.parse('data\\not_a_file.txt')


if __name__ == '__main__':
    tds.tests_setup_confirm()
    unittest.main()
