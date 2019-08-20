from generiranje import Naloga, preveri, MinMaxNapaka
import random
import sympy


def izberi_kompleksno_stevilo(od=-5, do=5):
    """
    Vrne naključno kompleksno število, ki ima realno in imagirano komponento neničelno.

    :param od: najmanjša možna vrednost za posamezno komponento
    :param do: največja možna vrednost za posamezno komponento
    :return: vrne naključno kompleksno število

    >>> izberi_kompleksno_stevilo()
    -3 + 5*I

    >>> izberi_kompleksno_stevilo(od=-10, do=20)
    -5 + 12*I
    """
    if od > do:
        raise MinMaxNapaka
    a = random.choice([x for x in range(od, do + 1) if x != 0])
    b = random.choice([x for x in range(od, do + 1) if x != 0])
    return a + b * sympy.I


# ~~~~~Naloge iz sklopa kompleksnih števil
class VsotaRazlika(Naloga):
    """
    Naloga za seštevanje in odštevanje treh kompleksnih števil.


    >>> VsotaRazlika().sestavi()
    {'racun': 2 - 3*I + (1 - 5*I)/4 - (-5 - 2*I), 'rezultat': 29/4 - 9*I/4}

    >>> VsotaRazlika().sestavi()
    {'racun': -3*(1 + 3*I) + 4 - 5*I - (5 - 5*I)/2, 'rezultat': -3/2 - 23*I/2}
    """
    besedilo_posamezne = r'''Izračunaj $z={{latex(naloga.racun)}}$.'''
    besedilo_vecih = r'''Izračunaj:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $z={{latex(naloga.racun)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$z={{latex(naloga.rezultat)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $z={{latex(naloga.rezultat)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        izbor = [-3, -2, -1, 1, 2, 3, 1, 1, 1, 1, 1,
                 -sympy.Rational(1, 2), sympy.Rational(1, 2),
                 -sympy.Rational(1, 3), sympy.Rational(1, 3),
                 -sympy.Rational(1, 4), sympy.Rational(1, 4),
                 -sympy.Rational(1, 4), sympy.Rational(1, 4),
                 -sympy.Rational(3, 4), sympy.Rational(3, 4),
                 -sympy.Rational(2, 3), sympy.Rational(2, 3)]
        a = random.choice(izbor)
        b = random.choice(izbor)
        c = random.choice(izbor)
        z1 = izberi_kompleksno_stevilo()
        z2 = izberi_kompleksno_stevilo()
        z3 = izberi_kompleksno_stevilo()
        preveri(z1 != z2 and z1 != z3 and z2 != z3)
        racun = sympy.Add(sympy.Mul(a, z1, evaluate=False), sympy.Mul(b, z2, evaluate=False),
                          sympy.Mul(c, z3, evaluate=False), evaluate=False)
        rezultat = a * z1 + b * z2 + c * z3
        return {'racun': racun, 'rezultat': rezultat}


class Ulomek(Naloga):
    """
    Naloga za seštevanje dveh kompleksnih ulomkov in racionalizacije ulomkov.

    :param nicelna_komponenta_stevca: števec ima eno od komponent enako 0, drugače v števcu poljubno kompleksno število


    >>> Ulomek().sestavi()
    {'racun': (-3 - I)/(2 - I) + (-1 - 3*I)/(3 + 3*I), 'rezultat': -5/3 - 4*I/3}

    >>> Ulomek(nicelna_komponenta_stevca=True).sestavi()
    {'racun': 1/(-3 + 2*I) + (4*I)/(2 + 3*I), 'rezultat': 9/13 + 6*I/13}
    """
    besedilo_posamezne = r'''Izračunaj $z={{latex(naloga.racun)}}$.'''
    besedilo_vecih = r'''Izračunaj:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $z={{latex(naloga.racun)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$z={{latex(naloga.rezultat)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $z={{latex(naloga.rezultat)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, nicelna_komponenta_stevca=False, **kwargs):
        super().__init__(**kwargs)
        self.nicelna_komponenta_stevca = nicelna_komponenta_stevca

    def _poskusi_sestaviti(self):
        izbor = list(range(1, 6)) + [x * sympy.I for x in range(-5, 6) if
                                     x != 0]  # TODO dodaj odštevanje ulomkov- če izbere celo negativno število, se račun poenostavi
        if self.nicelna_komponenta_stevca:
            a = random.choice(izbor)
            b = random.choice(izbor)
        else:
            a = izberi_kompleksno_stevilo(-3, 3)
            b = izberi_kompleksno_stevilo(-3, 3)

        z1 = izberi_kompleksno_stevilo(-3, 3)
        z2 = izberi_kompleksno_stevilo(-3, 3)
        preveri(a != z1 and b != z2 and z1 != z2)
        racun = sympy.Add(sympy.Mul(a, sympy.Pow(z1, -1, evaluate=False), evaluate=False),
                          sympy.Mul(b, sympy.Pow(z2, -1, evaluate=False), evaluate=False),
                          evaluate=False)
        # racun = '\\frac{{{0}}}{{{1}}} +\\frac{{{2}}}{{{3}}}'.format(sympy.latex(a), sympy.latex(z1), sympy.latex(b),
        #                                                             sympy.latex(
        #                                                                 z2))  # TODO kako avomatično zapisati neporačunan ulomek tudi če so cela negativna števila v števcu
        rezultat = sympy.simplify(a / z1 + b / z2)
        return {'racun': racun, 'rezultat': rezultat}


class Mnozenje(Naloga):
    """
    Naloga za množenje dveh kompleksnih števil.


    >>> Mnozenje().sestavi()
    {'racun': (-2 - 2*I)*(3 - 3*I), 'rezultat': -12}

    >>> Mnozenje().sestavi()
    {'racun': (4 + 4*I)*(5 - I), 'rezultat': 24 + 16*I}
    """
    besedilo_posamezne = r'''Izračunaj $z={{latex(naloga.racun)}}$.'''
    besedilo_vecih = r'''Izračunaj:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $z={{latex(naloga.racun)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$z={{latex(naloga.rezultat)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $z={{latex(naloga.rezultat)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        z1 = izberi_kompleksno_stevilo()
        z2 = izberi_kompleksno_stevilo()
        racun = sympy.Mul(z1, z2, evaluate=False)
        rezultat = sympy.simplify(z1 * z2)
        return {'racun': racun, 'rezultat': rezultat}


class Racunanje(Naloga):
    """
    Naloga za računanje absolutne vrednosti, potenciranja in konjugiranje kompleksnega števila ter višje potence števila :math:`i`.


    >>> Racunanje().sestavi()
    {'stevilo': -2 - 5*I, 'racun': z**2 + I**2000*conjugate(z) + Abs(z)**2, 'rezultat': 6 + 25*I}

    >>> Racunanje().sestavi()
    {'stevilo': 3 + I, 'racun': z**3 + I**2009*conjugate(z) + Abs(z)**2, 'rezultat': 29 + 29*I}
    """
    besedilo_posamezne = r'''Dano je kompleksno število $z={{latex(naloga.stevilo)}}$. Izračunaj število $w={{latex(naloga.racun)}}$.'''

    besedilo_vecih = r''' Za dano kompleksno število $z$ izračunaj število $w$:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $w={{latex(naloga.racun)}}$, $z={{latex(naloga.stevilo)}}$
        {% endfor %}
        \end{enumerate}
        '''
    resitev_posamezne = r'''$w={{latex(naloga.rezultat)}}$'''
    resitev_vecih = r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $w={{latex(naloga.rezultat)}}$
         {% endfor %}
         \end{enumerate}
         '''

    def _poskusi_sestaviti(self):
        z = sympy.symbols('z')
        z0 = izberi_kompleksno_stevilo()
        racun = sympy.Pow(z, random.randint(2, 3)) + sympy.Mul(
            sympy.Pow(sympy.I, random.randint(1991, 2018), evaluate=False), sympy.conjugate(z), evaluate=False) + abs(
            z) ** 2
        rezultat = sympy.simplify(racun.subs(z, z0))
        return {'stevilo': z0, 'racun': racun, 'rezultat': rezultat}


class Enacba(Naloga):
    """
    Naloga iz množenja, konjugiranja, absolutne vrednosti in komponent kompleksnih števil.

    :param konjugirana_vrednost: v enačbi poleg :math:`z` nastopa tudi :math:`\overline{z}`


    >>> Enacba().sestavi()
    {'enacba': Eq(z*(3 - 2*I), -5 - 14*I), 'resitev': 1 - 4*I, 'imaginarna': -4, 'realna': 1, 'absolutna': sqrt(17)}

    >>> Enacba(konjugirana_vrednost=True).sestavi()
    {'enacba': Eq(z*(1 + 3*I) + (-5 + 3*I)*conjugate(z), -16 + 6*I), 'resitev': 4 - 3*I, 'imaginarna': -3, 'realna': 4, 'absolutna': 5}
    """
    besedilo_posamezne = r'''Katero kompleksno število $z$ zadošča enačbi ${{latex(naloga.enacba)}}$? Zapiši $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunaj $\left| z \right|$.'''
    besedilo_vecih = r'''Izračunaj katero število $z$ reši enačbo in zapiši še $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunajte $\left| z \right|$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.enacba)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$z={{latex(naloga.resitev)}}$, $\operatorname{Re}(z)={{latex(naloga.realna)}}$, $\operatorname{Im}(z)={{latex(naloga.imaginarna)}}$, $\left|z\right|={{latex(naloga.absolutna)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $z={{latex(naloga.resitev)}}$, $\operatorname{Re}(z)={{latex(naloga.realna)}}$, $\operatorname{Im}(z)={{latex(naloga.imaginarna)}}$, $\left|z\right|={{latex(naloga.absolutna)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, konjugirana_vrednost=False, **kwargs):
        super().__init__(**kwargs)
        self.konjugirana_vrednost = konjugirana_vrednost

    def _poskusi_sestaviti(self):
        z = sympy.symbols('z')
        z1 = izberi_kompleksno_stevilo()
        resitev = izberi_kompleksno_stevilo()
        if not self.konjugirana_vrednost:
            enacba = z1 * z
        else:
            z2 = izberi_kompleksno_stevilo()
            enacba = z1 * z + z2 * sympy.conjugate(z)
        z3 = sympy.simplify(enacba.subs(z, resitev))
        im = sympy.im(resitev)
        re = sympy.re(resitev)
        absolutna = abs(resitev)

        return {'enacba': sympy.Eq(enacba, z3), 'resitev': resitev, 'imaginarna': im, 'realna': re,
                'absolutna': absolutna}


class NarisiTocke(Naloga):
    """
    Naloga za risanje kompleksnih števil v kompleksno ravnino.


    >>> NarisiTocke().sestavi()
    {'z1': 5 - 3*I, 'z2': 1 - 5*I, 'z3': -1 + 3*I, 'z4': -2 - 5*I, 'koordinatiz1': (5, -3), 'koordinatiz2': (1, -5), 'koordinatiz3': (-1, 3), 'koordinatiz4': (-2, -5)}

    >>> NarisiTocke().sestavi()
    {'z1': -1 + 2*I, 'z2': -4 + 4*I, 'z3': -2 - 2*I, 'z4': -4 + I, 'koordinatiz1': (-1, 2), 'koordinatiz2': (-4, 4), 'koordinatiz3': (-2, -2), 'koordinatiz4': (-4, 1)}
    """
    besedilo_posamezne = r'''V kompleksno ravnino nariši števila $z_1={{latex(naloga.z1)}}$, $z_2={{latex(naloga.z2)}}$, $z_3={{latex(naloga.z3)}}$ in $z_4={{latex(naloga.z4)}}$.'''

    besedilo_vecih = r'''V kompleksno ravnino nariši števila:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $z_1={{latex(naloga.z1)}}$, $z_2={{latex(naloga.z2)}}$, $z_3={{latex(naloga.z3)}}$ in $z_4={{latex(naloga.z4)}}$
        {% endfor %}
        \end{enumerate}
        '''
    resitev_posamezne = r'''$z_1={{latex(naloga.z1)}}$, $z_2={{latex(naloga.z2)}}$, $z_3={{latex(naloga.z3)}}$, $z_4={{latex(naloga.z4)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}
            [axis lines = center,
            xtick={-5,-4,...,5},
            ytick ={-5,...,5}, yticklabels={$-5i$, $-4i$, $-3i$, $-2i$, $-i$, $0$, $i$, $2i$, $3i$, $4i$, $5i$},
            xlabel=$Re(z)$,
            ylabel=$Im(z)$,
            ymin=-6, ymax=+6, xmin=-6,xmax=+6
            ]
            \node[label={0:{$z_1$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz1}} {};
            \node[label={0:{$z_2$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz2}} {};
            \node[label={0:{$z_3$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz3}} {};
            \node[label={0:{$z_4$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz4}} {};
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
        '''
    resitev_vecih = r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $z_1={{latex(naloga.z1)}}$, $z_2={{latex(naloga.z2)}}$, $z_3={{latex(naloga.z3)}}$, $z_4={{latex(naloga.z4)}}$\par
        \begin{minipage}{\linewidth}
        \centering
        \begin{tikzpicture}[baseline]
        \begin{axis}
            [axis lines = center,
            xtick={-5,-4,...,5},
            ytick ={-5,...,5}, yticklabels={$-5i$, $-4i$, $-3i$, $-2i$, $-i$, $0$, $i$, $2i$, $3i$, $4i$, $5i$},
            xlabel=$Re(z)$,
            ylabel=$Im(z)$,
            ymin=-6, ymax=+6, xmin=-6,xmax=+6
            ]
            \node[label={0:{$z_1$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz1}} {};
            \node[label={0:{$z_2$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz2}} {};
            \node[label={0:{$z_3$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz3}} {};
            \node[label={0:{$z_4$}},circle,fill,inner sep=2pt] at {{naloga.koordinatiz4}} {};
        \end{axis}
        \end{tikzpicture}
        \end{minipage}
         {% endfor %}
         \end{enumerate}
         '''

    def _poskusi_sestaviti(self):
        z1 = izberi_kompleksno_stevilo(-5, 5)
        z2 = izberi_kompleksno_stevilo(-5, 5)
        z3 = izberi_kompleksno_stevilo(-5, 5)
        z4 = izberi_kompleksno_stevilo(-5, 5)
        preveri(len({z1, z2, z3, z4}) == 4)
        koordinatiz1 = '(axis cs: {0}, {1})'.format(sympy.re(z1), sympy.im(z1))
        koordinatiz2 = '(axis cs: {0}, {1})'.format(sympy.re(z2), sympy.im(z2))
        koordinatiz3 = '(axis cs: {0}, {1})'.format(sympy.re(z3), sympy.im(z3))
        koordinatiz4 = '(axis cs: {0}, {1})'.format(sympy.re(z4), sympy.im(z4))
        return {'z1': z1, 'z2': z2, 'z3': z3, 'z4': z4, 'koordinatiz1': koordinatiz1, 'koordinatiz2': koordinatiz2,
                'koordinatiz3': koordinatiz3, 'koordinatiz4': koordinatiz4}


NarisiTocke().sestavi()
