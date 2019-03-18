from generiranje import *

def izberiKompleksnoStevilo(od=-5,do=5):
    a = random.choice([x for x in range(od,do+1) if x!=0])
    b = random.choice([x for x in range(od,do+1) if x!=0])
    return a+b*sympy.I

# ~~~~~Naloge iz sklopa kompleksnih števil
class VsotaRazlika(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''Izračunaj ${{latex(naloga.racun)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.racun)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.rezultat)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.rezultat)}}$
         {% endfor %}
         \end{enumerate}
         ''')

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
        z1=izberiKompleksnoStevilo()
        z2=izberiKompleksnoStevilo()
        z3=izberiKompleksnoStevilo()
        preveri(z1!=z2 and z1!=z3 and z2!=z3)
        racun = sympy.Add(sympy.Mul(a,z1,evaluate=False),sympy.Mul(b,z2,evaluate=False),sympy.Mul(c,z3,evaluate=False), evaluate=False)
        rezultat = a*z1+b*z2+c*z3
        return {'racun':racun, 'rezultat': rezultat}

class Ulomek(Naloga):
    def __init__(self, lazje=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''Izračunaj ${{latex(naloga.racun)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.racun)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.rezultat)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.rezultat)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazje = lazje

    def poskusi_sestaviti(self):
        izbor = [x for x in range(-5,6) if x!=0] +[x*sympy.I for x in range(-5,6) if x!=0]
        if self.lazje:
            a = random.choice(izbor)
            b = random.choice(izbor)
        else:
            a = izberiKompleksnoStevilo(-3,3)
            b = izberiKompleksnoStevilo(-3,3)

        z1=izberiKompleksnoStevilo(-3,3)
        z2=izberiKompleksnoStevilo(-3,3)
        preveri(a!=z1 and b!=z2 and z1!=z2)

        racun = '\\frac{{{0}}}{{{1}}} +\\frac{{{2}}}{{{3}}}'.format(a,z1,b,z2) #TODO kako avomatično zapisati neporačunan ulomek
        rezultat = sympy.simplify(a/z1+b/z2)
        return {'racun':racun, 'rezultat': rezultat}

class Mnozenje(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r'''Izračunaj ${{latex(naloga.racun)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.racun)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.rezultat)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.rezultat)}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        z1=izberiKompleksnoStevilo()
        z2=izberiKompleksnoStevilo()
        racun = sympy.simplify(sympy.Mul(z1,z2, evaluate=False))
        rezultat = sympy.simplify(z1*z2)
        return {'racun':racun, 'rezultat': rezultat}
#
# class Racunanje(Naloga): #TODO ne dela izpis
#     def __init__(self, **kwargs):
#         super().__init__(self, **kwargs)
#         self.besedilo_posamezne = jinja2.Template(r'''Dano je kompleksno število $z={{latex(naloga.stevilo)}}$. Izračunaj število $w={{latex(naloga.racun)}}$.''')
#         self.besedilo_vecih = jinja2.Template(r''' Za dano kompleksno število $z$ izračunaj število $w={{latex(naloga.racun)}}$:
#         \begin{enumerate}
#         {% for naloga in naloge %}
#         \item $w={{latex(naloga.rezultat)}}$
#         {% endfor %}
#         \end{enumerate}
#         ''')
#         self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.stevilo)}}$''')
#         self.resitev_vecih = jinja2.Template(r'''
#         \begin{enumerate}
#          {% for naloga in naloge %}
#          \item $w={{latex(naloga.rezultat)}}$
#          {% endfor %}
#          \end{enumerate}
#          ''')
#
#     def poskusi_sestaviti(self):
#         z=sympy.symbols('z')
#         z0=izberiKompleksnoStevilo()
#         racun = sympy.I*z+z**2+sympy.Rational(1,2)*abs(z)**2
#         rezultat = sympy.simplify(racun.subs(z,z0))
#
#         return {'stevilo':z0,'racun':racun, 'rezultat':rezultat}