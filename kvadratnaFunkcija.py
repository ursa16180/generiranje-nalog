from generiranje import Naloga, preveri
import random
import sympy
import jinja2
import linearnaFunkcija


def seznamPolovick(od=-10, do=10):
    return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def seznamTretinj(od=-10, do=10):
    return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def nicelnaOblika(od=-5, do=5, risanje=False):
    odDejanski = min(od, do)
    doDejanski = max(od, do)
    if risanje:
        a = random.choice([-2, -1, sympy.Rational(-1, 2), sympy.Rational(1, 2), 1, 2])
    else:
        a = random.choice(seznamPolovick(-4, 4) + seznamTretinj(-4, 4))
    x1 = random.choice(seznamPolovick(odDejanski, doDejanski) + seznamTretinj(odDejanski, doDejanski))
    x2 = random.choice(seznamPolovick(odDejanski, doDejanski) + seznamTretinj(odDejanski, doDejanski))
    x = sympy.symbols('x')
    # nicelna = a * (x - x1) * (x - x2)
    nicelna = sympy.Mul(a, x - x1, x - x2, evaluate=False)
    return [a, x1, x2, nicelna]


def splosnaOblika(risanje=False):
    if risanje:
        a = random.choice([-2, -1, sympy.Rational(-1, 2), sympy.Rational(1, 2), 1, 2])
    else:
        a = random.choice(seznamPolovick(-4, 4) + seznamTretinj(-4, 4))

    b = random.choice(seznamPolovick(-4, 4) + seznamTretinj(-4, 4))
    c = random.choice(seznamPolovick(-4, 4) + seznamTretinj(-4, 4))
    x = sympy.symbols('x')
    splosna = a * x ** 2 + b * x + c
    return [a, b, c, splosna]


def nicle(a, b, c):
    D = diskriminanta(a, b, c)
    if D >= 0:
        d = sympy.sqrt(D)
    else:
        d = sympy.sqrt(-D) * sympy.I
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return (x1, x2)


def izracunajTeme(a, b, c):
    p = -b / (2 * a)
    q = -(diskriminanta(a, b, c)) / (4 * a)
    return [p, q]


def diskriminanta(a, b, c):
    return b ** 2 - 4 * a * c


# ~~~~~Naloge in sklopa: Kvadratna funkcija

class IzracunajNicle(Naloga):
    # Lažja različica ima realne ničle, težja pa kompleksne
    besedilo_posamezne = r'''Izračunaj ničle kvadratne funkcije $f(x)={{latex(naloga.splosna)}}$.'''
    besedilo_vecih = r'''Izračunaj ničle naslednjih kvadratnih funkcij:
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        [a, b, c, splosna] = splosnaOblika()
        if self.lazja:
            preveri(diskriminanta(a, b, c) > 0 and abs(diskriminanta(a, b, c)) <= 200)
        else:
            preveri(diskriminanta(a, b, c) <= 0 and abs(diskriminanta(a, b, c)) <= 200)
        [x1, x2] = nicle(a, b, c)
        return {'splosna': splosna, 'x1': x1, 'x2': x2}


class NarisiGraf(Naloga):
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

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        [a, x1, x2, nicelna] = nicelnaOblika(-3, 3, risanje=True)
        funkcija = sympy.expand(nicelna)
        [p, q] = izracunajTeme(a, -a * (x1 + x2), a * x1 * x2)
        preveri(abs(q) <= 5)
        zacetna = funkcija.subs(x, 0)
        return {'funkcija': funkcija, 'narisiFunkcijo': nicelna, 'p': p, 'q': q, 'x1': x1, 'x2': x2, 'zacetna': zacetna}


class TemenskaOblika(Naloga):
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

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        [a, b, c, splosna] = splosnaOblika()
        D = diskriminanta(a, b, c)
        preveri(D >= 0 and abs(diskriminanta(a, b, c)) <= 200)
        [p, q] = izracunajTeme(a, b, c)
        return {'splosna': splosna, 'p': p, 'q': q, 'a': a}


class Presecisce(Naloga):  # TODO zagotovi lepše rezultate
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        b = sympy.symbols('b')
        c = sympy.symbols('c')
        a = random.choice([-2, -1, sympy.Rational(-1, 2), sympy.Rational(1, 2), 1, 2])
        x1 = random.choice(seznamPolovick(-5, 5) + seznamTretinj(-5, 5))
        x2 = random.choice(seznamPolovick(-5, 5) + seznamTretinj(-5, 5))
        y1 = random.choice(seznamPolovick(-5, 5) + seznamTretinj(-5, 5))
        y2 = random.choice(seznamPolovick(-5, 5) + seznamTretinj(-5, 5))
        premica = linearnaFunkcija.skoziTocki(x1, y1, x2, y2)[-1]
        koeficienta = sympy.solve((a * x1 ** 2 + b * x1 + c - y1, a * x2 ** 2 + b * x2 + c - y2), b, c)
        print(koeficienta)
        preveri(koeficienta !=[]) #Če ni rešitve vrne prazen seznam in ne praznega slovarja
        preveri(abs(koeficienta[b]) < 5 and abs(koeficienta[c]) < 5) #Todo lepša rešitve (grozni ulomki)
        kvadratna = a * x ** 2 + koeficienta[b] * x + koeficienta[c]
        return {'parabola': kvadratna, 'premica': premica, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}


class Neenacba(Naloga):
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):  # TODO ali želimo lepše rešitve
        x = sympy.symbols('x')
        splosna1 = splosnaOblika(risanje=True)[-1]
        if self.lazja:
            primerjava = random.choice(seznamPolovick(-10, 10) + seznamTretinj(-10, 10))
        else:
            primerjava = splosnaOblika()[-1]
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
    besedilo_posamezne = r'''Graf kvadratne funkcije $f$ poteka skozi točke $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$, 
        $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$ in $C({{latex(naloga.x3)}},{{latex(naloga.y3)}})$. Določi 
        predpis funkcije $f.$'''
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        [a, nicla1, nicla2, funkcija] = nicelnaOblika(risanje=True)
        if self.lazja:
            x1 = nicla1
            x2 = 0
        else:
            x1 = random.randint(-5, 5)
            x2 = random.randint(-5, 5)

        x3 = random.randint(-5, 5)
        y1 = funkcija.subs(x, x1)
        y2 = funkcija.subs(x, x2)
        y3 = funkcija.subs(x, x3)

        preveri(len({x1, x2, x3}) == 3)
        return {'x1': x1, 'x2': x2, 'x3': x3, 'y1': y1, 'y2': y2, 'y3': y3, 'funkcija': sympy.expand(funkcija)}
