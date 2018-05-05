from string import Template
from datetime import date
import generiranje
import os
import shutil

def sestaviVseTeste(datoteka_seznam_dijakov, naloge, ime_naloge=date.today().strftime("%d-%B-%Y"), zdruzene_resitve=True): ###TODO če ni seznama naredi 1 test
    stevilo_nalog = len(naloge)
    seznam_ljudi = open(datoteka_seznam_dijakov).readlines() #TODO close
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
        napisiTest(podmapa+"/vzorec_testa.txt", naloge, dijak, potNaloge)
    if zdruzene_resitve:
        print("tuki bodo rešitve")
        #zdruziVseResitve()
    else:
        vzorec_resitev = napisiVzorecResitev(stevilo_nalog, podmapa)
        #todo vpiši rešitve iz textov
        #todo delete text files

    return "bu"

def napisiTest(vzorec_testa, naloge, dijak, potNaloge):
    ### Napiše Naloge (že v tex obliki)
    dokument = open(vzorec_testa, encoding="utf8")
    vzorec = Template(dokument.read())
    slovar_za_vstavljanje={"ime_dijaka": dijak}
    for zaporedna_stevilka, naloga in enumerate(naloge):
        slovar_za_vstavljanje['naloga%d'%(zaporedna_stevilka +1)] = naloga(dijak)[0]

    #naloga1 = generiranje.poisci_nicle_polinoma()[0]
    #naloga2 = generiranje.racionalna()["funkcija"]
    #slovar_za_vstavljanje = {"naslov":naslov, "naloga1":naloga1, "naloga2":naloga2}
    koncni_dokument = vzorec.substitute(slovar_za_vstavljanje)
    #print(koncni_dokument)
    dokument.close()
    izhodna = open("%s/%s.tex" %(potNaloge, dijak), "w+", encoding="utf8")
    izhodna.write(koncni_dokument)
    izhodna.close()



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
            vzorec_resitev.write("\\item $resitev%d\n\n" %i)
        vzorec_resitev.writelines(["\\end{enumerate}\n","\\end{document}"])

sestaviVseTeste("dijaki.txt",[generiranje.poisci_nicle_polinoma],"ULTIMATE POSKUS")






