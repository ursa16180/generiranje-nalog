from datetime import date, datetime
import os
import subprocess
import random
import shutil
import jinja2
import sympy
import importlib

sympy_printing_latex = importlib.import_module('sympy.printing.latex')


# ~~~~~~~~~SESTAVLJANJE NALOG

class NapacnaNaloga(Exception):
    """
    Izjema, kadar sestavljena naloga ne ustreza pogojem.
    """
    pass


MinMaxNapaka = ValueError("Minimalna vrednost mora biti manjša ali enaka maksimalni vrednosti.")


def preveri(pogoj):
    """
    Funkcija preveri, če sestavljena naloga ustreza pogojem, sicer javi napako NapacnaNaloga.

    :param pogoj: True, če naloga ustreza pogojem in False, kadar naloga ne ustreza pogojem
    """
    if not pogoj:
        raise NapacnaNaloga


class MojLatexPrinter(sympy_printing_latex.LatexPrinter):
    """
    Razred MojLatexPrinter je popravljena različica razreda LatexPrinter iz paketa sympy. Popravljeno je izpisovanje tuple-ov brez presledka.
    """

    def _print_tuple(self, expr):
        return r"\left( %s\right)" % r", ".join([self._print(i) for i in expr])


def moj_latex(expr):
    """
    Funkcija kliče razred MojLatexPrinter in nastavi izpis naravnega logaritma kot :math:`ln`.

    :param expr: niz
    """
    settings = {
        'ln_notation': True
    }
    return MojLatexPrinter(settings).doprint(expr)


class Naloga:
    """ Razred Naloga je splošni razred za posamezne naloge. Privzete ima splošna besedila nalog in rešitev, ki jih posamezne naloge lahko prepišejo.

    :param st_nalog: stevilo primerov posamezne naloge
    :param besedilo_posamezne: besedilo naloge
    :param besedilo_vecih: besedilo za nalogo z več primeri
    :param resitev_posamezne: besedilo za rešitev naloge
    :param resitev_vecih: besedilo za rešitev naloge z več primeri

    """
    besedilo_posamezne = r'''Reši nalogo: ${{ naloga }}$'''
    besedilo_vecih = r'''
        Reši sledeče naloge:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item ${{ naloga }}$
        {% endfor %}
        \end{enumerate}
        '''
    resitev_posamezne = r'''Rešitev: ${{ naloga }}$'''
    resitev_vecih = r'''Rešitve nalog:
        \begin{enumerate}
        {% for naloga in naloge %}
        \item${{ naloga }}$
        {% endfor %}
        \end{enumerate}
        '''

    def __init__(self, besedilo_posamezne=None, besedilo_vecih=None, resitev_posamezne=None, resitev_vecih=None,
                 st_nalog=None):
        self.st_nalog = st_nalog

        if besedilo_posamezne is not None:
            self.besedilo_posamezne = besedilo_posamezne

        if besedilo_vecih is not None:
            self.besedilo_vecih = besedilo_vecih

        if resitev_posamezne is not None:
            self.resitev_posamezne = resitev_posamezne

        if resitev_vecih is not None:
            self.resitev_vecih = resitev_vecih

    def _poskusi_sestaviti(self):
        """Poskusi sestaviti nalogo."""
        pass

    def sestavi(self):
        """Sestavi nalogo, ki ustreza pogojem."""
        while True:
            try:
                return self._poskusi_sestaviti()
            except NapacnaNaloga:
                pass

    def sestavi_vec(self, stevilo_nalog):
        """
        Sestavi nalogo z več primeri

        :param stevilo_nalog: stevilo primerov posamezne naloge

        """
        naloge = []
        for _ in range(stevilo_nalog):
            naloge.append(self.sestavi())
        return naloge

    def besedilo(self):
        """
        Ustvari predloge besedila in rešitev ter vanj vstavi vrednosti posameznih primerov.
        """
        razsiritve = {
            'latex': moj_latex, 'expand': sympy.expand
        }

        template_besedilo_posamezne = jinja2.Template(self.besedilo_posamezne)
        template_besedilo_vecih = jinja2.Template(self.besedilo_vecih)
        template_resitev_posamezne = jinja2.Template(self.resitev_posamezne)
        template_resitev_vecih = jinja2.Template(self.resitev_vecih)

        for kljuc, vrednost in razsiritve.items():
            template_besedilo_posamezne.globals[kljuc] = vrednost
            template_besedilo_vecih.globals[kljuc] = vrednost
            template_resitev_posamezne.globals[kljuc] = vrednost
            template_resitev_vecih.globals[kljuc] = vrednost

        if self.st_nalog is None or self.st_nalog == 1:
            naloga = self.sestavi()
            return {'naloga': template_besedilo_posamezne.render(naloga=naloga),
                    'resitev': template_resitev_posamezne.render(naloga=naloga)}

        else:
            naloge = self.sestavi_vec(self.st_nalog)

            return {'naloga': template_besedilo_vecih.render(naloge=naloge),
                    'resitev': template_resitev_vecih.render(naloge=naloge)}

    def primer(self):
        besedilo = self.besedilo_posamezne
        slovar = self.sestavi()
        # template = jinja2.Template(besedilo)
        # koncno_besedilo = template.render(naloga=slovar)
        # če želimo končno verzijo mormo v template uvozit latex in expand
        print(besedilo)
        print(slovar)
        # print(koncno_besedilo)


