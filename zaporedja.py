from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random


def vsota_aritmeticnega(a1, d, n):
    """
    Izračuna vsoto prvih n členov aritmetičnega zaporedja.

    :param a1: prvi člen aritmetičnega zaporedja
    :param d: diferenca aritmetičnega zaporedja
    :param n: število členov
    :return: vsoto prvih n členov

    >>> vsota_aritmeticnega(3, 1/3, 15)
    80

    >>> vsota_aritmeticnega(15, -3, 20)
    -270
    """
    sn = sympy.Rational(n * (2 * a1 + (n - 1) * d), 2)
    return sn


def vsota_geometrijskega(a1, q, n):
    """
    Izračuna vsoto prvih n členov geometrijskega zaporedja.

    :param a1: prvi člen geometrijskega zaporedja
    :param q: kvocient geometrijskega zaporedja
    :param n: število členov
    :return: vsoto prvih n členov


    >>> vsota_geometrijskega(-16, 1/2, 10)
    -31.9687500000000

    >>> vsota_geometrijskega(2, 3, 18)
    387420488
    """
    sn = sympy.Mul(a1, q ** n - 1, sympy.Pow(q - 1, -1))
    # sn = sympy.Rational(a1 * (q ** n - 1), (q - 1))
    return sn


def vsota_geometrijske_vrste(a1, q):
    """
    Izračuna vsoto geometrijske vrste ali opozori če zaporedje ni konvergentno.

    :param a1: prvi člen geometrijskega zaporedja
    :param q: kvocient geometrijskega zaporedja
    :return: vsoto geometrijske vrste


    >>> vsota_geometrijske_vrste(8, -1/2)
    5.33333333333333

    >>> vsota_geometrijske_vrste(1, 1/5)
    1.25000000000000
    """
    if abs(q) < 1:
        s = sympy.Mul(a1, sympy.Pow(1 - q, -1))
        return s
    else:
        raise ValueError('Zaporedje ni konvergentno.')


def clen_aritmeticnega(a1, d, n):
    """
    Izračuna n-ti člen aritmetičnega zaporedja.

    :param a1: prvi člen aritmetičnega zaporedja
    :param d: diferenca aritmetičnega zaporedja
    :param n: zaporedni člen #TODO Ni člen ampak index člena?
    :return: n-ti člen aritmetičnega zaporedja


    >>> clen_aritmeticnega(1/2, 5, 17)
    80.5

    >>> clen_aritmeticnega(-10, 2, 50)
    88
    """
    an = a1 + (n - 1) * d
    return an


def clen_geometrijskega(a1, q, n):
    """
    Izračuna n-ti člen geometrijskega zaporedja.

    :param a1: prvi člen geometrijskega zaporedja
    :param q: kvocient geometrijskega zaporedja
    :param n: zaporedni člen#TODO Ni člen ampak index člena?
    :return: n-ti člen geometrijskega zaporedja

    >>> clen_geometrijskega(3, 2, 5)
    48

    >>> clen_geometrijskega(-4, 1/2, 3)
    -1.0
    """
    # an = sympy.Mul(a1,sympy.Pow(q,(n-1)))
    an = a1 * q ** (n - 1)
    return an


# ~~~~~Naloge iz sklopa zaporedja

