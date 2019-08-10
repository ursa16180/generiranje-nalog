Uporaba
============

Program za generiranje nalog je sestavljen iz knjižnice nalog iz različnih področij srednješolske matematike in programa
za sestavljanje testov. Ko zaženemo program z želenimi parametri nam ustvari testov in rešitve v `LaTeX` obliki ter po želju tudi v `PDF` obliki.

********
Naloge
********
Vsebuje 60 takih nalog iz teh področij
.. todo katere naloge

**************
Izpis testov
**************
Za izpis testov je potrebno poklicati funkcijo ``sestavi_vse_teste`` iz programa ``generiranje.py``. Funkcija sprejme pet parametrov:

#. seznam nalog
#. ime testa
#. datoteko, ki vsebuje seznam dijakov
#. izbira združenih ali ločenih rešitev
#. izbira za avtomatično generiranje PDF datotek

in ustvari teste ter rešitve kot `LaTeX` dokumente. Po želji pa lahko avtomatično ustvari dokumente v `PDF` formatu.
`LaTeX` dokument je na voljo, zato da vedno lahko kaj naknadno spremenimo.

.. code-block:: python

    >>>sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3),
                                          izrazi.RazstaviRazliko(min_potenca=3),
                                          naravna_stevila.DeliteljVeckratnik()],
                                  ime_testa='Izrazi in deljivost', datoteka_seznam_dijakov='dijaki.txt',
                                  zdruzene_resitve=False, pdf=False)
    Sestavljam test Izrazi in deljivost.
    Izpisujem test: 2717089
    Izpisujem rešitve: 2717089
    Izpisujem test: Ana
    Izpisujem rešitve: Ana
    Izpisujem test: Julija
    Izpisujem rešitve: Julija
    Izpisujem test: Katarina
    Izpisujem rešitve: Katarina
    Izpisujem test: Marjan Novak
    Izpisujem rešitve: Marjan Novak
    Izpisujem test: Matjaž
    Izpisujem rešitve: Matjaž
    Izpisujem test: Tjaša
    Izpisujem rešitve: Tjaša
    Test Izrazi in deljivost je sestavljen.

Program ustvari mapo z enakim imenom kot ime testa in 2 podmapi:

#. Naloge
#. Rešitve

.. figure:: slike/mape.png
    :align: center

    Ustvarjeni mapi za teste in rešitve testov

Mapa `Naloge` vsebuje posamezne zgenerirane teste, mapa `Rešitve` pa rešitve zgeneriranih testov.

Kadar mapa z enakim imenom že obstaja, nas program vpraša, če jo želimo prepisati. Če izberemo možnost `da`, se stara mapa izbriše in ustvari nova.
Če izberemo možnost `ne`, stara mapa ostane nespremenjena hkrati pa se ustvari nova mapa z enakim imenom kot ime testa in uro ustvarjanja testa.

.. code-block:: python
    :emphasize-lines: 7,8,23

    >>>sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3),
                                          izrazi.RazstaviRazliko(min_potenca=3),
                                          naravna_stevila.DeliteljVeckratnik()],
                                  ime_testa='Izrazi in deljivost', datoteka_seznam_dijakov='dijaki.txt',
                                  zdruzene_resitve=False, pdf=False)
    Sestavljam test Izrazi in deljivost.
    Mapa z imenom Izrazi in deljivost že obstaja.
    Ali jo želite prepisati z novo vsebino? [da/NE]>? ne
    Izpisujem test: 2717089
    Izpisujem rešitve: 2717089
    Izpisujem test: Ana
    Izpisujem rešitve: Ana
    Izpisujem test: Julija
    Izpisujem rešitve: Julija
    Izpisujem test: Katarina
    Izpisujem rešitve: Katarina
    Izpisujem test: Marjan Novak
    Izpisujem rešitve: Marjan Novak
    Izpisujem test: Matjaž
    Izpisujem rešitve: Matjaž
    Izpisujem test: Tjaša
    Izpisujem rešitve: Tjaša
    Test Izrazi in deljivost-18-37-30 je sestavljen.


Seznam nalog
#############

Parameter ``naloge`` je seznam nalog iz knjižnice, ki jih želimo na posameznem testu. Na seznamu lahko podamo poljubno število nalog.

``naloge=[izrazi.PotencaDvoclenika(st_nalog=3),izrazi.RazstaviRazliko(min_potenca=3),naravna_stevila.DeliteljVeckratnik()]``

.. todo popravi naslednji stavek da bo jasno da so naloge isto poimenovane in ne področja

Knjižnica vsebuje naloge z različnih področij. Naloge iz različnih področij imajo lahko enaka imena,
zato moramo vedno nalogo klicati tako, da najprej napišemo ime poglavja in nato ime naloge. Naloge imajo različne
parametre, ki so pojasnjeni v #TODOsklic točki.

``ime_poglavja.ime_naloge(parametri)``.

Primeri:

``kvadratna_funkcija.Neenacba(st_nalog=3)``

``linearna_funkcija.Neenacba()``

Ime testa
############
Parameter ``ime_testa`` je niz željenega imena testa. Izbrano ime je lahko poljubno in lahko vsebuje tudi presledke,
šumnike in druge znake. Ime testa se izpiše na vrhu posameznega testa in rešitev. Enako ime ima tudi na novo ustvarjena
mapa, ki vsebuje teste in rešitve. Če imena testa ne podamo, se namesto njega izpiše današnji datum.

Primer:

``ime_testa='Izrazi in deljivost'``

