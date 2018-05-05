import random
import sympy


class PogojNiIzpolnjen(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise PogojNiIzpolnjen


def racionalna(dijak = "Padawan",razpon=(-9, 9), st_nicel=3, st_polov=3):
    random.seed(dijak)
    od, do = razpon
    nicle = [random.randint(od, do) for _ in range(st_nicel)]
    poli = [random.randint(od, do) for _ in range(st_polov)]
    preveri(set(nicle) & set(poli) == set())
    return {
        'funkcija': 'x / (x - 1)',
        'nicle': nicle,
        'poli': poli,
    }
def poisci_nicle_polinoma(dijak = "Padawan", od=-7, do=7 , stevilo_nicel=3):
    random.seed(dijak)
    print(dijak)
    nicle = random.sample(range(od, do), stevilo_nicel)  # Naredi seznam treh celih ničel #TODO kako je bolje izbrati ničle*
    x = sympy.symbols('x')
    polinom = '*'.join('(x-{0})'.format(nicla) for nicla in nicle)
    naloga = sympy.latex(sympy.expand(polinom))
    resitev = "Ničle polinoma so " + ', '.join('{0}'.format(nicla) for nicla in nicle) + "."
    return "Poišči ničle polinoma $ %s $." %naloga , resitev


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
#print(poisci_nicle_polinoma())
