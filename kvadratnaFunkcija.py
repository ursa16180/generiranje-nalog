from generiranje import *


def nicelnaOblika(od=-5, do=5):
    odDejanski = min(od, do)
    doDejanski = max(od, do)
    a = random.choice(seznamPolovick(-2, 2) + seznamTretinj(-2, 2))
    x1 = random.choice(seznamPolovick(odDejanski, doDejanski) + seznamTretinj(odDejanski, doDejanski))
    x2 = random.choice(seznamPolovick(odDejanski, doDejanski) + seznamTretinj(odDejanski, doDejanski))
    x = sympy.symbols('x')
    nicelna = a * (x - x1) * (x - x2)  # TODO nej se ničle ne poenostavljajo in a zmnoži not (factor ne pomaga)
    return [a, x1, x2, nicelna]


def splosnaOblika():
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


# ~~~~~~~~~~~~~VZOREC za nalogo
class VzorecNaloge(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r''' ''')
        self.besedilo_vecih = jinja2.Template(r'''
        \begin{enumerate}
        {% for naloga in naloge %}
        \item
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r''' ''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        return {'naloga': 1, 'resitev': 2}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

class IzracunajNicle(Naloga):
    # Lažja različica ima realne ničle, težja pa kompleksne
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Izračunaj ničle kvadratne funkcije $f(x)={{latex(naloga.splosna)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj ničle naslednjih kvadratnih funkcij:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $f(x)={{latex(naloga.splosna)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$x_1={{latex(naloga.x1)}}$, $x_2={{latex(naloga.x2)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $x_1={{latex(naloga.x1)}}$, $x_2={{latex(naloga.x2)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        [a, b, c, splosna] = splosnaOblika()
        if self.lazja:
            preveri(diskriminanta(a, b, c) > 0)
        else:
            preveri(diskriminanta(a, b, c) <= 0)
        [x1, x2] = nicle(a, b, c)
        return {'splosna': splosna, 'x1': x1, 'x2': x2}


class NarisiGraf(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''Nariši graf funkcije $f(x)={{latex(naloga.funkcija)}}$''')
        self.besedilo_vecih = jinja2.Template(r'''Nariši grafe funkcij:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item  $f(x)={{latex(naloga.funkcija)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$f(x)={{latex(naloga.funkcija)}}$\par
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
         ''')
        self.resitev_vecih = jinja2.Template(r'''
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
         ''')

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        [a, x1, x2, nicelna] = nicelnaOblika(-3, 3)
        funkcija = sympy.expand(nicelna)
        [p, q] = izracunajTeme(a, -a * (x1 + x2), a * x1 * x2)
        preveri(abs(q)<=5)
        zacetna = funkcija.subs(x, 0)
        return {'funkcija': funkcija, 'narisiFunkcijo':nicelna, 'p': p, 'q': q, 'x1': x1, 'x2': x2, 'zacetna': zacetna}


