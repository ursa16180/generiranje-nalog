from generiranje import Naloga, preveri
import sympy
import random
import linearnaFunkcija
import jinja2


def kotMedPremicama(k1, k2):
    # Funkcija v radianih izračuna kot med premicama
    if k1 * k2 == -1:
        kot = sympy.pi / 2
    else:
        kot = sympy.atan(abs((k2 - k1) / (1 + k1 * k2)))
    return kot


def vseFunkcije(polinom=True, racionalna=True, potencna=True, logaritem=True, kotna=True, krozna=True):
    x = sympy.symbols('x')
    funkcije = []
    if polinom:
        stopnja = random.randint(2, 4)
        polinom = sympy.Poly([random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnja)],
                             x).as_expr()  # Pazi za stacionarne naj bo največ 3.stopnje!
        funkcije.append(polinom)
    if racionalna:
        stopnjaStevca = random.randint(2, 4)
        stopnjaImenovalca = random.randint(1, 2)
        stevec = sympy.Poly([random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnjaStevca)],
                            x).as_expr()
        imenovalec = sympy.Poly(
            [random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnjaImenovalca)],
            x).as_expr()
        racionalna = sympy.simplify(stevec / imenovalec)
        funkcije.append(racionalna)
    if potencna:
        baza = random.choice([2, 3, 5])
        eksponentnaB = baza ** x
        eksponentnaE = sympy.exp(x)
        funkcije += [eksponentnaB, eksponentnaE]

    if logaritem:
        # baza = random.choice([2, 3, 4, 5, 10])
        # logaritem = sympy.log(x, baza) #todo izpis log_baza v latexu
        # funkcije.append(logaritem)
        naravniLogaritem = sympy.ln(x)  # Todo latex izpis ln namesto log
        funkcije.append(naravniLogaritem)
    if kotna:
        kosinus = sympy.cos(x)
        sinus = sympy.sin(x)
        tangens = sympy.tan(x)
        kotangens = sympy.cot(x)
        funkcije += [kosinus, sinus, tangens, kotangens]
    if krozna:
        arcusKosinus = sympy.acos(x)
        arcusSinus = sympy.asin(x)
        arcusTangens = sympy.atan(x)
        arcusKotangens = sympy.acot(x)
        funkcije += [arcusKosinus, arcusSinus, arcusTangens, arcusKotangens]
    return funkcije


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

    def __init__(self, polinom=True, racionalna=True, potencna=True, logaritem=True, kotna=True, krozna=False,
                 lazja=True,
                 **kwargs):
        super().__init__(**kwargs)

        if polinom == racionalna == potencna == logaritem == kotna == krozna == False:
            raise ValueError(
                'Izbrana mora biti vsaj ena izmed funkcij: polinom, acionalna fukcija, kotna funkcija, krožna funkcija,'
                ' potencna funkcija ali logaritemska funkcija. ')
        self.polinom = polinom
        self.racionalna = racionalna
        self.potencna = potencna
        self.logaritem = logaritem
        self.kotna = kotna
        self.krozna = krozna
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        funkcije = vseFunkcije(polinom=self.polinom, racionalna=self.racionalna, potencna=self.potencna,
                               logaritem=self.logaritem, kotna=self.kotna, krozna=self.krozna)

        if self.lazja:
            funkcija1 = random.choice(funkcije)
            # funkcija2 = x  # todo Če izbere poli ali racionalno, nej bo funkcija2 kar x
            funkcija2 = sympy.Poly([random.choice([-2, -1, 1, 2, 3]), random.randint(-3, 3)], x).as_expr()
        else:
            funkcija1 = random.choice(funkcije)
            funkcija2 = random.choice(funkcije)
        funkcija = funkcija1.subs(x, funkcija2)
        odvod = funkcija.diff(x)
        return {'funkcija': funkcija, 'odvod': odvod}


