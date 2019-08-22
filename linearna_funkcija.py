from generiranje import Naloga, preveri
import random
import sympy


# ~~~~~Pomožne funkcije
def seznam_polovick(od=-10, do=10):
    """
    Funkcija sestavi seznam vseh celih iz polovic med vrednostima od in do (brez 0).

    :param od: najmanjša vrednost
    :param do: največja vrednost
    :return: seznam celih števil in polovic


    >>> seznam_polovick()
    [-10, -19/2, -9, -17/2, -8, -15/2, -7, -13/2, -6, -11/2, -5, -9/2, -4, -7/2, -3, -5/2, -2, -3/2, -1, -1/2, 1/2, 1, 3/2, 2, 5/2, 3, 7/2, 4, 9/2, 5, 11/2, 6, 13/2, 7, 15/2, 8, 17/2, 9, 19/2, 10, 21/2]

    >>> seznam_polovick(od=0, do=3)
    [1/2, 1, 3/2, 2, 5/2, 3, 7/2]
    """
    return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]


def seznam_tretinj(od=-10, do=10):
    """
    Funkcija sestavi seznam vseh celih iz tretinj med vrednostima od in do (brez 0).

    :param od: najmanjša vrednost
    :param do: največja vrednost
    :return: seznam celih števil in tretinj


    >>> seznam_tretinj()
    [-10, -29/3, -28/3, -9, -26/3, -25/3, -8, -23/3, -22/3, -7, -20/3, -19/3, -6, -17/3, -16/3, -5, -14/3, -13/3, -4, -11/3, -10/3, -3, -8/3, -7/3, -2, -5/3, -4/3, -1, -2/3, -1/3, 1/3, 2/3, 1, 4/3, 5/3, 2, 7/3, 8/3, 3, 10/3, 11/3, 4, 13/3, 14/3, 5, 16/3, 17/3, 6, 19/3, 20/3, 7, 22/3, 23/3, 8, 25/3, 26/3, 9, 28/3, 29/3, 10, 31/3, 32/3]

    >>> seznam_tretinj(od=0, do=3)
    [1/3, 2/3, 1, 4/3, 5/3, 2, 7/3, 8/3, 3, 10/3, 11/3]
    """
    return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]


def eksplicitna_premica():
    """
    Vrne naključno eksplicitno obliko premice, ki jo moramo izenačiti z y.

    :return: smerni koeficient, začetno vrednost in eksplicitno podano premico


    >>> eksplicitna_premica()
    (-4/3, 2, 2 - 4*x/3)

    >>> eksplicitna_premica()
    (3, -11/3, 3*x - 11/3)
    """
    # Funkcija vrne naključno eksplicitno podano premico
    k = random.choice(seznam_polovick(-3, 3) + seznam_tretinj(-3, 3))
    n = random.choice(seznam_polovick(-4, 4) + seznam_tretinj(-4, 4))
    x = sympy.symbols('x')
    eksplicitna = k * x + n
    return (k, n, eksplicitna)


def implicitna_premica():
    """
    Vrne implicitno podano obliko premice, ki jo moramo izenačiti z 0. Premice niso vzporedne z osema.

    :return: koeficiente in implicitno podano premico


    >>> implicitna_premica()
    (-7, 2, 3, -7*x + 2*y + 3)

    >>> implicitna_premica()
    (-2, 7, -6, -2*x + 7*y - 6)

    """
    seznamStevil = [x for x in range(-10, 10) if x != 0]
    a = random.choice(seznamStevil)
    b = random.choice(seznamStevil)
    c = random.choice(seznamStevil)
    x = sympy.symbols('x')
    y = sympy.symbols('y')
    implicitna = sympy.simplify(a * x + b * y + c)
    return (a, b, c, implicitna)


def skozi_tocki(x1, y1, x2, y2):
    """
    Izračuna predpis premice skozi dve točki.

    :param x1: x koordinata prve točke
    :param y1: y koordinata prve točke
    :param x2: x koordinata druge točke
    :param y2: y koordinata druge točke
    :return: smerni koeficient, začetno vrednost in eksplicitno podano premico


    >>> skozi_tocki(1,1,2,4)
    (3.0, -2.0, 3.0*x - 2.0)

    >>> skozi_tocki(-3,5,2,6)
    (0.2, 5.6, 0.2*x + 5.6)
    """
    x = sympy.symbols('x')
    k = (y2 - y1) / (x2 - x1)
    n = y1 - k * x1
    return (k, n, k * x + n)


