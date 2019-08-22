from generiranje import Naloga, preveri, MinMaxNapaka
import random
import sympy


def izberi_mnozico(velikost=4, od=1, do=10):
    """
    Naredi naključno množico poljubne velikosti.

    :param velikost: velikost množice
    :param od: najmanjša možna vrednost elementa
    :param do: največja možna vrednost elementa
    :return: množica celih števil


    >>> izberi_mnozico(velikost=7)
    {1, 2, 4, 5, 7, 8, 9}

    >>> izberi_mnozico(velikost=5, od=-27, do=4)
    {-20, -7, -4, 3, 4}
    """
    if od > do:
        raise MinMaxNapaka
    izbor = [x for x in range(od, do + 1)]
    mnozica = sympy.FiniteSet(*random.sample(izbor, velikost))
    return mnozica


# TODO ali smiselno delat besedilne naloge? Sklanjanje?

class ElementiMnozice(Naloga):
    """
    Naloga za izpis posameznih elementov množice iz podanega predpisa. Lažja zazličica ima predpis samo za n, težja pa za a*n +b.

    :param linearna_kombinacija: predpis vsebuje linearno kombinacijo :math:`a*n +b`, drugače samo :math:`n`


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> ElementiMnozice().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> ElementiMnozice(linearna_kombinacija=False).primer()
    """
    besedilo_posamezne = r'''Zapiši elemente množice $ \mathcal{A} =\{ {{latex(naloga.n)}}; 
    (n \in \mathbb{N}) \land (n{{latex(naloga.pogoj)}} {{latex(naloga.stevilo)}} ) \} $.'''

    besedilo_vecih = r'''Zapiši elemente množic:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $ \mathcal{A} =\{ {{latex(naloga.n)}}; 
    (n \in \mathbb{N}) \land (n{{latex(naloga.pogoj)}} {{latex(naloga.stevilo)}} ) \} $
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$ \mathcal{A} ={{latex(naloga.mnozica)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $ \mathcal{A} ={{latex(naloga.mnozica)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, linearna_kombinacija=True, **kwargs):
        super().__init__(**kwargs)
        self.linearna_kombinacija = linearna_kombinacija

    def _poskusi_sestaviti(self):
        pogoj = random.choice(['|', '<', '<='])
        n = sympy.symbols('n')
        if not self.linearna_kombinacija:
            a = 1
            b = 0
        else:
            a = random.randint(1, 3)
            b = random.choice([-2, -1, 0, 1, 2])
        if pogoj == '|':
            stevilo = random.randint(15, 45)
            ustrezni = sympy.divisors(stevilo)
        elif pogoj == '<':
            stevilo = random.randint(5, 12)
            ustrezni = list(range(stevilo))
        elif pogoj == '<=':
            stevilo = random.randint(5, 8)
            ustrezni = list(range(stevilo + 1))
        mnozica = sympy.FiniteSet(*[a * x + b for x in ustrezni if a * x + b > 0])
        return {'n': sympy.simplify(a * n + b), 'pogoj': pogoj, 'stevilo': stevilo, 'mnozica': mnozica}


class PotencnaMnozica(Naloga):
    """
    Naloga za zapis potenčne množice.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> PotencnaMnozica().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> PotencnaMnozica().primer()
    """
    besedilo_posamezne = r'''Zapiši potenčno množico množice $ \mathcal{A} ={{latex(naloga.mnozica)}}$'''
    besedilo_vecih = r'''Zapiši potenčno množico množice $ \mathcal{A} $:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $ \mathcal{A} ={{latex(naloga.mnozica)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$\mathcal{P}( \mathcal{A} ) ={{latex(naloga.potencna)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $\mathcal{P}( \mathcal{A} ) ={{latex(naloga.potencna)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        velikost = random.randint(2, 3)
        mnozice = [['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z'], ['alpha', 'beta', 'gamma'], ['Pi', 'Phi', 'Xi'],
                   [3, 6, 9], [3, 7, 42]]
        mnozica = sympy.FiniteSet(*random.choice(mnozice)[:velikost])
        potencna = mnozica.powerset()
        return {'mnozica': mnozica, 'potencna': potencna}


class UnijaPresekRazlika(Naloga):  # Todo ali potrebne 3 množice - za unijo presek razliko dovolj 2 #Todo ime naloge?
    """
    Naloga za zapis unije, presek, razlike in kartezičnega produkta množic.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> UnijaPresekRazlika().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> UnijaPresekRazlika().primer()
    """
    besedilo_posamezne = r'''Dane so množice $ \mathcal{A} ={{latex(naloga.A)}}$, $ \mathcal{B} ={{latex(naloga.B)}}$ in $ \mathcal{C} ={{latex(naloga.C)}}$.
    Zapiši množice $ \mathcal{A} \cup  \mathcal{C} $, $ \mathcal{A} \cap  \mathcal{B} $, $ \mathcal{A} - \mathcal{C} $, $ \mathcal{C} - \mathcal{B} $, $ \mathcal{A} \times  \mathcal{C} $ in $( \mathcal{A} \cup  \mathcal{C} )-( \mathcal{A} \cap  \mathcal{B} )$.'''

    besedilo_vecih = r''' Za dane množice $ \mathcal{A} $, $ \mathcal{B} $ in $ \mathcal{C} $ zapiši množice $ \mathcal{A} \cup  \mathcal{C} $, $ \mathcal{A} \cap  \mathcal{B} $, $ \mathcal{A} - \mathcal{C} $, $ \mathcal{C} - \mathcal{B} $, $ \mathcal{A} \times  \mathcal{C} $ in $( \mathcal{A} \cup  \mathcal{C} )-( \mathcal{A} \cap  \mathcal{B} )$
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $ \mathcal{A} ={{latex(naloga.A)}}$, $ \mathcal{B} ={{latex(naloga.B)}}$, $ \mathcal{C} ={{latex(naloga.C)}}$
    {% endfor %}
    \end{enumerate}
    '''

    resitev_posamezne = r'''$ \mathcal{A} \cup  \mathcal{C} ={{latex(naloga.AunijaC)}}$, $ \mathcal{A} \cap  \mathcal{B} ={{latex(naloga.ApresekB)}}$, $ \mathcal{A} - \mathcal{C} ={{latex(naloga.AbrezC)}}$,
         $ \mathcal{C} - \mathcal{B} ={{latex(naloga.CbrezB)}}$, $ \mathcal{A} \times  \mathcal{C} ={{latex(naloga.AkartezicnoC)}}$, $( \mathcal{A} \cup  \mathcal{C} )-( \mathcal{A} \cap  \mathcal{B} )={{latex(naloga.AunijaCbrezApresekB)}}$'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $ \mathcal{A} \cup  \mathcal{C} ={{latex(naloga.AunijaC)}}$, $ \mathcal{A} \cap  \mathcal{B} ={{latex(naloga.ApresekB)}}$, $ \mathcal{A} - \mathcal{C} ={{latex(naloga.AbrezC)}}$,
         $ \mathcal{C} - \mathcal{B} ={{latex(naloga.CbrezB)}}$, $ \mathcal{A} \times  \mathcal{C} ={{latex(naloga.AkartezicnoC)}}$, $( \mathcal{A} \cup  \mathcal{C} )-( \mathcal{A} \cap  \mathcal{B} )={{latex(naloga.AunijaCbrezApresekB)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        A = izberi_mnozico(4, 1, 6)
        B = izberi_mnozico(3, 1, 6)
        C = izberi_mnozico(2, 1, 6)
        AunijaC = A.union(C)
        ApresekB = A.intersection(B)
        AbrezC = sympy.Complement(A, C)
        CbrezB = sympy.Complement(C, B)
        AkartezicnoC = sympy.FiniteSet(*A * C)
        AunijaCbrezApresekB = sympy.Complement(AunijaC, ApresekB)
        return {'A': A, 'B': B, 'C': C, 'AunijaC': AunijaC, 'ApresekB': ApresekB, 'AbrezC': AbrezC, 'CbrezB': CbrezB,
                'AkartezicnoC': AkartezicnoC, 'AunijaCbrezApresekB': AunijaCbrezApresekB}


class IzpeljaneMnozice(Naloga):
    """
    Naloga za izračun komplementa, unije in razlike množic ter izpis elementov izpeljane množice pri podani univerzalni množici.


    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> IzpeljaneMnozice().primer()

    .. runblock:: pycon

        >>> import sys
        >>> sys.path.append('../')
        >>> from mnozice import *
        >>> IzpeljaneMnozice().primer()
    """
    besedilo_posamezne = r'''Dana je univerzalna množica $ \mathcal{U} =\mathbb{N}_{ {{naloga.velikost_univerzalne}} }$ 
    in njene pomnožice $ \mathcal{A} =\{ {{latex(naloga.navodiloA)}}; k \in \mathbb{N} \}$, $ \mathcal{B} =\{ {{latex(naloga.navodiloB)}}; k \in \mathbb{N} \}$, 
    $ \mathcal{C} ={{latex(naloga.C)}}$. Zapiši elemente množic $ \mathcal{A} $, $ \mathcal{B} $, $ \mathcal{A}  \cup  \mathcal{B} $, $ \mathcal{C} ^{\mathsf{c}}$ in $ \mathcal{B}  -  \mathcal{A} $.'''

    besedilo_vecih = r''' Za dano univerzalno množico $ \mathcal{U} $ in njene podmnožice 
    $ \mathcal{A} $, $ \mathcal{B} $ in $ \mathcal{C} $ zapiši elemente množic $ \mathcal{A} $, $ \mathcal{B} $, $ \mathcal{A}  \cup  \mathcal{B} $, $ \mathcal{C} ^{\mathsf{c}}$ in $ \mathcal{B}  -  \mathcal{A} $
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $ \mathcal{U} =\mathbb{N}_{ {{naloga.velikost_univerzalne}} }$, $ \mathcal{A} =\{ {{latex(naloga.navodiloA)}}; k \in \mathbb{N} \}$, 
    $ \mathcal{B} =\{ {{latex(naloga.navodiloB)}}; k \in \mathbb{N} \}$, $ \mathcal{C} ={{latex(naloga.C)}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$ \mathcal{A} ={{latex(naloga.A)}}$, $ \mathcal{B} ={{latex(naloga.B)}}$, 
    $ \mathcal{A}  \cup  \mathcal{B}  ={{latex(naloga.AunijaB)}}$, $ \mathcal{C} ^{\mathsf{c}}={{latex(naloga.Ckomplement)}}$,  $ \mathcal{B}  -  \mathcal{A}  ={{latex(naloga.BbrezA)}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $ \mathcal{A} ={{latex(naloga.A)}}$, $ \mathcal{B} ={{latex(naloga.B)}}$, 
    $ \mathcal{A}  \cup  \mathcal{B}  ={{latex(naloga.AunijaB)}}$, $ \mathcal{C} ^{\mathsf{c}}={{latex(naloga.Ckomplement)}}$,  $ \mathcal{B}  -  \mathcal{A}  ={{latex(naloga.BbrezA)}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):
        k = sympy.symbols('k')
        a = random.randint(2, 5)
        b = random.choice([-4, -3, -2, -1, 0, 1, 2, 3, 4])
        c = random.randint(2, 5)
        d = random.choice([-4, -3, -2, -1, 0, 1, 2, 3, 4])
        preveri(abs(b) != a and abs(d) != c)
        velikost_univerzalne = random.randint(12, 20)
        univerzalna = sympy.FiniteSet(*range(1, velikost_univerzalne + 1))
        navodiloA = a * k + b
        navodiloB = c * k + d
        A = sympy.FiniteSet(
            *[a * x + b for x in range(1, velikost_univerzalne + 1) if 0 < a * x + b <= velikost_univerzalne])
        B = sympy.FiniteSet(
            *[c * x + d for x in range(1, velikost_univerzalne + 1) if 0 < a * x + b <= velikost_univerzalne])
        C = sympy.FiniteSet(*random.sample(set(univerzalna), 8))
        AunijaB = A.union(B)
        Ckomplement = sympy.Complement(univerzalna, C)
        BbrezA = sympy.Complement(B, A)

        return {'navodiloA': navodiloA, 'navodiloB': navodiloB, 'A': A, 'B': B, 'C': C,
                'AunijaB': AunijaB, 'Ckomplement': Ckomplement, 'BbrezA': BbrezA,
                'velikost_univerzalne': velikost_univerzalne}

