class Film:
    # eredetiCim;magyarCim;bemutato;forgalmazo;bevel;latogato
    # protected adattagok:
    _eredeti_cim: str
    _magyar_cim: str
    _bemutato: str
    _forgalmazo: str
    _bevetel: int
    _latogato: int

    @property  # jellemző
    def bemutató_éve(self) -> int:
        return int(self._bemutato.split('.')[0])

#    def bemutató_éve(self) -> int:
#       return int(self.bemutato.split('.')[0])

    @property
    def ez_UIP(self) -> bool:
        return self._forgalmazo == "UIP"

    @property
    def ez_intercom(self) -> bool:
        return self._forgalmazo == "InterCom"

    @property
    def latogato(self) -> int:
        return self._latogato

    @property
    def bevetel(self) -> int:
        return self._bevetel

    def __init__(self, sor: str):
        ec, mc, bm, f, bv, lat = sor.split(';')
        self._eredeti_cim = ec
        self._magyar_cim = mc
        self._bemutato = bm
        self._forgalmazo = f
        self._bevetel = int(bv)
        self._latogato = int(lat)
