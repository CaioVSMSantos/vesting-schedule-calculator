from pandas.core.frame import DataFrame
import pandas as pd
import directory_setup as tds
import unittest
from src.classes.schedule_standard import Schedule_Standard


class Schedule_Standard_TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.event_parser = Schedule_Standard()

        d = {1: ['VEST', 'ID1', 'Ann', 'A1', '2020-01-01', 500],
             2: ['VEST', 'ID2', 'Bob', 'A2', '2020-01-01', 300],
             3: ['CANCEL', 'ID1', 'Ann', 'A1', '2020-01-01', 200],
             4: ['VEST', 'ID2', 'Bob', 'A2', '3030-01-01', 300],
             5: ['VEST', 'ID3', 'Clark', 'A3', '2020-01-01', 1000]}
        columns = ['VEST', 'EMPLOYEE ID', 'EMPLOYEE NAME',
                   'AWARD ID', 'DATE', 'QUANTITY']
        self.test_events_df = DataFrame.from_dict(data=d, orient='index',
                                                  columns=columns)

    def test_set_precision(self):
        # Precision 0, integer
        number = self.event_parser._Schedule_Standard__set_precision(99, 0)
        self.assertEqual(number, '99', 'Should be 99')

        # Precision 2, float
        number = self.event_parser._Schedule_Standard__set_precision(99, 2)
        self.assertEqual(number, '99.00', 'Should be 99.00')

        # Wrong arg, string
        with self.assertRaises(TypeError):
            number = self.event_parser. \
                _Schedule_Standard__set_precision('Hello', 2)

    def test_schedule_dict_to_dataframe(self):
        dict1 = {'ID1|Ann|A1': '400', 'ID2|Bob|A2': 600, 'ID3|Clark|A3': 700}
        dict2 = {'Ann': '400', 'Bob': 600, 'Clark': 700}

        # DataFrame size, columns and rows
        df = self.event_parser. \
            _Schedule_Standard__schedule_dict_to_dataframe(dict1, '|')
        self.assertEqual(type(df), DataFrame, 'Should be a DataFrame')
        self.assertEqual(len(df), 3, 'Should have 3 rows')
        self.assertEqual(len(df.columns), 4, 'Should have 4 columns')
        self.assertEqual(df.size, 12, 'Should have 12 cells')

        # DataFrame size, columns and rows
        df = self.event_parser. \
            _Schedule_Standard__schedule_dict_to_dataframe(dict2, '|')
        self.assertEqual(type(df), DataFrame, 'Should be a DataFrame')
        self.assertEqual(len(df), 3, 'Should have 3 rows')
        self.assertEqual(len(df.columns), 2, 'Should have 2 columns')
        self.assertEqual(df.size, 6, 'Should have 6 cells')

        # Wrong args Error
        not_a_dict = ['This', 'is', 'not', 'a', 'dictionary']
        with self.assertRaises(AttributeError):
            df = self.event_parser. \
                _Schedule_Standard__schedule_dict_to_dataframe(not_a_dict, '|')

    def test_get_row_id(self):
        row_clark = ['VEST', 'ID3', 'Clark', 'A3', '3030-01-01', 500]
        row_index = ['VEST', 'EMPLOYEE ID', 'EMPLOYEE NAME',
                     'AWARD ID', 'DATE', 'QUANTITY']
        ser = pd.Series(data=row_clark, index=row_index)

        # Testing with standard | separator
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '|')
        self.assertEqual(row_id, 'ID3|Clark|A3', 'Should be \'ID3|Clark|A3\'')

        # Testing with -- separator
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '--')
        self.assertEqual(row_id, 'ID3--Clark--A3',
                         'Should be \'ID3|Clark|A3\'')

    def test_calculate_row(self):
        d = {'ID1|Ann|A1': 400, 'ID2|Bob|A2': 600}

        row_index = ['VEST', 'EMPLOYEE ID', 'EMPLOYEE NAME',
                     'AWARD ID', 'DATE', 'QUANTITY']
        row_clark_zero = ['VEST', 'ID3', 'Clark', 'A3', '3030-01-01', 500]
        row_dan_300 = ['VEST', 'ID4', 'Dan', 'A1', '2020-01-01', 300]
        row_ann_out_date = ['VEST', 'ID1', 'Ann', 'A1', '3030-01-01', 300]
        row_bob_900 = ['VEST', 'ID2', 'Bob', 'A2', '2020-01-01', 300]
        row_bob_400 = ['CANCEL', 'ID2', 'Bob', 'A2', '2020-01-01', 500]

        args = {'Date': '2021-01-01', 'Precision': 0}

        # New ID out of Date
        ser = pd.Series(data=row_clark_zero, index=row_index)
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '|')
        result = self.event_parser. \
            _Schedule_Standard__calculate_row(ser, d, row_id, args)
        self.assertEqual(result, '0', 'Result should be 0')

        # New ID with valid Date
        ser = pd.Series(data=row_dan_300, index=row_index)
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '|')
        result = self.event_parser. \
            _Schedule_Standard__calculate_row(ser, d, row_id, args)
        self.assertEqual(result, '300', 'Result should be 300')

        # Old ID out of Date
        ser = pd.Series(data=row_ann_out_date, index=row_index)
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '|')
        result = self.event_parser. \
            _Schedule_Standard__calculate_row(ser, d, row_id, args)
        self.assertEqual(result, '400', 'Result should be 400')

        # Old ID with valid Date, Vest
        ser = pd.Series(data=row_bob_900, index=row_index)
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '|')
        result = self.event_parser. \
            _Schedule_Standard__calculate_row(ser, d, row_id, args)
        self.assertEqual(result, '900', 'Result should be 900')

        # Old ID with valid Date, Cancel
        ser = pd.Series(data=row_bob_400, index=row_index)
        row_id = self.event_parser. \
            _Schedule_Standard__get_row_id(ser, '|')
        result = self.event_parser. \
            _Schedule_Standard__calculate_row(ser, d, row_id, args)
        self.assertEqual(result, '100', 'Result should be 100')

    def test_get_schedule(self):
        args = {'Date': '2021-01-01', 'Precision': 2}
        df = self.event_parser.get_schedule(self.test_events_df, args)

        self.assertEqual(type(df), DataFrame, 'Should be a DataFrame')
        self.assertEqual(len(df), 3, 'Should have 3 rows')
        self.assertEqual(len(df.columns), 4, 'Should have 4 columns')
        self.assertEqual(df.size, 12, 'Should have 12 cells')


if __name__ == '__main__':
    tds.tests_setup_confirm()
    unittest.main()
