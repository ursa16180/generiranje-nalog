from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random
import jinja2


class PotencaDvoclenika(Naloga):
    def __init__(self, min_potenca=2, max_potenca=3, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.besedilo_posamezne = jinja2.Template(r'''Potenciraj izraz ${{latex(naloga.izraz)}}$''')
        self.besedilo_vecih = jinja2.Template(r'''Potenciraj izraze:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.izraz)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.potenciran)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.potenciran)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        # TODO ali želim opozarjati na TypeError lazja=Bool, potence=int
        # if lazja not in {True, False}:
        #     raise TypeError('Vrednost "lazja" mora biti True ali False.')

        self.lazja = lazja
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca
        print(min_potenca,max_potenca)



    def poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        simboli = ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']
        izbranSimbol = random.choice(simboli)
        x = sympy.symbols(izbranSimbol)
        simboli.remove(izbranSimbol)
        if self.lazja:
            a = 1
            b = random.choice([x for x in range(-5, 5) if x != 0])
            n = 1
            y = 1
            m = 1
        else:
            a = random.randint(1, 5)
            b = random.choice([x for x in range(-5, 5) if x != 0])
            n = random.randint(2, 5)
            m = random.randint(1, 5)
            y = sympy.symbols(random.choice(simboli))

        izraz = sympy.Pow(a * x ** n + b * y ** m, potenca, evaluate=False)
        potenciran = izraz.expand()
        return {'izraz': izraz, 'potenciran': potenciran}



class PotencaTroclenika(Naloga):
    def __init__(self, min_potenca=2, max_potenca=2, **kwargs):
        super().__init__(self, **kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca


        self.besedilo_posamezne = jinja2.Template(r'''Potenciraj izraz ${{latex(naloga.izraz)}}$''')
        self.besedilo_vecih = jinja2.Template(r'''Potenciraj izraze:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.izraz)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.potenciran)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.potenciran)}}$
         {% endfor %}
         \end{enumerate}
         ''')


    def poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        simboli = [sympy.symbols(x) for x in ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']]
        (x, y, z) = random.sample(simboli, 3)
        a = random.randint(1, 4)
        b = random.choice([x for x in range(-4, 4) if x != 0])
        c = random.choice([x for x in range(-4, 4) if x != 0])

        izraz = sympy.Pow(a * x + b * y + c * z, potenca, evaluate=False)
        potenciran = izraz.expand()
        return {'izraz': izraz, 'potenciran': potenciran}


class RazstaviVieta(Naloga):
    def __init__(self, minimalna_vrednost=-9, maksimalna_vrednost=9, lazja=True,
                 **kwargs):  # TODO ali so te min maks vrednosti smiselne?
        super().__init__(self, **kwargs)
        if minimalna_vrednost>maksimalna_vrednost:
            raise MinMaxNapaka
        self.minimalna_vrednost = minimalna_vrednost
        self.maksimalna_vrednost = maksimalna_vrednost
        self.besedilo_posamezne = jinja2.Template('Razstavi izraz ${{latex(naloga.nerazstavljeno)}}$.')
        self.besedilo_vecih = jinja2.Template('Razstavi naslednje izraze '
                                              '\\begin{enumerate}'
                                              '{% for naloga in naloge %}'
                                              '\\item ${{latex(naloga.nerazstavljeno)}}=$'
                                              '{% endfor %}'
                                              '\\end{enumerate}'
                                              )
        self.resitev_posamezne = jinja2.Template('${{latex(naloga.razstavljeno)}}$')
        self.resitev_vecih = jinja2.Template('\\begin{enumerate}'
                                             '{% for naloga in naloge %}'
                                             '\\item ${{latex(naloga.razstavljeno)}}$'
                                             '{% endfor %}'
                                             '\\end{enumerate}')

        self.lazja = lazja

    def poskusi_sestaviti(self):
        x1 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        x2 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        if not self.lazja:
            a = random.randint(2, 4)
        else:
            a = 1
        x = sympy.symbols('x')
        razstavljeno = sympy.Mul(a, (x - x1), (x - x2), evaluate=False)
        nerazstavljeno = sympy.expand(razstavljeno)
        return {'razstavljeno': razstavljeno, 'nerazstavljeno': nerazstavljeno}


class RazstaviRazliko(Naloga):
    def __init__(self, min_potenca=2, max_potenca=3, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca
        self.besedilo_posamezne = jinja2.Template(r'''Razstavi izraz ${{latex(naloga.izraz)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Razstavi izraze:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item${{latex(naloga.izraz)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.razstavljen)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.razstavljen)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        if potenca == 2:
            do = 10
        else:
            do = 5
        simboli = ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']
        izbranSimbol = random.choice(simboli)
        x = sympy.symbols(izbranSimbol)
        simboli.remove(izbranSimbol)
        if self.lazja:
            a = 1
            b = random.choice([x for x in range(-do, do) if x != 0])
            y = 1
            m = 1
            n = 1
        else:
            a = random.randint(1, do)
            b = random.choice([x for x in range(-do, do) if x != 0])
            n = random.randint(1, 3)
            m = random.randint(1, 3)
            y = sympy.symbols(random.choice(simboli))
        izraz = (a * x ** n) ** potenca - (
                b * y ** m) ** potenca  # Todo kako preprečiti da so členi po abecedi? -4b**2+y**2
        razstavljen = sympy.factor(izraz)

        return {'izraz': izraz, 'razstavljen': razstavljen}


class RazstaviPotenco(Naloga):
    def __init__(self, min_potenca=2, max_potenca=3, min_clenov=2, max_clenov=2, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        if min_potenca > max_potenca:
            raise MinMaxNapaka
        self.min_potenca = min_potenca
        self.max_potenca = max_potenca
        if max_clenov > max_clenov:
            raise MinMaxNapaka
        self.max_clenov = max_clenov
        self.max_clenov = max_clenov
        if max_clenov not in {2,3} or min_clenov not in {2,3}:
            raise ValueError('Naloga razsatvi potenco ima za rešitev lahko samo dvočlenike ali tročlenike.')
        self.besedilo_posamezne = jinja2.Template(r'''Razstavi izraz ${{latex(naloga.izraz)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Razstavi izraze:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item${{latex(naloga.izraz)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{latex(naloga.razstavljen)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{latex(naloga.razstavljen)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.min_potenca = int(min(min_potenca, max_potenca))
        self.max_potenca = int(max(min_potenca, max_potenca))
        self.min_clenov = int(min(min_clenov, max_clenov))
        self.max_clenov = int(max(min_clenov, max_clenov))
        self.lazja = lazja

    def poskusi_sestaviti(self):
        potenca = random.randint(self.min_potenca, self.max_potenca)
        cleni = random.randint(self.min_clenov, self.max_clenov)
        simboli = [sympy.symbols(x) for x in ['a', 'b', 'c', 'x', 'y', 'z', 'v', 't']]
        (x, y, z) = random.sample(simboli, 3)
        if potenca == 2:
            do = 10
        else:
            do = 5

        if cleni == 2:
            z = 0

        if self.lazja:
            a = 1
            b = random.choice([x for x in range(-do, do) if x != 0])
            c = random.choice([x for x in range(-do, do) if x != 0])
            y = 1
            m = 1
            n = 1
            o = 1
        else:
            a = random.randint(1, do)
            b = random.choice([x for x in range(-do, do) if x != 0])
            c = random.choice([x for x in range(-do, do) if x != 0])
            n = random.randint(1, 3)
            m = random.randint(1, 3)
            o = random.randint(1, 3)

        razstavljen = sympy.Pow((a * x ** n) + (b * y ** m) + (c * z ** o), potenca, evaluate=False)
        izraz = sympy.expand(razstavljen)

        return {'izraz': izraz, 'razstavljen': razstavljen}
