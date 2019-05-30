from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random


class DeliteljVeckratnik(Naloga):
    """
    Naloga za izračun največjega skupnega delitelja in najmanjšega skupnega večkratnika dveh števil.

    :param od: najmanjše možno število
    :param do: največje možno število
    :param najvecje_prastevilo: največje možno praštevilo v praštevilskem razcepu


    >>> DeliteljVeckratnik().sestavi()
    {'stevilo1': 192, 'stevilo2': 100, 'najvecji_delitelj': 4, 'najmanjsi_veckratnik': 4800}

    >>> DeliteljVeckratnik(do=100, najvecje_prastevilo=11).sestavi()
    {'stevilo1': 56, 'stevilo2': 75, 'najvecji_delitelj': 1, 'najmanjsi_veckratnik': 4200}
    """
    besedilo_posamezne = r'''Določi največji skupni delitelj in najmanjši skupni večkratnik števil ${{naloga.stevilo1}}$ in ${{naloga.stevilo2}}$.'''
    besedilo_vecih = r'''Določi največji skupni delitelj in najmanjši skupni večkratnik števil:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.stevilo1}}$ in ${{naloga.stevilo2}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$D( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najvecji_delitelj}}$, $v( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najmanjsi_veckratnik}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $D( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najvecji_delitelj}}$, $v( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najmanjsi_veckratnik}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, od=50, do=200, najvecje_prastevilo=17, **kwargs):
        super().__init__(**kwargs)
        if od > do:
            raise MinMaxNapaka
        if od < 1:
            raise ValueError('Izbrana naj bodo naravna števila.')

        self.od = od
        self.do = do
        self.najvecje_prastevilo = najvecje_prastevilo

    def _poskusi_sestaviti(self):
        # TODO težja = 3 števila, izrazi
        # TODO ali bilo boljše da izbere praštevila in jih množi?
        # #TODO ali bolje da ločimo nalogo za gcd in lcm? ker lcm lahko zelo velik
        stevilo1 = random.randint(self.od, self.do)
        stevilo2 = random.randint(self.od, self.do)
        preveri(max(sympy.factorint(stevilo1).keys()) <= self.najvecje_prastevilo and max(
            sympy.factorint(stevilo2).keys()) <= self.najvecje_prastevilo and stevilo1 != stevilo2)
        najvecji_delitelj = sympy.gcd(stevilo1, stevilo2)
        najmanjsi_veckratnik = sympy.lcm(stevilo1, stevilo2)

        return {'stevilo1': stevilo1, 'stevilo2': stevilo2, 'najvecji_delitelj': najvecji_delitelj,
                'najmanjsi_veckratnik': najmanjsi_veckratnik}

    # class DolociStevko(Naloga):
    """
    
    """  # TODO besedilo za 2 delitelja - ali lahko 2 različna besedila?


#     def __init__(self, lazja=True, **kwargs):
#         """
#         :param lazja: lažja ali težja oblika naloge
#         """
#         super().__init__(**kwargs)
#         besedilo_posamezne =
#             r'''Za katero števko $a$ število ${{naloga.delitelj1}}$ deli ${{naloga.stevilo}}$?'''
#         besedilo_vecih =r'''Za katero števko $a$ je število $n$ deljivo s $k$:
#         \begin{enumerate}
#         {% for naloga in naloge %}
#         \item $n={{naloga.stevilo}}$, $k={{naloga.delitelj1}}$
#         {% endfor %}
#         \end{enumerate}
#         '''
#         resitev_posamezne =r'''$a \in {{latex(naloga.resitev)}}$'''
#         resitev_vecih =r'''
#         \begin{enumerate}
#          {% for naloga in naloge %}
#          \item $a \in {{latex(naloga.resitev)}}$
#          {% endfor %}
#          \end{enumerate}
#          '''
#         self.lazja = lazja
#
#     def _poskusi_sestaviti(self):
#         """Poskusi sestaviti nalogo """
#         dolzina = random.randint(5, 8)
#         if self.lazja:
#             zamenjaj1 = random.randint(2, min(3,dolzina - 3))
#             mesta1 = random.sample(list(range(dolzina)), zamenjaj1)
#             mesta2 = list()
#         else:
#             zamenjaj1 = random.randint(1, min(2, dolzina - 4))
#             mesta1 = random.sample(list(range(dolzina)), zamenjaj1)
#             zamenjaj2 = random.randint(1, min(2, dolzina - 4))
#             mesta2 = random.sample(list(range(dolzina)), zamenjaj2)
#             preveri(len(set(mesta1).intersection(set(mesta2))) < min(zamenjaj1, zamenjaj2))
#
#         a = sympy.symbols('a')
#         b = sympy.symbols('b')
#         vrednost = 0
#         stevke = str()
#         for i in range(dolzina):
#             if i in mesta1:
#                 vrednost += a * 10 ** i
#                 stevke += 'a'
#             elif i in mesta2:
#                 vrednost += b * 10 ** i
#                 stevke += 'b'
#             else:
#                 stevka = random.randint(1, 9)
#                 vrednost += stevka * 10 ** i
#                 stevke += str(stevka)
#         stevke = stevke[::-1]
#
#         if not self.lazja:
#             delitelj1 = random.choice([3, 9, 11])
#             delitelj2 = random.choice([2, 4, 5])
#             preveri(delitelj1 != delitelj2)
#         else:
#             delitelj1 = random.choice([3, 4, 5, 6, 8, 9, 10, 11])
#             delitelj2 = 1
#         resitev = set()
#         for stevkaA in range(10):
#             for stevkaB in range(10):
#                 if vrednost.subs([(a, stevkaA), (b, stevkaB)]) % delitelj1 == 0 and vrednost.subs(
#                         [(a, stevkaA), (b, stevkaB)]) % delitelj2 == 0:
#                     resitev.add((stevkaA, stevkaB))
#         preveri(len(resitev) != 0)
#         return {'stevilo': stevke, 'delitelj1': delitelj1, 'delitelj2': delitelj2, 'resitev': resitev}


