from generiranje import Naloga, preveri
import sympy
import random
import linearnaFunkcija
import jinja2


def kotMedPremicama(k1, k2):
    # Funkcija v radianih izračuna kot med premicama
    if k1 * k2 == -1:
        kot = sympy.pi / 2
    else:
        kot = sympy.atan(abs((k2 - k1) / (1 + k1 * k2)))
    return kot


# ~~~~~ Naloge iz sklopa odvodi
class KotMedPremicama(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        # if min_potenca > max_potenca:
        #     raise MinMaxNapaka
        self.besedilo_posamezne = jinja2.Template(
            r'''Izračunaj kot, ki ga oklepata $y={{latex(naloga.premica1)}}$ in {{naloga.premica2}}.''')
        # TODO kako različna navodila za lažjo in težjo? Je potrebno ali pustim tako kot je?
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj kot, ki ga oklepata:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $y={{latex(naloga.premica1)}}$ in {{naloga.premica2}}
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$\varphi ={{naloga.stopinje}}\degree{{naloga.minute}}' $''')

        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $\varphi ={{naloga.stopinje}}\degree{{naloga.minute}}' $
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x = sympy.symbols('x')
        y = sympy.symbols('y')
        k1, k2 = random.sample([x for x in range(-6, 7) if x != 0], 2)
        n1, n2 = random.sample([x for x in range(-10, 11) if x != 0], 2)
        premica1 = k1 * x + n1
        if self.lazja:
            premica2 = 'abscisa os'
            k2 = 0
        else:
            premica2 = '$' + sympy.latex(sympy.Eq(y, k2 * x + n2)) + '$'

        kot = sympy.N(sympy.deg(kotMedPremicama(k1, k2)))
        stop = kot // 1
        min = round(kot % 1 * 60) #Todo če ni minut
        return {'premica1': premica1, 'premica2': premica2, 'stopinje': stop, 'minute': min}