# ~~~~~~~SESTAVLJANJE TESTOV

def sestavi_vse_teste(naloge=[], ime_testa=date.today().strftime("%d-%B-%Y"), datoteka_seznam_dijakov=None,
                      zdruzene_resitve=True, pdf=True):
    """Ustvari mapi za teste in rešitve. Sestavi teste za vse dijake s podanega seznama.

    :param naloge: seznam željenih nalog
    :param ime_testa: ime testa
    :param datoteka_seznam_dijakov: besedilna datoteka, ki vsebuje seznam dijakov
    :param zdruzene_resitve: rešitve v eni združeni datoteki ali za vsakega dijaka v svoji datoteki
    :param pdf: program ustvari tudi pdf datoteke
    """
    if not datoteka_seznam_dijakov:
        seznam_ljudi = ["Matematika"]
    else:
        seznam_ljudi = sorted(open(datoteka_seznam_dijakov, encoding="utf8").readlines())

    podmapa = ime_testa


    if os.path.exists(podmapa):  # Zbriše staro mapo s tem imenom in ustvari novo
        print('Mapa z imenom {} že obstaja.'.format(podmapa))
        if input('Ali jo želite prepisati z novo vsebino? [da/NE]') != 'da':
           podmapa = ime_testa + datetime.now().strftime('-%H-%M-%S')
        else:
            shutil.rmtree(podmapa)
    pot_resitve = podmapa + "/Rešitve"
    pot_naloge = podmapa + "/Naloge"
    os.makedirs(podmapa)
    os.makedirs(pot_naloge)
    os.makedirs(pot_resitve)

    seznam_vseh_resitev = []
    for ucenec in seznam_ljudi:
        ucenec = ucenec.strip()
        random.seed(ucenec)
        seznam_nalog = [naloga.besedilo() for naloga in
                        naloge]  # Se mora klicat tukaj in ne v jinji, da dobimo naenkrat naloge in rešitve
        napisi_test(ime_testa, seznam_nalog, ucenec, pot_naloge, pdf)

        seznam_resitev = [naloga['resitev'] for naloga in seznam_nalog]
        if zdruzene_resitve:
            seznam_vseh_resitev.append({'ucenec': ucenec, 'resitve': seznam_resitev})
        else:
            napisi_posamezno_resitev(ime_testa, seznam_resitev, ucenec, pot_resitve, pdf)
    if zdruzene_resitve:  # če se izpisuje znotraj zanke ni potrebno imet dveh if-ov
        napisi_skupno_resitev(ime_testa, seznam_vseh_resitev, pot_resitve, pdf)
    print('Test {} je sestavljen.'.format(podmapa))


