from TicTacHuman import TicTacHuman
from TicTacComputer import TicTacComputer
from exceptions import *


class TicTacSettings:
    def __init__(self):
        self.size_of_field = None
        self.player1 = None
        self.player2 = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__
        return NotImplemented

    def set_user_settings(self):
        input_size_of_field = None
        player1 = None
        player2 = None

        print('Это игра в крестики нолики!')

        while input_size_of_field is None or player1 is None or player2 is None:
            try:
                input_size_of_field = self.validate_size_of_field(self.user_input_size_of_field())
                player1, player2 = self.validate_mod_and_choose_players(self.user_input_mod())
            except IncorrectSizeOfField:
                print('Некорректный ввод, можно ввести числа от 2 до oo, повторите ввод')
            except ModNotExist:
                print('Некорректный ввод, такого режима нет, повторите ввод')

        self.size_of_field = input_size_of_field
        self.player1 = player1
        self.player2 = player2

    def user_input_size_of_field(self):
        return input('Введите размер поля для игры (n x n)(числа от 2 до oo)\n')

    def user_input_mod(self):
        return input('Введите режим игры ('
                     '"cc" - компьютер с компьютером; '
                     '"ch" - компьютер за 0, вы за x; '
                     '"hc" - компьютер за x, вы за 0; '
                     '"hh" - человек с человеком) '
                     '!игрок за 0 ходит первым!\n')

    def validate_size_of_field(self, input_size_of_field):
        try:
            input_size_of_field = int(input_size_of_field)
        except ValueError:
            raise IncorrectSizeOfField

        if input_size_of_field < 2:
            raise IncorrectSizeOfField

        return input_size_of_field

    def validate_mod_and_choose_players(self, mod_to_validate):

        if mod_to_validate == "cc":
            player1 = TicTacComputer('0')
            player2 = TicTacComputer('x')
        elif mod_to_validate == "ch":
            player1 = TicTacComputer('0')
            player2 = TicTacHuman('x')
        elif mod_to_validate == "hc":
            player1 = TicTacHuman('0')
            player2 = TicTacComputer('x')
        elif mod_to_validate == "hh":
            player1 = TicTacHuman('0')
            player2 = TicTacHuman('x')
        else:
            raise ModNotExist

        return player1, player2
