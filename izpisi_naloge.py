from datetime import date
import os
import random
import shutil
import jinja2
import naravnaStevila
import mnozice
import izrazi
import linearnaFunkcija
import kompleksnaStevila
import kvadratnaFunkcija
import eksponentnaFunkcija
import polinom
import stoznice
import zaporedja
import odvodi

vzorec_testa = jinja2.Template(r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{gensymb}

\pgfplotsset{compat=1.7}

\begin{document}

\title{ {{ime_testa}} }
\author{ {{ucenec}} }
\maketitle
\begin{enumerate}
{% for naloga in naloge %}
\item {{naloga.naloga}}
{% endfor%}

\end{enumerate}
\end{document}""")

vzorec_posameznih_resitev = jinja2.Template(r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{gensymb}

\pgfplotsset{compat=1.7}

\begin{document}

\title{Rešitve testa {{ime_testa}} }
\author{ {{ucenec}} }
\maketitle
\begin{enumerate}
{% for resitev in resitve %}
\item {{resitev}}
{% endfor%}

\end{enumerate}
\end{document}""")

vzorec_skupnih_resitev = jinja2.Template(r"""
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{gensymb}

\pgfplotsset{compat=1.7}

\begin{document}

\title{Skupne rešitve testa {{ime_testa}} }
\maketitle
{% for posameznik in seznam %}
\section*{ {{posameznik.ucenec}} }
\begin{enumerate}
{% for resitev in posameznik.resitve %}
\item {{resitev}}
{% endfor%}
\end{enumerate}
\newpage
{% endfor%}

\end{document}""")


def sestavi_vse_teste(naloge, ime_testa=date.today().strftime("%d-%B-%Y"), datoteka_seznam_dijakov=None,
                      zdruzene_resitve=True):
    """Ustvari mapi za teste in rešitve. Sestavi teste za vse dijake s podanega seznama.

    :type naloge: list
    :param naloge: seznam željenih nalog
    :type ime_testa: str
    :param ime_testa: ime testa
    :type datoteka_seznam_dijakov: file
    :param datoteka_seznam_dijakov: besedilna datoteka, ki vsebuje seznam dijakov
    :type zdruzene_resitve: Bool
    :param zdruzene_resitve: rešitve v eni združeni datoteki ali za vsakega dijaka v svoji datoteki
    """
    if not datoteka_seznam_dijakov:
        seznam_ljudi = ["Gimnazija Kranj"]
    else:
        seznam_ljudi = sorted(open(datoteka_seznam_dijakov, encoding="utf8").readlines())

    podmapa = ime_testa
    pot_resitve = podmapa + "/Rešitve"
    pot_naloge = podmapa + "/Naloge"

    if os.path.exists(podmapa):  # Zbriše staro mapo s tem imenom in ustvari novo
        shutil.rmtree(podmapa)
    os.makedirs(podmapa)
    os.makedirs(pot_naloge)
    os.makedirs(pot_resitve)

    seznam_vseh_resitev = []
    for ucenec in seznam_ljudi:
        ucenec = ucenec.strip()
        random.seed(ucenec)
        seznam_nalog = [naloga.besedilo() for naloga in
                        naloge]  # Se mora klicat tukaj in ne v jinji, da dobimo naenkrat naloge in rešitve
        napisi_test(ime_testa, seznam_nalog, ucenec, pot_naloge)

        seznam_resitev = [naloga['resitev'] for naloga in seznam_nalog]
        if zdruzene_resitve:
            seznam_vseh_resitev.append({'ucenec': ucenec, 'resitve': seznam_resitev})
        else:
            napisi_posamezno_resitev(ime_testa, seznam_resitev, ucenec, pot_resitve)
    if zdruzene_resitve:  # če se izpisuje znotraj zanke ni potrebno imet dveh if-ov
        napisi_skupno_resitev(ime_testa, seznam_vseh_resitev, pot_resitve)
    print('Test {} je sestavljen.'.format(ime_testa))


