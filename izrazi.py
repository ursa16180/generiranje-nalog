from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random
import jinja2


class PotencaDvoclenika(Naloga):
    """
    Naloga iz potenciranja dvočlenika.
    """
    besedilo_posamezne = r'''Potenciraj izraz ${{latex(naloga.izraz)}}$'''
    besedilo_vecih = r'''Potenciraj izraze:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.izraz)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''${{latex(naloga.potenciran)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{latex(naloga.potenciran)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, min_potenca=2, max_potenca=3, lazja=True, **kwargs):
        """
        :param min_potenca: najmajši možen eksponent dvočlenika
        :type min_potenca: int
        :param max_potenca: največji možen eksponent dvočlenika
        :type max_potenca: int
        :param lazja: lažja ali težja oblika naloge
        :type lazja: Bool
        """
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka

        self.lazja = lazja
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo PotencaDvoclenika"""
        potenca = random.randint(self.min_potenca, self.max_potenca)
        simboli = ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']
        izbranSimbol = random.choice(simboli)
        x = sympy.symbols(izbranSimbol)
        simboli.remove(izbranSimbol)
        if self.lazja:
            a = 1
            b = random.choice([x for x in range(-5, 5) if x != 0])
            n = 1
            y = 1
            m = 1
        else:
            a = random.randint(1, 5)
            b = random.choice([x for x in range(-5, 5) if x != 0])
            n = random.randint(2, 5)
            m = random.randint(1, 5)
            y = sympy.symbols(random.choice(simboli))

        izraz = sympy.Pow(a * x ** n + b * y ** m, potenca, evaluate=False)
        potenciran = izraz.expand()
        return {'izraz': izraz, 'potenciran': potenciran}


class PotencaTroclenika(Naloga):
    """Naloga iz potenciranja tročlenika"""
    besedilo_posamezne = r'''Potenciraj izraz ${{latex(naloga.izraz)}}$'''
    besedilo_vecih = r'''Potenciraj izraze:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.izraz)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''${{latex(naloga.potenciran)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{latex(naloga.potenciran)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, min_potenca=2, max_potenca=2, **kwargs):
        """
        :param min_potenca: najmajši možen eksponent tročlenika
        :type min_potenca: int
        :param max_potenca: največji možen eksponent tročlenika
        :type max_potenca: int
        """
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo PotencaTroclenika"""
        potenca = random.randint(self.min_potenca, self.max_potenca)
        simboli = [sympy.symbols(x) for x in ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']]
        (x, y, z) = random.sample(simboli, 3)
        a = random.randint(1, 4)
        b = random.choice([x for x in range(-4, 4) if x != 0])
        c = random.choice([x for x in range(-4, 4) if x != 0])

        izraz = sympy.Pow(a * x + b * y + c * z, potenca, evaluate=False)
        potenciran = izraz.expand()
        return {'izraz': izraz, 'potenciran': potenciran}


class RazstaviVieta(Naloga):
    """Naloga za razstavljanje s pomočjo Vietovega pravila."""
    besedilo_posamezne = r'''Razstavi izraz ${{latex(naloga.nerazstavljeno)}}$.'''
    besedilo_vecih = r'''Razstavi naslednje izraze
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.nerazstavljeno)}}=$
    {% endfor %}
    \end{enumerate}'''

    resitev_posamezne = r'''${{latex(naloga.razstavljeno)}}$'''
    resitev_vecih = r'''\begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.razstavljeno)}}$
    {% endfor %}
    \end{enumerate}'''

    def __init__(self, minimalna_vrednost=-9, maksimalna_vrednost=9, lazja=True,
                 **kwargs):  # TODO ali so te min maks vrednosti smiselne?
        """
        :param minimalna_vrednost: najmanjša možna vrednost razstavljenega člena
        :type minimalna_vrednost: int
        :param maksimalna_vrednost: največja možna vrednost razstavljenega člena
        :type maksimalna_vrednost: int
        :param lazja: lažja ali težja oblika naloge
        :type lazja: Bool
        """
        super().__init__(**kwargs)
        if minimalna_vrednost > maksimalna_vrednost:
            raise MinMaxNapaka
        self.minimalna_vrednost = minimalna_vrednost
        self.maksimalna_vrednost = maksimalna_vrednost

        self.lazja = lazja

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo RazstaviVieta."""
        x1 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        x2 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        if not self.lazja:
            a = random.randint(2, 4)
        else:
            a = 1
        x = sympy.symbols('x')
        razstavljeno = sympy.Mul(a, (x - x1), (x - x2), evaluate=False)
        nerazstavljeno = sympy.expand(razstavljeno)
        return {'razstavljeno': razstavljeno, 'nerazstavljeno': nerazstavljeno}


class RazstaviRazliko(Naloga):
    """
    Naloga za razstavljanje razlike kvadratov, kubov in višjih potenc.
    """
    besedilo_posamezne = r'''Razstavi izraz ${{latex(naloga.izraz)}}$.'''
    besedilo_vecih = r'''Razstavi izraze:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item${{latex(naloga.izraz)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''${{latex(naloga.razstavljen)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{latex(naloga.razstavljen)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, min_potenca=2, max_potenca=3, lazja=True, **kwargs):
        """
        :param min_potenca: najmanjša možna potenca za razstavljanje
        :type min_potenca: int
        :param max_potenca: največja možna potenca za razstavljanje
        :type max_potenca: int
        :param lazja: lažja ali težja oblika naloge
        :type lazja: Bool
        """
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca

        self.lazja = lazja

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo RazstaviRazliko"""
        potenca = random.randint(self.min_potenca, self.max_potenca)
        if potenca == 2:
            do = 10
        else:
            do = 5
        simboli = ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']
        izbranSimbol = random.choice(simboli)
        x = sympy.symbols(izbranSimbol)
        simboli.remove(izbranSimbol)
        if self.lazja:
            a = 1
            b = random.choice([x for x in range(-do, do) if x != 0])
            y = 1
            m = 1
            n = 1
        else:
            a = random.randint(1, do)
            b = random.choice([x for x in range(-do, do) if x != 0])
            n = random.randint(1, 3)
            m = random.randint(1, 3)
            y = sympy.symbols(random.choice(simboli))
        izraz = (a * x ** n) ** potenca - (
                b * y ** m) ** potenca  # Todo kako preprečiti da so členi po abecedi? -4b**2+y**2
        razstavljen = sympy.factor(izraz)

        return {'izraz': izraz, 'razstavljen': razstavljen}


class PotencirajVecclenik(Naloga):
    """
    Naloga za potenciranje dvočlenikov in tročlenikov
    """
    besedilo_posamezne = r'''Potenciraj izraz ${{latex(naloga.izraz)}}$.'''
    besedilo_vecih = r'''Potenciraj izraze:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item${{latex(naloga.izraz)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''${{latex(expand(naloga.izraz))}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{latex(expand(naloga.izraz))}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, min_potenca=2, max_potenca=3, min_clenov=2, max_clenov=2, lazja=True, **kwargs):
        """
        :param min_potenca: najmanjša možna potenca
        :type min_potenca: int
        :param max_potenca: največja možna potenca
        :type max_potenca: int
        :param min_clenov: najmanjše možno število členov
        :type min_clenov: int
        :param max_clenov: največje možno število členov
        :type max_clenov: int
        :param lazja: lažja ali težja oblika naloge
        :type lazja: Bool
        """
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca
        if min_clenov > max_clenov:
            raise MinMaxNapaka
        self.min_clenov = min_clenov
        self.max_clenov = max_clenov
        if max_clenov not in {2, 3} or min_clenov not in {2, 3}:
            raise ValueError('Naloga razsatvi potenco ima za rešitev lahko samo dvočlenike ali tročlenike.')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        cleni = random.randint(self.min_clenov, self.max_clenov)
        simboli = [sympy.symbols(x) for x in ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']]
        (x, y, z) = random.sample(simboli, 3)
        if potenca == 2:
            do = 10
        else:
            do = 5

        if cleni == 2:
            z = 0

        if self.lazja:
            a = 1
            b = random.choice([x for x in range(-do, do) if x != 0])
            c = random.choice([x for x in range(-do, do) if x != 0])
            y = 1
            m = 1
            n = 1
            o = 1
        else:
            a = random.randint(1, do)
            b = random.choice([x for x in range(-do, do) if x != 0])
            c = random.choice([x for x in range(-do, do) if x != 0])
            n = random.randint(1, 3)
            m = random.randint(1, 3)
            o = random.randint(1, 3)

        izraz = sympy.Pow((a * x ** n) + (b * y ** m) + (c * z ** o), potenca, evaluate=False)

        return {'izraz': izraz}
