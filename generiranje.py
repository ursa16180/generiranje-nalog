import random
import jinja2
import sympy


class NapacnaNaloga(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise NapacnaNaloga


class Naloga:
    def __init__(self, besedilo_posamezne=None, besedilo_vecih=None, resitev_posamezne=None, resitev_vecih=None,
                 st_nalog=None):
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
            ''')  # TODO REŠITEV - ali vrnem nalogo in rešitev ali samo rešitev
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
            naloga = self.sestavi()
            return {'naloga': self.besedilo_posamezne.render(naloga=naloga),
                    'resitev': self.resitev_posamezne.render(naloga=naloga)}
        else:
            naloge = self.sestavi_vec(self.st_nalog)
            return {'naloga': self.besedilo_vecih.render(naloge=naloge),
                    'resitev': self.resitev_vecih.render(naloge=naloge)}


# ~~~~~~~~~~~~~VZOREC za nalogi
class VzorecNaloge(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template('')
        self.besedilo_vecih = jinja2.Template('')
        self.resitev_posamezne = jinja2.Template('')
        self.resitev_vecih = jinja2.Template('')

    def poskusi_sestaviti(self):
        return {'naloga': 1, 'resitev': 2}


# ~~~~~~~~~~~~~~~~~~~~~1.letnik~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RazstaviVieta(Naloga):
    def __init__(self, minimalna_vrednost=-9, maksimalna_vrednost=9, lazja=True, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template('Razstavi izraz ${{naloga.naloga}}$.')
        self.besedilo_vecih = jinja2.Template('Razstavi naslednje izraze '
                                              '\\begin{enumerate}'
                                              '{% for naloga in naloge %}'
                                              '\\item ${{naloga.naloga}}=$'
                                              '{% endfor %}'
                                              '\\end{enumerate}'
                                              )
        self.resitev_posamezne = jinja2.Template('${{naloga.resitev}}$')
        self.resitev_vecih = jinja2.Template('\\begin{enumerate}'
                                             '{% for naloga in naloge %}'
                                             '\\item ${{naloga.resitev}}$'
                                             '{% endfor %}'
                                             '\\end{enumerate}')
        if minimalna_vrednost > maksimalna_vrednost:
            self.minimalna_vrednost = maksimalna_vrednost
            self.maksimalna_vrednost = minimalna_vrednost
        else:
            self.minimalna_vrednost = minimalna_vrednost
            self.maksimalna_vrednost = maksimalna_vrednost
        self.lazja = lazja

    def poskusi_sestaviti(self):
        x1 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        x2 = random.randint(self.minimalna_vrednost, self.maksimalna_vrednost)
        if not self.lazja:
            a = random.randint(1, 4)
        else:
            a = 1
        x = sympy.symbols('x')
        problem = "({0}*x-{1})*(x-{2})".format(a, x1, x2)
        naloga = sympy.latex(sympy.expand(problem))
        resitev = naloga + "=" + sympy.latex(sympy.simplify(problem))

        return {'naloga': naloga, 'resitev': resitev}


# ~~~~~~~~~~~~~~~~~~~~~2.letnik~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~3.letnik~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Polinom(Naloga):
    def __init__(self, min_stopnja=3, max_stopnja=3, min_nicla=-9, max_nicla=9, **kwargs):
        super().__init__(self, **kwargs)
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

        self.resitev_vecih = jinja2.Template(  # TODO lepša slovnica v zapisu rešitev
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
        if min_stopnja > max_stopnja:
            self.max_stopnja = min_stopnja
        else:
            self.max_stopnja = max_stopnja
        self.min_nicla = min_nicla  ##TODO kaj če min ničla večja od max_nicle? Raise Error?
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        nicle = []
        stopnja = random.randint(self.min_stopnja, self.max_stopnja)
        vodilni_koeficient = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

        for _ in range(stopnja):
            nicla = random.randint(self.min_nicla, self.max_nicla)
            nicle.append(nicla)
        preveri(self.min_stopnja <= len(nicle) <= self.max_stopnja)
        x = sympy.symbols('x')
        polinom = sympy.latex(
            sympy.expand('{0}*('.format(vodilni_koeficient)+'*'.join('(x-{0})'.format(nicla) for nicla in nicle)+')'))  # jinja2 ne prebavi fukcije sympy.latex
        return {
            'polinom': polinom,
            'nicle': ', '.join('${0}$'.format(nicla) for nicla in nicle),
        }


class DolociNiclePoleAsimptotoRacionalne(Naloga):
    def __init__(self, min_stopnja_stevca=3, max_stopnja_stevca=3, min_stopnja_imenovalca=3, max_stopnja_imenovalca=3,
                 min_nicla=-9, max_nicla=9, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            'Določi ničle, pole in asimptoto racionalne funkcije $r(x)={{naloga.naloga}}$')
        self.besedilo_vecih = jinja2.Template('Določi ničle, pole in asimptoto naslednjih racionalnih funkcij'
                                              '\\begin{enumerate}'
                                              '{% for naloga in naloge%}'
                                              '\\item $r(x)={{naloga.naloga}}$'
                                              '{% endfor %}'
                                              '\\end{enumerate}')
        self.resitev_posamezne = jinja2.Template(
            'Racionalna funkcija ${{naloga.naloga}}$ ima ničle {{naloga.resitev[0]}}, pole {{naloga.resitev[1]}} in '
            'asimptoto $y={{naloga.resitev[2]}}$')
        self.resitev_vecih = jinja2.Template('\\begin{enumerate}'
                                             '{% for naloga in naloge%}'
                                             '\\item $r(x)={{naloga.naloga}}$ ima ničle {{naloga.resitev[0]}}, '
                                             'pole {{naloga.resitev[1]}} in asimptoto $y={{naloga.resitev[2]}}$'
                                             '{% endfor %}'
                                             '\\end{enumerate}')
        self.min_stopnja_stevca = min_stopnja_stevca
        self.max_stopnja_stevca = max_stopnja_stevca
        self.min_stopnja_imenovalca = min_stopnja_imenovalca
        self.max_stopnja_imenovalca = max_stopnja_imenovalca
        self.min_nicla = min_nicla
        self.max_nicla = max_nicla

    def poskusi_sestaviti(self):
        nicle = []
        stopnja_stevca = random.randint(self.min_stopnja_stevca, self.max_stopnja_stevca)
        vodilni_stevca = random.choice([-3, -2, -1, 1, 2, 3])
        for _ in range(stopnja_stevca):
            nicla = random.randint(self.min_nicla, self.max_nicla)
            nicle.append(nicla)
        poli = []
        stopnja_imenovalca = random.randint(self.min_stopnja_imenovalca, self.max_stopnja_imenovalca)
        vodilni_imenovalca = random.choice([-3, -2, -1, 1, 2, 3])
        for _ in range(stopnja_imenovalca):
            pol = random.randint(self.min_nicla, self.max_nicla)
            poli.append(pol)
        preveri(set(nicle) & set(poli) == set())
        x = sympy.symbols('x')
        stevec = '{0}*('.format(vodilni_stevca) + '*'.join('(x-{0})'.format(nicla) for nicla in nicle) + ')'
        imenovalec = '{}*('.format(vodilni_imenovalca) + '*'.join('(x-{0})'.format(pol) for pol in poli) + ')'
        if stopnja_stevca < stopnja_imenovalca:
            asimptota = 0
        elif stopnja_stevca == stopnja_imenovalca:
            asimptota = sympy.latex(sympy.nsimplify(vodilni_stevca/vodilni_imenovalca))
        elif stopnja_stevca > stopnja_imenovalca:
            q, r = sympy.div(stevec, imenovalec, x)
            asimptota = sympy.latex(q)

        naloga = sympy.latex(sympy.expand(stevec) / sympy.expand(imenovalec))
        resitev = (
            ', '.join('${0}$'.format(nicla) for nicla in nicle),
            ', '.join('${0}$'.format(pol) for pol in poli),
            asimptota)

        return {'naloga': naloga, 'resitev': resitev}

# ~~~~~~~~~~~~~~~~~~~~~4.letnik~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
