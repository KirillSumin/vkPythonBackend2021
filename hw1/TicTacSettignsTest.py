import unittest
from exceptions import *  # переделать
from unittest.mock import patch
from TicTacSettings import TicTacSettings
from TicTacComputer import TicTacComputer
from TicTacHuman import TicTacHuman


def empty_function(*args, **kwargs):
    pass


class TestTicTacSettingsTests(unittest.TestCase):
    def setUp(self):
        pass

    @patch('builtins.print', empty_function)
    def test_valid_settings(self):
        validation_sets = [
            {'input': ['2', 'cc'],
             'expected_players': [TicTacComputer('0'), TicTacComputer('x')], 'expected_size_of_field': 2},
            {'input': ['3', 'ch'],
             'expected_players': [TicTacComputer('0'), TicTacHuman('x')], 'expected_size_of_field': 3},
            {'input': ['100', 'hc'],
             'expected_players': [TicTacHuman('0'), TicTacComputer('x')], 'expected_size_of_field': 100},
            {'input': ['1000', 'hh'],
             'expected_players': [TicTacHuman('0'), TicTacHuman('x')], 'expected_size_of_field': 1000},
        ]
        settings = TicTacSettings()
        for validation_set in validation_sets:
            settings.user_input_size_of_field = lambda *args, **kwargs: validation_set.get('input')[0]
            settings.user_input_mod = lambda *args, **kwargs: validation_set.get('input')[1]
            settings.set_user_settings()
            self.assertEqual(settings.size_of_field, validation_set.get('expected_size_of_field'))
            self.assertEqual(settings.player1, validation_set.get('expected_players')[0])
            self.assertEqual(settings.player2, validation_set.get('expected_players')[1])

    def test_invalid_size_of_field(self):
        validation_sets = [
            {'input': ['0', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': ['-1', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': ['1', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': ['', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': ['c', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': ['-', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': ['@', 'cc'],
             'expected_raise': IncorrectSizeOfField},
            {'input': [' ', 'cc'],
             'expected_raise': IncorrectSizeOfField},
        ]
        settings = TicTacSettings()
        for validation_set in validation_sets:
            with self.assertRaises(validation_set.get('expected_raise')):
                settings.validate_size_of_field(validation_set.get('input')[0])

    def test_invalid_mod(self):
        validation_sets = [
            {'input': ['2', ''],
             'expected_raise': ModNotExist},
            {'input': ['3', '1'],
             'expected_raise': ModNotExist},
            {'input': ['4', '-1'],
             'expected_raise': ModNotExist},
            {'input': ['5', '@'],
             'expected_raise': ModNotExist},
            {'input': ['6', ' '],
             'expected_raise': ModNotExist},
            {'input': ['7', 'c'],
             'expected_raise': ModNotExist},
            {'input': ['8', 'h'],
             'expected_raise': ModNotExist},
        ]
        settings = TicTacSettings()
        for validation_set in validation_sets:
            with self.assertRaises(validation_set.get('expected_raise')):
                settings.validate_mod_and_choose_players(validation_set.get('input')[1])

    if __name__ == '__main__':
        unittest.main()
