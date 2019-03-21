import jinja2
import sympy


class NapacnaNaloga(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise NapacnaNaloga


class Naloga:
    def __init__(self, besedilo_posamezne=None, besedilo_vecih=None, resitev_posamezne=None, resitev_vecih=None,
                 st_nalog=None, **kwargs):
        self.st_nalog = st_nalog

        if besedilo_posamezne is None:
            besedilo_posamezne = '''
                Reši nalogo: ${{ naloga }}$
            '''

        if besedilo_vecih is None:
            besedilo_vecih = r'''
                Reši sledeče naloge:
                \begin{enumerate}
                {% for naloga in naloge %}
                \item ${{ naloga }}$
                {% endfor %}
                \end{enumerate}
            '''

        if resitev_posamezne is None:
            resitev_posamezne = r'''
                Rešitev: ${{ naloga }}$ 
            '''
        if resitev_vecih is None:
            resitev_vecih = r'''
                Rešitve nalog:
                \begin{enumerate}
                {% for naloga in naloge %}
                \item ${{ naloga }}$
                {% endfor %}
                \end{enumerate}
            '''

        self.besedilo_posamezne = jinja2.Template(besedilo_posamezne)
        self.besedilo_vecih = jinja2.Template(besedilo_vecih)
        self.resitev_posamezne = jinja2.Template(resitev_posamezne)
        self.resitev_vecih = jinja2.Template(resitev_vecih)

        razsiritve = {
            'latex': sympy.latex, 'expand': sympy.expand
        }

        self.besedilo_posamezne.globals.extend(razsiritve)
        self.besedilo_vecih.globals.extend(razsiritve)
        self.resitev_posamezne.globals.extend(razsiritve)
        self.resitev_vecih.globals.extend(razsiritve)

    def poskusi_sestaviti(self):
        pass

    def sestavi(self):
        while True:
            try:
                return self.poskusi_sestaviti()
            except NapacnaNaloga:
                pass

    def sestavi_vec(self, stevilo_nalog):
        naloge = []
        for _ in range(stevilo_nalog):
            naloge.append(self.sestavi())
        return naloge

    def besedilo(self):

        if self.st_nalog is None:
            naloga = self.sestavi()
            return {'naloga': self.besedilo_posamezne.render(naloga=naloga),
                    'resitev': self.resitev_posamezne.render(naloga=naloga)}

        else:
            naloge = self.sestavi_vec(self.st_nalog)
            return {'naloga': self.besedilo_vecih.render(naloge=naloge),
                    'resitev': self.resitev_vecih.render(naloge=naloge)}
