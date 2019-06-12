from generiranje import Naloga, preveri
import sympy
import random


def naredi_eksponentno(do=3, cela_osnova=False, premik=0):
    """
    Funkcija vrne naključno eksponentno funkcijo, ki ustreza vpisanim pogojem.

    :param do: osnovo izbere iz seznama od 2 do vrednosti do
    :param cela_osnova: celoštevilka osnova ali ne
    :param premik: premik osnovne eksponentne funkcije za vrednost premika
    :return: tuple, ki vsebuje osnovo, premik in eksponentno funkcijo


    >>> naredi_eksponentno(do=5)
    (19/5, 0, (19/5)**x)

    >>> naredi_eksponentno(cela_osnova=True, premik=2)
    (2, 2, 2**x + 2)

    """
    x = sympy.symbols('x')
    izbor = list(range(2, do + 1))
    if not cela_osnova:
        izbor += [sympy.Rational(x, 2) for x in range(1, 2 * (do)) if x != 2] + [sympy.Rational(x, 3) for x in
                                                                                 range(1, 3 * (do)) if x != 3] + [
                     sympy.Rational(x, 4) for x in range(1, 4 * (do)) if x != 4] + [sympy.Rational(x, 5) for x in
                                                                                    range(1, 5 * (do)) if x != 5]
    osnova = random.choice(izbor)
    return (osnova, premik, sympy.Add(sympy.Pow(osnova, x), premik, evaluate=False))


