from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random


class PotencaDvoclenika(Naloga):
    """
    Naloga iz potenciranja dvočlenika.

    :param min_potenca: najmajši možen eksponent dvočlenika
    :param max_potenca: največji možen eksponent dvočlenika
    :param linearna_kombinacija: potenciranje linearne kombinacije 2 neznank, drugače enostaven dvočlenik

    .. runblock:: pycon

        >>> import sys # ignore
        >>> sys.path.append('../') # ignore
        >>> from izrazi import * # ignore
        >>> PotencaDvoclenika().primer()


    >>> PotencaDvoclenika().sestavi()
    {'izraz': (5*t**4 - 5*y**5)**2, 'potenciran': 25*t**8 - 50*t**4*y**5 + 25*y**10}

    >>> PotencaDvoclenika(linearna_kombinacija=False, min_potenca=3).sestavi()
    {'izraz': (z + 4)**3, 'potenciran': z**3 + 12*z**2 + 48*z + 64}
    """
    besedilo_posamezne = r'''Potenciraj izraz ${{latex(naloga.izraz)}}$'''
    besedilo_vecih = r'''Potenciraj izraze:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.izraz)}}$
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

    def __init__(self, min_potenca=2, max_potenca=3, linearna_kombinacija=True, **kwargs):
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka

        self.linearna_kombinacija = linearna_kombinacija
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca

    def _poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        simboli = ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']
        izbranSimbol = random.choice(simboli)
        x = sympy.symbols(izbranSimbol)
        simboli.remove(izbranSimbol)
        if not self.linearna_kombinacija:
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
        return {'izraz': izraz}


class PotencaTroclenika(Naloga):
    """Naloga iz potenciranja tročlenika.

    :param min_potenca: najmajši možen eksponent tročlenika
    :param max_potenca: največji možen eksponent tročlenika
    :param linearna_kombinacija: potenciranje linearne kombinacije 3 neznank, drugače enostaven tročlenik


    >>> PotencaTroclenika().sestavi()
    {'izraz': (2*a + 3*t - z)**2, 'potenciran': 4*a**2 + 12*a*t - 4*a*z + 9*t**2 - 6*t*z + z**2}

    >>> PotencaTroclenika(linearna_kombinacija=False, max_potenca=3).sestavi()
    {'izraz': (a + b + 3)**3, 'potenciran': a**3 + 3*a**2*b + 9*a**2 + 3*a*b**2 + 18*a*b + 27*a + b**3 + 9*b**2 + 27*b + 27}

    """
    besedilo_posamezne = r'''Potenciraj izraz ${{latex(naloga.izraz)}}$'''
    besedilo_vecih = r'''Potenciraj izraze:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.izraz)}}$
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

    def __init__(self, min_potenca=2, max_potenca=2, linearna_kombinacija=True, **kwargs):
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca
        self.linearna_kombinacija = linearna_kombinacija

    def _poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo PotencaTroclenika"""
        potenca = random.randint(self.min_potenca, self.max_potenca)
        simboli = [sympy.symbols(x) for x in ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']]
        (x, y, z) = random.sample(simboli, 3)
        a = random.randint(1, 4)
        b = random.choice([x for x in range(-4, 4) if x != 0])
        c = random.choice([x for x in range(-4, 4) if x != 0])
        if not self.linearna_kombinacija:
            a = 1
            b = 1
            z = 1

        izraz = sympy.Pow(a * x + b * y + c * z, potenca, evaluate=False)
        return {'izraz': izraz}


class RazstaviVieta(Naloga):
    """
    Naloga za razstavljanje s pomočjo Vietovega pravila.

    :param minimalna_vrednost: najmanjša možna vrednost razstavljenega člena
    :param maksimalna_vrednost: največja možna vrednost razstavljenega člena
    :param vodilni_koeficient: vodilni koeficient ni enak 1


    >>> RazstaviVieta(minimalna_vrednost=-3).sestavi()
    {'izraz': (x - 3)*(x + 3)}

    >>> RazstaviVieta(minimalna_vrednost=-4, maksimalna_vrednost=3, vodilni_koeficient=True).sestavi()
    {'izraz': 3*(x + 2)*(x + 4)}
    """
    besedilo_posamezne = r'''Razstavi izraz ${{latex(expand(naloga.izraz))}}$.'''
    besedilo_vecih = r'''Razstavi naslednje izraze
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(expand(naloga.izraz))}}=$
    {% endfor %}
    \end{enumerate}'''

    resitev_posamezne = r'''${{latex(naloga.izraz)}}$'''
    resitev_vecih = r'''\begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.izraz)}}$
    {% endfor %}
    \end{enumerate}'''

    def __init__(self, minimalna_vrednost=-9, maksimalna_vrednost=9, vodilni_koeficient=False,
                 **kwargs):  # TODO ali so te min maks vrednosti smiselne?
        super().__init__(**kwargs)
        if minimalna_vrednost > maksimalna_vrednost:
            raise MinMaxNapaka
        self.minimalna_vrednost = minimalna_vrednost
        self.maksimalna_vrednost = maksimalna_vrednost
        self.vodilni_koeficient = vodilni_koeficient

    def _poskusi_sestaviti(self):
        x1 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        x2 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        if self.vodilni_koeficient:
            a = random.randint(2, 4)
        else:
            a = 1
        x = sympy.symbols('x')
        izraz = sympy.Mul(a, (x - x1), (x - x2), evaluate=False)
        return {'izraz': izraz}


class RazstaviRazliko(Naloga):
    """
    Naloga za razstavljanje razlike kvadratov, kubov in višjih potenc.

    :param min_potenca: najmanjša možna potenca za razstavljanje
    :param max_potenca: največja možna potenca za razstavljanje
    :param linearna_kombinacija: linearna kombinacija dveh neznank, drugače enostaven dvočlenik


    >>> RazstaviRazliko(max_potenca=5).sestavi()
    {'izraz': b**5 - 1, 'razstavljen': (b - 1)*(b**4 + b**3 + b**2 + b + 1)}

    >>> RazstaviRazliko(linearna_kombinacija=True).sestavi()
    {'izraz': -81*v**2 + 64*z**6, 'razstavljen': (-9*v + 8*z**3)*(9*v + 8*z**3)}
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

    def __init__(self, min_potenca=2, max_potenca=3, linearna_kombinacija=False, **kwargs):
        super().__init__(**kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca
        self.linearna_kombinacija = linearna_kombinacija

    def _poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        if potenca == 2:
            do = 10
        else:
            do = 5
        simboli = ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']
        izbranSimbol = random.choice(simboli)
        x = sympy.symbols(izbranSimbol)
        simboli.remove(izbranSimbol)
        if not self.linearna_kombinacija:
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
    Naloga za potenciranje dvočlenikov in tročlenikov.

    :param min_potenca: najmanjša možna potenca
    :param max_potenca: največja možna potenca
    :param min_clenov: najmanjše možno število členov
    :param max_clenov: največje možno število členov
    :param linearna_kombinacija: potenciranje linearne kombinacije dveh ali treh neznank, drugače enostaven veččlenik


    >>> PotencirajVecclenik(max_clenov=3).sestavi()
    {'izraz': (4*a + v + 3)**3}

    >>> PotencirajVecclenik(linearna_kombinacija=True).sestavi()
    {'izraz': (4*t**3 - z**3)**3}
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

    def __init__(self, min_potenca=2, max_potenca=3, min_clenov=2, max_clenov=2, linearna_kombinacija=False, **kwargs):
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
            raise ValueError('V nalogi lahko potenciramo samo dvočlenike in tročlenike.')
        self.linearna_kombinacija = linearna_kombinacija

    def _poskusi_sestaviti(self):
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

        if not self.linearna_kombinacija:
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