.. TODO ali želim tudi tukaj ponoviti kaj se zgodi če ime že obstaja

Seznam dijakov
################
Seznam dijakov napišemo v ločeni tekstovni datoteki (`.txt`), tako da so podatki posameznega dijaka v svoji vrstici.
Podatki dijaka so lahko poljubni: ime, priimek, vpisna številka,... Namesto podatkov dijakov lahko podamo tudi naprimer imena skupin: A in B.
Podatek v posamezni vrstici predstavlja podnaslov našega testa in ime datotetke posameznega testa ali rešitve.

.. figure:: slike/dijaki.png
    :align: center

    Primer tekstovne datotetke

.. figure:: slike/testi.png
    :align: center

    Primer mape z generirami testi.

Če datotetka s seznamom ni podana, bo program ustvaril samo 1 test s privzetim podnaslovom `Matematika`.

Semena
********
Vrednosti v posameznih nalogah so psevdo-naključno generirana. Za seme posameznega testa je uporabljen podnaslov testa,
ki ga običajno predstavlja ime dijaka ali skupine. To nam zagotavlja, da bomo za posameznega dijaka oziroma skupino
vedno dobili nalogo z enakimi podatki, ne glede na to, kolikokrat zaženemo program.
Na tak način zagotovimo, da če nam je posamezna naloga všeč, se s popravljanjem drugih ne bo spremenila.
Vendar se moramo zavedati, da na naključno generirane številke vpliva tudi vrstni red posameznih nalog.


Združene rešitve
##################
Rešitve nalog so lahko samostojna datoteka za vsakega dijaka ali pa so vse združene v eno datoteko. Privzete so združene rešitve.
Če želimo ločene moramo izbrati: ``zdruzene_resitve=False``.

PDF datoteke
#############
Testi in rešitve so `LaTeX` dokumenti, zato da imamo možnost spreminjanja in popravljanja. Ker pa za končno uporabo
potrebujemo `PDF` datoteke, nam jih lahko program avtomatično ustvari. Privzeto je ustvarjanje `PDF` datotek, vendar to
poveča časovno zahtevnost programa. Če ne želimo avtomatično generiranih `PDF` datotek, moramo klicati ``pdf=False``.

.. code-block:: python

    >>> sestavi_vse_teste(
        naloge=[izrazi.PotencaDvoclenika(st_nalog=3),izrazi.RazstaviRazliko(min_potenca=3),
        naravna_stevila.DeliteljVeckratnik()],
        ime_testa='Izrazi in deljivost',
        zdruzene_resitve=True)
    Sestavljam test Izrazi in deljivost.
    Izpisujem test: Matematika
    Izpisujem skupne rešitve za test Izrazi in deljivost.
    Test Izrazi in deljivost je sestavljen.


***********************
Spreminjanje parametrov
***********************
Naloge imajo različne parametre. Vse naloge imajo parametre, ki določajo besedilo nalog in besedila rešitev ter koliko
primerov naj vsebuje posamezna naloga.
Nekatere pa imajo tudi dodatne parametre s katerimi lahko malo prilagajamo zahtevnost naloge, kompleksnost rešitev ali tip naloge.

Parametri za besedilo nalog in rešitev
########################################
Vsaka naloga ima 4 parametre, ki so predloge za:

* besedilo naloge z enim primerom ``besedilo_posamezne``
* besedilo naloge z večimi primeri ``besedilo_vecih``
* besedilo rešitve naloge z enim primerom ``resitev_posamezne``
* besedilo rešitve naloge z večimi rešitvami ``resitev_vecih``

Besedila so surovi nizi, ki se pretvorijo v predloge Python knjižnice Jinja2 (``Jinja2.Template``).
V predlogo se na mesta spremenljivk označenih z dvojnimi zaviti oklepaji kasneje vstavijo posamezne vrednosti naloge.

.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: DeliteljVeckratnik
   :lines: 16

Metoda ``_poskusi_sestaviti`` vrne slovar vrednosti, ki se vstavijo na manjkajoča mesta v predlogo.
Ključi v slovarju, se morajo ujemati z imeni spremenljivk v predlogi.

.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: DeliteljVeckratnik._poskusi_sestaviti



Parameter število nalog
########################
Prav tako ima vsaka naloga parameter `število nalog`(``st_nalog``) s katerim določamo koliko primerov posamezne naloge želimo imeti.
Privzeta vrednost je en primer. Če želimo več primerov pa moramo podati naravno številsko vrednost, koliko primerov želimo.

Naslednja koda, bi ustvarila test, z dvema enakima nalogama. Prva naloga ima samo 1 primer računa, druga naloga pa 5 primerov (glej sliko).


.. code-block:: python

    >>>sestavi_vse_teste([kompleksna_stevila.Mnozenje(), kompleksna_stevila.Mnozenje(st_nalog=5)])

.. figure:: slike/st_nalog.png
    :align: center

    Izpis naloge z enim primerom in s 5 primeri.


Specifični/dodatni parametri
##############################
Ostali parametri so specifični za vsako nalogo.

Pri nalogi `DeliteljVeckratnik` mora dijak izračunati najmanjši skupni večkratnik in največji skupni delitelj dveh števil.
S parametrim ``do`` lahko določamo kako veliki sta lahko števili. Privzeta vrednost so števila do 200.
S parametrom ``najvecje_prastevilo`` pa določimo kaj je navečje praštevilo, ki se lahko pojavi v praštevilskem razcepu števil. Privzeta vrednost je 17.



.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: DeliteljVeckratnik






