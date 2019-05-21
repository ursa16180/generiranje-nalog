from generiranje import Naloga, preveri
from linearnaFunkcija import razdalja_med_tockama
import sympy
import random


# ~~~~~Naloge iz sklopa Stožnice
# ~~~~~~Krožnica
class PreseciscaKroznic(Naloga):
    """
    Naloga za iskanje presečišč dveh krožnic.


    >>> PreseciscaKroznic().sestavi()
    {'kroznica1': Eq((x + 5)**2 + (y + 4)**2, 4), 'kroznica2': Eq(x**2 + (y - 4)**2, 61), 'presek': [(-5, -2), (-285/89, -278/89)]}

    >>> PreseciscaKroznic().sestavi()
    {'kroznica1': Eq(x**2 + y**2, 41), 'kroznica2': Eq(y**2 + (x - 2)**2, 25), 'presek': [(5, -4), (5, 4)]}
    """
    besedilo_posamezne = r'''Določi medsebojno lego krožnic $\mathcal{K}_1:{{latex(naloga.kroznica1)}}$ in $\mathcal{K}_2:{{latex(naloga.kroznica2)}}$ ter določi presešišča, če obstajajo.'''
    besedilo_vecih = r'''Določi medsebojno lego krožnic $\mathcal{K}_1$ in $\mathcal{K}_2$ ter določi presešišča, če obstajajo:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $\mathcal{K}_1:{{latex(naloga.kroznica1)}}$, $\mathcal{K}_2:{{latex(naloga.kroznica2)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''Sekata se v {% for tocka in naloga.presek %}$T_{ {{loop.index}} }={{latex(tocka)}}$ {% endfor %}.'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item Sekata se v {% for tocka in naloga.presek %}$T_{ {{loop.index}} }={{latex(tocka)}}$ {% endfor %}.
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        p1 = random.randint(-5, 5)
        q1 = random.randint(-5, 5)
        p2 = random.randint(-5, 5)
        q2 = random.randint(-5, 5)
        x0 = random.randint(-5, 5)
        y0 = random.randint(-5, 5)
        preveri((p1, q1) != (p2, q2))
        r1 = razdalja_med_tockama(x0, y0, p1, q1)
        r2 = razdalja_med_tockama(x0, y0, p2, q2)
        kroznica1 = sympy.Circle(sympy.Point(p1, q1), r1)
        kroznica2 = sympy.Circle(sympy.Point(p2, q2), r2)
        presek = kroznica1.intersection(kroznica2)
        tocke = [(A.x, A.y) for A in presek]
        preveri((x0, y0) in tocke)  # Todo lepša 2. rešitev
        izpis_kroznica1 = sympy.Eq(kroznica1.equation() + r1 ** 2, r1 ** 2)
        izpis_kroznica2 = sympy.Eq(kroznica2.equation() + r2 ** 2, r2 ** 2)
        return {'kroznica1': izpis_kroznica1, 'kroznica2': izpis_kroznica2, 'presek': tocke}


# ~~~~~ Elipsa
class TemeGorisceEnacba(Naloga):
    """
    Naloga za zapis predpisa elipse, če poznamo središče, teme in gorišče.

    :param premaknjena: elipsa v premaknjeni ali središčni legi


    >>> TemeGorisceEnacba().sestavi()
    {'teme': (-1, 5), 'gorisce': (-1, -sqrt(21)), 'sredisce': (-1, 0), 'elipsa': Eq(y**2/25 + (x/2 + 1/2)**2, 1)}

    >>> TemeGorisceEnacba(premaknjena=True).sestavi()
    {'teme': (-5, -4), 'gorisce': (-4, -4 + 2*sqrt(6)), 'sredisce': (-4, -4), 'elipsa': Eq((x + 4)**2 + (y/5 + 4/5)**2, 1)}
    """
    besedilo_posamezne = r'''Zapiši enačbo elipse s središčem $S{{latex(naloga.sredisce)}}$, temenom $T_1{{latex(naloga.teme)}}$ in goriščem $F_1{{latex(naloga.gorisce)}}$.'''
    besedilo_vecih = r'''Zapiši enačbo elipse s središčem $S$, temenom $T_1$ in goriščem $F_1$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $S({{latex(naloga.sredisce)}})$, $T_1{{latex(naloga.teme)}}$, $F_1{{latex(naloga.gorisce)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''${{latex(naloga.elipsa)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{latex(naloga.elipsa)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, premaknjena=False, **kwargs):
        super().__init__(**kwargs)
        self.premaknjena = premaknjena

    def _poskusi_sestaviti(self):
        if self.premaknjena:
            S = sympy.Point(random.randint(-5, 5), random.randint(-5, 5))
        else:
            S = sympy.Point(0, 0)
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        preveri(a != b)
        teme = random.choice([S.translate(x=a), S.translate(x=-a), S.translate(y=b), S.translate(y=-b)])
        elipsa = sympy.Ellipse(S, a, b)
        gorisce = random.choice(elipsa.foci)
        return {'teme': (teme.x, teme.y), 'gorisce': (gorisce.x, gorisce.y), 'sredisce': (S.x, S.y),
                'elipsa': sympy.Eq(elipsa.equation() + 1, 1)}  # Todo lepši izpis #todo ali smiselne vgrajene krivulje


class NarisiKrivuljo(Naloga):  # todo dokumentacija
    """
    Naloga za dopolnjevanja do popolnih kvadratov ter risanje krožnice ali elipse. TODO ENUM
    """
    besedilo_posamezne = r'''Nariši krivuljo ${{latex(naloga.razsirjena)}}$.'''
    besedilo_vecih = r'''Nariši krivuljo:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.razsirjena)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''
    ${{latex(naloga.krivulja)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
    xtick={-6,-5,-4,...,5,6}, ytick={-6,-5,-4,...,5,6}, 
    xmin=-6.5, xmax=6.5, ymin=-6.5, ymax=6.5,,axis equal image]
    \addplot[black,mark = x, mark size=2pt] coordinates {({{naloga.p}},{{naloga.q}})};
    \draw (axis cs:{{naloga.p}},{{naloga.q}}) ellipse [x radius={{naloga.a}}, y radius = {{naloga.b}}];
    \end{axis}
    \end{tikzpicture}
    \end{minipage}'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{latex(naloga.krivulja)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
        xtick={-6,-5,-4,...,5,6}, ytick={-6,-5,-4,...,5,6}, 
        xmin=-6.5, xmax=6.5, ymin=-6.5, ymax=6.5,,axis equal image]
        \addplot[black,mark = x, mark size=2pt] coordinates {({{naloga.p}},{{naloga.q}})};
        \draw (axis cs:{{naloga.p}},{{naloga.q}}) ellipse [x radius={{naloga.a}}, y radius = {{naloga.b}}];
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, kroznica=True, elipsa=True, premaknjena=True, **kwargs):  # TODO ENUM za krivulje
        super().__init__(**kwargs)

        if kroznica == elipsa == False:
            raise ValueError('Izbrana mora biti vsaj ena od krivulj.')
        self.kroznica = kroznica
        self.elipsa = elipsa
        self.premaknjena = premaknjena

    def _poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        if self.premaknjena:
            p = random.randint(-2, 2)
            q = random.randint(-2, 2)
        else:
            p = 0
            q = 0
        izbor = []
        if self.kroznica:
            izbor.append('kroznica')
        if self.elipsa:
            izbor.append('elipsa')
        izbrana = random.choice(izbor)
        if izbrana == 'kroznica':
            a = random.randint(1, 4)
            b = a
            r = a  # definiran r zaradi različnega izpisa krivulj
            krivulja = ((x - p) ** 2) + ((y - q) ** 2)
        if izbrana == 'elipsa':
            a = random.randint(1, 4)
            b = random.randint(1, 4)
            r = 1  # definiran r zaradi različnega izpisa krivulj
            krivulja = ((x - p) ** 2) / a ** 2 + ((y - q) ** 2) / b ** 2
            preveri(a != b)
        # krivulja = sympy.Add(sympy.Mul((x - p) ** 2, sympy.Pow(a, -2, evaluate=False), evaluate=False),
        #                      sympy.Mul((y - q) ** 2, sympy.Pow(b , -2, evaluate=False), evaluate=False))

        razsirjena = a ** 2 * b ** 2 * krivulja.expand() - a ** 2 * b ** 2
        return {'razsirjena': sympy.Eq(razsirjena, 0), 'krivulja': sympy.Eq(krivulja, r ** 2), 'a': a, 'b': b, 'p': p,
                'q': q}
