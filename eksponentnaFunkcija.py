from generiranje import Naloga, preveri
import sympy
import random
import jinja2


def narediEksponentno(do=3, celaOsnova=False, premik=0):
    x = sympy.symbols('x')
    izbor = list(range(2, do + 1))
    if not celaOsnova:
        izbor += [sympy.Rational(x, 2) for x in range(1, 2 * (do)) if x != 2] + [sympy.Rational(x, 3) for x in
                                                                                 range(1, 3 * (do)) if x != 3] + [
                     sympy.Rational(x, 4) for x in range(1, 4 * (do)) if x != 4] + [sympy.Rational(x, 5) for x in
                                                                                    range(1, 5 * (do)) if x != 5]
    osnova = random.choice(izbor)
    return [osnova, premik, sympy.Add(sympy.Pow(osnova, x), premik, evaluate=False)]


class GrafEksponentne(Naloga):
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
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisiEksponentna1}} };
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisiEksponentna2}} };
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
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisiEksponentna1}} };
    \addplot[domain =-5.5:5.5, color=black, smooth]{ {{naloga.narisiEksponentna2}} };
    \addplot[domain =-5.5:5.5, color=black, dashed]{ {{naloga.premik2}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        if self.lazja:
            [osnova, premik, eksponentna1] = narediEksponentno(celaOsnova=True)
        else:
            [osnova, premik, eksponentna1] = narediEksponentno(celaOsnova=False)
        predznak = random.choice([1, -1])
        premik2 = random.choice([x for x in range(-3, 4) if x != 0])
        eksponentna2 = sympy.Add(predznak * sympy.Pow(osnova, x, evaluate=False), premik2, evaluate=False)
        narisiEksponentna1 = str(eksponentna1).replace('**', '^')
        narisiEksponentna2 = str(eksponentna2).replace('**', '^')
        return {'eksponentna1': eksponentna1, 'eksponentna2': eksponentna2, 'narisiEksponentna1': narisiEksponentna1,
                'narisiEksponentna2': narisiEksponentna2, 'premik2': premik2}


class Enacba(Naloga):
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')

        if self.lazja:
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        [osnova1, osnova2] = random.sample([2, 3, 5, 7, 10], 2)
        x = sympy.symbols('x')
        a = random.randint(-5, 5)
        if self.lazja:
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
        preveri(max([abs(d), abs(h)]) < 201)  # Zagotovi, da v enačbi ne nastopajo prevelike vrednosti.
        return {'enacba': enacba, 'resitev': resitev}
