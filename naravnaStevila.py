from generiranje import Naloga, preveri, MinMaxNapaka
import sympy
import random
import jinja2


class DeliteljVeckratnik(Naloga):
    besedilo_posamezne = r'''Določi največji skupni delitelj in najmanjši skupni večkratnik števil ${{naloga.stevilo1}}$ in ${{naloga.stevilo2}}$.'''
    besedilo_vecih = r'''Določi največji skupni delitelj in najmanjši skupni večkratnik števil:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.stevilo1}}$ in ${{naloga.stevilo2}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$D( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najvecjiDelitelj}}$, $v( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najmanjsiVeckratnik}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $D( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najvecjiDelitelj}}$, $v( {{naloga.stevilo1}},{{naloga.stevilo2}} )={{naloga.najmanjsiVeckratnik}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, od=50, do=200, najvecjePrastevilo=17, lazja=True, **kwargs):
        super().__init__(**kwargs)
        if od > do:
            raise MinMaxNapaka
        if od < 1:
            raise ValueError('Izbrana naj bodo naravna števila.')

        self.od = od
        self.do = do
        self.lazja = lazja
        self.najvecjePrastevilo = najvecjePrastevilo

    def poskusi_sestaviti(self):
        # TODO težja = 3 števila, izrazi
        # TODO ali bilo boljše da izbere praštevila in jih množi?
        # #TODO ali bolje da ločimo nalogo za gcd in lcm? ker lcm lahko zelo velik
        stevilo1 = random.randint(self.od, self.do)
        stevilo2 = random.randint(self.od, self.do)
        preveri(max(sympy.factorint(stevilo1).keys()) <= self.najvecjePrastevilo and max(
            sympy.factorint(stevilo2).keys()) <= self.najvecjePrastevilo and stevilo1 != stevilo2)
        najvecjiDelitelj = sympy.gcd(stevilo1, stevilo2)
        najmanjsiVeckratnik = sympy.lcm(stevilo1, stevilo2)

        return {'stevilo1': stevilo1, 'stevilo2': stevilo2, 'najvecjiDelitelj': najvecjiDelitelj,
                'najmanjsiVeckratnik': najmanjsiVeckratnik}


# class DolociStevko(Naloga):  # TODO besedilo za 2 delitelja - ali lahko 2 različna besedila?
#     def __init__(self, lazja=True, **kwargs):
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
#     def poskusi_sestaviti(self):
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
    besedilo_posamezne = r'''Z Evklidovim algoritmom poišči največji skupni delitelj števil ${{naloga.stevilo1}}$ in ${{naloga.stevilo2}}$. '''
    besedilo_vecih = r'''Z Evklidovim algoritmom poišči največji skupni delitelj števil:
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.stevilo1}}$, ${{naloga.stevilo2}}$
    {% endfor %}
    \end{enumerate}
    '''
    resitev_posamezne = r'''$D({{naloga.stevilo1}},{{naloga.stevilo2}})={{naloga.najvecjiDelitelj}}$'''
    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item $D({{naloga.stevilo1}},{{naloga.stevilo2}})={{naloga.najvecjiDelitelj}}$
     {% endfor %}
     \end{enumerate}
     '''

    def poskusi_sestaviti(self):  # TODO ali želimo izločiti tuja števila?
        steviloMalo = random.randint(50, 199)
        steviloVeliko = random.randint(200, 1000)
        preveri(steviloVeliko % steviloMalo != 0 and steviloMalo % (
                steviloVeliko % steviloMalo) != 0)  # Da se ne konča že v prvih dveh korakih
        najvecjiDelitelj = sympy.gcd(steviloMalo, steviloVeliko)
        return {'stevilo1': steviloMalo, 'stevilo2': steviloVeliko, 'najvecjiDelitelj': najvecjiDelitelj}