class Funkcija(enum):
    RACIONALNA = 1
    POLINOM = 2


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

    def __init__(self, funkcije=Funkcija.all, **kwargs):
        super().__init__(**kwargs)

        if polinom == racionalna == potencna == logaritem == kotna == krozna == False:
            raise ValueError(
                'Izbrana mora biti vsaj ena izmed funkcij: polinom, acionalna fukcija, kotna funkcija, krožna funkcija,'
                ' potencna funkcija ali logaritemska funkcija. ')
        self.polinom = polinom
        self.racionalna = racionalna
        self.potencna = potencna
        self.logaritem = logaritem
        self.kotna = kotna
        self.krozna = krozna

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        funkcije = vseFunkcije(polinom=False, racionalna=self.racionalna, potencna=self.potencna,
                               logaritem=self.logaritem, kotna=self.kotna, krozna=self.krozna)
        if self.polinom:  # Ker originalno je prevelik polinom
            stopnja = random.randint(1, 2)
            polinom = sympy.Poly([random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnja)],
                                 x).as_expr()
            funkcije.append(polinom)
        funkcija1 = random.choice(funkcije).subs(x, random.choice([-2, -1, 2]) * x)
        funkcija2 = random.choice(funkcije)
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

    def __init__(self, polinom=True, racionalna=True, potencna=True, logaritem=True, kotna=True, krozna=False,
                 **kwargs):
        super().__init__(**kwargs)

    if polinom == racionalna == potencna == logaritem == kotna == krozna == False:
        raise ValueError(
            'Izbrana mora biti vsaj ena izmed funkcij: polinom, acionalna fukcija, kotna funkcija, krožna funkcija,'
            ' potencna funkcija ali logaritemska funkcija. ')
    self.polinom = polinom
    self.racionalna = racionalna
    self.potencna = potencna
    self.logaritem = logaritem
    self.kotna = kotna
    self.krozna = krozna


def poskusi_sestaviti(self):
    x = sympy.symbols('x')
    funkcije = ['polinom', 'racionalna', 'potencna', 'logaritem', 'kotna', 'krozna']
    izbrane = [self.polinom, self.racionalna, self.potencna, self.logaritem, self.kotna, self.krozna]
    izbor = []
    for i in range(len(funkcije)):  # TODO elengantnejše da boole preslikaš v seznam
        if izbrane[0]:
            izbor.append(funkcije[i])
    izbrana = random.choice(izbor)

    if izbor == 'polinom':
        stopnja = random.randint(2, 3)
        polinom = sympy.Poly([random.choice([-2, -1, 1, 2])] + [random.randint(-3, 3) for i in range(stopnja)],
                             x).as_expr()
        funkcija = polinom
        x0 = random.randint(-2, 2)
    if izbor == 'racionalna':
        stopnjaStevca = random.randint(2, 3)
        stopnjaImenovalca = 3 - stopnjaStevca
        stevec = sympy.Poly([random.choice([-1, 1])] + [random.randint(-3, 3) for i in range(stopnjaStevca)],
                            x).as_expr()
        imenovalec = sympy.Poly(
            [random.choice([-1, 1])] + [random.randint(-3, 3) for i in range(stopnjaImenovalca)],
            x).as_expr()
        racionalna = sympy.simplify(stevec / imenovalec)
        funkcija = racionalna
        x0 = random.randint(-2, 2)
    if izbor == 'potencna':
        baza = random.choice([sympy.E, 2, 3, 5])
        eksponentna = baza ** x
        funkcija = eksponentna
        x0 = random.choice([sympy.log(n, baza) for n in [1, 2, 3]])  # Todo lepši izpis logaritmov
    if izbor == 'logaritem':
        # baza = random.choice([2, 3, 4, 5, 10])
        # logaritem = sympy.log(x, baza) #todo izpis log_baza v latexu
        # funkcije.append(logaritem)
        naravniLogaritem = sympy.ln(x)  # Todo latex izpis ln namesto log
        funkcija = naravniLogaritem
        x0 = sympy.E ** (random.randint(-1, 2))
    if izbor == 'kotna':
        kosinus = sympy.cos(x)
        sinus = sympy.sin(x)
        tangens = sympy.tan(x)
        kotangens = sympy.cot(x)
        funkcija = random.choice([kosinus, sinus, tangens, kotangens])
        x0 = random.choice(
            [sympy.pi / x for x in [6, 3, 4, 2]])  # TODO dodaj 0 in pi, vendar pazi da ni izbran tna/cot
    if izbor == 'krozna':
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
