from generiranje import *


# ~~~~~Pomožne funkcije
def seznamPolovick(od=-10, do=10):
    return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def seznamTretinj(od=-10, do=10):
    return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def eksplicitnaPremica():
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


# ~~~~~Posamezne naloge iz poglavja Linearna funkcija


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
        # odsekovna = sympy.latex(x/sympy.Rational(c,-a)+y/sympy.Rational(c,-b)) #TODO avtomatičen izpis dvojnih ulomkov s simboli
        odsekovna = '\\frac{x}{' + sympy.latex(sympy.Rational(c, -a)) + '}+\\frac{y}{' + sympy.latex(
            sympy.Rational(c, -b)) + '}=1'
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
            premica1 = sympy.latex(sympy.Eq(y, k1 * x + n1))
        if x3 == x2:
            premica2 = sympy.Eq(x, x3)
        else:
            k2 = sympy.Rational((y3 - y2), (x3 - x2))
            n2 = y3 - k2 * x3
            premica2 = sympy.latex(sympy.Eq(y, k2 * x + n2))

        ploscinaTrikotnika = sympy.simplify(abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2).evalf(3)
        # TODO ne prikazuj nepotrebnih ničel v decimalnem zapisu

        return {'premica1': premica1, 'premica2': premica2, 'ploscina': ploscinaTrikotnika}


class NarisiLinearnoFukcijo(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''Nariši graf funkcije linearne ${{latex(naloga.linearnaF)}}$.''')
        self.besedilo_vecih = jinja2.Template(r''' Nariši graf linearne funkcije:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.linearnaF)}}$
        {% endfor %}
        \end{enumerate}
        ''')

        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.linearnaF)}}$\par
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
         \item ${{latex(naloga.linearnaF)}}$\par
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
        return {'linearnaF': sympy.Eq(f, eksplicitna), 'linearna': eksplicitna, 'n': n, 'nicla': nicla}


class VrednostiLinearne(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

        self.besedilo_posamezne = jinja2.Template(r'''Dana je funkcija s predpisom ${{naloga.linearna}}$. Izračunajte vrednost $f({{naloga.x1}})$ in za kateri $x$ je $f(x)={{naloga.y2}}$. Za katere vrednosti $x$ so vrednosti funkcije negativne? ''')

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
        negativno = sympy.latex(
            sympy.solve_poly_inequality(sympy.Poly(funkcija, x), '<')[0])  # Solve vrne seznam intervalov
        return {'linearna': sympy.latex(sympy.Eq(f, funkcija)), 'x1': sympy.latex(x1), 'x2': sympy.latex(x2),
                'y1': sympy.latex(y1), 'y2': sympy.latex(y2), 'negativno': negativno}

# print(VrednostiLinearne().poskusi_sestaviti())
