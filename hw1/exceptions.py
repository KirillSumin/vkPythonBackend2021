class IncorrectInputFormat(Exception):
    """Вызывается, когда формат введённых данных не соотвествует ожидаемому"""
    pass


class CellAlreadyOccupied(Exception):
    """Вызывается, когда ячейка уже занята"""
    pass


class CellNotExist(Exception):
    """Вызывается, когда ячейка не существует"""
    pass


class IncorrectSizeOfField(Exception):
    """Вызывается, когда размер поля не корректный"""
    pass


class ModNotExist(Exception):
    """Вызывается, когда введённый режим не поддерживается"""
    pass


class InternalError(Exception):
    """Вызывается, когда происходит внутренняя ошибка"""
    pass
