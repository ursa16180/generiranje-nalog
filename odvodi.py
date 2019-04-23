from generiranje import Naloga, preveri
import sympy
import random
import enum
import linearnaFunkcija
import jinja2


class Funkcija(enum.Enum):
    RACIONALNA = "racionalna"
    POLINOM = "polinom"
    LOGARITEM = "logaritem"
    POTENCNA = "potencna"
    KOTNA = "kotna"
    KROZNA = "krozna"


def kotMedPremicama(k1, k2):
    # Funkcija v radianih izračuna kot med premicama
    if k1 * k2 == -1:
        kot = sympy.pi / 2
    else:
        kot = sympy.atan(abs((k2 - k1) / (1 + k1 * k2)))
    return kot


def DolociPolinom(min_stopnja=2, max_stopnja=3):
    x = sympy.symbols('x')
    stopnja = random.randint(min_stopnja, max_stopnja)
    polinom = sympy.Poly([random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnja)],
                         x).as_expr()  # Pazi za stacionarne naj bo največ 3.stopnje!
    return polinom


def DolociRacionalno(min_stopnja_stevca=2, max_stopnja_stevca=4, min_stopnja_imenovalca=1, max_stopnja_imenovalca=2):
    x = sympy.symbols('x')
    stopnjaStevca = random.randint(min_stopnja_stevca, max_stopnja_stevca)
    stopnjaImenovalca = random.randint(min_stopnja_imenovalca, max_stopnja_imenovalca)
    stevec = sympy.Poly([random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnjaStevca)],
                        x).as_expr()
    imenovalec = sympy.Poly(
        [random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnjaImenovalca)],
        x).as_expr()
    racionalna = sympy.simplify(stevec / imenovalec)
    return racionalna


def DolociPotencna(baze=[sympy.E, 2, 3, 5]):
    x = sympy.symbols('x')
    baza = random.choice(baze)
    eksponentna = baza ** x
    return eksponentna


def DolociLogaritem(baze=[sympy.E, 2, 3, 4, 5, 10]):
    x = sympy.symbols('x')
    baza = random.choice(baze)
    logaritem = sympy.log(x, baza)  # todo izpis log_baza v latexu
    # Todo latex izpis ln namesto log
    return logaritem


def DolociKotna():
    x = sympy.symbols('x')
    kosinus = sympy.cos(x)
    sinus = sympy.sin(x)
    tangens = sympy.tan(x)
    kotangens = sympy.cot(x)
    return [kosinus, sinus, tangens, kotangens]


def DolociKrozna():
    x = sympy.symbols('x')
    arcusKosinus = sympy.acos(x)
    arcusSinus = sympy.asin(x)
    arcusTangens = sympy.atan(x)
    arcusKotangens = sympy.acot(x)
    return [arcusKosinus, arcusSinus, arcusTangens, arcusKotangens]


