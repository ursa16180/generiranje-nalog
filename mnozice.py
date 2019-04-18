from generiranje import Naloga, preveri
import random
import sympy
import jinja2
import itertools  # potrebujemo za kartezični produkt


def izberiMnozico(velikost=4, od=1, do=10):
    izbor = [x for x in range(od, do + 1)]
    mnozica = sympy.FiniteSet(*random.sample(izbor, velikost))
    return mnozica


# TODO ali smiselno delat besedilne naloge? Sklanjanje?

class ElementiMnozice(Naloga):
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

    def __init__(self, lazja=True, **kwargs):
        super().__init__(**kwargs)

        self.lazja = lazja

    def poskusi_sestaviti(self):
        pogoj = random.choice(['|', '<', '<='])
        n = sympy.symbols('n')
        if self.lazja:
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def poskusi_sestaviti(self):
        velikost = random.randint(2, 3)
        mnozice = [['a', 'b', 'c'], [1, 2, 3], ['x', 'y', 'z'], ['alpha', 'beta', 'gamma'], ['Pi', 'Phi', 'Xi'],
                   [3, 6, 9], [3, 7, 42]]
        mnozica = sympy.FiniteSet(*random.choice(mnozice)[:velikost])
        potencna = mnozica.powerset()
        return {'mnozica': mnozica, 'potencna': potencna}


class UnijaPresekRazlika(Naloga):  # Todo ali potrebne 3 množice - za unijo presek razliko dovolj 2 #Todo ime naloge?
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def poskusi_sestaviti(self):
        A = izberiMnozico(4, 1, 6)
        B = izberiMnozico(3, 1, 6)
        C = izberiMnozico(2, 1, 6)
        AunijaC = A.union(C)
        ApresekB = A.intersection(B)
        AbrezC = sympy.Complement(A, C)
        CbrezB = sympy.Complement(C, B)
        AkartezicnoC = sympy.FiniteSet(*A * C)
        AunijaCbrezApresekB = sympy.Complement(AunijaC, ApresekB)
        return {'A': A, 'B': B, 'C': C, 'AunijaC': AunijaC, 'ApresekB': ApresekB, 'AbrezC': AbrezC, 'CbrezB': CbrezB,
                'AkartezicnoC': AkartezicnoC, 'AunijaCbrezApresekB': AunijaCbrezApresekB}


class IzpeljaneMnozice(Naloga):
    besedilo_posamezne = r'''Dana je univerzalna množica $ \mathcal{U} =\mathbb{N}_{ {{naloga.velikostUniverzalne}} }$ 
    in njene pomnožice $ \mathcal{A} =\{ {{latex(naloga.navodiloA)}}; k \in \mathbb{N} \}$, $ \mathcal{B} =\{ {{latex(naloga.navodiloB)}}; k \in \mathbb{N} \}$, 
    $ \mathcal{C} ={{latex(naloga.C)}}$. Zapiši elemente množic $ \mathcal{A} $, $ \mathcal{B} $, $ \mathcal{A}  \cup  \mathcal{B} $, $ \mathcal{C} ^{\mathsf{c}}$ in $ \mathcal{B}  -  \mathcal{A} $.'''

    besedilo_vecih = r''' Za dano univerzalno množico $ \mathcal{U} $ in njene podmnožice 
    $ \mathcal{A} $, $ \mathcal{B} $ in $ \mathcal{C} $ zapiši elemente množic $ \mathcal{A} $, $ \mathcal{B} $, $ \mathcal{A}  \cup  \mathcal{B} $, $ \mathcal{C} ^{\mathsf{c}}$ in $ \mathcal{B}  -  \mathcal{A} $
    \begin{enumerate}
    {% for naloga in naloge %}
    \item $ \mathcal{U} =\mathbb{N}_{ {{naloga.velikostUniverzalne}} }$, $ \mathcal{A} =\{ {{latex(naloga.navodiloA)}}; k \in \mathbb{N} \}$, 
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def poskusi_sestaviti(self):
        k = sympy.symbols('k')
        a = random.randint(2, 5)
        b = random.choice([-4, -3, -2, -1, 0, 1, 2, 3, 4])
        c = random.randint(2, 5)
        d = random.choice([-4, -3, -2, -1, 0, 1, 2, 3, 4])
        preveri(abs(b) != a and abs(d) != c)
        velikostUniverzalne = random.randint(12, 20)
        univerzalna = sympy.FiniteSet(*range(1, velikostUniverzalne + 1))
        navodiloA = a * k + b
        navodiloB = c * k + d
        A = sympy.FiniteSet(
            *[a * x + b for x in range(1, velikostUniverzalne + 1) if 0 < a * x + b <= velikostUniverzalne])
        B = sympy.FiniteSet(
            *[c * x + d for x in range(1, velikostUniverzalne + 1) if 0 < a * x + b <= velikostUniverzalne])
        C = sympy.FiniteSet(*random.sample(set(univerzalna), 8))
        AunijaB = A.union(B)
        Ckomplement = sympy.Complement(univerzalna, C)
        BbrezA = sympy.Complement(B, A)

        return {'navodiloA': navodiloA, 'navodiloB': navodiloB, 'A': A, 'B': B, 'C': C,
                'AunijaB': AunijaB, 'Ckomplement': Ckomplement, 'BbrezA': BbrezA,
                'velikostUniverzalne': velikostUniverzalne}
