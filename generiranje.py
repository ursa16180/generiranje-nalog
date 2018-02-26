import random


class PogojNiIzpolnjen(Exception):
    pass


def preveri(pogoj):
    if not pogoj:
        raise PogojNiIzpolnjen


def racionalna(razpon=(-9, 9), st_nicel=3, st_polov=3):
    od, do = razpon
    nicle = [random.randint(od, do) for _ in range(st_nicel)]
    poli = [random.randint(od, do) for _ in range(st_polov)]
    preveri(set(nicle) & set(poli) == set())
    return {
        'funkcija': 'x / (x - 1)',
        'nicle': nicle,
        'poli': poli,
    }


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


print(generiraj(racionalna, 'Funkcija {funkcija} ima ničle: {nicle}', st_polov=100))
