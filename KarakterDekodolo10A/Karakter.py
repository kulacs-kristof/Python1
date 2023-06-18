class Karakter(object):
    _karakter: str
    _matrix: list[list[int]]

    def __init__(self, karakter: str, matrix: list[list[int]]):
        self._karakter = karakter
        self._matrix = matrix
