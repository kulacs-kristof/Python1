class Valaszok:
    _azonosító: str
    _válaszok: str

    @property
    def azonosito(self) -> str:
        return self._azonosító

    @property
    def valaszok(self) -> str:
        return self._válaszok

    def __init__(self, sor: str) -> None:
        m: list[str] = sor.split(' ')
        self._azonosító = m[0]
        self._válaszok = m[1]
