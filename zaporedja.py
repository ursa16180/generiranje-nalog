from generiranje import*


class SplosniClenAritmeticnegaZaporedja(Naloga): #TODO preveri jinja latex
    def __init__(self, od=-5, do=5, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            "Določi splošni člen aritmetičnega zaporedja, če je $a_{ {{naloga.naloga[0]}} }={{naloga.naloga[1]}}$ in $a_{ {{naloga.naloga[2]}} }={{naloga.naloga[3]}}$")
        self.besedilo_vecih = jinja2.Template(
            'Določi splošne člene aritmetičnih zaporedij, če poznaš naslednja dva člena'
            '\\begin{enumerate}'
            '{% for naloga in naloge %}'
            '\\item $a_{ {{naloga.naloga[0]}} }={{naloga.naloga[1]}}$ in $a_{ {{naloga.naloga[2]}} }={{naloga.naloga[3]}}$'
            '{% endfor %}'
            '\\end{enumerate}')
        self.resitev_posamezne = jinja2.Template('Splošni člen zaporedja je ${{naloga.resitev}}$.')
        self.resitev_vecih = jinja2.Template(r'''Spločni členi aritmetičnih zaporedij so: '
                                             '\\begin{enumerate}'
                                             '{% for naloga in naloge %}'
                                             '\\item ${{naloga.resitev}}$'
                                             '{% endfor %}'
                                             '\\end{enumerate}''')
        if not (od < do):
            raise ValueError('Spodnja meja je večja od zgornje')
        assert od < do
        if do < od:
            self.od = do
            self.do = od
        else:
            self.od = od
            self.do = do

    def poskusi_sestaviti(self):
        seznam_polovick = [x / 2 for x in range(2 * self.od, 2 * self.do + 1) if x != 0]
        a1 = random.choice(seznam_polovick)
        d = random.choice(seznam_polovick)
        n1 = random.randrange(2, 10)
        n2 = random.randrange(2, 15)
        preveri(n1 != n2)
        an1 = sympy.latex(sympy.nsimplify(a1 + (n1 - 1) * d))
        an2 = sympy.latex(sympy.nsimplify(a1 + (n2 - 1) * d))
        naloga = (n1, an1, n2, an2)
        n = sympy.symbols('n')
        sympy.simplify(a1 + d * (n - 1))

        resitev = sympy.latex("{0}+({1})(n-1)".format(sympy.latex(sympy.nsimplify(a1)), sympy.latex(
            sympy.nsimplify(d))))  # TODO lepše izpisovanje množenja
        return {'naloga': naloga, 'resitev': resitev}