import jinja2
import sympy

def mojLatex(izraz):
    return sympy.latex(izraz).replace(r'\'','')
    # def _print_tuple(self, expr):
    #     return r"\left( %s\right)" % \
    #         r", \  ".join([self._print(i) for i in expr])

class NapacnaNaloga(Exception):
    pass

class MinMaxNapaka(ValueError):
    def __init__(self):
        ValueError.__init__(self, "Minimalna vrednost mora biti manjša ali enaka maksimalni vrednosti.")

def preveri(pogoj):
    if not pogoj:
        raise NapacnaNaloga

class Naloga:
    """Razred Naloga ima atrubute za splošno besedilo posamezne, besedilo večih, rešitev posamezne in reštev večih."""
    besedilo_posamezne = '''
                        Reši nalogo: ${{ naloga }}$
                    '''
    besedilo_vecih = '''
                        Reši sledeče naloge:
                        \\begin{enumerate}
                        {% for naloga in naloge %}
                        \\item${{ naloga }}$
                        {% endfor %}
                        \\end{enumerate}
                    '''
    resitev_posamezne = '''
                        Rešitev: ${{ naloga }}$ 
                    '''
    resitev_vecih = '''
                        Rešitve nalog:
                        \\begin{enumerate}
                        {% for naloga in naloge %}
                        \\item${{ naloga }}$
                        {% endfor %}
                        \\end{enumerate}
                '''
    def __init__(self, besedilo_naloge=None, st_nalog=None, **kwargs): #TODO kdaj je lahko besedilo posamezne None?
        self.st_nalog = st_nalog

        if besedilo_naloge.besedilo_posamezne is not None: #TODO besedilo posazmezne = besedilo naloge?
            self.besedilo_posamezne =jinja2.Template(besedilo_naloge.besedilo_posamezne)
        if besedilo_naloge.besedilo_vecih is not None:
            self.besedilo_vecih =jinja2.Template(besedilo_naloge.besedilo_vecih)
        if besedilo_naloge.resitev_posamezne is not None:
            self.resitev_posamezne =jinja2.Template(besedilo_naloge.resitev_posamezne)
        if besedilo_naloge.resitev_vecih is not None:
            self.resitev_vecih =jinja2.Template(besedilo_naloge.resitev_vecih)

    def poskusi_sestaviti(self):
        pass

    def sestavi(self):
        """Sestavi nalogo ali v primeru Napacne naloge, poskuša sestaviti novo."""
        while True:
            try:
                return self.poskusi_sestaviti()
            except NapacnaNaloga:
                pass

    def sestavi_vec(self, stevilo_nalog):
        """Metoda sestavi_vec sestavi več nalog.
        :type stevilo_nalog: int
        :param stevilo_nalog: koliko nalog določenega razreda želimo"""
        naloge = []
        for _ in range(stevilo_nalog):
            naloge.append(self.sestavi())
        return naloge

    def besedilo(self):
        # TODO expand funkcija samo podalsuje senzame
        # razsiritve = {
        #     'latex': sympy.latex, 'expand': sympy.expand
        # }
        # print(self.besedilo_posamezne)
        # self.besedilo_posamezne.globals.extend(razsiritve)
        # self.besedilo_vecih.globals.extend(razsiritve)
        # self.resitev_posamezne.globals.extend(razsiritve)
        # self.resitev_vecih.globals.extend(razsiritve)
        razsiritve = {
            'latex': sympy.latex, 'expand': sympy.expand
        }

        for kljuc, vrednost in razsiritve.items():
            self.besedilo_posamezne.globals[kljuc] = vrednost
            self.besedilo_vecih.globals[kljuc] = vrednost
            self.resitev_posamezne.globals[kljuc] = vrednost
            self.resitev_vecih.globals[kljuc] = vrednost

        if self.st_nalog is None or self.st_nalog==1:
            naloga = self.sestavi()
            return {'naloga': self.besedilo_posamezne.render(naloga=naloga),
                    'resitev': self.resitev_posamezne.render(naloga=naloga)}

        else:
            naloge = self.sestavi_vec(self.st_nalog)
            return {'naloga': self.besedilo_vecih.render(naloge=naloge),
                    'resitev': self.resitev_vecih.render(naloge=naloge)}
