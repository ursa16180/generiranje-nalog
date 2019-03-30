from generiranje import Naloga, preveri
import random
import sympy
import jinja2


# ~~~~~Pomožne funkcije
def seznamPolovick(od=-10, do=10):
    return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def seznamTretinj(od=-10, do=10):
    return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def eksplicitnaPremica():
    # Funkcija vrne naključno eksplicitno podano premico
    k = random.choice(seznamPolovick(-3, 3) + seznamTretinj(-3, 3))
    n = random.choice(seznamPolovick(-4, 4) + seznamTretinj(-4, 4))
    x = sympy.symbols('x')
    eksplicitna = k * x + n
    return [k, n, eksplicitna]


def implicinaPremica():
    # Vrne implicitno podano obliko premice, ki jo moramo izenačiti z 0
    # Premice niso vzporedne z osema
    seznamStevil = [x for x in range(-10, 10) if x != 0]
    a = random.choice(seznamStevil)
    b = random.choice(seznamStevil)
    c = random.choice(seznamStevil)
    x = sympy.symbols('x')
    y = sympy.symbols('y')
    implicitna = sympy.simplify(a * x + b * y + c)
    return [a, b, c, implicitna]


def skoziTocki(x1, y1, x2, y2):
    x = sympy.symbols('x')
    k = (y2 - y1) / (x2 - x1)
    n = y1 - k * x1
    return [k, n, k * x + n]


def izberiKoordinato(od=-10, do=10):
    koordinata = random.randint(od, do)
    return koordinata


# ~~~~~Posamezne naloge iz poglavja Linearna funkcija
#TODO ideja: reši linearno (ne)enačbo (težja s kvadrati ki se odštejejo)

