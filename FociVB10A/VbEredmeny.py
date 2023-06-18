class VbEredmeny:
    # Csapat;Részvételek száma;Első részvétel;Legutóbbi részvétel;Legjobb eredmény
    # Brazília;21;1930;2018;Világbajnok (1958, 1962, 1970, 1994, 2002)
    ország: str
    részvételek_száma: int
    első_év: int
    utolsó_év: int
    legjobb_eredmény: str

    @property
    def legjobb_eredmény_rövid(self):
        if self.részvételek_száma == 1:
            return self.legjobb_eredmény
        else:
            poz: int = self.legjobb_eredmény.find('(') - 1
            return self.legjobb_eredmény[:poz]

    def __init__(self, sor: str):
        orsz, r, e, u, leg = sor.split(';')
        self.ország = orsz
        self.részvételek_száma = int(r)
        self.első_év = int(e)
        self.utolsó_év = int(u)
        self.legjobb_eredmény = leg