def napisi_test(ime_testa, seznam_nalog, ucenec, pot_naloge):
    """
    Ustvari test za posameznega dijaka.

    :param ime_testa: ime testa
    :type ime_testa: str
    :param seznam_nalog: seznam besedil posameznih nalog
    :type seznam_nalog: list
    :param ucenec: ime dijaka
    :type ucenec: str
    :param pot_naloge: mapa, kjer se shranjujejo naloge
    :type pot_naloge: str
    """
    datoteka_test = open("{0}/{1}.tex".format(pot_naloge, ucenec), "w+", encoding="utf8")
    datoteka_test.write(vzorec_testa.render(ime_testa=ime_testa, naloge=seznam_nalog, ucenec=ucenec))
    datoteka_test.close()


def napisi_posamezno_resitev(ime_testa, seznam_resitvev, ucenec, pot_resitve):
    """
    Ustvari datoteko z rešitvami za posameznega dijaka.

    :param ime_testa: ime testa
    :type ime_testa: str
    :param seznam_resitvev: seznam rešitev posameznih nalog
    :type seznam_resitvev: list
    :param ucenec: ime dijaka
    :type ucenec: str
    :param pot_resitve: mapa, kjer se shranjujejo rešitve
    :type pot_resitve: str
    """
    datoteka_test = open("{0}/{1}-rešitve.tex".format(pot_resitve, ucenec), "w+", encoding="utf8")
    datoteka_test.write(vzorec_posameznih_resitev.render(ime_testa=ime_testa, resitve=seznam_resitvev, ucenec=ucenec))
    datoteka_test.close()


def napisi_skupno_resitev(ime_testa, seznam_vseh_resitev, pot_resitve):  # Napiše vse rešitve v 1 dokument
    """
    Ustvari datoteko z rešitvami vseh dijakov.

    :param ime_testa: ime testa
    :type ime_testa: str
    :param seznam_vseh_resitev: seznam seznamov rešitev za posameznega dijaka
    :type seznam_vseh_resitev: list
    :param pot_resitve: mapa, kjer se shranjujejo rešitve
    :type pot_resitve: str
    """
    datoteka_test = open("{0}/Resitve.tex".format(pot_resitve), "w+", encoding="utf8")
    datoteka_test.write(vzorec_skupnih_resitev.render(ime_testa=ime_testa, seznam=seznam_vseh_resitev))
    datoteka_test.close()


