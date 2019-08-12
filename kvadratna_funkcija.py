from generiranje import Naloga, preveri
import random
import sympy
from linearna_funkcija import skozi_tocki, seznam_polovick, seznam_tretinj


def nicelna_oblika(od=-5, do=5, risanje=False):
    """
    Vrne naključno kvadratno funkcijo v ničelni obliki.

    :param od: najmanjša možna vrednost za ničlo funkcije
    :param do: največja možna vrednost za ničlo funkcije
    :param risanje: če fukcijo potrebujejmo za risanje, izbere lepši vodilni koeficient
    :return: vodilni koeficient, ničli in kvadratno funkcijo v ničelni obliki


    >>> nicelna_oblika(od=0, do=15)
    (-11/3, 7, 10/3, -11*(x - 7)*(x - 10/3)/3)

    >>> nicelna_oblika(od=-2, risanje=True)
    (2, -2, 3/2, 2*(x - 3/2)*(x + 2))
    """
    if risanje:
        a = random.choice([-2, -1, sympy.Rational(-1, 2), sympy.Rational(1, 2), 1, 2])
    else:
        a = random.choice(seznam_polovick(-4, 4) + seznam_tretinj(-4, 4))
    x1 = random.choice(seznam_polovick(od, do) + seznam_tretinj(od, do))
    x2 = random.choice(seznam_polovick(od, do) + seznam_tretinj(od, do))
    x = sympy.symbols('x')
    # nicelna = a * (x - x1) * (x - x2)
    nicelna = sympy.Mul(a, x - x1, x - x2, evaluate=False)
    return (a, x1, x2, nicelna)


def splosna_oblika(risanje=False):
    """
    Vrne naključno kvadratno funkcijo v splošni obliki.

    :param risanje: če fukcijo potrebujejmo za risanje, izbere lepši vodilni koeficient
    :return: vrne seznam koeficientov in kvadratno funkcijo v splošni obliki


    >>> splosna_oblika()
    (8/3, 1/2, -1/3, 8*x**2/3 + x/2 - 1/3)

    >>> splosna_oblika(risanje=True)
    (-2, 5/2, 1/3, -2*x**2 + 5*x/2 + 1/3)
    """
    if risanje:
        a = random.choice([-2, -1, sympy.Rational(-1, 2), sympy.Rational(1, 2), 1, 2])
    else:
        a = random.choice(seznam_polovick(-4, 4) + seznam_tretinj(-4, 4))

    b = random.choice(seznam_polovick(-4, 4) + seznam_tretinj(-4, 4))
    c = random.choice(seznam_polovick(-4, 4) + seznam_tretinj(-4, 4))
    x = sympy.symbols('x')
    splosna = a * x ** 2 + b * x + c
    return (a, b, c, splosna)


def nicle(a, b, c):
    """
    Iz podanih koeficientov kvadratne funkcije izračuna ničli funkcije.

    :param a: vodilni koeficient
    :param b: linearni koeficient
    :param c: prosti člen
    :return: tuple ničel kvadratne funkcije


    >>> nicle(1,-4,4)
    (2, 2)

    >>> nicle(2,3,4)
    (-3/4 + sqrt(23)*I/4, -3/4 - sqrt(23)*I/4)
    """
    D = diskriminanta(a, b, c)
    if D >= 0:
        d = sympy.sqrt(D)
    else:
        d = sympy.sqrt(-D) * sympy.I
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return (x1, x2)


def izracunaj_teme(a, b, c):
    """
    Iz podanih koeficientov kvadratne funkcije koordinati temena.

    :param a: vodilni koeficient
    :param b: linearni koeficient
    :param c: prosti člen
    :return: tuple koordinat temena kvadratne funkcije


    >>> izracunaj_teme(2,-2,-12)
    (0.5, -12.5)

    >>> izracunaj_teme(2,1,-3)
    (-0.25, -3.125)
    """
    p = -b / (2 * a)
    q = -(diskriminanta(a, b, c)) / (4 * a)
    return (p, q)


def diskriminanta(a, b, c):
    """
    Iz podanih koeficientov kvadratne funkcije izračuna diskriminanto.
    
    :param a: vodilni koeficient
    :param b: linearni koeficient
    :param c: prosti člen
    :return: vrednost diskriminante kvadratne funkcije


    >>> diskriminanta(2,1,-3)
    25

    >>> diskriminanta(2,3,4)
    -23
    """
    return b ** 2 - 4 * a * c