class EvklidovAlgoritem(Naloga):
    """
    Naloga za izračun največjega skupnega delitelja dveh števil z Evklidovim algoritmom.


    >>> EvklidovAlgoritem().sestavi()
    {'stevilo1': 142, 'stevilo2': 519, 'najvecji_delitelj': 1}

    >>> EvklidovAlgoritem().sestavi()
    {'stevilo1': 90, 'stevilo2': 336, 'najvecji_delitelj': 6}
    """
    besedilo_posamezne = r'''Z Evklidovim algoritmom poišči največji skupni delitelj števil ${{naloga.stevilo1}}$ in ${{naloga.stevilo2}}$. '''
    besedilo_vecih = r'''Z Evklidovim algoritmom poišči največji skupni delitelj števil:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.stevilo1}}$, ${{naloga.stevilo2}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$D({{naloga.stevilo1}},{{naloga.stevilo2}})={{naloga.najvecji_delitelj}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $D({{naloga.stevilo1}},{{naloga.stevilo2}})={{naloga.najvecji_delitelj}}$
     {% endfor %}
     \end{enumerate}
     '''

    def _poskusi_sestaviti(self):  # TODO ali želimo izločiti tuja števila?
        stevilo_malo = random.randint(50, 199)
        stevilo_veliko = random.randint(200, 1000)
        preveri(stevilo_veliko % stevilo_malo != 0 and stevilo_malo % (
                stevilo_veliko % stevilo_malo) != 0)  # Da se ne konča že v prvih dveh korakih
        najvecji_delitelj = sympy.gcd(stevilo_malo, stevilo_veliko)
        return {'stevilo1': stevilo_malo, 'stevilo2': stevilo_veliko, 'najvecji_delitelj': najvecji_delitelj}
