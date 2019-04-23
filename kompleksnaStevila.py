from generiranje import Naloga, preveri
import random
import sympy
import jinja2


def izberiKompleksnoStevilo(od=-5, do=5):
    a = random.choice([x for x in range(od, do + 1) if x != 0])
    b = random.choice([x for x in range(od, do + 1) if x != 0])
    return a + b * sympy.I


# ~~~~~Naloge iz sklopa kompleksnih števil
class VsotaRazlika(Naloga):
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

    def poskusi_sestaviti(self):
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
        z1 = izberiKompleksnoStevilo()
        z2 = izberiKompleksnoStevilo()
        z3 = izberiKompleksnoStevilo()
        preveri(z1 != z2 and z1 != z3 and z2 != z3)
        racun = sympy.Add(sympy.Mul(a, z1, evaluate=False), sympy.Mul(b, z2, evaluate=False),
                          sympy.Mul(c, z3, evaluate=False), evaluate=False)
        rezultat = a * z1 + b * z2 + c * z3
        return {'racun': racun, 'rezultat': rezultat}


class Ulomek(Naloga):
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(**kwargs)
        self.lazja = lazja

    def poskusi_sestaviti(self):
        izbor = list(range(1, 6)) + [x * sympy.I for x in range(-5, 6) if
                                     x != 0]  # TODO dodaj odštevanje ulomkov- če izbere celo negativno število, se račun poenostavi
        if self.lazja:
            a = random.choice(izbor)
            b = random.choice(izbor)
        else:
            a = izberiKompleksnoStevilo(-3, 3)
            b = izberiKompleksnoStevilo(-3, 3)

        z1 = izberiKompleksnoStevilo(-3, 3)
        z2 = izberiKompleksnoStevilo(-3, 3)
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

    def poskusi_sestaviti(self):
        z1 = izberiKompleksnoStevilo()
        z2 = izberiKompleksnoStevilo()
        racun = sympy.Mul(z1, z2, evaluate=False)
        rezultat = sympy.simplify(z1 * z2)
        return {'racun': racun, 'rezultat': rezultat}


class Racunanje(Naloga):
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

    def poskusi_sestaviti(self):
        z = sympy.symbols('z')
        z0 = izberiKompleksnoStevilo()
        racun = sympy.Pow(z, random.randint(2, 3)) + sympy.Mul(
            sympy.Pow(sympy.I, random.randint(1991, 2018), evaluate=False), sympy.conjugate(z), evaluate=False) + abs(
            z) ** 2
        rezultat = sympy.simplify(racun.subs(z, z0))
        return {'stevilo': z0, 'racun': racun, 'rezultat': rezultat}


class Enacba(Naloga):
    besedilo_posamezne = r'''Katero kompleksno število $z$ zadošča enačbi ${{latex(naloga.enacba)}}$? Zapiši $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunaj $\left| z \right|$.'''
    besedilo_vecih = r'''Izračunaj katero število $z$ reši enačbo in zapiši še $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunajte $\left| z \right|$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $z={{latex(naloga.enacba)}}$
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

    def __init__(self, lazja, **kwargs):
        super().__init__(**kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        z = sympy.symbols('z')
        z1 = izberiKompleksnoStevilo()
        resitev = izberiKompleksnoStevilo()
        if self.lazja:
            enacba = z1 * z

        else:
            z2 = izberiKompleksnoStevilo()
            enacba = z1 * z + z2 * sympy.conjugate(z)
        z3 = sympy.simplify(enacba.subs(z, resitev))
        im = sympy.im(resitev)
        re = sympy.re(resitev)
        absolutna = abs(resitev)

        return {'enacba': sympy.Eq(enacba, z3), 'resitev': resitev, 'imaginarna': im, 'realna': re,
                'absolutna': absolutna}


class NarisiTocke(Naloga):
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

    def poskusi_sestaviti(self):
        z1 = izberiKompleksnoStevilo(-5, 5)
        z2 = izberiKompleksnoStevilo(-5, 5)
        z3 = izberiKompleksnoStevilo(-5, 5)
        z4 = izberiKompleksnoStevilo(-5, 5)
        preveri(len({z1, z2, z3, z4}) == 4)
        koordinatiz1 = (sympy.re(z1), sympy.im(z1))
        koordinatiz2 = (sympy.re(z2), sympy.im(z2))
        koordinatiz3 = (sympy.re(z3), sympy.im(z3))
        koordinatiz4 = (sympy.re(z4), sympy.im(z4))
        return {'z1': z1, 'z2': z2, 'z3': z3, 'z4': z4, 'koordinatiz1': koordinatiz1, 'koordinatiz2': koordinatiz2,
                'koordinatiz3': koordinatiz3, 'koordinatiz4': koordinatiz4}
