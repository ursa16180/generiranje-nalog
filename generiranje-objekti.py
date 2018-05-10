import random

class NapacnaNaloga(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise NapacnaNaloga

[
    Polinom(max_stopnja=5, min_nicla=0, max_nicla=5, st_nalog=5),
    Polinom(max_stopnja=5, max_nicla=100, sprememba_semena=1, besedilo_posamezne),
]

class Naloga:
    def __init__(self, st_nalog=None):
        self.st_nalog = st_nalog

    besedilo_posamezne = '''
        Reši nalogo: {{ naloga }}
    '''
    besedilo_vecih = '''
        Reši sledeče naloge:
        {% for naloga in naloge %}
        - {{ naloga }}
        {% endfor %}
    '''

    def besedilo(self):
        if self.st_nalog is None:
            return jinja_magic(self.besedilo_posamezne, {
                'naloga': self.sestavi()
            })
        else:
            return jinja_magic(self.besedilo_vecih, {
                'naloge': self.sestavi_vec(self.st_nalog)
            })

    def poskusi_sestaviti(self):
        pass

    def sestavi(self):
        while True:
            try:
                return self.poskusi_sestaviti()
            except NapacnaNaloga:
                pass

    def sestavi_vec(self, stevilo_nalog):
        naloge = []
        for _ in range(stevilo_nalog):
            naloge.append(self.sestavi())
        return naloge







class Polinom(Naloga):
    def __init__(self, min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, **kwargs):
        self.super().__init__(**kwargs)
        self.min_stopnja = min_stopnja
        self.max_stopnja = max_stopnja
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    besedilo_posamezne = '''
        Poišči ničle polinoma {{ polinom }}.
    '''

    besedilo_vecih = '''
        Poišči ničle sledečih polinomov:
        {% for polinom in polinomi %}
        - {{ polinom }}
        {% endfor %}
    '''

    def besedilo(self):
        if self.st_nalog is None:
            return jinja_magic(self.besedilo_posamezne, {
                'polinom': self.sestavi(),
            })
        else:
            return jinja_magic(self.besedilo_vecih, {
                'polinomi': self.sestavi_vec(self.st_nalog),
            })

    def poskusi_sestaviti(self):
        nicle = set()
        stopnja = random.randint(self.min_stopnja, self.max_stopnja)
        for _ in range(stopnja + 1):
            nicla = random.randint(self.min_nicla, self.max_nicla)
            nicle.add(nicla)
        preveri(self.min_stopnja <= len(nicle) <= self.max_stopnja)
        return nicle