sestavi_vse_teste([
    # mnozice.IzpeljaneMnozice(),mnozice.IzpeljaneMnozice(st_nalog=3),
    # mnozice.UnijaPresekRazlika(),mnozice.UnijaPresekRazlika(st_nalog=3),
    # mnozice.PotencnaMnozica(),mnozice.PotencnaMnozica(st_nalog=5),
    # mnozice.ElementiMnozice(lazja=False),mnozice.ElementiMnozice(st_nalog=5),
    # kompleksnaStevila.NarisiTocke(),kompleksnaStevila.NarisiTocke(st_nalog=3),
    # kompleksnaStevila.Racunanje(),kompleksnaStevila.Racunanje(st_nalog=3),
    # kompleksnaStevila.Ulomek(lazja=False),kompleksnaStevila.Ulomek(st_nalog=3),
    # kompleksnaStevila.VsotaRazlika(),kompleksnaStevila.VsotaRazlika(st_nalog=3),
    # kompleksnaStevila.Mnozenje(),kompleksnaStevila.Mnozenje(st_nalog=3),
    # polinom.DolociNiclePoleAsimptotoRacionalne(),
    # polinom.DolociNiclePoleAsimptotoRacionalne(st_nalog=3),
    # polinom.NiclePolinoma(),polinom.NiclePolinoma(st_nalog=3),
    # polinom.GrafPolinoma(),polinom.GrafPolinoma(st_nalog=3),
    # polinom.DvojnaNicla(),polinom.DvojnaNicla(st_nalog=3),
    # polinom.ParameteraDvojna(),polinom.ParameteraDvojna(st_nalog=3),
    # kvadratnaFunkcija.TemenskaOblika(), kvadratnaFunkcija.TemenskaOblika(st_nalog=3),
    # kvadratnaFunkcija.Neenacba(lazja=False), kvadratnaFunkcija.Neenacba(st_nalog=3),
    # kvadratnaFunkcija.Presecisce(),kvadratnaFunkcija.Presecisce(st_nalog=5),
    # kvadratnaFunkcija.IzracunajNicle(lazja=False), kvadratnaFunkcija.IzracunajNicle(st_nalog=3),
    # kvadratnaFunkcija.NarisiGraf(),kvadratnaFunkcija.NarisiGraf(st_nalog=5),
    # linearnaFunkcija.NarisiLinearnoFukcijo(), linearnaFunkcija.NarisiLinearnoFukcijo(st_nalog=5),
    # linearnaFunkcija.SistemDvehEnacb(lazja=False),linearnaFunkcija.SistemDvehEnacb(st_nalog=3),
    # linearnaFunkcija.SistemTrehEnacb(lazja=False),linearnaFunkcija.SistemTrehEnacb(st_nalog=3),
    # linearnaFunkcija.Neenacba(lazja=False), linearnaFunkcija.Neenacba(st_nalog=3),
    #izrazi.PotencaDvoclenika(lazja=False),#izrazi.PotencaDvoclenika(st_nalog=3),
    #izrazi.PotencaTroclenika(),izrazi.PotencaTroclenika(st_nalog=3),
    # izrazi.RazstaviRazliko(lazja=False), izrazi.RazstaviRazliko(st_nalog=3),
    # naravnaStevila.EvklidovAlgoritem(), naravnaStevila.EvklidovAlgoritem(st_nalog=3),
    # #naravnaStevila.DolociStevko(),naravnaStevila.DolociStevko(st_nalog=3),
    # naravnaStevila.DeliteljVeckratnik(), naravnaStevila.DeliteljVeckratnik(st_nalog=3),
    # eksponentnaFunkcija.GrafEksponentne(lazja=False),
    # eksponentnaFunkcija.Enacba(lazja=False), eksponentnaFunkcija.Enacba(st_nalog=3),
    # eksponentnaFunkcija.Enacba2osnovi(lazja=False), eksponentnaFunkcija.Enacba2osnovi(st_nalog=3),
    # zaporedja.SplosniClenZaporedja(),zaporedja.SplosniClenZaporedja(lazja=False, st_nalog=5),
    # zaporedja.SplosniClenAritmeticnegaZaporedja(),zaporedja.SplosniClenAritmeticnegaZaporedja(st_nalog=3),
    # zaporedja.SplosniClenAritmeticnegaEnacbi(),zaporedja.SplosniClenAritmeticnegaEnacbi(st_nalog=3),
    # zaporedja.VsotaAritmeticnega(st_nalog=3), zaporedja.VsotaAritmeticnega(lazja=False),
    # zaporedja.PrviCleniAritmeticnega(), zaporedja.PrviCleniAritmeticnega(st_nalog=3),
    # zaporedja.PrviCleniGeometrijskega(), zaporedja.PrviCleniGeometrijskega(st_nalog=3),
    # zaporedja.SplosniClenGeometrijskega(), zaporedja.SplosniClenGeometrijskega(st_nalog=3),
    # zaporedja.SplosniClenGeometrijskegaEnacbi(), zaporedja.SplosniClenGeometrijskegaEnacbi(st_nalog=3),
    # zaporedja.VsotaGeometrijskega(), zaporedja.VsotaGeometrijskega(st_nalog=3),
    # zaporedja.VsotaGeometrijskeVrste(lazja=False), zaporedja.VsotaGeometrijskeVrste(st_nalog=3),
    odvodi.KotMedPremicama(lazja=False),odvodi.KotMedPremicama(st_nalog=3),
    odvodi.OdvodElementarne(lazja=False), odvodi.OdvodElementarne(st_nalog=3),
    odvodi.OdvodSestavljenih(),odvodi.OdvodSestavljenih(st_nalog=3),
    #odvodi.KotMedGrafoma(),odvodi.KotMedGrafoma(st_nalog=3),
    # stoznice.NarisiKrivuljo(),stoznice.NarisiKrivuljo(st_nalog=3),
    # stoznice.PreseciscaKroznic(),stoznice.PreseciscaKroznic(st_nalog=3),
    # stoznice.TemeGorisceEnacba()

],
    "Tester", "dijaki.txt")#,zdruzene_resitve=False)