# ~~~~~ Naloge iz sklopa odvodi
class KotMedPremicama(Naloga):
    besedilo_posamezne = r'''Izračunaj kot, ki ga oklepata $y={{latex(naloga.premica1)}}$ in {{naloga.premica2}}.'''
    # TODO kako različna navodila za lažjo in težjo? Je potrebno ali pustim tako kot je?
    besedilo_vecih = r'''Izračunaj kot, ki ga oklepata:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $y={{latex(naloga.premica1)}}$ in {{naloga.premica2}}
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$\varphi ={{naloga.stopinje}}\degree{{naloga.minute}}' $'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $\varphi ={{naloga.stopinje}}\degree{{naloga.minute}}' $
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, lazja=True, **kwargs):
        super().__init__(**kwargs)
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        k1, k2 = random.sample([x for x in range(-6, 7) if x != 0], 2)
        n1, n2 = random.sample([x for x in range(-10, 11) if x != 0], 2)
        premica1 = k1 * x + n1
        if self.lazja:
            premica2 = 'abscisna os'
            k2 = 0
        else:
            premica2 = '$' + sympy.latex(sympy.Eq(y, k2 * x + n2)) + '$'

        kot = sympy.N(sympy.deg(kotMedPremicama(k1, k2)))
        stop = kot // 1
        min = round(kot % 1 * 60)  # Todo če ni minut
        return {'premica1': premica1, 'premica2': premica2, 'stopinje': stop, 'minute': min}


class OdvodElementarne(Naloga):
    besedilo_posamezne = r'''Določi odvod funkcije $f(x)={{latex(naloga.funkcija)}}$.'''
    besedilo_vecih = r'''Določi odvod funkcije $f$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $f(x)={{latex(naloga.funkcija)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$f'(x)={{latex(naloga.odvod)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f'(x)={{latex(naloga.odvod)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, funkcije=[Funkcija.POLINOM, Funkcija.RACIONALNA, Funkcija.POTENCNA, Funkcija.LOGARITEM,
                                 Funkcija.KOTNA], lazja=True,
                 **kwargs):
        super().__init__(**kwargs)
        self.funkcije = funkcije
        if self.funkcije == []:
            raise ValueError(
                'Izbrana mora biti vsaj ena izmed funkcij: polinom, acionalna fukcija, kotna funkcija, krožna funkcija,'
                ' potencna funkcija ali logaritemska funkcija. ')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')

        if self.lazja:
            izbrana1 = random.choice(self.funkcije)
            # funkcija2 = x  # todo Če izbere poli ali racionalno, nej bo funkcija2 kar x
            funkcija2 = sympy.Poly([random.choice([-2, -1, 1, 2, 3]), random.randint(-3, 3)], x).as_expr()
        else:
            izbrana1 = random.choice(self.funkcije)
            izbrana2 = random.choice([x for x in self.funkcije if x!=Funkcija.RACIONALNA])
            if izbrana2.value == 'polinom':
                funkcija2 = DolociPolinom()
            if izbrana2.value == 'potencna':
                funkcija2 = DolociPotencna()
            if izbrana2.value == 'logaritem':
                funkcija2 = DolociLogaritem(baze=[sympy.E])
            if izbrana2.value == 'kotna':
                funkcija2 = random.choice(DolociKotna())
            if izbrana2.value == 'krozna':
                funkcija2 = random.choice(DolociKrozna())

        if izbrana1.value == 'polinom':  # TODO manj if-ov
            funkcija1 = DolociPolinom()
        if izbrana1.value == 'racionalna':
            funkcija1 = DolociRacionalno()
        if izbrana1.value == 'potencna':
            funkcija1 = DolociPotencna()  # Todo lepši izpis logaritmov
        if izbrana1.value == 'logaritem':
            funkcija1 = DolociLogaritem(baze=[sympy.E])
        if izbrana1.value == 'kotna':
            funkcija1 = random.choice(DolociKotna())
        if izbrana1.value == 'krozna':
            funkcija1 = random.choice(DolociKrozna())



        funkcija = funkcija1.subs(x, funkcija2)
        odvod = funkcija.diff(x)
        return {'funkcija': funkcija, 'odvod': odvod}


class OdvodSestavljenih(Naloga):
    besedilo_posamezne = r'''Določi odvod funkcije $f(x)={{latex(naloga.funkcija)}}$.'''
    besedilo_vecih = r'''Določi odvod funkcije $f$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $f(x)={{latex(naloga.funkcija)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$f'(x)={{latex(naloga.odvod)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $f'(x)={{latex(naloga.odvod)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, funkcije=[Funkcija.POLINOM, Funkcija.RACIONALNA, Funkcija.POTENCNA, Funkcija.LOGARITEM,
                                 Funkcija.KOTNA], **kwargs):
        super().__init__(**kwargs)
        if funkcije == []:
            raise ValueError(
                'Izbrana mora biti vsaj ena izmed funkcij: polinom, acionalna fukcija, kotna funkcija, krožna funkcija,'
                ' potencna funkcija ali logaritemska funkcija. ')
        self.funkcije =funkcije

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        izbrana1 = random.choice(self.funkcije)
        izbrana2 = random.choice(self.funkcije)

        if izbrana1.value == 'polinom':  # TODO manj if-ov
            funkcija1 = DolociPolinom(min_stopnja=1, max_stopnja=2)
        if izbrana1.value == 'racionalna':
            funkcija1 = DolociRacionalno()
        if izbrana1.value == 'potencna':
            funkcija1 = DolociPotencna()
        if izbrana1.value == 'logaritem':
            funkcija1 = DolociLogaritem(baze=[sympy.E])
        if izbrana1.value == 'kotna':
            funkcija1 = random.choice(DolociKotna())
        if izbrana1.value == 'krozna':
            funkcija1 = random.choice(DolociKrozna())

        if izbrana2.value == 'polinom':
            funkcija2 = DolociPolinom(min_stopnja=1, max_stopnja=2)
        if izbrana2.value == 'racionalna':
            funkcija2 = DolociRacionalno()
        if izbrana2.value == 'potencna':
            funkcija2 = DolociPotencna()
        if izbrana2.value == 'logaritem':
            funkcija2 = DolociLogaritem(baze=[sympy.E])
        if izbrana2.value == 'kotna':
            funkcija2 = random.choice(DolociKotna())
        if izbrana2.value == 'krozna':
            funkcija2 = random.choice(DolociKrozna())

        funkcija1 = funkcija1.subs(x, random.choice([-2, -1, 2]) * x)
        preveri(funkcija1 != funkcija2)
        operatorji = [
            lambda a, b: a + b,
            lambda a, b: a - b,
            lambda a, b: a * b,
            lambda a, b: a / b]
        operator = random.choice(operatorji)
        funkcija = operator(funkcija1, funkcija2)
        odvod = sympy.simplify(funkcija).diff(x)
        return {'funkcija': funkcija, 'odvod': odvod}


class Tangenta(Naloga):
    besedilo_posamezne = r'''Zapiši enačbo tangente na graf funkcije $f(x)={{latex(naloga.funkcija)}}$ v točki z absciso $x_0={{latex(naloga.abscisa)}}$.'''

    besedilo_vecih = r'''Zapiši enačbo tangente na graf funkcije $f$ v točki z absciso $x_0$:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $f(x)={{latex(naloga.funkcija)}}$, $x_0={{latex(naloga.abscisa)}}$
        {% endfor %}
        \end{enumerate}
        '''
    resitev_posamezne = r'''$f'(x)={{latex(naloga.tangenta)}}$'''
    resitev_vecih = r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $f'(x)={{latex(naloga.tangenta)}}$
         {% endfor %}
         \end{enumerate}
         '''

    def __init__(self, funkcije=[Funkcija.POLINOM, Funkcija.RACIONALNA, Funkcija.POTENCNA, Funkcija.LOGARITEM,
                                 Funkcija.KOTNA], **kwargs):
        super().__init__(**kwargs)
        self.funkcije = funkcije
        if funkcije == []:
            raise ValueError(
                'Izbrana mora biti vsaj ena izmed funkcij: polinom, acionalna fukcija, kotna funkcija, krožna funkcija,'
                ' potencna funkcija ali logaritemska funkcija. ')


def poskusi_sestaviti(self):
    x = sympy.symbols('x')
    izbrana = random.choice(self.funkcije)

    if izbrana.value == 'polinom':
        funkcija = DolociPolinom()
        x0 = random.randint(-2, 2)

    if izbrana.value == 'racionalna':
        stopnjaStevca = random.randint(2, 3)
        stopnjaImenovalca = 3 - stopnjaStevca
        funkcija = DolociRacionalno(min_stopnja_stevca=stopnjaStevca, max_stopnja_stevca=stopnjaStevca,
                                    min_stopnja_imenovalca=stopnjaImenovalca, max_stopnja_imenovalca=stopnjaImenovalca)
        x0 = random.randint(-2, 2)
    if izbrana.value == 'potencna':
        baza = random.choice([sympy.E, 2, 3, 5])
        funkcija = DolociPotencna(baze=[baza])
        x0 = random.choice([sympy.log(n, baza) for n in [1, 2, 3]])  # Todo lepši izpis logaritmov

    if izbrana.value == 'logaritem':
        # baza = random.choice([2, 3, 4, 5, 10])
        # logaritem = sympy.log(x, baza) #todo izpis log_baza v latexu
        # funkcije.append(logaritem)
        funkcija = DolociLogaritem(baze=[sympy.E])
        x0 = sympy.E ** (random.randint(-1, 2))
    if izbrana.value == 'kotna':
        funkcija = random.choice(DolociKotna())
        x0 = random.choice(
            [sympy.pi / x for x in [6, 3, 4, 2]])  # TODO dodaj 0 in pi, vendar pazi da ni izbran tna/cot
    if izbrana.value == 'krozna':  # TODO izberi krožne tudi tangens
        arcusKosinus = sympy.acos(x)
        arcusSinus = sympy.asin(x)
        x0 = random.choice([0, 1 / 2, sympy.sqrt(2) / 2, sympy.sqrt(3) / 2, 1])
        # arcusTangens = sympy.atan(x)#Todo dodaj
        # arcusKotangens = sympy.acot(x)
        # tocka = random.choice([ sympy.sqrt(3), 1, sympy.sqrt(3) / 3])#Todo dodaj 0 vendar pazi da tan/cot definirana
        funkcija = random.choice([arcusKosinus, arcusSinus])  # , arcusTangens, arcusKotangens])
    odvod = sympy.simplify(funkcija).diff(x)
    y0 = funkcija.subs(x, x0)
    k = odvod.subs(x, x0)
    n = y0 - k * x0
    tangenta = k * x + n
    return {'funkcija': funkcija, 'abscisa': x0, 'tangenta': tangenta}


class KotMedGrafoma(Naloga):
    besedilo_posamezne = r'''Na minuto natančno izračunaj kot med grafoma funkcij $f(x)={{latex(naloga.funkcija1)}}$ in $g(x)={{latex(naloga.funkcija2)}}$.'''
    besedilo_vecih = r'''Na minuto natančno izračunaj kot med grafoma funkcij $f$ in $g$
            \begin{enumerate}
            {% for naloga in naloge %}
            \item $f(x)={{latex(naloga.funkcija1)}}$, $g(x)={{latex(naloga.funkcija2)}}$
            {% endfor %}
            \end{enumerate}
            '''
    resitev_posamezne = r'''$\varphi ={{naloga.stopinje}}\degree{{naloga.minute}}' $'''
    resitev_vecih = r'''
            \begin{enumerate}
             {% for naloga in naloge %}
             \item $\varphi ={{naloga.stopinje}}\degree{{naloga.minute}}' $
             {% endfor %}
             \end{enumerate}
             '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def poskusi_sestaviti(self):
        x = sympy.symbols('x', real=True)
        izbor = random.choice(['kvadratna', 'potencna', 'logaritem'])
        if izbor == 'potencna':
            baza = random.choice([sympy.E, 2, 3, 5])
            eksponentna = baza ** x
            a = random.randint(1, 2)
            funkcija1 = eksponentna.subs(x, sympy.Poly([a, random.randint(-3, 3)], x).as_expr())
            funkcija2 = eksponentna.subs(x, sympy.Poly([-a, random.randint(-3, 3)], x).as_expr())
        if izbor == 'logaritem':
            # baza = random.choice([2, 3, 4, 5, 10])
            # logaritem = sympy.log(x, baza) #todo izpis log_baza v latexu
            # funkcije.append(logaritem)
            naravniLogaritem = sympy.ln(x)  # Todo latex izpis ln namesto log
            a = random.randint(1, 2)
            funkcija1 = naravniLogaritem.subs(x, sympy.Poly([a, random.randint(-3, 3)], x).as_expr())
            funkcija2 = naravniLogaritem.subs(x, sympy.Poly([-a, random.randint(-3, 3)], x).as_expr())
        if izbor == 'kvadratna':
            x0 = random.choice([-2, -1, 1, 2])
            y0 = random.randint(-2, 2)
            a = random.choice([1, 2])
            c1 = random.randint(-4, -1)
            c2 = random.randint(0, 4)
            b1 = (y0 - a * x0 ** 2 - c1) / x0
            b2 = (y0 - a * x0 ** 2 - c2) / x0
            funkcija1 = sympy.Poly([int(a), int(b1), int(c1)], x).as_expr()
            funkcija2 = sympy.Poly([int(a), int(b2), int(c2)], x).as_expr()
        presek = sympy.solve((funkcija1 - funkcija2), x)
        preveri(len(presek) == 1)
        k1 = funkcija1.diff().subs(x, *presek)
        k2 = funkcija2.diff().subs(x, *presek)
        kot = sympy.N(sympy.deg(kotMedPremicama(k1, k2)))
        stop = kot // 1
        min = round(kot % 1 * 60)
        return {'funkcija1': funkcija1, 'funkcija2': funkcija2, 'stopinje': stop, 'minute': min}
