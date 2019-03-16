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
        nicla = random.randint(min_ni, max_ni) #TODO ničla 1/2
        nicle.append(nicla)
    polinom = '{0}*('.format(vodilni_koeficient) + '*'.join(
        '(x-{0})'.format(nicla) for nicla in nicle) + ')'

    return [vodilni_koeficient, nicle, stopnja, polinom]

#~~~~~Naloge iz sklopa Polinomi in Racionalna funkcija
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
                                                                      self.min_nicla, self.max_nicla, risanje=True)
        preveri(min(self.min_stopnja, self.max_stopnja) <= len(nicle) <= max(self.min_stopnja, self.max_stopnja))
        polinom = sympy.expand(nicelnaOblika)
        zacetna =polinom.subs(x, 0)

        return {'polinom': polinom, 'nicelna':nicelnaOblika, 'nicle': nicle, 'zacetna':zacetna}

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

class GrafRacionalne(Naloga):
    def __init__(self, min_stopnja_stevca=2, max_stopnja_stevca=4, min_stopnja_imenovalca=2, max_stopnja_imenovalca=4,
                 min_nicla=-3, max_nicla=3,lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Nariši graf racionalne funkcije $r(x)= {{naloga.racionalna}}$.''')

        self.besedilo_vecih = jinja2.Template(r'''
        Nariši grafe racionalnih funkcij:
        \begin{enumerate}
        {% for naloga in naloge%}
        \item $r(x)={{naloga.racionalna}}$
        {% endfor %}
        \end{enumerate}''')

        self.resitev_posamezne = jinja2.Template(r'''$r(x)={{latex(naloga.racionalna)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
        xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
        xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,]
        \addplot[domain =-5:5, color=black, smooth]{ {{naloga.nicelna}} };
        \addplot[domain =-5:5, color=black,dashed, smooth]{ {{naloga.asimptota}} };
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
        ''')

        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
        {% for naloga in naloge%}
        \item $r(x)={{latex(naloga.racionalna)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$, 
        xtick={-5,-4,...,5}, ytick={-5,-4,...,5}, 
        xmin=-5.5, xmax=5.5, ymin=-5.5, ymax=5.5,]
        \addplot[domain =-5:5, color=black, smooth]{ {{naloga.nicelna}} };
        \addplot[domain =-5:5, color=black,dashed, smooth]{ {{naloga.asimptota}} };
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
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
        self.lazja = lazja

    def poskusi_sestaviti(self):
        [vodilni_stevca, nicle, stopnja_stevca, stevec] = narediPolinom(self.min_stopnja_stevca,
                                                                        self.max_stopnja_stevca, self.min_nicla,
                                                                        self.max_nicla,risanje=True)
        [vodilni_imenovalca, poli, stopnja_imenovalca, imenovalec] = narediPolinom(self.min_stopnja_imenovalca,
                                                                                   self.max_stopnja_imenovalca,
                                                                                   self.min_nicla, self.max_nicla, risanje=True)
        preveri(set(nicle) & set(poli) == set())
        if self.lazja:
            preveri(stopnja_stevca-stopnja_imenovalca<2)
        else:
            preveri(stopnja_stevca-stopnja_imenovalca==2)
        x = sympy.symbols('x')

        if stopnja_stevca < stopnja_imenovalca:
            asimptota = 0
        elif stopnja_stevca == stopnja_imenovalca:
            asimptota = vodilni_stevca/vodilni_imenovalca
        elif stopnja_stevca > stopnja_imenovalca:

            q, r = sympy.div(stevec, imenovalec, x)
            asimptota = q
        if sympy.degree(asimptota)==2:
            asimptota = asimptota #TODO ničelna oblika kvadratne

        nicelna = '('+stevec+ ')/('+imenovalec +')'
        print(nicelna)
        racionalna = sympy.latex(sympy.expand(stevec) / sympy.expand(imenovalec))

        return {'racionalna': racionalna, 'nicelna':nicelna, 'nicle': nicle, 'poli': poli, 'asimptota': asimptota}
