import random
import sympy


class PogojNiIzpolnjen(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise PogojNiIzpolnjen


############################## Besedila rešitev
slovarKratkihNalog = {"poisci_nicle_polinoma": "Poišči vse ničle polinoma $p(x)= %s$.",
                      "racionalna": "Izračunaj ničle in pole racionalne funkcije $q(x) = %s$."}  # TODO a je smiselno imeti te slovarje

slovarDolgihNalog = {"poisci_nicle_polinoma": "Poišči ničle polinomov:\n\\begin{enumerate}\n"}


############################## Naloge

############################## 1.letnik
def narisiLinearnoFunkcijo():
    return "TODO"

############################## 2.letnik

def izračunajNicleTemeKvadratne():
    return "TODO"

############################## 3.letnik
def racionalna(seme="Padawan", razpon=(-9, 9), st_nicel=3, st_polov=3):
    random.seed(seme)
    od, do = razpon
    nicle = [random.randint(od, do) for _ in range(st_nicel)]
    poli = [random.randint(od, do) for _ in range(st_polov)]
    # preveri(set(nicle) & set(poli) == set()) #TODO ponavlej dokler ni vredu
    x = sympy.symbols('x')
    stevec = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
    imenovalec = '*'.join('(x-{0})'.format(pol) for pol in poli)
    naloga = sympy.expand(stevec) / sympy.expand(imenovalec)
    resitev = "Ničle funkcije so " + ', '.join('{0}'.format(nicla) for nicla in nicle) + ", poli pa so " + ', '.join(
        '{0}'.format(pol) for pol in poli) + "."
    # print(naloga)
    return (naloga, resitev)
    # return {
    #     'funkcija': 'x / (x - 1)',
    #     'nicle': nicle,
    #     'poli': poli,
    # }


def nalogaNiclePoliRacionalne(seme="Padawan", razpon=(-9, 9), st_nicel=3, st_polov=3, primeri=1):
    if primeri == 1:
        naloga, resitev = racionalna(seme, razpon, st_nicel, st_polov)
        besedilo_naloge = "Izračunaj ničle in pole funkcije $q(x) = %s$." % sympy.latex(naloga)
        besedilo_resitve = resitev
    else:
        besedilo_naloge = "Poišči ničle in pole funkcij:\n \\begin{enumerate}\n"
        besedilo_resitve = "Rešitve: \n\\begin{enumerate}\n"
        for i in range(1, primeri + 1):
            seme += str(i)
            naloga, resitev = racionalna(seme, razpon, st_nicel, st_polov)
            besedilo_naloge += "\\item $q(x) = %s$\n" % sympy.latex(naloga)
            besedilo_resitve += "\\item $%s$\n" % resitev
        besedilo_resitve += "\end{enumerate}"
        besedilo_naloge += "\end{enumerate}"
    return (besedilo_naloge, besedilo_resitve)


def nalogaGrafRacionalne(seme="Padawan", razpon=(-9, 9), st_nicel=3, st_polov=3, primeri=1):
    if primeri == 1:
        naloga, resitev = racionalna(seme, razpon, st_nicel, st_polov)
        besedilo_naloge = "Nariši graf funkcije $q(x) = %s$." % sympy.latex(naloga)
        graf_funkcije = str(naloga).replace("**", "^")
        besedilo_resitve = "\\begin{tikzpicture}\n\\begin{axis}[axis lines=middle, xlabel=$x$, ylabel=$y$]\n\\addplot[domain =-7:7, color=black]{%s};\n\\end{axis}\n\\end{tikzpicture}\n" % graf_funkcije
    else:
        besedilo_naloge = "Nariši grafe funkcij:\n \\begin{enumerate}\n"
        besedilo_resitve = "Rešitve: \n\\begin{enumerate}\n"
        for i in range(1, primeri + 1):
            seme += str(i)
            naloga, resitev = racionalna(seme, razpon, st_nicel, st_polov)
            besedilo_naloge += "\item $q(x) = %s$\n" % sympy.latex(naloga)
            graf_funkcije = str(naloga).replace("**", "^")
            besedilo_resitve += "\item \\begin{tikzpicture}\n\\begin{axis}[axis lines=middle, xlabel=$x$, " \
                                "ylabel=$y$]\n\\addplot[domain =-7:7, color=black]{%s};\n\end{axis}\n\end{tikzpicture}\n" % graf_funkcije  # TODO nariši asimpotote
        besedilo_resitve += "\end{enumerate}"
        besedilo_naloge += "\end{enumerate}"
    return (besedilo_naloge, besedilo_resitve)


def poisci_nicle_polinoma(od=-7, do=7, stevilo_nicel=3, seme="Padawan", primeri=1):
    random.seed(seme)
    # print(seme)
    if primeri == 1:
        nicle = [random.randint(od, do) for _ in range(stevilo_nicel)]  # Naredi seznam treh celih ničel
        x = sympy.symbols('x')
        polinom = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
        naloga = slovarKratkihNalog["poisci_nicle_polinoma"] % sympy.latex(sympy.expand(polinom))
        # print(naloga)
        resitev = "Ničle polinoma so " + ', '.join('{0}'.format(nicla) for nicla in nicle) + "."
        return naloga, resitev
    else:
        naloge = slovarDolgihNalog["poisci_nicle_polinoma"]
        resitve = "\\begin{enumerate}"
        for i in range(primeri):
            random.seed(seme + str(i))
            nicle = [random.randint(od, do) for _ in
                     range(stevilo_nicel)]  # Naredi seznam treh celih ničel
            x = sympy.symbols('x')
            polinom = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
            naloga = sympy.latex(sympy.expand(polinom))
            naloge += "\item $p(x)=" + naloga + "$\n"
            # print(naloga)
            resitve += "\item Ničle polinoma so " + ', '.join('{0}'.format(nicla) for nicla in nicle) + ".\n"
        naloge += "\end{enumerate}"
        resitve += "\end{enumerate}"
        return naloge, resitve

############################## 4.letnik

def splosniClenAritmericnegaZaporedja(od=-5, do=5, seme="Padawan", primeri=1):
    seznamPolovick = [x * (1 / 2) for x in range(2 * od, 2 * do)]
    seznamPolovick.remove(0)  # TODO numpy za seznam polovičk?
    if primeri == 1:
        random.seed(seme)
        a1 = random.choice(seznamPolovick)
        d = random.choice(seznamPolovick)
        n1 = random.randrange(2, 10)
        n2 = random.randrange(2, 15)
        # preveri(n1 != n2) #TODO preveri
        an1 = sympy.latex(sympy.nsimplify(a1 + (n1 - 1) * d))
        an2 = sympy.latex(sympy.nsimplify(a1 + (n2 - 1) * d))
        besedilo_naloge = "Določi splošni člen aritmetičnega zaporedja, če je $a_{{{0}}}={1}$ in $a_{{{2}}}={3}$." \
            .format(n1, an1, n2, an2)
        besedilo_rešitve = "$a_n={0}+(n-1)*{1}$".format(sympy.latex(sympy.nsimplify(a1)),
                                                        sympy.latex(sympy.nsimplify(d)))
        return besedilo_naloge, besedilo_rešitve
    else:
        besedilo_naloge = "Določi splošni člen aritmetičnega zaporedja, če je:\n \\begin{enumerate}\n"
        besedilo_resitve = "Splošni člen zaporedja je:\n \\begin{enumerate}\n"
        for i in range(1, primeri + 1):
            random.seed(seme + str(i))
            a1 = random.choice(seznamPolovick)
            d = random.choice(seznamPolovick)
            n1 = random.randrange(2, 10)
            n2 = random.randrange(2, 15)
            # preveri(n1 != n2) #TODO preveri
            an1 = sympy.latex(sympy.nsimplify(a1 + (n1 - 1) * d))
            an2 = sympy.latex(sympy.nsimplify(a1 + (n2 - 1) * d))
            besedilo_naloge += "\item $a_{{{0}}}={1}$ in $a_{{{2}}}={3}$\n".format(n1, an1, n2, an2)
            besedilo_resitve += "\item $a_n={0}+(n-1)*{1}$\n".format(sympy.latex(sympy.nsimplify(a1)),
                                                                     sympy.latex(sympy.nsimplify(d)))
        besedilo_naloge += "\end{enumerate}"
        besedilo_resitve += "\end{enumerate}"
        return besedilo_naloge, besedilo_resitve


def poskusi_sestaviti(naloga, parametri):
    try:
        return naloga(**parametri)
    except PogojNiIzpolnjen:
        return


def generiraj(naloga, vzorec, **parametri):
    podatki = None
    while podatki is None:
        podatki = poskusi_sestaviti(naloga, parametri)
    return vzorec.format(**podatki)

# print(generiraj(racionalna, 'Funkcija {funkcija} ima ničle: {nicle}', st_polov=5))

# print(poisci_nicle_polinoma( "B",-20,10,4))
# print(poisci_nicle_polinoma(primeri=2))

# print(nalogaRacionalna(primeri=3))
# print(splosniClenAritmericnegaZaporedja(primeri=2))