class SplosniClenZaporedja(Naloga):
    """
    Naloga za iskanje splošnega člena poljubnega zaporedja.

    :param zamik_alternirajoce: določa, če so v izbor predpisa vljučena zamaknjena zaporedja iz kvadratov in  kubov ter alternirajoča zaporedja


    >>> SplosniClenZaporedja().sestavi()
    {'cleni': [1, 3, 5, 7, 9], 'splosni': 2*n - 1}

    >>> SplosniClenZaporedja(zamik_alternirajoce=True).sestavi()
    {'cleni': [0, 7, 26, 63, 124], 'splosni': n**3 - 1}

    """
    besedilo_posamezne = r'''Poišči predpis za splošni člen, ki mu zadoščajo začetni členi zaporedja {% for clen in naloga.cleni %}${{latex(clen)}}$, {% endfor %}...'''
    besedilo_vecih = r'''Poišči predpis za splošni člen, ki mu zadoščajo začetni členi zaporedja:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item {% for clen in naloga.cleni %}${{latex(clen)}}$, {% endfor %}...
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$a_n={{latex(naloga.splosni)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $a_n={{latex(naloga.splosni)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, zamik_alternirajoce=False, **kwargs):
        super().__init__(**kwargs)
        self.zamik_alternirajoce = zamik_alternirajoce

    def _poskusi_sestaviti(self):
        n = sympy.symbols('n')
        a = random.choice([x for x in range(-5, 5) if x != 0])
        b = random.choice([x for x in range(-3, 3) if x != 0])
        c = random.choice([x for x in range(1, 3) if x != 0])
        d = random.choice([x for x in range(1, 3) if x != 0])
        predpisi = [a + (n - 1) * b, a * b ** (n - 1),
                    sympy.Mul((a + b * (n - 1)), sympy.Pow(c + d * (n - 1), -1, evaluate=False), evaluate=False),
                    n ** 2, n ** 3]
        if self.zamik_alternirajoce:
            predpisi += [n ** 2 - a, n ** 3 - a,
                         (-1) ** n * a * b ** (n - 1)]  # , a+sum(range(2,n+1)) #TODO kako podati predpis za rekurzivne
        predpis = random.choice(predpisi)
        cleni = []
        for x in range(1, 6):
            cleni.append(predpis.subs(n, x))
        return {'cleni': cleni, 'splosni': predpis}


# ~~~~~Naloge iz sklopa artimetično zaporedje
class PrviCleniAritmeticnega(Naloga):
    """
    Naloga za zapis splošnega člena aritmetičnega zaporedja in računanje prvih petih členov, če poznaš prvi člen in diferenco.

    :param racionalne_vrednosti: prvi člen in diferenca zaporedja sta lahko racionalni vrednosti


    >>> PrviCleniAritmeticnega().sestavi()
    {'cleni': [-9, -5, -1, 3, 7], 'a1': -9, 'd': 4, 'splosni': 4*(n - 1) - 9}

    >>> PrviCleniAritmeticnega(racionalne_vrednosti=True).sestavi()
    {'cleni': [1/4, -1/12, -5/12, -3/4, -13/12], 'a1': 1/4, 'd': -1/3, 'splosni': 1/4 - (n - 1)/3}
    """
    besedilo_posamezne = r'''Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1={{latex(naloga.a1)}}$
         in diferenco $d={{latex(naloga.d)}}$.'''
    besedilo_vecih = r'''Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1$ in diferenco $d$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $a_1={{latex(naloga.a1)}}$, $d={{latex(naloga.d)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''{% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item {% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, racionalne_vrednosti=False, **kwargs):
        super().__init__(**kwargs)
        self.racionalne_vrednosti = racionalne_vrednosti

    def _poskusi_sestaviti(self):
        if not self.racionalne_vrednosti:
            a1 = random.choice([x for x in range(-12, 12) if x != 0])
            d = random.choice([x for x in range(-5, 5) if x != 0])
        else:
            a1 = random.choice(
                [sympy.Rational(1, x) for x in range(-6, 6) if x != 0] + [sympy.Rational(2, x) for x in range(-6, 6) if
                                                                          x != 0])
            d = random.choice([sympy.Rational(1, x) for x in range(-6, 6) if x != 0])
        cleni = [a1]
        for N in range(2, 6):
            cleni.append(clen_aritmeticnega(a1, d, N))
        n = sympy.symbols('n')

        splosni = sympy.Add(a1, sympy.Mul(d, (n - 1), evaluate=False), evaluate=False)
        return {'cleni': cleni, 'a1': a1, 'd': d, 'splosni': splosni}


class SplosniClenAritmeticnegaZaporedja(Naloga):
    """
    Naloga za zapis splošnega člena aritmetičnega zaporedja, če poznaš dva člena zaporedja.

    :param od: najmanjša možna vrednost za prvi člen in diferenco
    :param do: največja možna vrednost za prvi člen in diferenco


    >>> SplosniClenAritmeticnegaZaporedja().sestavi()
    {'n1': 5, 'an1': 23/2, 'n2': 9, 'an2': 47/2, 'a1': -1/2, 'd': 3}

    >>> SplosniClenAritmeticnegaZaporedja(od=1).sestavi()
    {'n1': 5, 'an1': 19, 'n2': 14, 'an2': 119/2, 'a1': 1, 'd': 9/2}
    """
    besedilo_posamezne = r'''Določi splošni člen aritmetičnega zaporedja, če je $a_{ {{latex(naloga.n1)}} }={{latex(naloga.an1)}}$ in $a_{ {{latex(naloga.n2)}} }={{latex(naloga.an2)}}$.'''
    besedilo_vecih = r'''Določi splošne člene aritmetičnih zaporedij, če poznaš naslednja dva člena:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item $a_{ {{latex(naloga.n1)}} }={{latex(naloga.an1)}}$, $a_{ {{latex(naloga.n2)}} }={{latex(naloga.an2)}}$
        {% endfor %}
        \end{enumerate}'''
    resitev_posamezne = r'''$a_n={{latex(naloga.a1)}}+{{latex(naloga.d)}}(n-1)$'''
    resitev_vecih = r'''\begin{enumerate}
        {% for naloga in naloge %}
        \item $a_n={{latex(naloga.a1)}}+{{latex(naloga.d)}}(n-1)$
        {% endfor %}
        \end{enumerate}'''

    def __init__(self, od=-5, do=5, **kwargs):
        super().__init__(**kwargs)
        if od > od:  # TODO ali od, do smiselna?
            raise MinMaxNapaka
        self.od = od
        self.do = do

    def _poskusi_sestaviti(self):
        seznam_polovick = [sympy.Rational(x, 2) for x in range(2 * self.od, 2 * self.do + 1) if x != 0]
        a1 = random.choice(seznam_polovick)
        d = random.choice(seznam_polovick)
        nn1 = random.randint(2, 10)
        nn2 = random.randint(2, 15)
        preveri(nn1 != nn2)
        n1 = min(nn1, nn2)  # Zato da sta pri izpisu urejena po velikosti
        n2 = max(nn1, nn2)
        an1 = clen_aritmeticnega(a1, d, n1)
        an2 = clen_aritmeticnega(a1, d, n2)
        return {'n1': n1, 'an1': an1, 'n2': n2, 'an2': an2, 'a1': a1, 'd': d}


class SplosniClenAritmeticnegaEnacbi(Naloga):
    """
    Naloga za zapis splošnega člena aritmetičnega zaporedja, če imaš podani dve enačbi z različnimi členi zaporedja.

    >>> SplosniClenAritmeticnegaEnacbi().sestavi()
    {'n1': 3, 'n2': 14, 'n3': 12, 'n4': 6, 'operator': '-', 'vrednost1': -49, 'vrednost2': -18, 'a1': -2, 'd': -3}

    >>> SplosniClenAritmeticnegaEnacbi().sestavi()
    {'n1': 18, 'n2': 3, 'n3': 2, 'n4': 16, 'operator': '\\cdot', 'vrednost1': -43/2, 'vrednost2': 351/4, 'a1': -6, 'd': -1/2
    """
    besedilo_posamezne = r'''Določi prvi člen in diferenco artimetičnega zaporedja, pri katerem je 
        $a_{ {{naloga.n1}} }+a_{ {{naloga.n2}} }={{latex(naloga.vrednost1)}}$ in 
        $a_{ {{naloga.n3}} } {{latex(naloga.operator)}} a_{ {{naloga.n4}} }={{latex(naloga.vrednost2)}}$.'''
    besedilo_vecih = r'''Določi prvi člen in diferenco artimetičnega zaporedja, pri katerem je
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $a_{ {{naloga.n1}} }+a_{ {{naloga.n2}} }={{latex(naloga.vrednost1)}}$, 
        $a_{ {{naloga.n3}} } {{latex(naloga.operator)}} a_{ {{naloga.n4}} }={{latex(naloga.vrednost2)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$a_1={{naloga.a1}}$, $d={{naloga.d}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $a_1={{naloga.a1}}$, $d={{naloga.d}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        a1 = random.choice([x for x in range(-8, 8) if x != 0] + [-sympy.Rational(1, 2), sympy.Rational(1, 2)])
        d = random.choice([x for x in range(-3, 3) if x != 0] + [-sympy.Rational(1, 2), sympy.Rational(1, 2)])
        [n1, n2, n3, n4] = random.sample(list(range(2, 20)), 4)
        vrednost1 = clen_aritmeticnega(a1, d, n1) + clen_aritmeticnega(a1, d, n2)
        operatorji = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '\cdot': lambda a, b: a * b}

        operator = random.choice(list(operatorji.keys()))
        vrednost2 = operatorji[operator](clen_aritmeticnega(a1, d, n3), clen_aritmeticnega(a1, d, n4))

        return {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'operator': operator, 'vrednost1': vrednost1,
                'vrednost2': vrednost2, 'a1': a1, 'd': d}


class VsotaAritmeticnega(Naloga):
    """
    Naloga za izračun vsote prvih n členov aritmetičnega zaporedja.

    :param podan_splosni_clen: podan splošni člen zaporedja ali dva člena zaporedja


    >>> VsotaAritmeticnega().sestavi()
    {'izraz': '$a_n=3 \\left(n - 1\\right) + 1$', 'n': 28, 'vsota': 1162}

    >>> VsotaAritmeticnega(podan_splosni_clen=False).sestavi()
    {'izraz': '$s_{2}=-15$ in $s_{5}=-45$', 'n': 28, 'vsota': -574}
    """
    besedilo_posamezne = r'''Izračunaj vsoto prvih ${{naloga.n}}$ členov aritmetičnega zaporedja, če je {{naloga.izraz}}.'''
    besedilo_vecih = r'''Izračunaj vsoto prvih n členov aritmetičnega zaporedja, če je:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item {{naloga.izraz}}, $n={{naloga.n}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$s_{ {{naloga.n}} }={{naloga.vsota}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $s_{ {{naloga.n}} }={{naloga.vsota}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, podan_splosni_clen=True, **kwargs):
        super().__init__(**kwargs)
        self.podan_splosni_clen = podan_splosni_clen

    def _poskusi_sestaviti(self):
        N = random.randint(10, 30)
        n = sympy.symbols('n')
        a1 = random.choice([x for x in range(-8, 8) if x != 0])
        d = random.choice([x for x in range(-5, 5) if x != 0 and x != 1])
        if self.podan_splosni_clen:
            izraz = '$a_n=' + sympy.latex(sympy.Add(a1, sympy.Mul(d, (n - 1), evaluate=False), evaluate=False)) + '$'
        else:
            [n1, n2] = sorted(random.sample(list(range(1, 21)), 2))
            preveri(N not in {n1, n2})
            izraz = '$s_{{{0}}}={1}$ in $s_{{{2}}}={3}$'.format(n1, vsota_aritmeticnega(a1, d, n1), n2,
                                                                vsota_aritmeticnega(a1, d,
                                                                                    n2))  # TODO elegantnejša rešitev?
        vsota = vsota_aritmeticnega(a1, d, N)
        return {'izraz': izraz, 'n': N, 'vsota': vsota}


# ~~~~~Naloge iz sklopa geometrijsko zaporedje
class PrviCleniGeometrijskega(Naloga):
    """
    Naloga za zapis splošnega člena geometrijskega zaporedja in računanje prvih petih členov, če poznaš prvi člen in količnik.

    :param racionalne_vrednosti: prvi člen in kvocient zaporedja sta lahko racionalni vrednosti


    >>> PrviCleniGeometrijskega().sestavi()
    {'cleni': [4, -12, 36, -108, 324], 'a1': 4, 'q': -3, 'splosni': 4*(-3)**(n - 1)}

    >>> PrviCleniGeometrijskega(racionalne_vrednosti=True).sestavi()
    {'cleni': [1/2, 1/6, 1/18, 1/54, 1/162], 'a1': 1/2, 'q': 1/3, 'splosni': (1/3)**(n - 1)/2}
    """
    besedilo_posamezne = r'''Zapiši prvih pet členov in splošni člen geometrijskega zaporedja s prvim členom $a_1={{latex(naloga.a1)}}$
         in količnikom $q={{latex(naloga.q)}}$.'''
    besedilo_vecih = r'''Zapiši prvih pet členov in splošni člen geometrijskega zaporedja s prvim členom $a_1$ in količnikom $q$:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $a_1={{latex(naloga.a1)}}$, $d={{latex(naloga.q)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''{% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item {% for clen in naloga.cleni %}$a_{ {{loop.index}} }={{clen}}$, {% endfor %} $a_n={{latex(naloga.splosni)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, racionalne_vrednosti=False, **kwargs):
        super().__init__(**kwargs)
        self.racionalne_vrednosti = racionalne_vrednosti

    def _poskusi_sestaviti(self):
        if not self.racionalne_vrednosti:
            a1 = random.choice([x for x in range(-10, 10) if x != 0])
            q = random.choice([-3, -2, 2, 3])
        else:
            a1 = random.choice([sympy.Rational(1, x) for x in range(-6, 6) if x != 0] + [sympy.Rational(2, x) for x in range(-6, 6) if
                                                                           x != 0])
            q = random.choice([sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        cleni = [a1]
        for N in range(2, 6):
            cleni.append(clen_geometrijskega(a1, q, N))
        n = sympy.symbols('n')
        splosni = sympy.Mul(a1, sympy.Pow(q, (n - 1), evaluate=False), evaluate=False)
        return {'cleni': cleni, 'a1': a1, 'q': q, 'splosni': splosni}


class SplosniClenGeometrijskega(Naloga):
    """
    Naloga za zapis splošnega člena aritmetičnega zaporedja, če poznaš dva člena zaporedja ali en člen in količnik zaporedja.


    >>> SplosniClenGeometrijskega().sestavi()
    {'podatek1': 'q=-1/3', 'podatek2': 'a_{12}=-7/177147', 'splosni': 7*(-1/3)**(n - 1)}

    >>> SplosniClenGeometrijskega().sestavi()
    {'podatek1': 'a_{12}=10240', 'podatek2': 'q=2', 'splosni': 5*2**(n - 1)}
    """
    besedilo_posamezne = r'''Določi splošni člen geometrijskega zaporedja, če je ${{naloga.podatek1}}$ in ${{latex(naloga.podatek2)}}$.'''
    besedilo_vecih = r'''Določi splošne člene geometrijskih zaporedij, če je:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{naloga.podatek1}}$ in ${{latex(naloga.podatek2)}}$
        {% endfor %}
        \end{enumerate}'''
    resitev_posamezne = r'''$a_n={{latex(naloga.splosni)}}$'''
    resitev_vecih = r'''\begin{enumerate}
        {% for naloga in naloge %}
        \item $a_n={{latex(naloga.splosni)}}$
        {% endfor %}
        \end{enumerate}'''

    def _poskusi_sestaviti(self):
        a1 = random.choice([x for x in range(-10, 10) if x != 0])
        q = random.choice([-3, -2, 2, 3] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        n1 = random.choice(list(range(3, 16, 2)))  # en lih in en sod da v enačbi ni +/- q
        n2 = random.choice(list(range(2, 16, 2)))
        # preveri(n1 != n2) #Nepotrebno ker je en lih in en sod
        an1 = clen_geometrijskega(a1, q, n1)
        an2 = clen_geometrijskega(a1, q, n2)
        [podatek1, podatek2] = random.sample(
            ['a_{{{0}}}={1}'.format(n1, an1), 'a_{{{0}}}={1}'.format(n2, an2), 'q={}'.format(q)],
            2)  # TODO elegantnejši način za izpis?
        n = sympy.symbols('n')
        splosni = sympy.Mul(a1, sympy.Pow(q, (n - 1), evaluate=False), evaluate=False)  # TODO preprči (1/3)**n=3**(-n)

        return {'podatek1': podatek1, 'podatek2': podatek2, 'splosni': splosni}


class SplosniClenGeometrijskegaEnacbi(Naloga):
    """
    Naloga za zapis splošnega člena geometrijskega zaporedja, če imaš podani dve enačbi z različnimi členi zaporedja.


    >>> SplosniClenGeometrijskegaEnacbi().sestavi()
    {'n1': 5, 'n2': 6, 'n3': 3, 'operator': '\\cdot', 'vrednost1': 64, 'vrednost2': 2048, 'a1': 4, 'q': 2}

    >>> SplosniClenGeometrijskegaEnacbi().sestavi()
    {'n1': 5, 'n2': 7, 'n3': 6, 'operator': '\\cdot', 'vrednost1': -324, 'vrednost2': -2834352, 'a1': -4, 'q': -3}
    """
    besedilo_posamezne = r'''Določi prvi člen in količnik geometrijskega zaporedja, pri katerem je 
        $a_{ {{naloga.n1}} }={{latex(naloga.vrednost1)}}$ in 
        $a_{ {{naloga.n2}} } {{latex(naloga.operator)}} a_{ {{naloga.n3}} }={{latex(naloga.vrednost2)}}$.'''
    besedilo_vecih = r'''Določi prvi člen in količnik geometrijskega zaporedja, pri katerem je
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $a_{ {{naloga.n1}} }={{latex(naloga.vrednost1)}}$, 
    $a_{ {{naloga.n2}} } {{latex(naloga.operator)}} a_{ {{naloga.n3}} }={{latex(naloga.vrednost2)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$a_1={{latex(naloga.a1)}}$, $q={{latex(naloga.q)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $a_1={{latex(naloga.a1)}}$, $q={{latex(naloga.q)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
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
        vrednost1 = clen_geometrijskega(a1, q, n1)
        vrednost2 = operatorji[operator](clen_geometrijskega(a1, q, n2), clen_geometrijskega(a1, q, n3))

        return {'n1': n1, 'n2': n2, 'n3': n3, 'operator': operator, 'vrednost1': vrednost1,
                'vrednost2': vrednost2, 'a1': a1, 'q': q}


class VsotaGeometrijskega(Naloga):
    """
    Naloga za izračun vsote prvih :math:`n` členov geometrijskega zaporedja.

    :param podan_splosni_clen: podan splošni člen zaporedja ali dva člena zaporedja


    >>> VsotaGeometrijskega().sestavi()
    {'izraz': '$a_n=3 \\left(-3\\right)^{n - 1}$', 'n': 5, 'vsota': 183}

    >>> VsotaGeometrijskega(podan_splosni_clen=False).sestavi()
    {'izraz': '$a_{3}=-1/8$ in $a_{7}=-1/128$', 'n': 6, 'vsota': -63/64}
    """
    besedilo_posamezne = r'''Izračunaj vsoto prvih ${{naloga.n}}$ členov geometrijskega zaporedja, če je {{naloga.izraz}}.'''
    besedilo_vecih = r'''Izračunaj vsoto prvih n členov geometrijskega zaporedja, če je:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item {{naloga.izraz}}, $n={{naloga.n}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$s_{ {{naloga.n}} }={{latex(naloga.vsota)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $s_{ {{naloga.n}} }={{latex(naloga.vsota)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, podan_splosni_clen=True, **kwargs):
        super().__init__(**kwargs)
        self.podan_splosni_clen = podan_splosni_clen

    def _poskusi_sestaviti(self):
        N = random.randint(4, 10)
        n = sympy.symbols('n')
        a1 = random.choice([x for x in range(-5, 5) if x != 0] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        q = random.choice([x for x in [-3, -2, 2, 3]] + [sympy.Rational(1, x) for x in [-3, -2, 2, 3]])
        if self.podan_splosni_clen:
            izraz = '$a_n=' + sympy.latex(sympy.Mul(a1, sympy.Pow(q, (n - 1), evaluate=False), evaluate=False)) + '$'
        else:
            [n1, n2] = sorted(random.sample(list(range(2, 8)), 2))
            # TODO elegantnejša rešitev?
            izraz = '$a_{{{0}}}={1}$ in $a_{{{2}}}={3}$'.format(n1, clen_geometrijskega(a1, q, n1),
                                                                n2, clen_geometrijskega(a1, q, n2))
        vsota = vsota_geometrijskega(a1, q, N)
        return {'izraz': izraz, 'n': N, 'vsota': vsota}


class VsotaGeometrijskeVrste(Naloga):
    """
    Naloga za zapis geometrijske vrste, če poznaš dva podatka.

    :param lazji_podatki: na začetku podana dva lažja podatka (prvi člen, kvocient ali vsota vrste) ali lahko tudi težja (poljuben člen ali delna vsota)


    >>> VsotaGeometrijskeVrste().sestavi()
    {'podatek1': 'q', 'vrednost1': sqrt(2)/3, 'podatek2': 's', 'vrednost2': -6/(1 - sqrt(2)/3), 'vrsta': '-6+- 2 \\sqrt{2}+- \\frac{4}{3}+- \\frac{4 \\sqrt{2}}{9}+...'}

    >>> VsotaGeometrijskeVrste(lazji_podatki=False).sestavi()
    {'podatek1': 'a_1', 'vrednost1': 1, 'podatek2': 'a_4', 'vrednost2': -1/64, 'vrsta': '1+- \\frac{1}{4}+\\frac{1}{16}+- \\frac{1}{64}+...'}
    """
    besedilo_posamezne = r'''Zapiši geometrijsko vrsto, če je ${{latex(naloga.podatek1)}}={{latex(naloga.vrednost1)}}$ in
         ${{latex(naloga.podatek2)}}={{latex(naloga.vrednost2)}}$.'''
    besedilo_vecih = r'''Zapiši geometrijsko vrsto z danima podatkoma
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{latex(naloga.podatek1)}}={{latex(naloga.vrednost1)}}$,
         ${{latex(naloga.podatek2)}}={{latex(naloga.vrednost2)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''${{naloga.vrsta}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{naloga.vrsta}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, lazji_podatki=True, **kwargs):
        """
        """
        super().__init__(**kwargs)
        self.lazji_podatki = lazji_podatki

    def _poskusi_sestaviti(self):
        q = random.choice([-sympy.Rational(1, 2), sympy.Rational(1, 2),
                           -sympy.Rational(2, 3), -sympy.Rational(1, 3), sympy.Rational(2, 3), sympy.Rational(1, 3),
                           -sympy.Rational(3, 4), -sympy.Rational(1, 4), sympy.Rational(3, 4), sympy.Rational(1, 4),
                           -sympy.Rational(2, 5), -sympy.Rational(1, 5), sympy.Rational(2, 5), sympy.Rational(1, 5),
                           -sympy.Mul(sympy.sqrt(2), sympy.Pow(2, -1), evaluate=False),
                           sympy.Mul(sympy.sqrt(2), sympy.Pow(2, -1), evaluate=False),
                           -sympy.Mul(sympy.sqrt(2), sympy.Pow(3, -1), evaluate=False),
                           sympy.Mul(sympy.sqrt(2), sympy.Pow(3, -1), evaluate=False)])
        a1 = random.choice([x for x in range(-10, 11) if x != 0])
        s = vsota_geometrijske_vrste(a1, q)
        izbor = [('a_1', a1), ('q', q), ('s', s)]
        if not self.lazji_podatki:
            n1 = random.randint(3, 5)
            an = clen_geometrijskega(a1, q, n1)
            n2 = random.randint(3, 5)
            sn = vsota_geometrijskega(a1, q, n2)
            izbor += [('a_{}'.format(n1), an), ('s_{}'.format(n2), sn)]
        [izraz1, izraz2] = random.sample(izbor, 2)
        vrsta = '+'.join('{}'.format(sympy.latex(clen_geometrijskega(a1, q, n))) for n in range(1, 5)) + '+...'
        return {'podatek1': izraz1[0], 'vrednost1': izraz1[1], 'podatek2': izraz2[0], 'vrednost2': izraz2[1],
                'vrsta': vrsta}
