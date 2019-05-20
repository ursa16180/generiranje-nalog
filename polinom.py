from generiranje import Naloga, preveri, MinMaxNapaka
import random
import sympy
from kvadratnaFunkcija import splosna_oblika, nicle


def naredi_polinom(min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, risanje=False):
    """
    Vrne naključen polinom.

    :param min_stopnja: najmanjša možna stopnja polinoma
    :param max_stopnja: največja možna stopnja polinoma
    :param min_nicla: najmanjša možna ničla polinoma
    :param max_nicla: največja možna ničla polinoma
    :param risanje: v primeru risanja je manjši vodilni koeficient
    :return: polinom
    """
    x = sympy.symbols('x')
    if min_stopnja > max_stopnja or min_nicla > max_nicla:
        raise MinMaxNapaka

    if risanje:
        vodilni_koeficient = random.choice(
            [-1, sympy.Rational(-1, 2), sympy.Rational(-1, 4), sympy.Rational(1, 4), sympy.Rational(1, 2), 1])
    else:
        vodilni_koeficient = random.choice([-3, -2, -1, 1, 2, 3])

    nicle = []
    stopnja = random.randint(min(min_stopnja, max_stopnja), max(min_stopnja, max_stopnja))

    for _ in range(stopnja):
        nicla = random.randint(min_nicla, max_nicla)  # TODO ničla 1/2
        nicle.append(nicla)
    polinom = '{0}*('.format(vodilni_koeficient) + '*'.join(
        '(x-{0})'.format(nicla) for nicla in nicle) + ')'
    nicle.sort()
    return [vodilni_koeficient, nicle, stopnja, polinom]


# ~~~~~Naloge iz sklopa Polinomi in Racionalna funkcija
class NiclePolinoma(Naloga):
    """
    Naloga za izračun ničel polinoma.
    """
    besedilo_posamezne = r'''Poišči ničle polinoma $p(x)={{latex(naloga.polinom)}}$.'''

    besedilo_vecih = r'''Poišči ničle sledečih polinomov:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $p(x)={{latex(naloga.polinom)}}$
        {% endfor %}
        \end{enumerate}'''
    resitev_posamezne = r'''{% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}'''

    resitev_vecih = r'''Ničle polinomov:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item {% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}
        {% endfor %}
        \end{enumerate}'''

    def __init__(self, min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, **kwargs):
        """
        :param min_stopnja: najmanjša možna stopnja polinoma
        :param max_stopnja: najvenajvečja možna stopnja polinomačja možna stopnja polinoma
        :param min_nicla: najmanjša možna ničla polinoma
        :param max_nicla: največja možna ničla polinoma
        """
        super().__init__(**kwargs)
        if min_stopnja < 0:
            raise ValueError('Stopnja polinoma mora biti celo neničelno število.')
        if min_stopnja > max_stopnja or min_nicla > max_nicla:
            raise MinMaxNapaka
        self.min_stopnja = min_stopnja
        self.max_stopnja = max_stopnja
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo NiclePolinoma."""

        [vodilni_koeficient, nicle, stopnja, polinom] = naredi_polinom(self.min_stopnja, self.max_stopnja,
                                                                       self.min_nicla, self.max_nicla)
        preveri(min(self.min_stopnja, self.max_stopnja) <= len(nicle) <= max(self.min_stopnja, self.max_stopnja))
        x = sympy.symbols('x')
        # {'x{0}'.format(i + 1): nicle[i] for i in range(len(nicle))}
        return {
            'polinom': sympy.expand(polinom),
            'nicle': nicle}


class DvojnaNicla(Naloga):
    """
    Naloga za izračun ničel polinoma, če že poznaš dvojno ničlo.
    """
    besedilo_posamezne = r'''Pokaži, da je število ${{naloga.dvojna}}$ dvojna ničla polinoma $p(x)={{latex(naloga.polinom)}}$ in poišči še preostali ničli.'''
    besedilo_vecih = r''' Pokaži, da je  $x_1$ dvojna ničla polinoma in poišči preostali ničli:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $x_1={{naloga.dvojna}}$, $p(x)={{latex(naloga.polinom)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$x_3={{latex(naloga.x3)}}$, $x_4={{latex(naloga.x4)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $x_3={{latex(naloga.x3)}}$, $x_4={{latex(naloga.x4)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo DvojnaNicla."""
        x = sympy.symbols('x')
        dvojna = random.choice([-5, -4, -3, -2, -1, 2, 3, 4, 5])  # Nočem da je dvojna nišla 0 ali 1 ker prelahko
        [a, b, c, splosna] = splosna_oblika()
        [x3, x4] = nicle(a, b, c)
        preveri(x3 != dvojna and x4 != dvojna)
        polinom = sympy.expand(sympy.Mul((x - dvojna) ** 2, splosna))
        return {'polinom': polinom, 'dvojna': dvojna, 'x3': x3, 'x4': x4}


