class River:
#name;lenght_in_HR;total_length;drains_into

    name: str
    length: float
    total_l: float
    drain: str

    def __init__(self, sor: str):
        n, l, t, d = sor.split(';')
        self.name = n
        self.length = float(l.replace(',','.'))
        self.total_l = float(t.replace(',','.'))
        self.drain = d

