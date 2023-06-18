class Karakter(object):
    _karakter: list[list[int]]
    _matrix: list[list[int]]

    def __init__(self, karakter: str, matrix: list[list[int]]):
        self._karakter = karakter
        self._matrix = matrix
