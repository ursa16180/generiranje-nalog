from generiranje import Naloga, preveri
import sympy
import random


# ~~~~~~~~~~~~~VZOREC za nalogo
class VzorecNaloge(Naloga):
    """
    Opis naloge.

    :param : Opisani parametri

    Primer naloge.
    """

    besedilo_posamezne = r''' '''

    besedilo_vecih = r'''
    \begin{enumerate}
    {% for naloga in naloge %}
    \item
    {% endfor %}
    \end{enumerate}
    '''

    resitev_posamezne = r''' '''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, **kwargs):  # Dodamo kadar želimo da ima naloga dodatne parametre
        super().__init__(**kwargs)

    def _poskusi_sestaviti(self):
        sestavljena_naloga = 1
        sestavljena_resitev = 2
        return {'naloga': sestavljena_naloga, 'resitev': sestavljena_resitev}
