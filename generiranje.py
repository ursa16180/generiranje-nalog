import jinja2
import sympy
import importlib

sympy_printing_latex = importlib.import_module('sympy.printing.latex')


class NapacnaNaloga(Exception):
    """
    Izjema, kadar sestavljena naloga ne ustreza pogojem.
    """
    pass


MinMaxNapaka = ValueError("Minimalna vrednost mora biti manjša ali enaka maksimalni vrednosti.")


def preveri(pogoj):
    """
    Funkcija preveri, če sestavljena naloga ustreza pogojem, sicer javi napako NapacnaNaloga.

    :param pogoj: True, če naloga ustreza pogojem in False, kadar naloga ne ustreza pogojem
    """
    if not pogoj:
        raise NapacnaNaloga


class MojLatexPrinter(sympy_printing_latex.LatexPrinter):
    """
    Razred MojLatexPrinter je popravljena različica razreda LatexPrinter iz paketa sympy. Popravljeno je izpisovanje tuple-ov brez presledka.
    """

    def _print_tuple(self, expr):
        return r"\left( %s\right)" % r", ".join([self._print(i) for i in expr])


def moj_latex(expr):
    """
    Funkcija kliče razred MojLatexPrinter in nastavi izpis naravnega logaritma kot :math:`ln`.

    :param expr: niz
    """
    settings = {
        'ln_notation': True
    }
    return MojLatexPrinter(settings).doprint(expr)


class Naloga:
    """ Razred Naloga je splošni razred za posamezne naloge. Privzete ima splošna besedila nalog in rešitev, ki jih posamezne naloge lahko prepišejo.

    :param st_nalog: stevilo primerov posamezne naloge
    :param besedilo_posamezne: besedilo naloge
    :param besedilo_vecih: besedilo za nalogo z več primeri
    :param resitev_posamezne: besedilo za rešitev naloge
    :param resitev_vecih: besedilo za rešitev naloge z več primeri

    """
    besedilo_posamezne = r'''Reši nalogo: ${{ naloga }}$'''
    besedilo_vecih = r'''
        Reši sledeče naloge:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{ naloga }}$
        {% endfor %}
        \end{enumerate}
        '''
    resitev_posamezne = r'''Rešitev: ${{ naloga }}$'''
    resitev_vecih = r'''Rešitve nalog:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item${{ naloga }}$
        {% endfor %}
        \end{enumerate}
        '''

    def __init__(self, besedilo_posamezne=None, besedilo_vecih=None, resitev_posamezne=None, resitev_vecih=None,
                 st_nalog=None):
        self.st_nalog = st_nalog

        if besedilo_posamezne is not None:
            self.besedilo_posamezne = besedilo_posamezne

        if besedilo_vecih is not None:
            self.besedilo_vecih = besedilo_vecih

        if resitev_posamezne is not None:
            self.resitev_posamezne = resitev_posamezne

        if resitev_vecih is not None:
            self.resitev_vecih = resitev_vecih

    def _poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo."""
        pass

    def sestavi(self):
        """Sestavi nalogo, ki ustreza pogojem."""
        while True:
            try:
                return self._poskusi_sestaviti()
            except NapacnaNaloga:
                pass

    def sestavi_vec(self, stevilo_nalog):
        """
        Sestavi nalogo z več primeri

        :param stevilo_nalog: stevilo primerov posamezne naloge

        """
        naloge = []
        for _ in range(stevilo_nalog):
            naloge.append(self.sestavi())
        return naloge

    def besedilo(self):
        """
        Ustvari predloge besedila in rešitev ter vanj vstavi vrednosti posameznih primerov.
        """
        razsiritve = {
            'latex': moj_latex, 'expand': sympy.expand
        }

        template_besedilo_posamezne = jinja2.Template(self.besedilo_posamezne)
        template_besedilo_vecih = jinja2.Template(self.besedilo_vecih)
        template_resitev_posamezne = jinja2.Template(self.resitev_posamezne)
        template_resitev_vecih = jinja2.Template(self.resitev_vecih)

        for kljuc, vrednost in razsiritve.items():
            template_besedilo_posamezne.globals[kljuc] = vrednost
            template_besedilo_vecih.globals[kljuc] = vrednost
            template_resitev_posamezne.globals[kljuc] = vrednost
            template_resitev_vecih.globals[kljuc] = vrednost

        if self.st_nalog is None or self.st_nalog == 1:
            naloga = self.sestavi()
            return {'naloga': template_besedilo_posamezne.render(naloga=naloga),
                    'resitev': template_resitev_posamezne.render(naloga=naloga)}

        else:
            naloge = self.sestavi_vec(self.st_nalog)

            return {'naloga': template_besedilo_vecih.render(naloge=naloge),
                    'resitev': template_resitev_vecih.render(naloge=naloge)}
