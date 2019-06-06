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

    besedilo_posamezne = r'''${{naloga.sestavljena_naloga}}$'''

    besedilo_vecih = r'''
    \begin{enumerate}
    {% for naloga in naloge %}
    \item ${{naloga.sestavljena_naloga}}$
    {% endfor %}
    \end{enumerate}
    '''

    resitev_posamezne = r'''${{naloga.sestavljena_resitev}}$'''

    resitev_vecih = r'''
    \begin{enumerate}
     {% for naloga in naloge %}
     \item ${{naloga.sestavljena_resitev}}$
     {% endfor %}
     \end{enumerate}
     '''

    def __init__(self, **kwargs):  # Dodamo kadar želimo da ima naloga dodatne parametre
        super().__init__(**kwargs)

    def _poskusi_sestaviti(self):
        sestavljena_naloga = 'Tukaj sestavimo nalogo'
        sestavljena_resitev = 'Tukaj sestavimo rešitev'
        return {'naloga': sestavljena_naloga, 'resitev': sestavljena_resitev}