def izberi_koordinato(od=-10, do=10):
    """
    Izbere poljubno celoštevilsko koordinato med vrednostima od in do.

    :param od: najmanjša vrednost
    :param do: največja vrednost
    :return: celoštevilsko koordinato


    >>> izberi_koordinato()
    2

    >>> izberi_koordinato(do=0)
    -4
    """
    koordinata = random.randint(od, do)
    return koordinata


def razdalja_med_tockama(x1, y1, x2, y2):
    """
    Izračuna razdaljo med dvema točkama.

    :param x1: abscisa prve točke
    :param y1: ordinata prve točke
    :param x2: abscisa druge točke
    :param y2: ordinata druge točke
    :return: razdaljo med točkama


    >>> razdalja_med_tockama(-14,6,-17,8)
    sqrt(13)

    >>> razdalja_med_tockama(2,-8,5,-12)
    5
    """

    razdalja = sympy.Point(x1, y1).distance(sympy.Point(x2, y2))  # Todo preveri da deluje razdalja
    # razdalja =sympy.simplify(sympy.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2)))
    return razdalja


# ~~~~~Posamezne naloge iz poglavja Linearna funkcija
# TODO ideja: reši linearno (ne)enačbo (težja s kvadrati ki se odštejejo)

class PremicaSkoziTocki(Naloga):
    """
    Naloga za določanje enačbe premice skozi 2 točki.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> PremicaSkoziTocki().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> PremicaSkoziTocki().primer()
    """
    besedilo_posamezne = r'''Zapiši enačbo premice skozi točki $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$ in $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$.'''
    besedilo_vecih = r'''Zapiši enačbo premice skozi točki:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$, $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$y={{naloga.premica}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $y={{naloga.premica}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):  # TODO lepše rešitve
        x1 = random.choice(seznam_polovick(-5, 5) + seznam_tretinj(-5, 5))
        y1 = random.choice(seznam_polovick(-5, 5) + seznam_tretinj(-5, 5))
        x2 = random.randint(-10, 10)
        y2 = random.randint(-10, 10)
        preveri(x1 != x2 and y1 != y2)  # Preveri, da sta 2 različni točki in nista vzporedni osem
        premica = sympy.latex(skozi_tocki(x1, y1, x2, y2)[-1])
        return {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'premica': premica}


class RazdaljaMedTockama(Naloga):  # Todo težja racionalne koordinate? #TODO preveri jinja latex
    """
    Naloga za računanje razdalje med dvema točkama v koordinatenm sistemu.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> RazdaljaMedTockama().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> RazdaljaMedTockama().primer()
    """
    besedilo_posamezne = r'''Natančno izračunaj razdaljo med točkama $A({{naloga.x1}},{{naloga.y1}})$ in $B({{naloga.x2}},{{naloga.y2}})$.'''
    besedilo_vecih = r'''Natančno izračunaj razdaljo med točkama
                                          \begin{enumerate}
                                          {% for naloga in naloge %}
                                          \item $A({{naloga.x1}},{{naloga.y1}})$ in $B({{naloga.x2}},{{naloga.y2}})$
                                          {% endfor %}
                                          \end{enumerate}'''

    resitev_posamezne = r'''$d(A,B)={{naloga.razdalja}}$'''
    resitev_vecih = r'''\begin{enumerate}
                                         {% for naloga in naloge %}
                                         \item $d(A,B)={{naloga.razdalja}}$
                                         {% endfor %}
                                         \end{enumerate}'''

    def _poskusi_sestaviti(self):
        x1 = izberi_koordinato()
        y1 = izberi_koordinato()
        x2 = izberi_koordinato()
        y2 = izberi_koordinato()
        preveri(x1 != x2 and y1 != y2)
        razdalja = sympy.latex(razdalja_med_tockama(x1, y1, x2, y2))
        return {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'razdalja': razdalja}


class OblikeEnacbPremice(Naloga):  # TODO preveri jinja latex
    """
    Naloga za pretvarjanje med različnimi oblikami enačbe premice.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> OblikeEnacbPremice().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> OblikeEnacbPremice().primer()
    """
    besedilo_posamezne = r'''Zapiši implicitno in odsekovno obliko premice podane z enačbo ${{naloga.implicitna}}$'''
    besedilo_vecih = r''' Zapiši implicitno in odsekovno obliko premice podane z enačbo:
                                        \begin{enumerate}
                                          {% for naloga in naloge %}
                                          \item ${{naloga.implicitna}}$
                                          {% endfor %}
                                          \end{enumerate}'''
    resitev_posamezne = r'''${{naloga.eksplicitna}}$ in ${{naloga.odsekovna}}$'''
    resitev_vecih = r'''
                                        \begin{enumerate}
                                          {% for naloga in naloge %}
                                          \item ${{naloga.eksplicitna}}$ in ${{naloga.odsekovna}}$
                                          {% endfor %}
                                          \end{enumerate}
                                          '''

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        (a, b, c, implicitnaOblika) = implicitna_premica()
        implicitna = sympy.latex(sympy.Eq(implicitnaOblika, 0))
        eksplicitna = sympy.latex(sympy.Eq(y,
                                           sympy.Rational(-a, b) * x + sympy.Rational(-c, b)))
        odsekovna = sympy.latex(
            sympy.Eq(sympy.Add(sympy.Mul(x, sympy.Pow(sympy.Rational(c, -a), -1, evaluate=False), evaluate=False),
                               sympy.Mul(y, sympy.Pow(sympy.Rational(c, -b), -1, evaluate=False), evaluate=False),
                               evaluate=False), 1))

        return {'implicitna': implicitna, 'eksplicitna': eksplicitna, 'odsekovna': odsekovna}


class PremiceTrikotnik(Naloga):  # TODO preveri jinja latex
    """
    Naloga za računanje ploščine trikotnika, ki ga dve premici oklepata z abscisno osjo.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> PremiceTrikotnik().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> PremiceTrikotnik().primer()
    """
    besedilo_posamezne = r''' Izračunaj ploščino trikotnika, ki ga premici ${{naloga.premica1}}$ in ${{naloga.premica2}}$ oklepata z abscisno osjo. '''
    besedilo_vecih = r''' Izračunaj ploščino trikotnika, ki ga premici oklepata z abscisno osjo:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.premica1}}$ in ${{naloga.premica2}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$S={{naloga.ploscina}}$ '''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $S={{naloga.ploscina}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        x1 = izberi_koordinato(1, 5)
        y1 = 0
        x2 = random.choice([x for x in range(-5, 6) if x != 0])
        y2 = random.choice([x for x in range(-5, 6) if x != 0])
        x3 = izberi_koordinato(-5, 0)
        y3 = 0
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        preveri(x2 != x1 and x2 != x3)  # premici sta vzporedni
        if x2 == x1:
            premica1 = sympy.Eq(x, x1)
        else:
            k1 = sympy.Rational((y2 - y1), (x2 - x1))
            n1 = y1 - k1 * x1
            premica1 = sympy.Eq(y, k1 * x + n1)
        if x3 == x2:
            premica2 = sympy.Eq(x, x3)
        else:
            k2 = sympy.Rational((y3 - y2), (x3 - x2))
            n2 = y3 - k2 * x3
            premica2 = sympy.Eq(y, k2 * x + n2)

        ploscina_trikotnika = sympy.latex(
            sympy.simplify(abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2).evalf(3)).rstrip('0').rstrip('.')

        return {'premica1': sympy.latex(premica1), 'premica2': sympy.latex(premica2), 'ploscina': ploscina_trikotnika}


class NarisiLinearnoFunkcijo(Naloga):
    """
    Naloga za risanje grafa linearne premice.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> NarisiLinearnoFunkcijo().primer()


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> NarisiLinearnoFunkcijo().primer()

    """
    besedilo_posamezne = r'''Nariši graf funkcije linearne $f(x) = {{latex(naloga.linearna)}}$.'''
    besedilo_vecih = r''' Nariši graf linearne funkcije:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $f(x) = {{latex(naloga.linearna)}}$
    {% endfor %}
    \end{enumerate}
    '''

    resitev_posamezne = r'''$f(x)={{latex(naloga.linearna)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
    xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
    extra x ticks={ {{naloga.nicla}} },
    extra y ticks={ {{naloga.n}} },
    extra x tick labels={ ${{latex(naloga.nicla)}}$ },
    extra y tick labels={ ${{latex(naloga.n)}}$},
    extra x tick style={xticklabel style={above},},
    extra y tick style={yticklabel style={right},},]
    \addplot[domain =-5:5, color=black]{ {{naloga.linearna}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f(x) = {{latex(naloga.linearna)}}$\par
     \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
    xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
    extra x ticks={ {{naloga.nicla}} },
    extra y ticks={ {{naloga.n}} },
    extra x tick labels={ ${{latex(naloga.nicla)}}$ },
    extra y tick labels={ ${{latex(naloga.n)}}$},
    extra x tick style={xticklabel style={above},},
    extra y tick style={yticklabel style={right},},]
    \addplot[domain =-5:5, color=black]{ {{naloga.linearna}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        (k, n, eksplicitna) = eksplicitna_premica()
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        f = sympy.symbols('f(x)')
        nicla = (-n) / k
        return {'linearna': eksplicitna, 'n': n, 'nicla': nicla}


class VrednostiLinearne(Naloga):
    """
    Naloga za računanje vrednosti x oziroma f(x) linearne funkcije. Potrebno določiti tudi kdaj je funkcija negativna.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> VrednostiLinearne().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> VrednostiLinearne().primer()
    """
    besedilo_posamezne = r'''Dana je funkcija s predpisom ${{naloga.linearna}}$. Izračunajte vrednost $f({{naloga.x1}})$ in za kateri $x$ je $f(x)={{naloga.y2}}$. Za katere vrednosti $x$ so vrednosti funkcije negativne? '''

    besedilo_vecih = r''' Za podano funkcijo $f$ izračunaj $f(x_0)$ in za kateri $x$ je $f(x)=y_1$. Za katere vrednosti $x$ so vrednosti funkcije negativne?
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.linearna}}$, $x_0={{naloga.x1}}$, $y_1={{naloga.y2}}$
    {% endfor %}
    \end{enumerate}
    '''

    resitev_posamezne = r'''
    $f({{naloga.x1}})={{naloga.y1}}$, $x={{naloga.x2}}$, $x \in {{naloga.negativno}}$'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f({{naloga.x1}})={{naloga.y1}}$, $x={{naloga.x2}}$, $x \in {{naloga.negativno}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        f = sympy.symbols('f(x)')

        (k, n, funkcija) = eksplicitna_premica()

        x1 = random.choice(seznam_polovick(-3, 3) + seznam_tretinj(-3, 3))
        x2 = random.choice(seznam_polovick(-3, 3) + seznam_tretinj(-3, 3))
        preveri(x1 != x2)
        y1 = k * x1 + n
        y2 = k * x2 + n

        negativno = sympy.latex(sympy.solveset(funkcija < 0, domain=sympy.S.Reals))
        return {'linearna': sympy.latex(sympy.Eq(f, funkcija)), 'x1': sympy.latex(x1), 'x2': sympy.latex(x2),
                'y1': sympy.latex(y1), 'y2': sympy.latex(y2), 'negativno': negativno}


class Neenacba(Naloga):
    """
    Naloga za reševanje linearne neenačbe.

    :param kvadratna: v računu nastopa kvadratni člen, ki se odšteje


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> Neenacba().primer()


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> Neenacba(kvadratna=True).primer()

    """
    besedilo_posamezne = r'''Reši neenačbo ${{latex(naloga.neenacba)}}$.'''
    besedilo_vecih = r'''Reši neenačbo:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.neenacba)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x \in {{latex(naloga.resitev)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x \in {{latex(naloga.resitev)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, kvadratna=False, **kwargs):
        super().__init__(**kwargs)
        self.kvadratna = kvadratna

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        izbor = [x for x in range(-5, 5) if x != 0]
        if not self.kvadratna:
            a = random.choice(izbor)
            b = random.choice(izbor)
            c = random.choice(izbor)
            d = random.choice(izbor)
            leva = a * x + b
            desna = c * x + d
        else:
            a = random.choice(izbor)
            x1 = random.choice(izbor)
            x2 = random.choice(izbor)
            x3 = random.choice(izbor)
            x4 = random.choice(izbor)
            leva = sympy.Mul(a, (x - x1), (x - x2), evaluate=False)
            desna = a * (x - x3) * (x - x4)

        neenacaj = random.choice(['<', '<=', '>', '>='])
        neenacba = sympy.Rel(leva, desna, neenacaj)
        resitev = sympy.solveset(sympy.expand(neenacba), x, domain=sympy.S.Reals)
        return {'neenacba': neenacba, 'resitev': resitev}


class SistemDvehEnacb(Naloga):
    """
    Naloga za reševanje sistema dveh enačb z dvema nezankama.

    :param racionalne_resitve: naloga ima racionalne ali celoštevilske rešitve


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> SistemDvehEnacb().primer()


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> SistemDvehEnacb(racionalne_resitve=True).primer()

    """
    besedilo_posamezne = r'''Reši sistem enačb ${{latex(naloga.enacba1)}}$ in ${{latex(naloga.enacba2)}}$.'''
    besedilo_vecih = r'''Reši sistem enačb:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.enacba1)}}$, ${{latex(naloga.enacba2)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, racionalne_resitve=False, **kwargs):
        super().__init__(**kwargs)
        self.racionalne_resitve = racionalne_resitve

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        izborCela = [x for x in range(-5, 6) if x != 0]
        izborUlomki = [sympy.Rational(x, 2) for x in [-3, -1, 1, 3]] + [sympy.Rational(x, 3) for x in
                                                                        [-2, -1, 1, 2]] + [sympy.Rational(x, 4) for x in
                                                                                           [-3, -1, 1, 3]]
        if not self.racionalne_resitve:
            x1 = random.choice(izborCela + [0])
            y1 = random.choice(izborCela + [0])
        else:
            x1 = random.choice(izborCela + izborUlomki + [0])
            y1 = random.choice(izborCela + izborUlomki + [0])
        a = random.choice(izborCela)
        b = random.choice(izborCela)
        d = random.choice(izborCela)
        e = random.choice(izborCela)
        preveri((a, b) != (d, e) and (x1 != 0 or y1 != 0))
        c = a * x1 + b * y1
        f = d * x1 + e * y1
        enacba1 = a * x + b * y
        enacba2 = d * x + e * y
        return {'enacba1': sympy.Eq(enacba1, c), 'enacba2': sympy.Eq(enacba2, f), 'x': x1, 'y': y1}


class SistemTrehEnacb(Naloga):
    """Naloga za reševanje sistema treh enačb s tremi neznankami.

    :param manjsi_koeficienti: koeficienti (in rešitve) so med -2 in 2, drugače pa med -5 in 5


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> SistemTrehEnacb().primer()


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from linearna_funkcija import *
        >>> SistemTrehEnacb(manjsi_koeficienti=False).primer()

    """
    besedilo_posamezne = r'''Reši sistem enačb ${{latex(naloga.enacba1)}}$, ${{latex(naloga.enacba2)}}$ in ${{latex(naloga.enacba3)}}$.'''
    besedilo_vecih = r'''Reši sistem enačb:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.enacba1)}}$, ${{latex(naloga.enacba2)}}$, ${{latex(naloga.enacba3)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$, $z={{latex(naloga.z)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$, $z={{latex(naloga.z)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, manjsi_koeficienti=True, **kwargs):
        super().__init__(**kwargs)
        self.manjsi_koeficienti = manjsi_koeficienti

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        z = sympy.symbols('z')
        if self.manjsi_koeficienti:
            izborCela = [-2, -1, 0, 1, 2]
        else:
            izborCela = list(range(-5, 6))
        x1 = random.choice(izborCela)
        y1 = random.choice(izborCela)
        z1 = random.choice(izborCela)

        a = random.choice(izborCela)
        b = random.choice(izborCela)
        c = random.choice(izborCela)
        e = random.choice(izborCela)
        f = random.choice(izborCela)
        g = random.choice(izborCela)
        i = random.choice(izborCela)
        j = random.choice(izborCela)
        k = random.choice(izborCela)

        preveri(len({(a, b, c), (e, f, g), (i, j, k)}) == 3 and (
                x1 != 0 or y1 != 0 or z1 != 0))
        d = a * x1 + b * y1 + c * z1
        h = e * x1 + f * y1 + g * z1
        l = i * x1 + j * y1 + k * z1
        enacba1 = a * x + b * y + c * z
        enacba2 = e * x + f * y + g * z
        enacba3 = i * x + j * y + k * z
        return {'enacba1': sympy.Eq(enacba1, d), 'enacba2': sympy.Eq(enacba2, h), 'enacba3': sympy.Eq(enacba3, l),
                'x': x1, 'y': y1, 'z': z1}