class ParameteraDvojna(Naloga):
    """
    Naloga za izračun dveh koeficientov, če poznaš dvojno ničlo polinoma.
    """
    besedilo_posamezne = r''' Določi števili $a$ in $b$ tako, da bo število ${{naloga.dvojna}}$ dvojna ničla polinoma $p(x)={{latex(naloga.polinom)}}$.'''

    besedilo_vecih = r'''Določi števili $a$ in $b$ tako, da bo število $x_{1,2}$ dvojna ničla polinoma:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $p(x)={{latex(naloga.polinom)}}$, $x_{1,2}={{naloga.dvojna}}$
        {% endfor %}
        \end{enumerate}'''

    resitev_posamezne = r'''$a={{naloga.a}}$, $b={{naloga.b}}$, $p(x)={{latex(naloga.polinom_resitev)}}$'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $a={{naloga.a}}$, $b={{naloga.b}}$, $p(x)={{latex(naloga.polinom_resitev)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, min_stopnja=3, max_stopnja=4, min_nicla=-5, max_nicla=5, **kwargs):
        """
        :param min_stopnja: najmanjša možna stopnja polinoma
        :param max_stopnja: največja možna stopnja polinoma
        :param min_nicla: najmanjša možna ničla polinoma
        :param max_nicla: največja možna ničla polinoma
        """
        super().__init__(**kwargs)
        if min_nicla > max_nicla or min_stopnja > max_stopnja:
            raise MinMaxNapaka
        if min_stopnja < 3:  # Preveri da polinom ni premajhne stopnje za smiselno nalogo
            raise ValueError("Polinom mora biti vsaj 3. stopnje.")
        self.min_stopnja = min_stopnja
        self.max_stopnja = max_stopnja
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo ParameteraDvojna."""
        x = sympy.symbols('x')
        dvojna = random.choice([-3, -2, -1, 2, 3])

        [vodilni_koeficient, nicle, stopnja, polinomBrezDvojne] = naredi_polinom(self.min_stopnja - 2,
                                                                                 self.max_stopnja - 2,
                                                                                 self.min_nicla, self.max_nicla)
        preveri(min(self.min_stopnja - 2, self.max_stopnja - 2) <= len(nicle) <= max(self.min_stopnja - 2,
                                                                                     self.max_stopnja - 2))  # TODO len(nicle)==stopnja?
        x = sympy.symbols('x')
        polinom_resitev = sympy.expand(polinomBrezDvojne + '*(x-{0})*(x-{0})'.format(dvojna))
        koeficienti = sympy.Poly(polinom_resitev, x).all_coeffs()
        a = koeficienti[-3]
        b = koeficienti[-2]
        koeficienti[-3] = 'a'
        koeficienti[-2] = 'b'
        polinom = sympy.Poly(koeficienti,
                             x).as_expr()  # TODO Ne glede na to ali niz ali poly vedno uredi a na začetku polinoma: če je pa na roke napisan niz pa ne poračuna -- potence  ipd
        return {'polinom': polinom, 'polinom_resitev': polinom_resitev, 'dvojna': dvojna, 'a': a, 'b': b}


class GrafPolinoma(Naloga):
    """
    Naloga za risanje grafa polinoma.
    """
    besedilo_posamezne = r'''Nariši graf polinoma $p(x)={{latex(naloga.polinom)}}$.'''

    besedilo_vecih = r'''Nariši grafe polinomov:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $p(x)={{latex(naloga.polinom)}}$
        {% endfor %}
        \end{enumerate}'''
    resitev_posamezne = r'''$p(x)={{latex(naloga.polinom)}}$\par
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
        '''

    resitev_vecih = r'''
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
    '''

    def __init__(self, min_stopnja=3, max_stopnja=4, min_nicla=-3, max_nicla=3, **kwargs):
        """
        :param min_stopnja: najmanjša možna stopnja polinoma
        :param max_stopnja: največja možna stopnja polinoma
        :param min_nicla: najmanjša možna ničla polinoma
        :param max_nicla: največja možna ničla polinoma
        """
        super().__init__(**kwargs)
        if min_nicla > max_nicla or min_stopnja > max_stopnja:
            raise MinMaxNapaka
        if min_stopnja < 0:  # Preveri da ni vpisano kaj čudnega
            raise ValueError('Stopnja mora biti naravno število.')
        self.min_stopnja = min_stopnja
        self.max_stopnja = max_stopnja
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo GrafPolinoma."""
        x = sympy.symbols('x')
        [vodilni_koeficient, nicle, stopnja, nicelna_oblika] = naredi_polinom(self.min_stopnja, self.max_stopnja,
                                                                              self.min_nicla, self.max_nicla,
                                                                              risanje=True)
        preveri(min(self.min_stopnja, self.max_stopnja) <= len(nicle) <= max(self.min_stopnja, self.max_stopnja))
        polinom = sympy.expand(nicelna_oblika)
        zacetna = polinom.subs(x, 0)

        return {'polinom': polinom, 'nicelna': nicelna_oblika, 'nicle': nicle, 'zacetna': zacetna}


# TODO ideja: deljenje polinomov
# ~~~~~~Naloge iz sklopa: Racionalna funkcija
class DolociNiclePoleAsimptotoRacionalne(Naloga):
    """
    Naloga za izračun ničel, polov in asimptote racionalne funkcije.
    """
    besedilo_posamezne = r'''Določi ničle, pole in asimptoto racionalne funkcije $r(x)={{naloga.racionalna}}$.'''

    besedilo_vecih = r'''
        Določi ničle, pole in asimptoto naslednjih racionalnih funkcij
        \begin{enumerate}
        {% for naloga in naloge%}
        \item $r(x)={{naloga.racionalna}}$
        {% endfor %}
        \end{enumerate}'''

    resitev_posamezne = r'''
        Ničle: {% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}poli: {% for pol in naloga.poli %}$x_{ {{loop.index}} }={{pol}}$ {% endfor %}asimptota: $y={{naloga.asimptota}}$'''

    resitev_vecih = r'''\begin{enumerate}
        {% for naloga in naloge%}
        \item Ničle: {% for nicla in naloga.nicle %}$x_{ {{loop.index}} }={{nicla}}$ {% endfor %}poli: {% for pol in naloga.poli %}$x_{ {{loop.index}} }={{pol}}$ {% endfor %}asimptota: $y={{naloga.asimptota}}$
        {% endfor %}
        \end{enumerate}'''

    def __init__(self, min_stopnja_stevca=3, max_stopnja_stevca=3, min_stopnja_imenovalca=3, max_stopnja_imenovalca=3,
                 min_nicla=-9, max_nicla=9, **kwargs):
        """
        :param min_stopnja_stevca: najmanjša možna stopnja polinoma v števcu
        :param max_stopnja_stevca: največja možna stopnja polinoma v števcu
        :param min_stopnja_imenovalca: najmanjša možna stopnja polinoma v imenovalcu
        :param max_stopnja_imenovalca: največja možna stopnja polinoma v imenovalcu
        :param min_nicla: najmanjša možna ničla polinomov v števcu in imenovalcu
        :param max_nicla: največja možna ničla polinomov v števcu in imenovalcu
        """
        super().__init__(**kwargs)
        if min_stopnja_stevca < 0 or min_stopnja_imenovalca < 0:
            raise ValueError('Stopnja polinoma mora biti neničelno celo število.')
        if min_stopnja_imenovalca > max_stopnja_imenovalca or min_stopnja_stevca > max_stopnja_stevca or min_nicla > max_nicla:
            raise MinMaxNapaka
        self.min_stopnja_stevca = min_stopnja_stevca
        self.max_stopnja_stevca = max_stopnja_stevca
        self.min_stopnja_imenovalca = min_stopnja_imenovalca
        self.max_stopnja_imenovalca = max_stopnja_imenovalca
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo DolociNiclePoleAsimptotoRacionalne."""
        [vodilni_stevca, nicle, stopnja_stevca, stevec] = naredi_polinom(self.min_stopnja_stevca,
                                                                         self.max_stopnja_stevca, self.min_nicla,
                                                                         self.max_nicla)
        [vodilni_imenovalca, poli, stopnja_imenovalca, imenovalec] = naredi_polinom(self.min_stopnja_imenovalca,
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


# TODO ideja: matura 94/7,8 : definicijsko območje in enačbe

class GrafRacionalne(
    Naloga):  # TODO stacionarne točke naj bodo manjše od 5, drugače ni vej na grafu (funkcija.diff je odvod)
    """
    Naloga za risanje grafa racionalne funkcije. Lažja različica ima vodoravno asimptoto, težja pa ima za asimptoto poševno premico ali pa parabola.
    """
    besedilo_posamezne = r'''Nariši graf racionalne funkcije $r(x)= {{naloga.racionalna}}$.'''

    besedilo_vecih = r'''
    Nariši grafe racionalnih funkcij:
    \begin{enumerate}
    {% for naloga in naloge%}
    \item $r(x)={{naloga.racionalna}}$
    {% endfor %}
    \end{enumerate}'''

    resitev_posamezne = r'''$r(x)={{latex(naloga.racionalna)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$,
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5},
    xmin=-5.5, xmax=5.5, 
    restrict y to domain=-5.5:5.5,]

    {% for i in range( naloga.domena_poli|count -1) %}
    \addplot[domain ={{naloga.domena_poli[i]}}+0.1 : {{naloga.domena_poli[i+1]}}-0.1, color=black, smooth, samples=100]{ {{naloga.nicelna}} };
    {% endfor %}

    {% for i in range(1, naloga.domena_poli|count -1) %}
    \addplot[dashed] coordinates{ ({{naloga.domena_poli[i]}},-5.5) ({{naloga.domena_poli[i]}},5.5) };
    {% endfor %}



    \addplot[domain =-5:5, color=black, dashed, smooth]{ {{naloga.asimptota}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
    '''

    resitev_vecih = r'''
    \begin{enumerate}
    {% for naloga in naloge%}
    \item $r(x)={{latex(naloga.racionalna)}}$\par
    \begin{minipage}{\linewidth}
    \centering
    \begin{tikzpicture}[baseline]
    \begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$,
    xtick={-5,-4,...,5}, ytick={-5,-4,...,5},
    xmin=-5.5, xmax=5.5,
    restrict y to domain=-5.5:5.5,]

    {% for i in range( naloga.domena_poli|count -1) %}
    \addplot[domain ={{naloga.domena_poli[i]}}+0.3 : {{naloga.domena_poli[i+1]}}-0.3, color=black, smooth, samples=100]{ {{naloga.nicelna}} };
    {% endfor %}

    {% for i in range(1, naloga.domena_poli|count -1) %}
    \addplot[dashed] coordinates{ ({{naloga.domena_poli[i]}},-5.5) ({{naloga.domena_poli[i]}},5.5) };
    {% endfor %}

    \addplot[domain =-5:5, color=black, dashed, smooth]{ {{naloga.asimptota}} };
    \end{axis}
    \end{tikzpicture}
    \end{minipage}
    {% endfor %}
    \end{enumerate}'''

    def __init__(self, min_stopnja_stevca=2, max_stopnja_stevca=4, min_stopnja_imenovalca=2, max_stopnja_imenovalca=4,
                 min_nicla=-5, max_nicla=5, lazja=True, **kwargs):
        """
        :param min_stopnja_stevca: najmanjša možna stopnja polinoma v števcu
        :param max_stopnja_stevca: največja možna stopnja polinoma v števcu
        :param min_stopnja_imenovalca: najmanjša možna stopnja polinoma v imenovalcu
        :param max_stopnja_imenovalca: največja možna stopnja polinoma v imenovalcu
        :param min_nicla: najmanjša možna ničla polinomov v števcu in imenovalcu
        :param max_nicla: največja možna ničla polinomov v števcu in imenovalcu
        :param lazja: lažja ali težja oblika naloge
        """
        super().__init__(**kwargs)
        if min_nicla > max_nicla or min_stopnja_stevca > max_stopnja_stevca or min_stopnja_imenovalca > max_stopnja_imenovalca:
            raise MinMaxNapaka
        if min_stopnja_imenovalca < 0 or min_stopnja_stevca < 0:
            raise ValueError('Stopnja polinoma mora biti večja od nič.')

        self.min_stopnja_stevca = min_stopnja_stevca
        self.max_stopnja_stevca = max_stopnja_stevca
        self.min_stopnja_imenovalca = min_stopnja_imenovalca
        self.max_stopnja_imenovalca = max_stopnja_imenovalca
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla
        self.lazja = lazja

    def poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo GrafRacionalne."""
        [vodilni_stevca, nicle, stopnja_stevca, stevec] = naredi_polinom(self.min_stopnja_stevca,
                                                                         self.max_stopnja_stevca, self.min_nicla,
                                                                         self.max_nicla, risanje=True)
        [vodilni_imenovalca, poli, stopnja_imenovalca, imenovalec] = naredi_polinom(self.min_stopnja_imenovalca,
                                                                                    self.max_stopnja_imenovalca,
                                                                                    self.min_nicla, self.max_nicla,
                                                                                    risanje=True)
        razlika_stopenj = stopnja_stevca - stopnja_imenovalca
        preveri(set(nicle) & set(poli) == set() and
                razlika_stopenj < 3)  # Ker ne znajo narisati asimptote 3.stopnje
        if self.lazja:
            preveri(razlika_stopenj < 1)
        else:
            preveri(1 <= razlika_stopenj <= 2)  # Poševna asimptota in kvadratna sta težki za dijake

        x = sympy.symbols('x')

        if stopnja_stevca < stopnja_imenovalca:
            asimptota = 0
        elif stopnja_stevca == stopnja_imenovalca:
            asimptota = vodilni_stevca / vodilni_imenovalca
        elif stopnja_stevca > stopnja_imenovalca:
            q, r = sympy.div(stevec, imenovalec, x)
            asimptota = q
        if razlika_stopenj == 2:
            asimptota = sympy.latex(asimptota.evalf())

        nicelna = '(' + stevec + ')/(' + imenovalec + ')'
        # nicelna= str(sympy.N(sympy.factor(stevec)) / sympy.N(sympy.factor(imenovalec))).replace('**','^')
        # print(nicelna)
        racionalna = sympy.latex(sympy.expand(stevec) / sympy.expand(imenovalec))
        print(racionalna)
        domena_poli = [-5.8] + list(set(poli)) + [5.8]

        return {'racionalna': racionalna, 'nicelna': nicelna, 'nicle': nicle, 'poli': poli, 'asimptota': asimptota,
                'domena_poli': domena_poli}
