from string import Template
from datetime import date
import generiranje
import os
import shutil

def sestaviVseTeste(datoteka_seznam_dijakov, naloge, ime_naloge=date.today().strftime("%d-%B-%Y"), zdruzene_resitve=True): ###TODO če ni seznama naredi 1 test
    stevilo_nalog = len(naloge)
    seznam_ljudi = open(datoteka_seznam_dijakov, encoding="utf8").readlines() #TODO close? #TODO če ni seznama naredi samo 1 test
    podmapa = ime_naloge
    potResitve = podmapa+"/rešitve"
    potNaloge = podmapa+"/naloge"

    if os.path.exists(podmapa):  #Zbriše staro mapo s tem imenom in ustvari novo
        shutil.rmtree(podmapa)
        os.makedirs(podmapa)
        os.makedirs(potNaloge)
        os.makedirs(potResitve)
    else:
        os.makedirs(podmapa)
        os.makedirs(potNaloge)
        os.makedirs(potResitve)

    napisiVzorecTesta(stevilo_nalog, podmapa)
    napisiVzorecResitev(stevilo_nalog,podmapa)
    for dijak in seznam_ljudi:
        dijak = dijak.strip()
        napisiTest(podmapa+"/vzorec_testa.txt",podmapa+"/vzorec_resitev.txt", naloge, dijak, potNaloge, potResitve)
    if zdruzene_resitve:
        print("TODO") #TODO združevanje rešitev
        #zdruziVseResitve()
    else:
        vzorec_resitev = napisiVzorecResitev(stevilo_nalog, podmapa)
        #todo vpiši rešitve iz textov
        #todo delete text files

    return "bu"

def napisiTest(vzorec_testa, vzorec_resitev, naloge, dijak, potNaloge, potResitve): #Napiše naloge in njihove rešitve #TODO rešitve kot txt?
    ### Napiše Naloge (že v tex obliki)
    dokumentNaloge = open(vzorec_testa, encoding="utf8")
    vzorecNaloge = Template(dokumentNaloge.read())
    dokumentResitve = open(vzorec_resitev, encoding="utf8")
    vzorecResitve = Template(dokumentResitve.read())

    slovar_za_vstavljanje_nalog={"ime_dijaka": dijak}
    slovar_za_vstavljanje_resitev = {"ime_dijaka": dijak}
    for zaporedna_stevilka, naloga in enumerate(naloge):
        (besediloNaloge, besediloResitve) = naloga(seme=dijak, primeri=1) #TODO Kako podaš že nekej argumentov
        slovar_za_vstavljanje_nalog['naloga%d'%(zaporedna_stevilka +1)] = besediloNaloge
        slovar_za_vstavljanje_resitev['naloga%d' % (zaporedna_stevilka + 1)] = besediloNaloge
        slovar_za_vstavljanje_resitev['resitev%d' % (zaporedna_stevilka + 1)] = besediloResitve

    #naloga1 = generiranje.poisci_nicle_polinoma()[0]
    #naloga2 = generiranje.racionalna()["funkcija"]
    #slovar_za_vstavljanje_nalog = {"naslov":naslov, "naloga1":naloga1, "naloga2":naloga2}
    koncni_dokumentNaloge = vzorecNaloge.substitute(slovar_za_vstavljanje_nalog)
    koncniDokumentResitve =vzorecResitve.substitute(slovar_za_vstavljanje_resitev)
    #print(koncni_dokumentNaloge)
    dokumentNaloge.close()
    dokumentResitve.close()

    izhodneNaloge = open("%s/%s.tex" %(potNaloge, dijak), "w+", encoding="utf8")
    izhodneNaloge.write(koncni_dokumentNaloge)
    izhodneNaloge.close()

    izhodneResitve = open("%s/%s.tex" %(potResitve, dijak), "w+", encoding="utf8")
    izhodneResitve.write(koncniDokumentResitve)
    izhodneResitve.close()




def zdruziVseResitve(vseResitve):
    return #TODO

def napisiVzorecTesta(steviloNalog,podmapa):
    with open("%s/vzorec_testa.txt" %podmapa, "w+",encoding="utf8") as vzorec_testa:
        vzorec_testa.writelines(["\\documentclass{article}\n\n","\\usepackage[utf8]{inputenc}\n\n","\\begin{document}\n\n",
                                "\\title{%s}\n"%podmapa,"\\author{$ime_dijaka}\n","\\maketitle\n", "\\begin{enumerate}\n"])
        for i in range(1,steviloNalog+1):
            vzorec_testa.write("\\item $naloga%d\n\n" %i)
        vzorec_testa.writelines(["\\end{enumerate}\n","\\end{document}"])

def napisiVzorecResitev(steviloNalog, podmapa):
    with open("%s/vzorec_resitev.txt" %podmapa, "w+",encoding="utf8") as vzorec_resitev:
        vzorec_resitev.writelines(["\\documentclass{article}\n\n","\\usepackage[utf8]{inputenc}\n\n","\\begin{document}\n\n",
                                "\\title{Rešitve: %s}\n"%podmapa,"\\author{$ime_dijaka}\n","\\maketitle\n", "\\begin{enumerate}\n"])
        for i in range(1,steviloNalog+1):
            vzorec_resitev.write("\\item $naloga%d\n" %i)
            vzorec_resitev.write("$resitev%d\n\n" %i)
        vzorec_resitev.writelines(["\\end{enumerate}\n","\\end{document}"])

sestaviVseTeste("dijaki.txt",[generiranje.poisci_nicle_polinoma,generiranje.nalogaRacionalna],"Test za testiranje")
#TODO Kako lahko daš nekatere zahteve notr
#TODO Če daš dvakrat isto nalogo na seznam vzame enako seme - torej enaki primeri