class PremicaSkoziTocki(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Zapiši enačbo premice skozi točki $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$ in $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$.''')
        self.besedilo_vecih = jinja2.Template(r'''Zapiši enačbo premice skozi točki:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $A({{latex(naloga.x1)}},{{latex(naloga.y1)}})$, $B({{latex(naloga.x2)}},{{latex(naloga.y2)}})$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$y={{naloga.premica}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $y={{naloga.premica}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        x1 = random.choice(seznamPolovick(-5, 5) + seznamTretinj(-5, 5))
        y1 = random.choice(seznamPolovick(-5, 5) + seznamTretinj(-5, 5))
        x2 = random.randint(-10, 10)
        y2 = random.randint(-10, 10)
        preveri(x1 != x2 and y1 != y2)  # Preveri, da sta 2 vzporedni točki in nista vzporedni osem
        premica = sympy.latex(skoziTocki(x1, y1, x2, y2)[-1])
        return {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'premica': premica}


class RazdaljaMedTockama(Naloga):  # Todo težja racionalne koordinate? #TODO preveri jinja latex
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Natančno izračunaj razdaljo med točkama $A({{naloga.x1}},{{naloga.y1}})$ in $B({{naloga.x2}},{{naloga.y2}})$.''')
        self.besedilo_vecih = jinja2.Template(r'''Natančno izračunaj razdaljo med točkama
                                              \begin{enumerate}
                                              {% for naloga in naloge %}
                                              \item $A({{naloga.x1}},{{naloga.y1}})$ in $B({{naloga.x2}},{{naloga.y2}})$
                                              {% endfor %}
                                              \end{enumerate}'''
                                              )
        self.resitev_posamezne = jinja2.Template(r'''$d(A,B)={{naloga.razdalja}}$''')
        self.resitev_vecih = jinja2.Template(r'''\begin{enumerate}
                                             {% for naloga in naloge %}
                                             \item $d(A,B)={{naloga.razdalja}}$
                                             {% endfor %}
                                             \end{enumerate}''')

    def poskusi_sestaviti(self):
        x1 = izberiKoordinato()
        y1 = izberiKoordinato()
        x2 = izberiKoordinato()
        y2 = izberiKoordinato()
        preveri(x1 != x2 and y1 != y2)
        razdalja = sympy.latex(sympy.simplify(sympy.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))))
        return {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'razdalja': razdalja}


class OblikeEnacbPremice(Naloga):  # TODO preveri jinja latex
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Zapiši implicitno in odsekovno obliko premice podane z enačbo ${{naloga.implicitna}}$''')
        self.besedilo_vecih = jinja2.Template(r''' Zapiši implicitno in odsekovno obliko premice podane z enačbo:
                                            \begin{enumerate}
                                              {% for naloga in naloge %}
                                              \item ${{naloga.implicitna}}$
                                              {% endfor %}
                                              \end{enumerate}''')
        self.resitev_posamezne = jinja2.Template(r'''${{naloga.eksplicitna}}$ in ${{naloga.odsekovna}}$''')
        self.resitev_vecih = jinja2.Template(r'''
                                            \begin{enumerate}
                                              {% for naloga in naloge %}
                                              \item ${{naloga.eksplicitna}}$ in ${{naloga.odsekovna}}$
                                              {% endfor %}
                                              \end{enumerate}
                                              ''')

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        [a, b, c, implicitnaOblika] = implicinaPremica()
        implicitna = sympy.latex(sympy.Eq(implicitnaOblika, 0))
        eksplicitna = sympy.latex(sympy.Eq(y,
                                           sympy.Rational(-a, b) * x + sympy.Rational(-c, b)))
        odsekovna = sympy.latex(
            sympy.Eq(sympy.Add(sympy.Mul(x, sympy.Pow(sympy.Rational(c, -a), -1, evaluate=False), evaluate=False),
                               sympy.Mul(y, sympy.Pow(sympy.Rational(c, -b), -1, evaluate=False), evaluate=False),
                               evaluate=False), 1))

        return {'implicitna': implicitna, 'eksplicitna': eksplicitna, 'odsekovna': odsekovna}


class PremiceTrikotnik(Naloga):  # TODO preveri jinja latex
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r''' Izračunaj ploščino trikotnika, ki ga premici ${{naloga.premica1}}$ in ${{naloga.premica2}}$ oklepata z abscisno osjo. ''')
        self.besedilo_vecih = jinja2.Template(r''' Izračunaj ploščino trikotnika, ki ga premici oklepata z abscisno osjo:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{naloga.premica1}}$ in ${{naloga.premica2}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$S={{naloga.ploscina}}$ ''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $S={{naloga.ploscina}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        x1 = izberiKoordinato(1, 5)
        y1 = 0
        x2 = random.choice([x for x in range(-5, 6) if x != 0])
        y2 = random.choice([x for x in range(-5, 6) if x != 0])
        x3 = izberiKoordinato(-5, 0)
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

        ploscinaTrikotnika = sympy.latex(
            sympy.simplify(abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2).evalf(3)).rstrip('0').rstrip('.')

        return {'premica1': sympy.latex(premica1), 'premica2': sympy.latex(premica2), 'ploscina': ploscinaTrikotnika}


class NarisiLinearnoFukcijo(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Nariši graf funkcije linearne $f(x) = {{latex(naloga.linearna)}}$.''')
        self.besedilo_vecih = jinja2.Template(r''' Nariši graf linearne funkcije:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $f(x) = {{latex(naloga.linearna)}}$
        {% endfor %}
        \end{enumerate}
        ''')

        self.resitev_posamezne = jinja2.Template(r'''$f(x)={{latex(naloga.linearna)}}$\par
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
        \end{minipage}''')

        self.resitev_vecih = jinja2.Template(r'''
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
         ''')

    def poskusi_sestaviti(self):
        [k, n, eksplicitna] = eksplicitnaPremica()
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        f = sympy.symbols('f(x)')
        nicla = (-n) / k
        return {'linearna': eksplicitna, 'n': n, 'nicla': nicla}


class VrednostiLinearne(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        self.besedilo_posamezne = jinja2.Template(
            r'''Dana je funkcija s predpisom ${{naloga.linearna}}$. Izračunajte vrednost $f({{naloga.x1}})$ in za kateri $x$ je $f(x)={{naloga.y2}}$. Za katere vrednosti $x$ so vrednosti funkcije negativne? ''')

        self.besedilo_vecih = jinja2.Template(r''' Za podano funkcijo $f$ izračunaj $f(x_0)$ in za kateri $x$ je $f(x)=y_1$. Za katere vrednosti $x$ so vrednosti funkcije negativne?
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{naloga.linearna}}$, $x_0={{naloga.x1}}$, $y_1={{naloga.y2}}$
        {% endfor %}
        \end{enumerate}
        ''')

        self.resitev_posamezne = jinja2.Template(r'''
        $f({{naloga.x1}})={{naloga.y1}}$, $x={{naloga.x2}}$, $x \in {{naloga.negativno}}$''')

        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $f({{naloga.x1}})={{naloga.y1}}$, $x={{naloga.x2}}$, $x \in {{naloga.negativno}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        f = sympy.symbols('f(x)')

        [k, n, funkcija] = eksplicitnaPremica()

        x1 = random.choice(seznamPolovick(-3, 3) + seznamTretinj(-3, 3))
        x2 = random.choice(seznamPolovick(-3, 3) + seznamTretinj(-3, 3))
        preveri(x1 != x2)
        y1 = k * x1 + n
        y2 = k * x2 + n

        negativno = sympy.latex(sympy.solveset(funkcija < 0, domain=sympy.S.Reals))
        return {'linearna': sympy.latex(sympy.Eq(f, funkcija)), 'x1': sympy.latex(x1), 'x2': sympy.latex(x2),
                'y1': sympy.latex(y1), 'y2': sympy.latex(y2), 'negativno': negativno}


class Neenacba(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        # if min_potenca > max_potenca:
        #     raise MinMaxNapaka
        self.besedilo_posamezne = jinja2.Template(r'''Reši neenačbo ${{latex(naloga.neenacba)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Reši neenačbo:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.neenacba)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$x \in {{latex(naloga.resitev)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $x \in {{latex(naloga.resitev)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        izbor = [x for x in range(-5, 5) if x != 0]
        if self.lazja:
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
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Reši sistem enačb ${{latex(naloga.enacba1)}}$ in ${{latex(naloga.enacba2)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Reši sistem enačb:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.enacba1)}}$, ${{latex(naloga.enacba2)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        izborCela = [x for x in range(-5, 6) if x != 0]
        izborUlomki = [sympy.Rational(x, 2) for x in [-3, -1, 1, 3]] + [sympy.Rational(x, 3) for x in
                                                                        [-2, -1, 1, 2]] + [sympy.Rational(x, 4) for x in
                                                                                           [-3, -1, 1, 3]]
        if self.lazja:
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
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Reši sistem enačb ${{latex(naloga.enacba1)}}$, ${{latex(naloga.enacba2)}}$ in ${{latex(naloga.enacba3)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Reši sistem enačb:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.enacba1)}}$, ${{latex(naloga.enacba2)}}$, ${{latex(naloga.enacba3)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(
            r'''$x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$, $z={{latex(naloga.z)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $x={{latex(naloga.x)}}$, $y={{latex(naloga.y)}}$, $z={{latex(naloga.z)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        z = sympy.symbols('z')
        if self.lazja:
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

        preveri((a, b, c) != (e, f, g) and (a, b, c) != (i, j, k) and (i, j, k) != (e, f, g) and (
                x1 != 0 or y1 != 0 or z1 != 0))
        d = a * x1 + b * y1 + c * z1
        h = e * x1 + f * y1 + g * z1
        l = i * x1 + j * y1 + k * z1
        enacba1 = a * x + b * y + c * z
        enacba2 = e * x + f * y + g * z
        enacba3 = i * x + j * y + k * z
        return {'enacba1': sympy.Eq(enacba1, d), 'enacba2': sympy.Eq(enacba2, h), 'enacba3': sympy.Eq(enacba3, l),
                'x': x1, 'y': y1, 'z': z1}
