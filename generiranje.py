import random
import jinja2
import sympy


class NapacnaNaloga(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise NapacnaNaloga


class Naloga:
    def __init__(self, besedilo_posamezne=None, besedilo_vecih=None, resitev_posamezne=None, resitev_vecih=None, st_nalog=None):
        self.st_nalog = st_nalog
        if besedilo_posamezne:
            self.besedilo_posamezne = besedilo_posamezne
        else:
            self.besedilo_posamezne = jinja2.Template('''
                Reši nalogo: ${{ naloga }}$
            ''')
        if besedilo_vecih:
            self.besedilo_vecih = besedilo_vecih
        else:
            self.besedilo_vecih = jinja2.Template('''
                Reši sledeče naloge:
                \\begin{enumerate}
                {% for naloga in naloge %}
                \\item${{ naloga }}$
                {% endfor %}
                \\end{enumerate}
            ''')
        if resitev_posamezne:
            self.resitev_posamezne = resitev_posamezne
        else:
            self.resitev_posamezne = jinja2.Template('''
                Rešitev: ${{ naloga }}$ 
            ''')#TODO REŠITEV - ali vrnem nalogo in rešitev ali samo rešitev
        if resitev_vecih:
            self.resitev_vecih = resitev_vecih
        else:
            self.resitev_vecih = jinja2.Template('''
                Rešitve nalog:
                \\begin{enumerate}
                {% for naloga in naloge %}
                \\item${{ naloga }}$
                {% endfor %}
                \\end{enumerate}
            ''')

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
            naloga=self.sestavi()
            return {'naloga' : self.besedilo_posamezne.render(naloga=naloga), 'resitev': self.resitev_posamezne.render(naloga=naloga)}
        else:
            naloge = self.sestavi_vec(self.st_nalog)
            return {'naloga' : self.besedilo_vecih.render(naloge=naloge), 'resitev': self.resitev_vecih.render(naloge=naloge)}


class Polinom(Naloga):
    def __init__(self, min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, **kwargs):
        super().__init__(self,**kwargs)
        self.besedilo_posamezne = jinja2.Template(
            '''Poišči ničle polinoma $p(x)={{ naloga.polinom }}$.''')

        self.besedilo_vecih = jinja2.Template(
            '''Poišči ničle sledečih polinomov:
            \\begin{enumerate}
            {% for naloga in naloge %}
            \\item $p(x)={{ naloga.polinom }}$
            {% endfor %}
            \\end{enumerate}''')
        self.resitev_posamezne = jinja2.Template(
            '''
            Ničle polinoma $p(x)={{ naloga.polinom }}$ so {{naloga.nicle}}.
        ''')

        self.resitev_vecih = jinja2.Template( #TODO lepša slovnica v zapisu rešitev
            '''Ničle sledečih polinomov:
            \\begin{enumerate}
            {% for naloga in naloge %}
            \\item $p(x)={{ naloga.polinom}}$ ima ničle {{naloga.nicle }}.
            {% endfor %}
            \\end{enumerate}''')
        if max_stopnja < min_stopnja:
            self.min_stopnja = max_stopnja
        else:
            self.min_stopnja = min_stopnja
        if min_stopnja>max_stopnja:
            self.max_stopnja = min_stopnja
        else:
            self.max_stopnja = max_stopnja
        self.min_nicla = min_nicla ##TODO kaj če min ničla večja od max_nicle? Raise Error?
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        nicle = []
        stopnja = random.randint(self.min_stopnja, self.max_stopnja)
        for _ in range(stopnja):
            nicla = random.randint(self.min_nicla, self.max_nicla)
            nicle.append(nicla)
        preveri(self.min_stopnja <= len(nicle) <= self.max_stopnja)
        x = sympy.symbols('x')
        polinom = sympy.latex(sympy.expand('*'.join('(x-{0})'.format(nicla) for nicla in nicle))) #jinja2 ne prebavi fukcije sympy.latex
        return {
            'polinom': polinom,
            'nicle': ', '.join('${0}$'.format(nicla) for nicla in nicle),
        }


