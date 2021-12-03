from exceptions import *


class TicTacHuman:
    def __init__(self, char_to_play):
        self.char_to_play = char_to_play
        self.size_of_field = 0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.__dict__ == self.__dict__
        return NotImplemented

    def user_input_line_and_column(self, num_of_step):
        try:
            if int(num_of_step) < 0:
                raise InternalError
        except ValueError:
            raise InternalError
        return input(
            f'{num_of_step + 1} ход: Игрок за {self.char_to_play}, введите номер строки и колонки слитно '
            f'(отсчёт индексов идёт 0)\n')

    def get_step_indexes(self, num_of_step, field_lines):
        try:
            if int(num_of_step) < 0:
                raise InternalError
        except ValueError:
            raise InternalError
        self.size_of_field = len(field_lines)
        input_line_and_column = self.user_input_line_and_column(num_of_step)

        try:
            input_line = int(input_line_and_column[0])
            input_column = int(input_line_and_column[1])
        except (ValueError, IndexError):
            raise IncorrectInputFormat

        if input_line < 0 or input_line >= self.size_of_field \
                or input_column < 0 or input_column >= self.size_of_field:
            raise CellNotExist

        return input_line, input_column