def napisi_test(ime_testa, seznam_nalog, ucenec, pot_naloge, pdf):
    """
    Ustvari test za posameznega dijaka.

    :param ime_testa: ime testa
    :param seznam_nalog: seznam besedil posameznih nalog
    :param ucenec: ime dijaka
    :param pot_naloge: mapa, kjer se shranjujejo naloge
    :param pdf: program ustvari tudi pdf testa
    """
    datoteka_test = open("{0}/{1}.tex".format(pot_naloge, ucenec), "w+", encoding="utf8")
    vzorec_testa = jinja2.Template(
        open("vzorci/vzorec_testa.txt", "r", encoding="utf8").read())  # TODO pretvori v ne raw, close?
    datoteka_test.write(vzorec_testa.render(ime_testa=ime_testa, naloge=seznam_nalog, ucenec=ucenec))
    datoteka_test.close()
    if pdf:
        subprocess.call(["pdflatex", '-output-directory', pot_naloge, "{0}/{1}.tex".format(pot_naloge, ucenec)],
                        encoding="utf8")
        os.unlink("{0}/{1}.aux".format(pot_naloge, ucenec))
        os.unlink("{0}/{1}.log".format(pot_naloge, ucenec))


def napisi_posamezno_resitev(ime_testa, seznam_resitvev, ucenec, pot_resitve, pdf):
    """
    Ustvari datoteko z rešitvami za posameznega dijaka.

    :param ime_testa: ime testa
    :param seznam_resitvev: seznam rešitev posameznih nalog
    :param ucenec: ime dijaka
    :param pot_resitve: mapa, kjer se shranjujejo rešitve
    :param pdf: program ustvari tudi pdf rešitve
    """
    datoteka_test = open("{0}/{1}-rešitve.tex".format(pot_resitve, ucenec), "w+", encoding="utf8")
    vzorec_posameznih_resitev = jinja2.Template(
        open("vzorci/vzorec_posameznih_resitev.txt", "r", encoding="utf8").read())  # TODO pretvori v ne raw, close?
    datoteka_test.write(vzorec_posameznih_resitev.render(ime_testa=ime_testa, resitve=seznam_resitvev, ucenec=ucenec))
    datoteka_test.close()
    if pdf:
        subprocess.call(
            ["pdflatex", '-output-directory', pot_resitve, "{0}/{1}-rešitve.tex".format(pot_resitve, ucenec)],
            encoding="utf8")
        os.unlink("{0}/{1}-rešitve.log".format(pot_resitve, ucenec))
        os.unlink("{0}/{1}-rešitve.aux".format(pot_resitve, ucenec))


def napisi_skupno_resitev(ime_testa, seznam_vseh_resitev, pot_resitve, pdf):  # Napiše vse rešitve v 1 dokument
    """
    Ustvari datoteko z rešitvami vseh dijakov.

    :param ime_testa: ime testa
    :param seznam_vseh_resitev: seznam seznamov rešitev za posameznega dijaka
    :param pot_resitve: mapa, kjer se shranjujejo rešitve
    :param pdf: program ustvari tudi pdf rešitve
    """
    datoteka_test = open("{0}/Resitve.tex".format(pot_resitve), "w+", encoding="utf8")
    vzorec_skupnih_resitev = jinja2.Template(
        open("vzorci/vzorec_skupnih_resitev.txt", "r", encoding="utf8").read())  # TODO pretvori v ne raw, close?
    datoteka_test.write(vzorec_skupnih_resitev.render(ime_testa=ime_testa, seznam=seznam_vseh_resitev))
    datoteka_test.close()
    if pdf:
        subprocess.call(["pdflatex", '-output-directory', pot_resitve, "{0}/Resitve.tex".format(pot_resitve)],
                        encoding="utf8")
        os.unlink("{0}/Resitve.aux".format(pot_resitve))
        os.unlink("{0}/Resitve.log".format(pot_resitve))
