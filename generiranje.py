import random
import jinja2
import sympy


class NapacnaNaloga(Exception):
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~Pomožne funkcije
def seznamPolovick(od=-10, do=10):
    return [sympy.Rational(x, 2) for x in range(2 * od, 2 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def seznamTretinj(od=-10, do=10):
    return [sympy.Rational(x, 3) for x in range(3 * od, 3 * (do + 1)) if x != 0]
    # funkcija vrne seznam polovičk brez ničle


def izberiKoordinato(od=-10, do=10):
    koordinata = random.randint(od, do)
    return koordinata

#~~~~~


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
        #TODO ali se da kako drugače uvoziti funkcijo v jinjo
        self.besedilo_posamezne.globals['latex']=sympy.latex
        self.besedilo_vecih.globals['latex']=sympy.latex
        self.resitev_posamezne.globals['latex']=sympy.latex
        self.resitev_vecih.globals['latex']=sympy.latex

        if self.st_nalog is None:
            naloga = self.sestavi()
            return {'naloga': self.besedilo_posamezne.render(naloga=naloga),
                    'resitev': self.resitev_posamezne.render(naloga=naloga)}

        else:
            naloge = self.sestavi_vec(self.st_nalog)
            return {'naloga': self.besedilo_vecih.render(naloge=naloge),
                    'resitev': self.resitev_vecih.render(naloge=naloge)}


# ~~~~~~~~~~~~~VZOREC za nalogo
class VzorecNaloge(Naloga):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(r''' ''')
        self.besedilo_vecih = jinja2.Template(r'''
        \begin{enumerate}
        {% for naloga in naloge %}
        \item
        {% endfor %}
        \end{enumerate}
        ''')
        self.resitev_posamezne = jinja2.Template(r''' ''')
        self.resitev_vecih = jinja2.Template(r'''
        \begin{enumerate}
         {% for naloga in naloge %}
         \item
         {% endfor %}
         \end{enumerate}
         ''')

    def poskusi_sestaviti(self):
        return {'naloga': 1, 'resitev': 2}


# ~~~~~~~~~~~~~~~~~~~~~1.letnik~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RazstaviVieta(Naloga): #TODO preveri jinja latex
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
            a = random.randint(2, 4)
        else:
            a = 1
        x = sympy.symbols('x')
        problem = "({0}*x-{1})*(x-{2})".format(a, x1, x2)
        naloga = sympy.latex(sympy.expand(problem))
        resitev = naloga + "=" + sympy.latex(sympy.simplify(problem))

        return {'naloga': naloga, 'resitev': resitev}


class RazdaljaMedTockama(Naloga):  # Todo težja racionalne koordinate? #TODO preveri jinja latex
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)
        self.besedilo_posamezne = jinja2.Template(
            r'''Natančno izračunaj razdaljo med točkama $A({{naloga.x1}},{{naloga.y1}})$ in $B({{naloga.x2}},{{naloga.y2}})$.''')
        self.besedilo_vecih = jinja2.Template(r'''Natančno izračunaj razdaljo med točkama
                                              \begin{enumerate}
                                              {% for naloga in naloge %}
                                              \item $A({{naloga.x1}},{{naloga.y1}})$ in $B({{naloga.x2}},{{naloga.y2}})$
                                              {% endfor %}
                                              \end{enumerate}'''
                                              )
        self.resitev_posamezne = jinja2.Template(r'''$d(A,B)={{naloga.razdalja}}$''')
        self.resitev_vecih = jinja2.Template(r'''\begin{enumerate}
                                             {% for naloga in naloge %}
                                             \item $d(A,B)={{naloga.razdalja}}$
                                             {% endfor %}
                                             \end{enumerate}''')

    def poskusi_sestaviti(self):
        x1 = izberiKoordinato()
        y1 = izberiKoordinato()
        x2 = izberiKoordinato()
        y2 = izberiKoordinato()
        preveri(x1 != x2 and y1 != y2)
        razdalja = sympy.latex(sympy.simplify(sympy.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))))
        return {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'razdalja': razdalja}