# ~~~~~Naloge in sklopa: Kvadratna funkcija

class IzracunajNicle(Naloga):
    """
    Naloga za računanje ničel kvadratne funkcije.

    :param kompleksni_nicli: kompleksne ali realna ničle


    >>> IzracunajNicle().sestavi()
    {'splosna': 3*x**2 + 8*x/3 + 1/3, 'x1': -4/9 + sqrt(7)/9, 'x2': -4/9 - sqrt(7)/9}

    >>> IzracunajNicle(kompleksni_nicli=True).sestavi()
    {'splosna': -3*x**2 - x - 4, 'x1': -1/6 - sqrt(47)*I/6, 'x2': -1/6 + sqrt(47)*I/6}
    """
    besedilo_posamezne = r'''Izračunaj ničli kvadratne funkcije $f(x)={{latex(naloga.splosna)}}$.'''
    besedilo_vecih = r'''Izračunaj ničli naslednjih kvadratnih funkcij:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $f(x)={{latex(naloga.splosna)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x_1={{latex(naloga.x1)}}$, $x_2={{latex(naloga.x2)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x_1={{latex(naloga.x1)}}$, $x_2={{latex(naloga.x2)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, kompleksni_nicli=False, **kwargs):
        super().__init__(**kwargs)
        self.kompleksni_nicli = kompleksni_nicli

    def _poskusi_sestaviti(self):
        (a, b, c, splosna) = splosna_oblika()
        if not self.kompleksni_nicli:
            preveri(diskriminanta(a, b, c) >= 0 and abs(diskriminanta(a, b, c)) <= 200)
        else:
            preveri(diskriminanta(a, b, c) < 0 and abs(diskriminanta(a, b, c)) <= 200)
        [x1, x2] = nicle(a, b, c)
        return {'splosna': splosna, 'x1': x1, 'x2': x2}


class NarisiGraf(Naloga):
    """
    Naloga za risanje grafa kvadratne funkcije.


    >>> NarisiGraf().sestavi()
    {'funkcija': x**2/2 + 5*x/6 + 1/3, 'narisiFunkcijo': (x + 2/3)*(x + 1)/2, 'p': -5/6, 'q': -1/72, 'x1': -1, 'x2': -2/3, 'zacetna': 1/3}

    >>> NarisiGraf().sestavi()
    {'funkcija': -x**2 - 5*x/3 + 14/9, 'narisiFunkcijo': -(x - 2/3)*(x + 7/3), 'p': -5/6, 'q': 9/4, 'x1': 2/3, 'x2': -7/3, 'zacetna': 14/9}
    """
    besedilo_posamezne = r'''Nariši graf funkcije $f(x)={{latex(naloga.funkcija)}}$'''
    besedilo_vecih = r'''Nariši grafe funkcij:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item  $f(x)={{latex(naloga.funkcija)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$f(x)={{latex(naloga.funkcija)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
    xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
    extra x ticks={ {{naloga.x1}},{{naloga.x2}},{{naloga.p}} },
    extra y ticks={ {{naloga.q}},{{naloga.zacetna}} },
    extra x tick labels={ ${{latex(naloga.x1)}}$,${{latex(naloga.x2)}}$,${{latex(naloga.p)}}$ },
    extra y tick labels={ ${{latex(naloga.q)}}$,${{latex(naloga.zacetna)}}$ },
    extra x tick style={xticklabel style={above},},
    extra y tick style={yticklabel style={right},},]
    \addplot[domain =-5:5, color=black, smooth]{ {{naloga.narisiFunkcijo}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
     '''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f(x)={{latex(naloga.funkcija)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
    xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
    extra x ticks={ {{naloga.x1}},{{naloga.x2}},{{naloga.p}} },
    extra y ticks={ {{naloga.q}},{{naloga.zacetna}} },
    extra x tick labels={ ${{latex(naloga.x1)}}$,${{latex(naloga.x2)}}$,${{latex(naloga.p)}}$ },
    extra y tick labels={ ${{latex(naloga.q)}}$,${{latex(naloga.zacetna)}}$ },
    extra x tick style={xticklabel style={above},},
    extra y tick style={yticklabel style={right},},]
    \addplot[domain =-5:5, color=black, smooth]{ {{naloga.narisiFunkcijo}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):  # TODO expand v jinji? potem spremeni kot primer v 03-grafi
        x = sympy.symbols('x')
        (a, x1, x2, nicelna) = nicelna_oblika(-3, 3, risanje=True)
        funkcija = sympy.expand(nicelna)
        [p, q] = izracunaj_teme(a, -a * (x1 + x2), a * x1 * x2)
        preveri(abs(q) <= 5)
        zacetna = funkcija.subs(x, 0)
        return {'funkcija': funkcija, 'narisiFunkcijo': nicelna, 'p': p, 'q': q, 'x1': x1, 'x2': x2, 'zacetna': zacetna}


class TemenskaOblika(Naloga):
    """
    Naloga za dopoljevanje do popolnega kvadrata.


    >>> TemenskaOblika().sestavi()
    {'splosna': x**2 - 4*x - 1/2, 'p': 2, 'q': -9/2, 'a': 1}

    >>> TemenskaOblika().sestavi()
    {'splosna': -4*x**2 - 2*x + 3, 'p': -1/4, 'q': 13/4, 'a': -4}
    """
    besedilo_posamezne = r'''Zapiši temensko obliko funkcije $f(x)={{latex(naloga.splosna)}}$.'''
    besedilo_vecih = r'''Zapiši temensko obliko naslednjih kvadratnih funkcij:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $f(x)={{latex(naloga.splosna)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$f(x)={{latex(naloga.a)}}(x-{{latex(naloga.p)}})^2+{{latex(naloga.q)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f(x)={{latex(naloga.a)}}(x-{{latex(naloga.p)}})^2+{{latex(naloga.q)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        (a, b, c, splosna) = splosna_oblika()
        D = diskriminanta(a, b, c)
        preveri(D >= 0 and abs(D) <= 200)
        (p, q) = izracunaj_teme(a, b, c)
        return {'splosna': splosna, 'p': p, 'q': q, 'a': a}


class Presecisce(Naloga):  # TODO zagotovi lepše rezultate
    """
    Naloga za računanje presečišč parabole in premice.


    >>> Presecisce().sestavi()
    {'parabola': x**2/2 - 137*x/78 - 173/39, 'premica': 317/78 - 11*x/26, 'x1': -3, 'x2': 17/3, 'y1': 16/3, 'y2': 5/3}

    >>> Presecisce().sestavi()
    {'parabola': -x**2/2 - 7*x/10 + 13/5, 'premica': -6*x/5 - 2/5, 'x1': 3, 'x2': -2, 'y1': -4, 'y2': 2}
    """
    besedilo_posamezne = r'''Izračunaj presečišče parabole $y={{latex(naloga.parabola)}}$ in premice $y={{latex(naloga.premica)}}$.'''
    besedilo_vecih = r'''Izračunaj presečišče parabole in premice:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $y={{latex(naloga.parabola)}}$, $y={{latex(naloga.premica)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$T_1({{latex(naloga.x1)}},{{latex(naloga.y1)}})$,$T_2({{latex(naloga.x2)}},{{latex(naloga.y2)}})$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $T_1({{latex(naloga.x1)}},{{latex(naloga.y1)}})$,$T_2({{latex(naloga.x2)}},{{latex(naloga.y2)}})$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        b = sympy.symbols('b')
        c = sympy.symbols('c')
        a = random.choice([-2, -1, sympy.Rational(-1, 2), sympy.Rational(1, 2), 1, 2])
        x1 = random.choice(seznam_polovick(-5, 5) + seznam_tretinj(-5, 5))
        x2 = random.choice(seznam_polovick(-5, 5) + seznam_tretinj(-5, 5))
        y1 = random.choice(seznam_polovick(-5, 5) + seznam_tretinj(-5, 5))
        y2 = random.choice(seznam_polovick(-5, 5) + seznam_tretinj(-5, 5))
        premica = skozi_tocki(x1, y1, x2, y2)[-1]
        koeficienta = sympy.solve((a * x1 ** 2 + b * x1 + c - y1, a * x2 ** 2 + b * x2 + c - y2), b, c)
        preveri(koeficienta != [])  # Če ni rešitve vrne prazen seznam in ne praznega slovarja
        preveri(abs(koeficienta[b]) < 5 and abs(koeficienta[c]) < 5)  # Todo lepša rešitve (grozni ulomki)
        kvadratna = a * x ** 2 + koeficienta[b] * x + koeficienta[c]
        return {'parabola': kvadratna, 'premica': premica, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}


class Neenacba(Naloga):
    """
    Naloga za reševanje kvadratne neenačbe.

    :param primerjava_stevilo: kvadratno enačbo izenači s številom ali drugo kvadratno funkcijo


    >>> Neenacba().sestavi()
    {'neenakost': -x**2/2 - 4*x + 11/3 <= -4/3, 'resitev': Union(Interval(-oo, -sqrt(26) - 4), Interval(-4 + sqrt(26), oo))}

    >>> Neenacba(primerjava_stevilo=False).sestavi()
    {'neenakost': 2*x**2 + 4*x/3 + 1 <= 11*x**2/3 - 4*x + 5/2, 'resitev': Union(Interval(-oo, 8/5 - sqrt(166)/10), Interval(sqrt(166)/10 + 8/5, oo))}
    """
    besedilo_posamezne = r'''Reši kvadratno neenačbo ${{latex(naloga.neenakost)}}$.'''
    besedilo_vecih = r'''Reši kvadratne neenačbe:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.neenakost)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x \in {{latex(naloga.resitev)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item$x \in {{latex(naloga.resitev)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, primerjava_stevilo=True, **kwargs):
        super().__init__(**kwargs)
        self.primerjava_stevilo = primerjava_stevilo

    def _poskusi_sestaviti(self):  # TODO ali želimo lepše rešitve
        x = sympy.symbols('x')
        splosna1 = splosna_oblika(risanje=True)[-1]
        if self.primerjava_stevilo:
            primerjava = random.choice(seznam_polovick(-10, 10) + seznam_tretinj(-10, 10))
        else:
            primerjava = splosna_oblika()[-1]
        preveri(splosna1 != primerjava)
        neenacaj = random.choice(['<', '<=', '>', '>='])
        neenakost = sympy.Rel(splosna1, primerjava, neenacaj)
        nicli = sympy.solve(sympy.Eq(splosna1, primerjava), x)
        if len(nicli) == 0:  # TODO preveri da dela
            pass
        else:
            preveri(
                nicli[0].is_real and abs(max(nicli, key=abs)) < 10 and sympy.denom(max(nicli, key=sympy.denom)) < 20)
        resitev = sympy.solveset(neenakost, domain=sympy.S.Reals)
        # print(nicli, sympy.denom(max(nicli, key=sympy.denom)))
        return {'neenakost': neenakost, 'resitev': resitev}


class SkoziTocke(Naloga):
    """
    Naloga za določanje predpisa kvadratne funkcije iz treh točk, skozi katere poteka graf funkcije. Reševanje sistema treh enačb in treh neznank.

    :param nakljucne_tocke: izbrane so 3 naključne točke ali ničla, začetna vrednost in ena naključna vrednost


    >>> SkoziTocke().sestavi()
    {'x1': -3, 'x2': 0, 'x3': 2, 'y1': 0, 'y2': -30, 'y3': -30, 'funkcija': 2*x**2 - 4*x - 30}

    >>> SkoziTocke(nakljucne_tocke=True).sestavi()
    {'x1': -5, 'x2': -3, 'x3': -4, 'y1': -13/3, 'y2': 0, 'y3': -5/3, 'funkcija': -x**2/2 - 11*x/6 - 1}
    """
    besedilo_posamezne = r'''Graf kvadratne funkcije $f$ poteka skozi točke $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$, 
        $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$ in $C({{latex(naloga.x3)}},{{latex(naloga.y3)}})$. Določi 
        predpis funkcije $f$.'''
    besedilo_vecih = r''' Določi predpis kvadratne funkcije $f$, katere graf poteka skozi točke:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$, 
        $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$, $C({{latex(naloga.x3)}},{{latex(naloga.y3)}})$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$f(x)={{latex(naloga.funkcija)}}$ '''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f(x)={{latex(naloga.funkcija)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, nakljucne_tocke=False, **kwargs):
        super().__init__(**kwargs)
        self.nakljucne_tocke = nakljucne_tocke

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        (a, nicla1, nicla2, funkcija) = nicelna_oblika(risanje=True)
        if not self.nakljucne_tocke:
            x1 = nicla1
            x2 = 0
        else:
            x1 = random.randint(-5, 5)
            x2 = random.randint(-5, 5)

        x3 = random.randint(-5, 5)
        preveri(len({x1, x2, x3}) == 3)
        y1 = funkcija.subs(x, x1)
        y2 = funkcija.subs(x, x2)
        y3 = funkcija.subs(x, x3)

        return {'x1': x1, 'x2': x2, 'x3': x3, 'y1': y1, 'y2': y2, 'y3': y3,
                'funkcija': sympy.expand(funkcija)}  # Todo expand v besedilu
