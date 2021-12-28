import directory_setup as tds
import unittest
import src.utils.file_utils as fu


class FileUtils_TestCase(unittest.TestCase):
    def test_exists(self):
        # Existent File Path
        valid_file = fu.exists('data\\example1.csv')
        self.assertTrue(valid_file, 'Should be True')

        # Not Existent File Path
        invalid_file = fu.exists('data\\not_a_file.txt')
        self.assertFalse(invalid_file, 'Should be False')

    def test_get_extension(self):
        # Existent File Path and Extension
        csv = fu.get_extension('data\\example1.csv')
        self.assertEqual(csv, '.csv', 'Should be .csv')

        # Not Existent File Path
        none_extension = fu.get_extension('data\\not_a_file.txt')
        self.assertIsNone(none_extension, 'Should be None')

    def test_validate_extension(self):
        # Correct Validation
        valid_extension = fu.validate_extension('data\\example1.csv', '.csv')
        self.assertTrue(valid_extension, 'Should be True')

        # Incorrect Validation
        invalid_extension = fu.validate_extension('data\\wrong_file.txt',
                                                  '.csv')
        self.assertFalse(invalid_extension, 'Should be False')


if __name__ == '__main__':
    tds.tests_setup_confirm()
    unittest.main()
