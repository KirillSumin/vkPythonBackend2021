import random
import exceptions


class TicTacComputer:
    def __init__(self, char_to_play):
        self.size_of_field = 0
        self.char_to_play = char_to_play
        self.opponent_char = 'x' if self.char_to_play == '0' else '0'
        self.max_opponent_score = 0
        self.index_of_line_to_play = -1
        self.index_of_column_to_play = -1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__
        return NotImplemented

    def get_step_indexes(self, num_of_step, field_lines):

        try:
            if int(num_of_step) < 0:
                raise exceptions.InternalError
        except (ValueError, IndexError):
            raise exceptions.InternalError

        self.size_of_field = len(field_lines)
        self.index_of_line_to_play = -1
        self.index_of_column_to_play = -1
        self.max_opponent_score = 0

        print(f'{num_of_step + 1} ход: компьютер за {self.char_to_play}')

        for index_of_line in range(self.size_of_field):  # горизонталь
            cur_line_state = ''.join(field_lines[index_of_line])
            if self.__need_to_change_strategy(cur_line_state):
                self.__change_strategy('horizontal', cur_line_state, index_of_line)

        for index_of_сolumn in range(self.size_of_field):  # вертикаль
            cur_line_state = ''
            for index_of_line in range(self.size_of_field):
                cur_line_state += field_lines[index_of_line][index_of_сolumn]
            if self.__need_to_change_strategy(cur_line_state):
                self.__change_strategy('vertical', cur_line_state, index_of_line, index_of_сolumn)

        cur_line_state = ''
        for index_of_line in range(self.size_of_field):  # главная диагональ
            cur_line_state += field_lines[index_of_line][index_of_line]
        if self.__need_to_change_strategy(cur_line_state):
            self.__change_strategy('diagonal', cur_line_state)

        cur_line_state = ''
        for index in range(self.size_of_field):  # побочная диагональ
            cur_line_state += field_lines[index][self.size_of_field - 1 - index]
        if self.__need_to_change_strategy(cur_line_state):
            self.__change_strategy('sub_diagonal', cur_line_state)

        if self.index_of_line_to_play == -1 or self.index_of_column_to_play == -1:
            # for index_of_line in range(size_of_field):  #  последовательное заполнение
            #     cur_line_state = "".join(field_lines[index_of_line])
            #     if cur_line_state.find(char_to_play) == -1:
            #         index_of_line_to_play = index_of_line
            #         index_of_column_to_play = cur_line_state.find(" ")
            while 1:
                self.index_of_line_to_play = random.randrange(0, self.size_of_field)  # рандомное заполнение
                self.index_of_column_to_play = random.randrange(0, self.size_of_field)
                if field_lines[self.index_of_line_to_play][self.index_of_column_to_play] == ' ':
                    break
                else:
                    continue
        return self.index_of_line_to_play, self.index_of_column_to_play

    def __need_to_change_strategy(self, cur_line_state):
        if cur_line_state.find(self.char_to_play) == -1:
            cur_line_opponent_score = cur_line_state.count(self.opponent_char)
            if self.max_opponent_score < cur_line_opponent_score:
                return True

        return False

    def __change_strategy(self, type_of_iteration, cur_line_state, index_of_line=None, index_of_column=None):
        self.max_opponent_score = cur_line_state.count(self.opponent_char)
        if type_of_iteration == 'horizontal':
            self.index_of_line_to_play = index_of_line
            self.index_of_column_to_play = cur_line_state.find(' ')
        elif type_of_iteration == 'vertical':
            self.index_of_line_to_play = cur_line_state.find(' ')
            self.index_of_column_to_play = index_of_column
        elif type_of_iteration == 'diagonal':
            index_to_play = cur_line_state.find(' ')
            self.index_of_line_to_play = index_to_play
            self.index_of_column_to_play = index_to_play
        elif type_of_iteration == 'sub_diagonal':
            index_to_play = cur_line_state.find(' ')
            self.index_of_line_to_play = index_to_play
            self.index_of_column_to_play = self.size_of_field - 1 - index_to_play
