from datetime import date
import os
import random
import shutil
import jinja2
import generiranje
import linearnaFunkcija

vzorec_testa = jinja2.Template("""\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz}
\\usepackage{pgfplots}

\\pgfplotsset{compat=1.16}

\\begin{document}

\\title{ {{ime_testa}} }
\\author{ {{ucenec}} }
\\maketitle
\\begin{enumerate}
{% for naloga in naloge %}
\\item {{naloga.naloga}}
{% endfor%}

\end{enumerate}
\end{document}""")

vzorec_posameznih_resitev = jinja2.Template("""\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz}
\\usepackage{pgfplots}

\\pgfplotsset{compat=1.16}

\\begin{document}

\\title{Rešitve testa {{ime_testa}} }
\\author{ {{ucenec}} }
\\maketitle
\\begin{enumerate}
{% for resitev in resitve %}
\\item {{resitev}}
{% endfor%}

\end{enumerate}
\end{document}""")

vzorec_skupnih_resitev = jinja2.Template("""\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{tikz}
\\usepackage{pgfplots}

\\pgfplotsset{compat=1.16}

\\begin{document}

\\title{Skupne rešitve testa {{ime_testa}} }
\\maketitle
{% for posameznik in seznam %}
\\section*{ {{posameznik.ucenec}} }
\\begin{enumerate}
{% for resitev in posameznik.resitve %}
\\item {{resitev}}
{% endfor%}
\\end{enumerate}
\\newpage
{% endfor%}

\end{document}""")


def sestavi_vse_teste(naloge, ime_testa=date.today().strftime("%d-%B-%Y"), datoteka_seznam_dijakov=None,
                      zdruzene_resitve=True):
    if not datoteka_seznam_dijakov:
        seznam_ljudi = ["Gimnazija Kranj"]
    else:
        seznam_ljudi = sorted(open(datoteka_seznam_dijakov, encoding="utf8").readlines())

    podmapa = ime_testa
    potResitve = podmapa + "/Rešitve"
    potNaloge = podmapa + "/Naloge"

    if os.path.exists(podmapa):  # Zbriše staro mapo s tem imenom in ustvari novo
        shutil.rmtree(podmapa)
    os.makedirs(podmapa)
    os.makedirs(potNaloge)
    os.makedirs(potResitve)

    seznam_vseh_resitev = []
    for ucenec in seznam_ljudi:
        ucenec = ucenec.strip()
        random.seed(ucenec)
        seznam_nalog = [naloga.besedilo() for naloga in
                        naloge]  # Se mora klicat tukaj in ne v jinji, da dobimo naenkrat naloge in rešitve
        napisi_test(ime_testa, seznam_nalog, ucenec, potNaloge)

        seznam_resitev = [naloga['resitev'] for naloga in seznam_nalog]
        if zdruzene_resitve:
            seznam_vseh_resitev.append({'ucenec': ucenec, 'resitve': seznam_resitev})
        else:
            napisi_posamezno_resitev(ime_testa, seznam_resitev, ucenec, potResitve)
    if zdruzene_resitve:  # če se izpisuje znotraj zanke ni potrebno imet dveh if-ov
        napisi_skupno_resitev(ime_testa, seznam_vseh_resitev, potResitve)


def napisi_test(ime_testa, seznam_nalog, ucenec, potNaloge):  # Napiše naloge
    datoteka_test = open("{0}/{1}.tex".format(potNaloge, ucenec), "w+", encoding="utf8")
    datoteka_test.write(vzorec_testa.render(ime_testa=ime_testa, naloge=seznam_nalog, ucenec=ucenec))
    datoteka_test.close()


def napisi_posamezno_resitev(ime_testa, seznam_resitvev, ucenec, potResitve):  # Napiše posamezne rešitve
    datoteka_test = open("{0}/{1}-rešitve.tex".format(potResitve, ucenec), "w+", encoding="utf8")
    datoteka_test.write(vzorec_posameznih_resitev.render(ime_testa=ime_testa, resitve=seznam_resitvev, ucenec=ucenec))
    datoteka_test.close()


def napisi_skupno_resitev(ime_testa, seznam_vseh_resitev, potResitve):  # Napiše vse rešitve v 1 dokument
    datoteka_test = open("{0}/Resitve.tex".format(potResitve), "w+", encoding="utf8")
    datoteka_test.write(vzorec_skupnih_resitev.render(ime_testa=ime_testa, seznam=seznam_vseh_resitev))
    datoteka_test.close()


sestavi_vse_teste([
    linearnaFunkcija.VrednostiLinearne(), linearnaFunkcija.VrednostiLinearne(st_nalog=5)
    #linearnaFunkcija.NarisiLinearnoFukcijo(), linearnaFunkcija.NarisiLinearnoFukcijo(st_nalog=5)
        #generiranje.PremiceTrikotnik(), generiranje.PremiceTrikotnik(st_nalog=5)
       # generiranje.Polinom(),generiranje.Polinom(st_nalog=5),
       # generiranje.RazstaviVieta(lazja=False), generiranje.RazstaviVieta(st_nalog=3),
       # generiranje.DolociNiclePoleAsimptotoRacionalne(), generiranje.DolociNiclePoleAsimptotoRacionalne(st_nalog=4),
       # generiranje.SplosniClenAritmeticnegaZaporedja(), generiranje.SplosniClenAritmeticnegaZaporedja(st_nalog=5)
       ],
      "Tester2019", "dijaki.txt")
