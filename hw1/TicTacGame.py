from TicTacSettings import TicTacSettings
from exceptions import *


class TicTacGame:
    def __init__(self, settings: TicTacSettings):  # аннотация
        self.size_of_field = settings.size_of_field
        self.field_lines = [[" " for index in range(self.size_of_field)] for index in range(self.size_of_field)]
        self.player1 = settings.player1  # зависит от режима игры
        self.player2 = settings.player2  # зависит от режима игры

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__ #убрать
        return NotImplemented

    def show_board(self):
        for index_of_line in range(self.size_of_field):
            print(' | '.join(self.field_lines[index_of_line]))

    def check_winner(self):
        gamer_x_win_comb = 'x' * self.size_of_field
        gamer_0_win_comb = '0' * self.size_of_field

        for index_of_line in range(self.size_of_field):  # горизонталь
            cur_line_state = ''.join(self.field_lines[index_of_line])
            if cur_line_state == gamer_x_win_comb or cur_line_state == gamer_0_win_comb:
                return cur_line_state[0]

        for index_of_сolumn in range(self.size_of_field):  # вертикаль
            cur_line_state = ''
            for index_of_line in range(self.size_of_field):
                cur_line_state += self.field_lines[index_of_line][index_of_сolumn]
            if cur_line_state == gamer_x_win_comb or cur_line_state == gamer_0_win_comb:
                return cur_line_state[0]

        cur_line_state = ''
        for index_of_line in range(self.size_of_field):  # главная диагональ
            cur_line_state += self.field_lines[index_of_line][index_of_line]
        if cur_line_state == gamer_x_win_comb or cur_line_state == gamer_0_win_comb:
            return cur_line_state[0]

        cur_line_state = ''
        for index in range(self.size_of_field):  # побочная диагональ
            cur_line_state += self.field_lines[index][self.size_of_field - 1 - index]
        if cur_line_state == gamer_x_win_comb or cur_line_state == gamer_0_win_comb:
            return cur_line_state[0]

        return 'nobody'

    def play_once(self):
        winner = 'nobody'
        self.show_board()
        for num_of_step in range(self.size_of_field ** 2):  # цикл выполнения инструкций на каждом ходе
            step_player_line = None
            step_player_column = None

            if num_of_step % 2 == 0:
                step_player = self.player1
                step_char = '0'
            else:
                step_player = self.player2
                step_char = 'x'

            while step_player_line is None or step_player_column is None:
                try:
                    step_player_line, step_player_column = step_player.get_step_indexes(num_of_step, self.field_lines)
                    self.__check_cell_occupancy(step_player_line, step_player_column)
                except IncorrectInputFormat:
                    print('Некорректный формат ввода, повторите ввод')
                except CellNotExist:
                    print('Такой строки или столбца не существует, повторите ход')
                except CellAlreadyOccupied:
                    step_player_line = None
                    step_player_column = None
                    print('Это поле уже занято, повторите ход')

            self.field_lines[step_player_line][step_player_column] = step_char

            self.show_board()
            winner = self.check_winner()
            if winner != 'nobody':
                break

        if winner != 'nobody':
            print(f'Победил игрок за {winner}!')
        else:
            print('Ничья\n')

        self.__clear_game_story()

    def __check_cell_occupancy(self, line_to_check, column_to_check):
        if line_to_check > self.size_of_field or column_to_check > self.size_of_field:
            raise InternalError

        if not self.field_lines[line_to_check][column_to_check] == " ":
            raise CellAlreadyOccupied

    def __clear_game_story(self):
        self.field_lines = [[" " for index in range(self.size_of_field)] for index in range(self.size_of_field)]
