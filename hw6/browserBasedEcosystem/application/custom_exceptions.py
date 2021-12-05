# coding: utf8
class HttpMethodIsNotSupported(Exception):
    """метод, который был использован при запросе не поддерживается"""
    pass


class FileIdAlreadyExist(Exception):
    """файл с таким id уже существует"""
    pass


class FileNotExist(Exception):
    """файл с полученным id не существует"""
    pass