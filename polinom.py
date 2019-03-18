from generiranje import *
import kvadratnaFunkcija


def narediPolinom(min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, risanje=False):
    x = sympy.symbols('x')
    min_ni = min(min_nicla, max_nicla)
    max_ni = max(min_nicla, max_nicla)

    if risanje:
        vodilni_koeficient = random.choice(
            [-1, sympy.Rational(-1, 2), sympy.Rational(-1, 4), sympy.Rational(1, 4), sympy.Rational(1, 2), 1])
    else:
        vodilni_koeficient = random.choice([-3, -2, -1, 1, 2, 3])

    nicle = []
    stopnja = random.randint(min(min_stopnja, max_stopnja), max(min_stopnja, max_stopnja))

    for _ in range(stopnja):
        nicla = random.randint(min_ni, max_ni)  # TODO ničla 1/2
        nicle.append(nicla)
    polinom = '{0}*('.format(vodilni_koeficient) + '*'.join(
        '(x-{0})'.format(nicla) for nicla in nicle) + ')'

    return [vodilni_koeficient, nicle, stopnja, polinom]


# ~~~~~Naloge iz sklopa Polinomi in Racionalna funkcija
class NiclePolinoma(Naloga):
    def __init__(self, min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''
        Poišči ničle polinoma $p(x)={{latex(naloga.polinom)}}$.''')

        self.besedilo_vecih = jinja2.Template(
            r'''Poišči ničle sledečih polinomov:
            \begin{enumerate}
            {% for naloga in naloge %}
            \item $p(x)={{latex(naloga.polinom)}}$
            {% endfor %}
            \end{enumerate}''')
        self.resitev_posamezne = jinja2.Template(
            r'''{% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}
            ''')

        self.resitev_vecih = jinja2.Template(
            r'''Ničle polinomov:
            \begin{enumerate}
            {% for naloga in naloge %}
            \item {% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}
            {% endfor %}
            \end{enumerate}''')

        if min_stopnja < 0:  # Preveri da ni vpisano kaj čudnega
            self.min_stopnja = 0
        else:
            self.min_stopnja = int(min_stopnja)
        if max_stopnja < 0:
            self.max_stopnja = 0
        else:
            self.max_stopnja = int(max_stopnja)

        self.min_nicla = int(min_nicla)
        self.max_nicla = int(max_nicla)

    def poskusi_sestaviti(self):

        [vodilni_koeficient, nicle, stopnja, polinom] = narediPolinom(self.min_stopnja, self.max_stopnja,
                                                                      self.min_nicla, self.max_nicla)
        preveri(min(self.min_stopnja, self.max_stopnja) <= len(nicle) <= max(self.min_stopnja, self.max_stopnja))
        x = sympy.symbols('x')
        # {'x{0}'.format(i + 1): nicle[i] for i in range(len(nicle))}
        return {
            'polinom': sympy.expand(polinom),
            'nicle': nicle}

class DvojnaNicla(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Pokaži, da je število ${{naloga.dvojna}}$ dvojna ničla polinoma $p(x)={{latex(naloga.polinom)}}$ in poišči še preostali ničli.''')
        self.besedilo_vecih = jinja2.Template(r''' Pokaži, da je  $x_1$ dvojna ničla polinoma in poišči preostali ničli:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $x_1={{naloga.dvojna}}$, $p(x)={{latex(naloga.polinom)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$x_3={{latex(naloga.x3)}}$, $x_4={{latex(naloga.x4)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $x_3={{latex(naloga.x3)}}$, $x_4={{latex(naloga.x4)}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        dvojna = random.choice([-5, -4, -3, -2, -1, 2, 3, 4, 5])  # Nočem da je dvojna nišla 0 ali 1 ker prelahko
        [vodilni_koeficient, nicle, stopnja, polinomBrezDvojne] = narediPolinom(2, 2, -5,5)
        [x3,x4]=nicle
        preveri(x3 != dvojna and x4 != dvojna)
        polinom = sympy.expand('(x - {0}) ** 2 *'.format(dvojna)+ polinomBrezDvojne)
        return {'polinom': polinom, 'dvojna': dvojna, 'x3': x3, 'x4': x4}

class ParameteraDvojna(Naloga):
    def __init__(self, min_stopnja=3, max_stopnja=4, min_nicla=-5, max_nicla=5, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r''' Določi števili $a$ in $b$ tako, da bo število ${{naloga.dvojna}}$ dvojna ničla polinoma $p(x)={{latex(naloga.polinom)}}$.
        ''')

        self.besedilo_vecih = jinja2.Template(
            r'''Določi števili $a$ in $b$ tako, da bo število $x_{1,2}$ dvojna ničla polinoma:
            \begin{enumerate}
            {% for naloga in naloge %}
            \item $p(x)={{latex(naloga.polinom)}}$, $x_{1,2}={{naloga.dvojna}}$
            {% endfor %}
            \end{enumerate}''')

        self.resitev_posamezne = jinja2.Template(
            r'''$a={{naloga.a}}$, $b={{naloga.b}}$, $p(x)={{latex(naloga.polinomResitev)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $a={{naloga.a}}$, $b={{naloga.b}}$, $p(x)={{latex(naloga.polinomResitev)}}$
         {% endfor %}
         \end{enumerate}
         ''')

        if min_stopnja < 3:  # Preveri da ni vpisano kaj čudnega in določi da je vsaj polinom 3.stopnje
            self.min_stopnja = 3
        else:
            self.min_stopnja = int(min_stopnja)
        if max_stopnja < 3:
            self.max_stopnja = 3
        else:
            self.max_stopnja = int(max_stopnja)

        self.min_nicla = int(min_nicla)
        self.max_nicla = int(max_nicla)

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        dvojna = random.choice([-3, -2, -1, 2, 3])

        [vodilni_koeficient, nicle, stopnja, polinomBrezDvojne] = narediPolinom(self.min_stopnja - 2,
                                                                                self.max_stopnja - 2,
                                                                                self.min_nicla, self.max_nicla)
        preveri(min(self.min_stopnja - 2, self.max_stopnja - 2) <= len(nicle) <= max(self.min_stopnja - 2,
                                                                                     self.max_stopnja - 2))  # TODO len(nicle)==stopnja?
        x = sympy.symbols('x')
        polinomResitev = sympy.expand(polinomBrezDvojne + '*(x-{0})*(x-{0})'.format(dvojna))
        koeficienti = sympy.Poly(polinomResitev, x).all_coeffs()
        a = koeficienti[-3]
        b = koeficienti[-2]
        koeficienti[-3] = 'a'
        koeficienti[-2] = 'b'
        polinom = sympy.Poly(koeficienti,x).as_expr() #TODO Ne glede na to ali niz ali poly vedno uredi a na začetku polinoma: če je pa na roke napisan niz pa ne poračuna -- potence o ipd
        return {'polinom': polinom, 'polinomResitev': polinomResitev, 'dvojna': dvojna, 'a': a, 'b': b}

class GrafPolinoma(Naloga):
    def __init__(self, min_stopnja=3, max_stopnja=4, min_nicla=-3, max_nicla=3, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''
        Nariši graf polinoma $p(x)={{latex(naloga.polinom)}}$.''')

        self.besedilo_vecih = jinja2.Template(
            r'''Nariši grafe polinomov:
            \begin{enumerate}
            {% for naloga in naloge %}
            \item $p(x)={{latex(naloga.polinom)}}$
            {% endfor %}
            \end{enumerate}''')
        self.resitev_posamezne = jinja2.Template(
            r'''$p(x)={{latex(naloga.polinom)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
        xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
        xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
        extra y ticks={ {{naloga.zacetna}} },
        extra y tick labels={ ${{latex(naloga.zacetna)}}$ },
        extra y tick style={yticklabel style={right},},]
        \addplot[domain =-5:5, color=black, smooth]{ {{naloga.nicelna}} };
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
            ''')

        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $p(x)={{latex(naloga.polinom)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
        xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
        xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,
        extra y ticks={ {{naloga.zacetna}} },
        extra y tick labels={ ${{latex(naloga.zacetna)}}$ },
        extra y tick style={yticklabel style={right},},]
        \addplot[domain =-5:5, color=black, smooth]{ {{naloga.nicelna}} };
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
        {% endfor %}
        \end{enumerate}
        ''')

        if min_stopnja < 0:  # Preveri da ni vpisano kaj čudnega
            self.min_stopnja = 0
        else:
            self.min_stopnja = int(min_stopnja)
        if max_stopnja < 0:
            self.max_stopnja = 0
        else:
            self.max_stopnja = int(max_stopnja)

        self.min_nicla = int(min_nicla)
        self.max_nicla = int(max_nicla)

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        [vodilni_koeficient, nicle, stopnja, nicelnaOblika] = narediPolinom(self.min_stopnja, self.max_stopnja,
                                                                            self.min_nicla, self.max_nicla,
                                                                            risanje=True)
        preveri(min(self.min_stopnja, self.max_stopnja) <= len(nicle) <= max(self.min_stopnja, self.max_stopnja))
        polinom = sympy.expand(nicelnaOblika)
        zacetna = polinom.subs(x, 0)

        return {'polinom': polinom, 'nicelna': nicelnaOblika, 'nicle': nicle, 'zacetna': zacetna}

#TODO ideja: deljenje polinomov
# ~~~~~~Naloge iz sklopa: Racionalna funkcija
class DolociNiclePoleAsimptotoRacionalne(Naloga):
    def __init__(self, min_stopnja_stevca=3, max_stopnja_stevca=3, min_stopnja_imenovalca=3, max_stopnja_imenovalca=3,
                 min_nicla=-9, max_nicla=9, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Določi ničle, pole in asimptoto racionalne funkcije $r(x)={{naloga.racionalna}}$.''')

        self.besedilo_vecih = jinja2.Template(r'''
        Določi ničle, pole in asimptoto naslednjih racionalnih funkcij
        \begin{enumerate}
        {% for naloga in naloge%}
        \item $r(x)={{naloga.racionalna}}$
        {% endfor %}
        \end{enumerate}''')

        self.resitev_posamezne = jinja2.Template(r'''
        Ničle: {% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}poli: {% for pol in naloga.poli %}$x_{ {{loop.index}} }={{pol}}$ {% endfor %}asimptota: $y={{naloga.asimptota}}$''')

        self.resitev_vecih = jinja2.Template(r'''\begin{enumerate}
        {% for naloga in naloge%}
        \item Ničle: {% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}poli: {% for pol in naloga.poli %}$x_{ {{loop.index}} }={{pol}}$ {% endfor %}asimptota: $y={{naloga.asimptota}}$
        {% endfor %}
        \end{enumerate}''')

        if min_stopnja_stevca < 0:  # Preveri da ni vpisano kaj čudnega
            self.min_stopnja_stevca = 0
        else:
            self.min_stopnja_stevca = int(min_stopnja_stevca)
        if max_stopnja_stevca < 0:
            self.max_stopnja_stevca = 0
        else:
            self.max_stopnja_stevca = int(max_stopnja_stevca)

        if min_stopnja_imenovalca < 0:  # Preveri da ni vpisano kaj čudnega
            self.min_stopnja_imenovalca = 0
        else:
            self.min_stopnja_imenovalca = int(min_stopnja_imenovalca)
        if max_stopnja_imenovalca < 0:
            self.max_stopnja_imenovalca = 0
        else:
            self.max_stopnja_imenovalca = int(max_stopnja_imenovalca)
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        [vodilni_stevca, nicle, stopnja_stevca, stevec] = narediPolinom(self.min_stopnja_stevca,
                                                                        self.max_stopnja_stevca, self.min_nicla,
                                                                        self.max_nicla)
        [vodilni_imenovalca, poli, stopnja_imenovalca, imenovalec] = narediPolinom(self.min_stopnja_imenovalca,
                                                                                   self.max_stopnja_imenovalca,
                                                                                   self.min_nicla, self.max_nicla)
        preveri(set(nicle) & set(poli) == set())
        x = sympy.symbols('x')

        if stopnja_stevca < stopnja_imenovalca:
            asimptota = 0
        elif stopnja_stevca == stopnja_imenovalca:
            asimptota = sympy.Rational(vodilni_stevca, vodilni_imenovalca)
        elif stopnja_stevca > stopnja_imenovalca:

            q, r = sympy.div(stevec, imenovalec, x)
            asimptota = q

        racionalna = sympy.latex(sympy.expand(stevec) / sympy.expand(imenovalec))
        return {'racionalna': racionalna, 'nicle': nicle, 'poli': poli, 'asimptota': asimptota}

#TODO ideja: matura 94/7,8 : definicijsko območje in enačbe

# class GrafRacionalne(Naloga): #Ta naloga je skoraj nemogoča, saj latex ne more narisati grafa racionalne, ker se ne zna izognit polom Ideja: samles, unbounded coords=jump
#     def __init__(self, min_stopnja_stevca=2, max_stopnja_stevca=4, min_stopnja_imenovalca=2, max_stopnja_imenovalca=4,
#                  min_nicla=-3, max_nicla=3, lazja=True, **kwargs):
#         super().__init__(self, **kwargs)
#         self.besedilo_posamezne = jinja2.Template(
#             r'''Nariši graf racionalne funkcije $r(x)= {{naloga.racionalna}}$.''')
#
#         self.besedilo_vecih = jinja2.Template(r'''
#         Nariši grafe racionalnih funkcij:
#         \begin{enumerate}
#         {% for naloga in naloge%}
#         \item $r(x)={{naloga.racionalna}}$
#         {% endfor %}
#         \end{enumerate}''')
#
#         self.resitev_posamezne = jinja2.Template(r'''$r(x)={{latex(naloga.racionalna)}}$\par
#         \begin{minipage}{\linewidth}
#         \centering
#         \begin{tikzpicture}[baseline]
#         \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$,
#         xtick={-5,-4,...,5}, ytick={-5,-4,...,5},
#         xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,]
#         \addplot[domain =-5:5,samples=10, color=black, smooth,]{ {{naloga.nicelna}} };
#         \addplot[domain =-5:5, color=black, dashed, smooth]{ {{naloga.asimptota}} };
#         \end{axis}
#         \end{tikzpicture}
#         \end{minipage}
#         ''')
#
#         self.resitev_vecih = jinja2.Template(r'''
#         \begin{enumerate}
#         {% for naloga in naloge%}
#         \item $r(x)={{latex(naloga.racionalna)}}$\par
#         \begin{minipage}{\linewidth}
#         \centering
#         \begin{tikzpicture}[baseline]
#         \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$,
#         xtick={-5,-4,...,5}, ytick={-5,-4,...,5},
#         xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,]
#         \addplot[domain =-5:5,samples=10, color=black, smooth,unbounded coords=jump,]{ {{naloga.nicelna}} };
#         \addplot[domain =-5:5, color=black, dashed, smooth]{ {{naloga.asimptota}} };
#         \end{axis}
#         \end{tikzpicture}
#         \end{minipage}
#         {% endfor %}
#         \end{enumerate}''')
#
#         if min_stopnja_stevca < 0:  # Preveri da ni vpisano kaj čudnega
#             self.min_stopnja_stevca = 0
#         else:
#             self.min_stopnja_stevca = int(min_stopnja_stevca)
#         if max_stopnja_stevca < 0:
#             self.max_stopnja_stevca = 0
#         else:
#             self.max_stopnja_stevca = int(max_stopnja_stevca)
#
#         if min_stopnja_imenovalca < 0:  # Preveri da ni vpisano kaj čudnega
#             self.min_stopnja_imenovalca = 0
#         else:
#             self.min_stopnja_imenovalca = int(min_stopnja_imenovalca)
#         if max_stopnja_imenovalca < 0:
#             self.max_stopnja_imenovalca = 0
#         else:
#             self.max_stopnja_imenovalca = int(max_stopnja_imenovalca)
#         self.min_nicla = min_nicla
#         self.max_nicla = max_nicla
#         self.lazja = lazja
#
#     def poskusi_sestaviti(self):
#         [vodilni_stevca, nicle, stopnja_stevca, stevec] = narediPolinom(self.min_stopnja_stevca,
#                                                                         self.max_stopnja_stevca, self.min_nicla,
#                                                                         self.max_nicla, risanje=True)
#         [vodilni_imenovalca, poli, stopnja_imenovalca, imenovalec] = narediPolinom(self.min_stopnja_imenovalca,
#                                                                                    self.max_stopnja_imenovalca,
#                                                                                    self.min_nicla, self.max_nicla,
#                                                                                    risanje=True)
#         razlika_stopenj = stopnja_stevca - stopnja_imenovalca
#         preveri(set(nicle) & set(poli) == set() and
#                 razlika_stopenj < 3)  # Ker ne znajo narisati asimptot3 3.stopnje
#         if self.lazja:
#             preveri(razlika_stopenj < 1)
#         else:
#             preveri(1 <= razlika_stopenj <= 2)  # Poševna asimptota in kvadratna sta težki za dijake
#         x = sympy.symbols('x')
#
#         if stopnja_stevca < stopnja_imenovalca:
#             asimptota = 0
#         elif stopnja_stevca == stopnja_imenovalca:
#             asimptota = vodilni_stevca / vodilni_imenovalca
#         elif stopnja_stevca > stopnja_imenovalca:
#
#             q, r = sympy.div(stevec, imenovalec, x)
#             asimptota = q
#         if razlika_stopenj == 2:
#             asimptota = sympy.latex(asimptota.evalf())
#             #print(asimptota)
#
#         nicelna = '(' + stevec + ')/(' + imenovalec + ')'
#         #nicelna= str(sympy.N(sympy.factor(stevec)) / sympy.N(sympy.factor(imenovalec))).replace('**','^')
#         print(nicelna)
#         racionalna = sympy.latex(sympy.expand(stevec) / sympy.expand(imenovalec))
#
#
#         return {'racionalna': racionalna, 'nicelna': nicelna, 'nicle': nicle, 'poli': poli, 'asimptota': asimptota}
