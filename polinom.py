from generiranje import *


class Polinom(Naloga): #TODO preveri jinja latex
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
        print("poskusi sestavit Polimom")
        nicle = []
        stopnja = random.randint(self.min_stopnja, self.max_stopnja)
        vodilni_koeficient = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

        for _ in range(stopnja):
            nicla = random.randint(self.min_nicla, self.max_nicla)
            nicle.append(nicla)
        preveri(self.min_stopnja <= len(nicle) <= self.max_stopnja)
        x = sympy.symbols('x')
        polinom = sympy.latex(
            sympy.expand('{0}*('.format(vodilni_koeficient) + '*'.join(
                '(x-{0})'.format(nicla) for nicla in nicle) + ')'))  # jinja2 ne prebavi fukcije sympy.latex
        print(polinom)
        return {
            'polinom': polinom,
            'nicle': ', '.join('${0}$'.format(nicla) for nicla in nicle),
        }


class DolociNiclePoleAsimptotoRacionalne(Naloga): #TODO preveri jinja latex
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
            asimptota = sympy.latex(sympy.nsimplify(vodilni_stevca / vodilni_imenovalca))
        elif stopnja_stevca > stopnja_imenovalca:
            q, r = sympy.div(stevec, imenovalec, x)
            asimptota = sympy.latex(q)

        naloga = sympy.latex(sympy.expand(stevec) / sympy.expand(imenovalec))
        resitev = (
            ', '.join('${0}$'.format(nicla) for nicla in nicle),
            ', '.join('${0}$'.format(pol) for pol in poli),
            asimptota)

        return {'naloga': naloga, 'resitev': resitev}