import random
import sympy


class PogojNiIzpolnjen(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise PogojNiIzpolnjen


############################## Besedila rešitev
slovarKratkihNalog = {"poisci_nicle_polinoma": "Poišči vse ničle polinoma $p(x)= %s$.",
                      "racionalna" : "Izračunaj ničle in pole racionalne funkcije $q(x) = %s$."} #TODO a je smiselno imeti te slovarje

slovarDolgihNalog= {"poisci_nicle_polinoma": "Poišči ničle polinomov:\n\\begin{enumerate}\n"}

############################## Naloge

def racionalna(seme = "Padawan",razpon=(-9, 9), st_nicel=3, st_polov=3):
    random.seed(seme)
    od, do = razpon
    nicle = [random.randint(od, do) for _ in range(st_nicel)]
    poli = [random.randint(od, do) for _ in range(st_polov)]
    #preveri(set(nicle) & set(poli) == set())
    x = sympy.symbols('x')
    stevec = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
    imenovalec = '*'.join('(x-{0})'.format(pol) for pol in poli)
    naloga = sympy.latex(sympy.expand(stevec)/sympy.expand(imenovalec))
    resitev = "Ničle funkcije so " + ', '.join('{0}'.format(nicla) for nicla in nicle)+", poli pa so "+ ', '.join('{0}'.format(pol) for pol in poli) + "."
    print(naloga)
    return (naloga, resitev)
    # return {
    #     'funkcija': 'x / (x - 1)',
    #     'nicle': nicle,
    #     'poli': poli,
    # }

def nalogaRacionalna(seme = "Padawan",razpon=(-9, 9), st_nicel=3, st_polov=3, primeri = 1):
    if primeri ==1:
        naloga, resitev = racionalna(seme, razpon, st_nicel, st_polov)
        besedilo_naloge = "Izračunaj ničle in pole funkcije $q(x) = %s$."% naloga
        besedilo_resitve = resitev
    else:
        besedilo_naloge= "Poišči ničle in pole funkcij:\n \\begin{enumerate}\n"
        besedilo_resitve ="Rešitve: \n\\begin{enumerate}\n"
        for i in range(1, primeri+1):
            seme +=str(i)
            naloga, resitev = racionalna(seme, razpon, st_nicel, st_polov)
            besedilo_naloge +="\\item $q(x) = %s$\n" % naloga
            besedilo_resitve += "\\item $%s$\n" %resitev
        besedilo_resitve += "\end{enumerate}"
        besedilo_naloge += "\end{enumerate}"
    return (besedilo_naloge, besedilo_resitve )

def poisci_nicle_polinoma(od=-7, do=7 , stevilo_nicel=3, seme = "Padawan", primeri = 1):
    random.seed(seme)
    #print(seme)
    if primeri == 1:
        nicle = [random.randint(od, do) for _ in range(stevilo_nicel)]  # Naredi seznam treh celih ničel
        x = sympy.symbols('x')
        polinom = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
        naloga = slovarKratkihNalog["poisci_nicle_polinoma"] % sympy.latex(sympy.expand(polinom))
        #print(naloga)
        resitev = "Ničle polinoma so " + ', '.join('{0}'.format(nicla) for nicla in nicle) + "."
        return naloga, resitev
    else:
        naloge= slovarDolgihNalog["poisci_nicle_polinoma"]
        resitve="\\begin{enumerate}"
        for i in range(primeri):
            random.seed(seme+str(i))
            nicle = [random.randint(od, do) for _ in
                     range(stevilo_nicel)]  # Naredi seznam treh celih ničel
            x = sympy.symbols('x')
            polinom = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
            naloga = sympy.latex(sympy.expand(polinom))
            naloge += "\item $p(x)=" +naloga +"$\n"
            #print(naloga)
            resitve += "Ničle polinoma so " + ', '.join('{0}'.format(nicla) for nicla in nicle) + ".\n"
        naloge += "\end{enumerate}"
        resitve += "\end{enumerate}"
        return naloge, resitve


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


#print(generiraj(racionalna, 'Funkcija {funkcija} ima ničle: {nicle}', st_polov=5))

#print(poisci_nicle_polinoma( "B",-20,10,4))
#print(poisci_nicle_polinoma(primeri=2))

print(nalogaRacionalna(primeri=3))