class GrafEksponentne(Naloga):
    """
    Naloga iz risanja dveh grafov eksponentne funkcije.

    :param cela_osnova: določi, če ima funkcija lahko samo celoštevilsko osnovo ali tudi racionalno

    >>> GrafEksponentne().sestavi()
    {'eksponentna1': 2**x, 'eksponentna2': -2**x - 1, 'narisi_eksponentna1': '2^x', 'narisi_eksponentna2': '-2^x - 1', 'premik2': -1}

    >>> GrafEksponentne(cela_osnova=False).sestavi()
    {'eksponentna1': (4/3)**x, 'eksponentna2': (4/3)**x + 3, 'narisi_eksponentna1': '(4/3)^x', 'narisi_eksponentna2': '(4/3)^x + 3', 'premik2': 3}
    """
    besedilo_posamezne = r'''V isti koordinatni sistem nariši grafa funkcij $f(x)={{latex(naloga.eksponentna1)}}$ in $g(x)={{latex(naloga.eksponentna2)}}$.'''

    besedilo_vecih = r'''V isti koordinatni sistem nariši grafa funkcij:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $f(x)={{latex(naloga.eksponentna1)}}$, $g(x)={{latex(naloga.eksponentna2)}}$
    {% endfor %}
    \end{enumerate}
    '''

    # TODO izpisovanje imena funkcij na grafu
    resitev_posamezne = r'''$f(x)={{latex(naloga.eksponentna1)}}$, $g(x)={{latex(naloga.eksponentna2)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
    xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,]
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisi_eksponentna1}} };
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisi_eksponentna2}} };
    \addplot[domain =-5.5:5.5, color=black, dashed]{ {{naloga.premik2}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f(x)={{latex(naloga.eksponentna1)}}$, $g(x)={{latex(naloga.eksponentna2)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
    xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,]
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisi_eksponentna1}} };
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisi_eksponentna2}} };
    \addplot[domain =-5.5:5.5, color=black, dashed]{ {{naloga.premik2}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, cela_osnova=True, **kwargs):
        super().__init__(**kwargs)
        self.cela_osnova = cela_osnova

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        (osnova, premik, eksponentna1) = naredi_eksponentno(cela_osnova=self.cela_osnova)
        predznak = random.choice([1, -1])
        premik2 = random.choice([x for x in range(-3, 4) if x != 0])
        eksponentna2 = sympy.Add(predznak * sympy.Pow(osnova, x, evaluate=False), premik2, evaluate=False)
        narisi_eksponentna1 = str(eksponentna1).replace('**', '^')
        narisi_eksponentna2 = str(eksponentna2).replace('**', '^')
        return {'eksponentna1': eksponentna1, 'eksponentna2': eksponentna2, 'narisi_eksponentna1': narisi_eksponentna1,
                'narisi_eksponentna2': narisi_eksponentna2, 'premik2': premik2}


class Enacba(Naloga):
    """
    Naloga za reševanje eksponentne enačbe.

    :param vsota: enačba z enim členom ali vsota dveh členov


    >>> Enacba().sestavi()
    {'enacba': Eq((1/49)**(-x - 1), 1), 'resitev': -1}

    >>> Enacba(vsota = False).sestavi()
    {'enacba': Eq(5**(x/2 + 1/2), sqrt(5)/5), 'resitev': -2}
    """
    besedilo_posamezne = r'''Reši enačbo ${{latex(naloga.enacba)}}$.'''
    besedilo_vecih = r'''Reši enačbe:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.enacba)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x={{latex(naloga.resitev)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x={{latex(naloga.resitev)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, vsota=False, **kwargs):
        super().__init__(**kwargs)
        self.vsota = vsota

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        if not self.vsota:
            osnova = sympy.Pow(random.choice([2, 3, 4, 5, 7, 10]), random.choice([-2, -1, sympy.Rational(1, 2), 1, 2]))
            a = random.choice([-2, -1, 1, 2])
            b = random.choice([-2, -1, 1, 2])
            d = 0
            k = 0
        else:
            osnova = random.choice([2, 3, 4, 5, 7, 10])
            a = 1
            b = random.choice([-3, -2, -1, 1, 2, 3])
            d = random.choice([-3, -2, -1, 1, 2, 3])
            k = random.choice([-3, -2, -1, 1, 2, 3])
        x1 = random.choice([-3, -2, -1, 0, 1, 2, 3])
        vrednost = osnova ** (a * x1 + b) + k * (osnova) ** (x1 + d)
        enacba = sympy.Eq(sympy.Pow(osnova, (a * x + b)) + k * sympy.Pow(osnova, (x + d)), vrednost)

        return {'enacba': enacba, 'resitev': x1}


class Enacba2osnovi(Naloga):
    """
    Naloga enačbe, kjer imata potenci dve različni osnovi.

    :param deli_z_osnovo: ali je v zadnjem koraku potrebno vrednosti deliti z nasprotno osnovo


    >>> Enacba2osnovi().sestavi()
    {'enacba': Eq(2**x/4 - 5*7**x/2401, 7*2**x/32 - 34*7**x/16807), 'resitev': 5}

    >>> Enacba2osnovi(deli_z_osnovo=True).sestavi()
    {'enacba': Eq(2**(x + 2) - 3**(x - 1), 13*2**x/4 - 3**x/9), 'resitev': 3
    """
    besedilo_posamezne = r'''Reši enačbo ${{latex(naloga.enacba)}}$.'''
    besedilo_vecih = r'''Reši enačbe:
    \begin{enumerate} 
    {% for naloga in naloge %}
    \item ${{latex(naloga.enacba)}}$.
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x={{latex(naloga.resitev)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x={{latex(naloga.resitev)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, deli_z_osnovo=False, **kwargs):
        super().__init__(**kwargs)
        self.deli_z_osnovo = deli_z_osnovo

    def _poskusi_sestaviti(self):
        [osnova1, osnova2] = random.sample([2, 3, 5, 7, 10], 2)
        x = sympy.symbols('x')
        a = random.randint(-5, 5)
        if not self.deli_z_osnovo:
            u = 0
            v = 0
        else:
            u = random.choice([0, 1, 2, 3])
            v = random.choice([0, 1, 2, 3])
        e = a - v + u
        b = random.choice([1, 2])
        f = random.choice([1, 2])
        c = random.choice([1, 2, 3, 4, 5])
        g = random.choice([1, 2, 3, 4, 5])
        d = osnova2 ** u - osnova1 ** b * c
        h = osnova1 ** v - osnova2 ** f * g
        resitev = -(a - v)
        enacba = sympy.Eq(sympy.simplify(c * osnova1 ** (x + a + b) - g * osnova2 ** (x + e + f)),
                          sympy.simplify(-d * osnova1 ** (x + a) + h * osnova2 ** (x + e)))
        preveri(max([abs(d), abs(h)]) < 50)  # Zagotovi, da v enačbi ne nastopajo prevelike vrednosti.
        return {'enacba': enacba, 'resitev': resitev}
