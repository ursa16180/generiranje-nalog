from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random
import jinja2


def vsotaAritmeticnega(a1, d, n):
    sn = sympy.Rational(n * (2 * a1 + (n - 1) * d), 2)
    return sn


def vsotaGeometrijskega(a1, q, n):
    sn = sympy.Mul(a1,q ** n - 1,sympy.Pow(q - 1,-1))
    #sn = sympy.Rational(a1 * (q ** n - 1), (q - 1))
    return sn


def vsotaGeometrijskeVrste(a1, q):
    if abs(q) < 1:
        s=sympy.Mul(a1,sympy.Pow(1-q,-1))
        return s
    else:
        raise ValueError('Zaporedje ni konvergentno.')


def clenAritmeticnega(a1, d, n):
    an = a1 + (n - 1) * d
    return an


def clenGeometrijskega(a1, q, n):
    # an = sympy.Mul(a1,sympy.Pow(q,(n-1)))
    an = a1 * q ** (n - 1)
    return an


# ~~~~~Naloge iz sklopa zaporedja

class SplosniClenZaporedja(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Poišči predpis za splošni člen, ki mu zadoščajo začetni členi zaporedja {% for clen in naloga.cleni %}${{latex(clen)}}$, {% endfor %}...''')
        self.besedilo_vecih = jinja2.Template(r'''Poišči predpis za splošni člen, ki mu zadoščajo začetni členi zaporedja:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item {% for clen in naloga.cleni %}${{latex(clen)}}$, {% endfor %}...
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$a_n={{latex(naloga.splosni)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $a_n={{latex(naloga.splosni)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        n = sympy.symbols('n')
        a = random.choice([x for x in range(-5, 5) if x != 0])
        b = random.choice([x for x in range(-3, 3) if x != 0])
        c = random.choice([x for x in range(1, 3) if x != 0])
        d = random.choice([x for x in range(1, 3) if x != 0])
        predpisi = [a + (n - 1) * b, a * b * (n - 1),
                    sympy.Mul((a + b * (n - 1)), sympy.Pow(c + d * (n - 1), -1, evaluate=False), evaluate=False),
                    n ** 2, n ** 3]
        if not self.lazja:
            predpisi += [n ** 2 - a, n ** 3 - a,
                         (-1) ** n * a * b ** (n - 1)]  # , a+sum(range(2,n+1)) #TODO kako podati predpis za rekurzivne
        predpis = random.choice(predpisi)
        cleni = []
        for x in range(1, 6):
            cleni.append(predpis.subs(n, x))
        return {'cleni': cleni, 'splosni': predpis}


# ~~~~~Naloge iz sklopa artimetično zaporedje
class PrviCleniAritmeticnega(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1={{latex(naloga.a1)}}$
             in diferenco $d={{latex(naloga.d)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1$ in diferenco $d$:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $a_1={{latex(naloga.a1)}}$, $d={{latex(naloga.d)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(
            r'''{% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item {% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        if self.lazja:
            a1 = random.choice([x for x in range(-12, 12) if x != 0])
            d = random.choice([x for x in range(-5, 5) if x != 0])
        else:
            a1 = [sympy.Rational(1, x) for x in range(-6, 6) if x != 0] + [sympy.Rational(2, x) for x in range(-6, 6) if
                                                                           x != 0]
            d = [sympy.Rational(1, x) for x in range(-6, 6) if x != 0]
        cleni = [a1]
        for N in range(2, 6):
            cleni.append(clenAritmeticnega(a1, d, N))
        n = sympy.symbols('n')
        splosni = sympy.Add(a1, sympy.Mul(d, (n - 1), evaluate=False), evaluate=False)
        return {'cleni': cleni, 'a1': a1, 'd': d, 'splosni': splosni}


class SplosniClenAritmeticnegaZaporedja(Naloga):
    def __init__(self, od=-5, do=5, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Določi splošni člen aritmetičnega zaporedja, če je $a_{ {{latex(naloga.n1)}} }={{latex(naloga.an1)}}$ in $a_{ {{latex(naloga.n2)}} }={{latex(naloga.an2)}}$.''')
        self.besedilo_vecih = jinja2.Template(
            r'''Določi splošne člene aritmetičnih zaporedij, če poznaš naslednja dva člena:
            \begin{enumerate}
            {% for naloga in naloge %}
            \item $a_{ {{latex(naloga.n1)}} }={{latex(naloga.an1)}}$, $a_{ {{latex(naloga.n2)}} }={{latex(naloga.an2)}}$
            {% endfor %}
            \end{enumerate}''')
        self.resitev_posamezne = jinja2.Template(r'''$a_n={{latex(naloga.a1)}}+{{latex(naloga.d)}}(n-1)$''')
        self.resitev_vecih = jinja2.Template(
            r'''\begin{enumerate}
            {% for naloga in naloge %}
            \item $a_n={{latex(naloga.a1)}}+{{latex(naloga.d)}}(n-1)$
            {% endfor %}
            \end{enumerate}''')
        if od > od:  # TODO ali od, do smiselna?
            raise MinMaxNapaka
        self.od = od
        self.do = do

    def poskusi_sestaviti(self):
        seznam_polovick = [sympy.Rational(x, 2) for x in range(2 * self.od, 2 * self.do + 1) if x != 0]
        a1 = random.choice(seznam_polovick)
        d = random.choice(seznam_polovick)
        nn1 = random.randint(2, 10)
        nn2 = random.randint(2, 15)
        preveri(nn1 != nn2)
        n1 = min(nn1, nn2)  # Zato da sta pri izpisu urejena po velikosti
        n2 = max(nn1, nn2)
        an1 = clenAritmeticnega(a1, d, n1)
        an2 = clenAritmeticnega(a1, d, n2)
        return {'n1': n1, 'an1': an1, 'n2': n2, 'an2': an2, 'a1': a1, 'd': d}


class SplosniClenAritmeticnegaEnacbi(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Določi prvi člen in diferenco artimetičnega zaporedja, pri katerem je 
            $a_{ {{naloga.n1}} }+a_{ {{naloga.n2}} }={{latex(naloga.vrednost1)}}$ in 
            $a_{ {{naloga.n3}} } {{latex(naloga.operator)}} a_{ {{naloga.n4}} }={{latex(naloga.vrednost2)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Določi prvi člen in diferenco artimetičnega zaporedja, pri katerem je
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $a_{ {{naloga.n1}} }+a_{ {{naloga.n2}} }={{latex(naloga.vrednost1)}}$, 
            $a_{ {{naloga.n3}} } {{latex(naloga.operator)}} a_{ {{naloga.n4}} }={{latex(naloga.vrednost2)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$a_1={{naloga.a1}}$, $d={{naloga.d}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $a_1={{naloga.a1}}$, $d={{naloga.d}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        a1 = random.choice([x for x in range(-8, 8) if x != 0] + [-sympy.Rational(1, 2), sympy.Rational(1, 2)])
        d = random.choice([x for x in range(-3, 3) if x != 0] + [-sympy.Rational(1, 2), sympy.Rational(1, 2)])
        [n1, n2, n3, n4] = random.sample(list(range(2, 20)), 4)
        vrednost1 = clenAritmeticnega(a1, d, n1) + clenAritmeticnega(a1, d, n2)
        operatorji = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '\cdot': lambda a, b: a * b}

        operator = random.choice(list(operatorji.keys()))
        vrednost2 = operatorji[operator](clenAritmeticnega(a1, d, n3), clenAritmeticnega(a1, d, n4))

        return {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'operator': operator, 'vrednost1': vrednost1,
                'vrednost2': vrednost2, 'a1': a1, 'd': d}


class VsotaAritmeticnega(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Izračunaj vsoto prvih ${{naloga.n}}$ členov aritmetičnega zaporedja, če je {{naloga.izraz}}.''')
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj vsoto prvih n členov aritmetičnega zaporedja, če je:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item {{naloga.izraz}}, $n={{naloga.n}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$s_{ {{naloga.n}} }={{naloga.vsota}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $s_{ {{naloga.n}} }={{naloga.vsota}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        N = random.randint(10, 30)
        n = sympy.symbols('n')
        a1 = random.choice([x for x in range(-8, 8) if x != 0])
        d = random.choice([x for x in range(-5, 5) if x != 0 and x != 1])
        if self.lazja:
            izraz = '$a_n=' + sympy.latex(sympy.Add(a1, sympy.Mul(d, (n - 1), evaluate=False), evaluate=False)) + '$'
        else:
            [n1, n2] = sorted(random.sample(list(range(1, 21)), 2))
            preveri(N not in {n1, n2})
            izraz = '$s_{{{0}}}={1}$ in $s_{{{2}}}={3}$'.format(n1, vsotaAritmeticnega(a1, d, n1), n2,
                                                                vsotaAritmeticnega(a1, d,
                                                                                   n2))  # TODO elegantnejša rešitev?
        vsota = vsotaAritmeticnega(a1, d, N)
        return {'izraz': izraz, 'n': N, 'vsota': vsota}


# ~~~~~Naloge iz sklopa geometrijsko zaporedje
class PrviCleniGeometrijskega(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Zapiši prvih pet členov in splošni člen geometrijskega zaporedja s prvim členom $a_1={{latex(naloga.a1)}}$
             in količnikom $q={{latex(naloga.q)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Zapiši prvih pet členov in splošni člen geometrijskega zaporedja s prvim členom $a_1$ in količnikom $q$:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $a_1={{latex(naloga.a1)}}$, $d={{latex(naloga.q)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(
            r'''{% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item {% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        if self.lazja:
            a1 = random.choice([x for x in range(-10, 10) if x != 0])
            q = random.choice([-3, -2, 2, 3])
        else:
            a1 = [sympy.Rational(1, x) for x in range(-6, 6) if x != 0] + [sympy.Rational(2, x) for x in range(-6, 6) if
                                                                           x != 0]
            q = [sympy.Rational(1, x) for x in [-3, -2, 2, 3]]
        cleni = [a1]
        for N in range(2, 6):
            cleni.append(clenGeometrijskega(a1, q, N))
        n = sympy.symbols('n')
        splosni = sympy.Mul(a1, sympy.Pow(q, (n - 1), evaluate=False), evaluate=False)
        return {'cleni': cleni, 'a1': a1, 'q': q, 'splosni': splosni}


class SplosniClenGeometrijskega(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Določi splošni člen geometrijskega zaporedja, če je ${{naloga.podatek1}}$ in ${{latex(naloga.podatek2)}}$.''')
        self.besedilo_vecih = jinja2.Template(
            r'''Določi splošne člene geometrijskih zaporedij, če je:
            \begin{enumerate}
            {% for naloga in naloge %}
            \item ${{naloga.podatek1}}$ in ${{latex(naloga.podatek2)}}$
            {% endfor %}
            \end{enumerate}''')
        self.resitev_posamezne = jinja2.Template(r'''$a_n={{latex(naloga.splosni)}}$''')
        self.resitev_vecih = jinja2.Template(
            r'''\begin{enumerate}
            {% for naloga in naloge %}
            \item $a_n={{latex(naloga.splosni)}}$
            {% endfor %}
            \end{enumerate}''')

    def poskusi_sestaviti(self):
        a1 = random.choice([x for x in range(-10, 10) if x != 0])
        q = random.choice([-3, -2, 2, 3] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        n1 = random.choice(list(range(3,16,2))) #en lih in en sod da v enačbi ni +/- q
        n2 = random.choice(list(range(2,16,2)))
        #preveri(n1 != n2) #Nepotrebno ker je en lih in en sod
        an1 = clenGeometrijskega(a1, q, n1)
        an2 = clenGeometrijskega(a1, q, n2)
        [podatek1, podatek2] = random.sample(
            ['a_{{{0}}}={1}'.format(n1, an1), 'a_{{{0}}}={1}'.format(n2, an2), 'q={}'.format(q)],
            2)  # TODO elegantnejši način za izpis?
        n = sympy.symbols('n')
        splosni = sympy.Mul(a1, sympy.Pow(q, (n - 1), evaluate=False), evaluate=False)  # TODO preprči (1/3)**n=3**(-n)

        return {'podatek1': podatek1, 'podatek2': podatek2, 'splosni': splosni}


class SplosniClenGeometrijskegaEnacbi(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Določi prvi člen in količnik geometrijskega zaporedja, pri katerem je 
            $a_{ {{naloga.n1}} }={{latex(naloga.vrednost1)}}$ in 
            $a_{ {{naloga.n2}} } {{latex(naloga.operator)}} a_{ {{naloga.n3}} }={{latex(naloga.vrednost2)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Določi prvi člen in količnik geometrijskega zaporedja, pri katerem je
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $a_{ {{naloga.n1}} }={{latex(naloga.vrednost1)}}$, 
        $a_{ {{naloga.n2}} } {{latex(naloga.operator)}} a_{ {{naloga.n3}} }={{latex(naloga.vrednost2)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$a_1={{latex(naloga.a1)}}$, $q={{latex(naloga.q)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $a_1={{latex(naloga.a1)}}$, $q={{latex(naloga.q)}}$
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        a1 = random.choice([x for x in range(-5, 5) if x != 0] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        q = random.choice([x for x in [-3, -2, 2, 3]] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])

        operatorji = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '\cdot': lambda a, b: a * b}

        operator = random.choice(list(operatorji.keys()))
        if operator in ['+', '-']:
            k = random.randint(2, 8)
            seznam = [k, k + 1, k + 2]
            random.shuffle(seznam)
            [n1, n2,
             n3] = seznam  # želimo da so 3 zaporedna števila, drugače dobimo polinomsko enačbo kar je preveč računanja
        else:
            [n1, n2, n3] = random.sample(list(range(1, 8)), 3)
        vrednost1 = clenGeometrijskega(a1, q, n1)
        vrednost2 = operatorji[operator](clenGeometrijskega(a1, q, n2), clenGeometrijskega(a1, q, n3))

        return {'n1': n1, 'n2': n2, 'n3': n3, 'operator': operator, 'vrednost1': vrednost1,
                'vrednost2': vrednost2, 'a1': a1, 'q': q}


class VsotaGeometrijskega(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Izračunaj vsoto prvih ${{naloga.n}}$ členov geometrijskega zaporedja, če je {{naloga.izraz}}.''')
        self.besedilo_vecih = jinja2.Template(r'''Izračunaj vsoto prvih n členov geometrijskega zaporedja, če je:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item {{naloga.izraz}}, $n={{naloga.n}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''$s_{ {{naloga.n}} }={{latex(naloga.vsota)}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item $s_{ {{naloga.n}} }={{latex(naloga.vsota)}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        N = random.randint(4, 10)
        n = sympy.symbols('n')
        a1 = random.choice([x for x in range(-5, 5) if x != 0] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        q = random.choice([x for x in [-3, -2, 2, 3]] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        if self.lazja:
            izraz = '$a_n=' + sympy.latex(sympy.Mul(a1, sympy.Pow(q, (n - 1), evaluate=False), evaluate=False)) + '$'
        else:
            [n1, n2] = sorted(random.sample(list(range(2, 8)), 2))
            # TODO elegantnejša rešitev?
            izraz = '$a_{{{0}}}={1}$ in $a_{{{2}}}={3}$'.format(n1, clenGeometrijskega(a1, q, n1),
                                                                n2, clenGeometrijskega(a1, q, n2))
        vsota = vsotaGeometrijskega(a1, q, N)
        return {'izraz': izraz, 'n': N, 'vsota': vsota}


class VsotaGeometrijskeVrste(Naloga):
    def __init__(self, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Zapiši geometrijsko vrsto, če je ${{latex(naloga.podatek1)}}={{latex(naloga.vrednost1)}}$ in
             ${{latex(naloga.podatek2)}}={{latex(naloga.vrednost2)}}$.''')
        self.besedilo_vecih = jinja2.Template(r'''Zapiši geometrijsko vrsto z danima podatkoma
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{latex(naloga.podatek1)}}={{latex(naloga.vrednost1)}}$,
             ${{latex(naloga.podatek2)}}={{latex(naloga.vrednost2)}}$
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r'''${{naloga.vrsta}}$''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item ${{naloga.vrsta}}$
         {% endfor %}
         \end{enumerate}
         ''')
        self.lazja = lazja

    def poskusi_sestaviti(self):
        q = random.choice([-sympy.Rational(1, 2), sympy.Rational(1, 2),
                           -sympy.Rational(2, 3), -sympy.Rational(1, 3), sympy.Rational(2, 3), sympy.Rational(1, 3),
                           -sympy.Rational(3, 4), -sympy.Rational(1, 4), sympy.Rational(3, 4), sympy.Rational(1, 4),
                           -sympy.Rational(2, 5), -sympy.Rational(1, 5), sympy.Rational(2, 5), sympy.Rational(1, 5),
                           -sympy.Mul(sympy.sqrt(2), sympy.Pow(2,-1),evaluate=False), sympy.Mul(sympy.sqrt(2), sympy.Pow(2,-1),evaluate=False),
                           -sympy.Mul(sympy.sqrt(2), sympy.Pow(3,-1),evaluate=False), sympy.Mul(sympy.sqrt(2), sympy.Pow(3,-1),evaluate=False)])
        a1 = random.choice([x for x in range(-10, 11) if x != 0])
        s = vsotaGeometrijskeVrste(a1, q)
        izbor = [('a_1', a1), ('q', q), ('s', s)]
        if not self.lazja:
            n1 = random.randint(3, 5)
            an = clenGeometrijskega(a1, q, n1)
            n2 = random.randint(3, 5)
            sn = vsotaGeometrijskega(a1, q, n2)
            izbor += [('a_{}'.format(n1), an), ('s_{}'.format(n2), sn)]
        [izraz1, izraz2] = random.sample(izbor, 2)
        vrsta = '+'.join('{}'.format(sympy.latex(clenGeometrijskega(a1,q,n))) for n in range(1, 5)) + '+...'
        return {'podatek1': izraz1[0], 'vrednost1': izraz1[1], 'podatek2': izraz2[0], 'vrednost2': izraz2[1],
                'vrsta': vrsta}
