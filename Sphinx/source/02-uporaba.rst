.. _ref_uporaba:

Uporaba
============

Program za generiranje nalog je sestavljen iz knjižnice nalog iz različnih področij srednješolske matematike in programa
za sestavljanje testov. Ko zaženemo program z želenimi parametri nam ustvari teste in rešitve v `LaTeX` datotekah ter po
želji tudi v `PDF` datotekah.
Če želimo uporabiti že sestavljene naloge, program ne zahteva veliko razumevanja programiranja. Kogar zanima pa si lahko
osnove programiranja v jeziku `Python` ogleda na spletu.

********
Naloge
********
Knjižnica nalog vsebuje naloge iz različnih področij srednješolske matematike. Naloge so različno zahtevne. Nekatere so
lahko primerne za spoznavanje konceptov, utrjevanje, pripravo na maturo ali celo kontrolne naloge. V času nastanka te
knjižnica vsebuje 59 nalog, vendar je še veliko možnosti za dodajanje.

Sklop `naravna_stevila`
########################
V tem sklopu sta 2 nalogi za izračun največjega skupnega delitelja in najmanjšega skupnega večkratnika dveh števil.
Eno nalogo naj bi reševali z praštevilskim razcepom, drugo pa s pomočjo Evklidovega algoritme.
Vsebuje nalogi:

* ``DeliteljVeckratnik`` in
* ``EvklidovAlgoritem``.

Sklop `izrazi`
################
Sklop izrazi je namenjen za utrjevanje računanja z algebrajskimi izrazi. Vsebuje naloge:

* ``PotencaDvoclenika``,
* ``PotencaTroclenika``,
* ``RazstaviVieta``,
* ``RazstaviRazliko`` in
* ``PotencirajVecclenik``.

Sklop `mnozice`
################
V sklopu so naloge za zapis elementov množic in različne operacije z množicami. Preverjajo znanje unije, preseka,
komplementa, razlike in potenčne množice. V njem so naloge:

* ``ElementiMnozice``,
* ``PotencnaMnozica``,
* ``UnijaPresekRazlika`` in
* ``IzpeljaneMnozice``.

Sklop `linearna_funkcija`
##########################
V tem sklopu so različne naloge, ki zahtevajo razumevanje linearne funkcije in enačb premic v ravnini. Pojavijo se tudi
naloge z enačbami dveh in treh neznank.
Vsebuje naloge:

* ``PremicaSkoziTocki``,
* ``RazdaljaMedTockama``,
* ``OblikeEnacbPremice``,
* ``PremiceTrikotnik``,
* ``NarisiLinearnoFunkcijo``,
* ``VrednostiLinearne``,
* ``Neenacba``,
* ``SistemDvehEnacb`` in
* ``SistemTrehEnacb``.

Sklop `kvadratna_funkcija`
###########################
Naloge iz sklopa utrjujejo znanje kvdaratne funkcije, različnih oblik zapisov funkcije, računanje ničel in risanje
grafov:

* ``IzracunajNicle``,
* ``NarisiGraf``,
* ``TemenskaOblika``,
* ``Presecisce``,
* ``Neenacba`` in
* ``SkoziTocke``.

Sklop `kompleksna_stevila`
###########################
V sklopu so naloge za začetno osvajanje računskih operacij s kompleksnimi števili ter pa nalogi,
ki združujeta vse operacije. Vsebovane so naloge:

* ``NarisiTocke``,
* ``VsotaRazlika``,
* ``Ulomek``,
* ``Mnozenje``,
* ``Racunanje`` in
* ``Enacba``.

Sklop `eksponentna_funkcija`
###############################
Naloge iz sklopa so namenjene utrjevanju znanju eksponentne funkcije in pripadajočih grafov ter enačb.
Vsebuje naloge:

* ``GrafEksponentne``,
* ``Enacba`` in
* ``Enacba2osnovi``.

Sklop `polinomska_racionalna_funkcija`
########################################
V tem sklopu so naloge za računanje ničel, iskanje neznanih koeficientov in risanje grafov polinomov:

* ``NiclePolinoma``,
* ``DvojnaNicla``,
* ``ParametraDvojna`` in
* ``GrafPolinoma``.

Ker je snov zelo povezana tudi z racionalno funkcijo, vsebuje tudi nalogi za računanje ničel, pol in asimptote ter graf racionalne funkcije:

* ``DolociNiclePoleAsimptotoRacionalne`` in
* ``GrafRacionalne``.

Sklop `stoznice`
#################
Za reševanje nalog iz sklope `stoznice` je potrebno znanje enačbe krožnice in elipse v premaknjeni legi:

* ``PreseciscaKroznic``,
* ``TemeGorisceEnacba`` in
* ``NarisiKrivuljo``.

Sklop `odvodi`
###############
Za reševanje nalog iz sklopa odvodi je potrebno znanje kako odvajamo elementarne in sestavljene funkcije, ter
razumevanje tangente na krivuljo. Vsebuje naloge:

* ``OdvodElementarne``,
* ``OdvodSestavljene``,
* ``KotMedPremicama``,
* ``Tangenta`` in
* ``KotMedGrafoma``.

Sklop `zaporedja`
##################
V sklopu `zaporedja` so naloge določanje splošnega člena poljubnega zaporedja, računanje prvih členov in vsote
aritmetičnega in geometrijskega zaporedja:

* ``SplosniClenZaporedja``,
* ``PrviCleniAritmeticnega``,
* ``SplosniClenAritmeticnegaZaporedja``,
* ``SplosniClenAritmeticnegaEnacbi``,
* ``VsotaAritmeticnega``,
* ``PrviCleniGeometrijskega``,
* ``SplosniClenGeometrijskega``,
* ``SplosniClenGeometrijskegaEnacbi``,
* ``VsotaGeometrijskega`` in
* ``VsotaGeometrijskeVrste``.

**************
Izpis testov
**************
Za izpis testov je potrebno poklicati funkcijo ``sestavi_vse_teste`` iz datoteke ``generiranje.py``. Funkcija sprejme
osem parametrov:

#. seznam nalog
#. ime testa
#. datoteko, ki vsebuje seznam učencev
#. izbira združenih ali ločenih rešitev
#. izbira za avtomatično generiranje PDF datotek
#. kateri vzorec za test želimo uporabiti
#. kateri vzorec za rešitve želimo uporabiti
#. seznam možnih točk pri posamezni nalogi

in ustvari teste ter rešitve kot `LaTeX` dokumente. Če želimo lahko avtomatično ustvari dokumente tudi v `PDF` formatu.
`LaTeX` dokument je na voljo zato, da vedno lahko kaj naknadno spremenimo ali popravimo.

V nadaljevanju je najprej na kratko predstavljen primer za sestavljanje testa, kasneje pa so posamezni parametri opisani
tudi bolj podrobno.
Če želimo sestaviti test, moramo poklicati funkcijo `sestavi_vse_teste` z želenimi parametri. Če želimo za vsakega
učenca s seznama ustvariti test z naslovom `Izrazi in deljivost`, ki vsebuje 3 naloge: za potenciranje dvočlenika,
razstavljanje razlike kubov in iskanje najmanjšega skupnega večkratnika ter največjega skupnega delitelja, potem bomo poklicali:

.. code-block:: python

    >>> generiranje.sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3), izrazi.RazstaviRazliko(min_potenca=3), naravna_stevila.DeliteljVeckratnik()], ime_testa='Izrazi in deljivost', datoteka_seznam_ucencev="ucenci.txt", zdruzene_resitve=False, pdf=True, pot_vzorca_testa="vzorci/vzorec_testa2.tex", pot_vzorca_resitev="vzorci/vzorec_posameznih_resitev1.tex", tocke=[5,5,7])

Izpisala se nam bo naslednja koda, ki nas za vsakega učenca s seznama obvesti, da sestavlja zanj test in rešitve. Ko
uspešno sestavi vse teste in rešitve nas obvesti da je `Test Izrazi in deljivost je sestavljen.`.
.. code-block:: python

    >>> generiranje.sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3), izrazi.RazstaviRazliko(min_potenca=3), naravna_stevila.DeliteljVeckratnik()], ime_testa='Izrazi in deljivost', datoteka_seznam_ucencev="ucenci.txt", zdruzene_resitve=False, pdf=True, pot_vzorca_testa="vzorci/vzorec_testa2.tex", pot_vzorca_resitev="vzorci/vzorec_posameznih_resitev1.tex", tocke=[5,5,7])
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

Program najprej ustvari mapo z enakim imenom kot ime testa in 2 podmapi:

#. Naloge
#. Rešitve

.. figure:: slike/mape.png
    :align: center

    Ustvarjeni mapi za teste in rešitve testov

Mapa `Naloge` vsebuje posamezne zgenerirane teste, mapa `Rešitve` pa rešitve zgeneriranih testov.

Spodaj so prikazane prve strani treh testov. Primere testov si lahko v celoti ogledate v prilogi.
.. todo ref na prilogo

.. figure:: slike/test1.png
    :align: center
    :width: 30%
.. figure:: slike/test2.png
    :align: center
    :width: 30%
.. figure:: slike/test3.png
    :align: center
    :width: 30%

    Primeri prvih strani testov

Na slikah se vidi, kako izgledajo rešitve različnih učencev. V celoti so prav tako dostopni v prilogi.
.. todo ref na prilog

.. figure:: slike/resitve1.png
    :align: center
    :width: 30%
.. figure:: slike/resitve2.png
    :align: center
    :width: 30%
.. figure:: slike/resitve3.png
    :align: center
    :width: 30%

    Primeri rešitev


Kadar mapa z enakim imenom že obstaja, nas program vpraša, če jo želimo prepisati. Če izberemo možnost `da`, se stara mapa izbriše in ustvari nova.
Če izberemo možnost `ne`, stara mapa ostane nespremenjena hkrati pa se ustvari nova mapa z enakim imenom kot ime testa in uro ustvarjanja testa.

.. code-block:: python
    :emphasize-lines: 3,4, 13

    >>> generiranje.sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3), izrazi.RazstaviRazliko(min_potenca=3), naravna_stevila.DeliteljVeckratnik()], ime_testa='Izrazi in deljivost', datoteka_seznam_ucencev="ucenci.txt", zdruzene_resitve=True, pdf=False, tocke=[5,5,7])
    Sestavljam test Izrazi in deljivost.
    Mapa z imenom Izrazi in deljivost že obstaja.
    Ali jo želite prepisati z novo vsebino? [da/NE]>? ne
    Izpisujem test: 2717089
    Izpisujem test: Ana
    Izpisujem test: Julija
    Izpisujem test: Katarina
    Izpisujem test: Marjan Novak
    Izpisujem test: Matjaž
    Izpisujem test: Tjaša
    Izpisujem skupne rešitve za test Izrazi in deljivost.
    Test Izrazi in deljivost-02-13-50 je sestavljen.


V datoteki `izpisi_naloge.py` je predstavljenih nekaj različnih primerov testov. Če si želimo ogledati,
kako program deluje, je to odlično mesto za začetek.
Seznam nalog
#############

Parameter ``naloge`` je seznam nalog iz knjižnice, ki jih želimo na posameznem testu. Na seznamu lahko podamo poljubno
število nalog, ne sme pa biti prazen.

``naloge=[izrazi.PotencaDvoclenika(st_nalog=3),izrazi.RazstaviRazliko(min_potenca=3),naravna_stevila.DeliteljVeckratnik()]``

.. todo popravi naslednji stavek da bo jasno da so naloge isto poimenovane in ne področja

Knjižnica vsebuje naloge z različnih področij. Naloge iz različnih področij imajo lahko enaka imena,
zato moramo vedno nalogo klicati tako, da najprej napišemo ime poglavja in nato ime naloge. Naloge imajo različne
parametre, ki so pojasnjeni v razdelku :ref:'parametri'.

``ime_poglavja.ime_naloge(parametri)``.

Primeri:

``kvadratna_funkcija.Neenacba(st_nalog=3)``

``linearna_funkcija.Neenacba()``

Ime testa
############
Parameter ``ime_testa`` je niz želenega imena testa. Izbrano ime je lahko poljubno in lahko vsebuje tudi presledke,
šumnike in druge znake. Pozorni moramo biti na posebne `LaTeX` in `Jinja2` znake, kot so recimo podčrtaj`_`, znak za
dolar `$` ali zavita oklepaja `{}`. Ime testa se izpiše na vrhu posameznega testa in rešitev. Enako ime ima tudi na novo ustvarjena
mapa, ki vsebuje teste in rešitve. Če imena testa ne podamo, se namesto njega izpiše današnji datum.

Primer:

``ime_testa='Izrazi in deljivost'``

.. TODO ali želim tudi tukaj ponoviti kaj se zgodi če ime že obstaja

Seznam učencev
################
Seznam učencev napišemo v ločeni tekstovni datoteki (`.txt`), tako da so podatki posameznega učenca v svoji vrstici.
Podatki učenca so lahko poljubni: ime, priimek, vpisna številka... Namesto podatkov učencev lahko podamo tudi na primer
imena skupin: A in B.
Podatek v posamezni vrstici predstavlja podnaslov našega testa in ime datoteke posameznega testa ali rešitve.

.. figure:: slike/ucenci.png
    :align: center
    :width: 50%

    Primer tekstovne datotetke

.. figure:: slike/testi.png
    :align: center
    :width: 50%

    Primer mape z generiranimi testi.

Če datoteka s seznamom ni podana, bo program ustvaril samo 1 test s privzetim podnaslovom `Matematika`.

.. _ref-semena:

Semena
********
Vrednosti v posameznih nalogah so psevdo-naključno generirane. Za seme posameznega testa je uporabljen podnaslov testa,
ki ga običajno predstavlja ime učenca ali skupine. To nam zagotavlja, da bomo za posameznega učenca oziroma skupino
vedno dobili nalogo z enakimi podatki, ne glede na to, kolikokrat zaženemo program.
Na tak način zagotovimo, da če nam je posamezna naloga všeč, se s popravljanjem drugih ne bo spremenila.
Vendar se moramo zavedati, da na naključno generirane številke vpliva tudi vrstni red posameznih nalog.


Združene rešitve
##################
Rešitve nalog so lahko samostojna datoteka za vsakega učenca ali pa so vse združene v eno datoteko. Privzete so združene rešitve.
Če želimo ločene moramo izbrati: ``zdruzene_resitve=False``.

PDF datoteke
#############
Testi in rešitve so `LaTeX` dokumenti, zato da imamo možnost spreminjanja in popravljanja. Ker pa za končno uporabo običajno
potrebujemo `PDF` datoteke, nam jih lahko program avtomatično ustvari. Privzeto je ustvarjanje `PDF` datotek, vendar to
poveča časovno zahtevnost programa. Če ne želimo avtomatično generiranih `PDF` datotek, moramo nastaviti ``pdf=False``.

.. code-block:: python

    >>> generiranje.sestavi_vse_teste(
        naloge=[izrazi.PotencaDvoclenika(st_nalog=3),izrazi.RazstaviRazliko(min_potenca=3),
        naravna_stevila.DeliteljVeckratnik()],
        ime_testa='Izrazi in deljivost',
        zdruzene_resitve=True)
    Sestavljam test Izrazi in deljivost.
    Izpisujem test: Matematika
    Izpisujem skupne rešitve za test Izrazi in deljivost.
    Test Izrazi in deljivost je sestavljen.


.. _ref-parametri:

Vzorci testov
##############
V mapi `vzorci` so štirje različne predloge oziroma vzorci testov. Uporabnik se odloči, kateri je najprimernejši zanj in nastavi
spremenljivko `pot_vzorca_testa` kot niz, do želene predloge. Privzeta je predloga `vzorec_testa1.tex`.

Primer: ``pot_vzorca_testa=vzorci/vzorec_testa2.tex``

Predloga `vzorec_testa1.tex` je verjetno najprimernejša za utrjevanje znanja. Na vrhu je napisano ime testa, pod njim
podnaslov, ki ga razbere iz seznama učencev. Nato so brez večjih razmakov naštete vse naloge.

.. figure:: slike/vzorec_testa1.png
    :align: center
    :height: 450px

    Primer testa sestavljenega iz `vzorec_testa1.tex`

Predlogi `vzorec_testa2.tex` in `vzorec_testa3.tex` sta primernejši za kontrolne naloge. Imata prostor za podpis učenca,
ime testa, podnaslov in kriterij ocenjevanja. Če želimo da je pod nalogo prostor za reševanje, je bolj primeren vzorec
`vzorec_testa2.tex`.

.. figure:: slike/vzorec_testa2.png
    :align: center
    :height: 450px

    Primer testa sestavljenega iz `vzorec_testa2.tex`

Če uporabimo predlogo `vzorec_testa3.tex`, so vse naloge naštete na eni strani.

.. figure:: slike/vzorec_testa3.png
    :align: center
    :height: 450px

    Primer testa sestavljenega iz `vzorec_testa3.tex`

Predloga `vzorec_testa4.tex` je bolj primerna za popravne izpite, saj ima naslovna stran veliko prostora za
natančno podane zahteve znanja in jasno zapisan kriterij. Vsaka naloga je na svoji strani, tako da imajo učenci dovolj
prostora za reševanje na test.

.. figure:: slike/vzorec_testa4.png
    :align: center
    :height: 450px

    Primer testa sestavljenega iz `vzorec_testa4.tex`

Vzorci rešitev
###############
V mapi `vzorci` so tudi predloge oziroma vzorci za rešitve. Pozorni moramo biti, ali smo se odločili za združene
rešitve ali ne, saj se predloge za njih razlikujejo.

Združene rešitve
*****************
V primeru združenih rešitev, program sestavi samo eno datoteko z vsemi rešitvami. Privzeta nastavitev je predloga
`vzorec_skupnih_resitev1.tex`. Za vsakega učenca se rešitve začnejo na novi strani in ima naštete samo rešitve.

.. figure:: slike/vzorec_skupne1.png
    :align: center
    :height: 450px

    Primer rešitev sestavljenih iz `vzorec_skupnih_resitev1.tex`

Predloga `vzorec_skupnih_resitev2.tex` ji je zelo podobna, le da se rešitve naslednjega učenca ne začnejo na novi strani.

.. figure:: slike/vzorec_skupne2.png
    :align: center
    :height: 450px

    Primer rešitev sestavljenih iz `vzorec_skupnih_resitev2.tex`

Če uporabimo predlogo `vzorec_skupnih_resitev3.tex` pa imamo najprej zapisano nalogo in šele nato rešitev.

.. figure:: slike/vzorec_skupne3.png
    :align: center
    :height: 450px

    Primer rešitev sestavljenih iz `vzorec_skupnih_resitev3.tex`

Posamezne rešitve
*******************
Privzeta predloga za posamezne rešitve je `vzorec_posameznih_resitev1.tex`. Na vrhu je naslov, nato pa so
zaporedno naštete vse rešitve.

.. figure:: slike/vzorec_posamezne1.png
    :align: center
    :height: 450px

    Primer rešitev sestavljenih iz `vzorec_posameznih_resitev1.tex`

Če želimo, da imamo najprej zapisane naloge in nato rešitve, moramo izbrati predlogo `vzorec_posameznih_resitev2.tex`.

.. figure:: slike/vzorec_posamezne2.png
    :align: center
    :height: 450px

    Primer rešitev sestavljenih iz `vzorec_posameznih_resitev2.tex`

Včasih želimo učencem dati rešitve za samostojno preverjanje, vendar nočemo da se rešitve razberejo že ob prvem pogledu.
Zato ima predloga `vzorec_posameznih_resitev3.tex` zelo majhno pisavo za katero se moramo potruditi, da jo lahko razberemo.

.. figure:: slike/vzorec_posamezne3.png
    :align: center
    :height: 450px

    Primer rešitev sestavljenih iz `vzorec_posameznih_resitev3.tex`

Točke
######
Na kontrolnih nalogah mora biti jasno zapisano, koliko točk je vredna posamezna naloga. Če želimo, da se vrednosti
avtomatično izpišejo zraven posamezne naloge oziroma rešitev, moramo kot parameter `tocke` podati seznam možnih točk.
Privzeta vrednost je prazen seznam - v tem primeru je namesto točk le prazen prostor.
Pri podajanju parametra je pomemben vrstni red, saj prva vrednost na seznamu predstavlja število možnih točk pri prvi
nalogi. Če na primer podamo `tocke=[6,3,9]`, pomeni da je prva naloga vredna 6 točk, druga 3 točke, tretja pa 9 točk.

Pomembno je, da je seznam nalog `naloge` enako dolg kot seznam točk `tocke`. V nasprotnem primeru nas program na to
opozori.

Včasih lahko zahtevnost naloge določimo šele, ko vidimo dejanske vrednosti v nalogi in ne prej. V tem primeru najprej
zaženemo program brez podanega seznama točk in šele ko vemo koliko bodo posamezne naloge vredne, ponovno zaženemo
program s podanim parametrom `tocke`. Semena (glej :ref:'ref-semena'.) nam zagotavljajo, da bomo v obeh primerih dobili enake vrednosti.

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
* besedilo naloge z več primeri ``besedilo_vecih``
* besedilo rešitve naloge z enim primerom ``resitev_posamezne``
* besedilo rešitve naloge z več rešitvami ``resitev_vecih``

Za vsako nalogo želimo imeti prilagojeno besedilo, ki pravzaprav najpogosteje predstavlja navodilo za reševanje.
Pri vsaki nalogi tako lahko prilagodimo navodila. Na enak način lahko prilagodimo tudi izpis rešitev.

Naloge se pojavljajo v dveh oblikah - naloga z enim primerom ali naloga z več primeri. Ker se v takih primerih
navodila pogosto razlikujejo imamo 2 različna parametra.

Besedila so surovi nizi, ki se pretvorijo v predloge Python knjižnice Jinja2 (``Jinja2.Template``).
V predlogo se na mesta spremenljivk označenih z dvojnimi zaviti oklepaji kasneje vstavijo posamezne vrednosti naloge.

.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: DeliteljVeckratnik
   :lines: 16

Metoda ``_poskusi_sestaviti`` vrne slovar vrednosti, ki se vstavijo na manjkajoča mesta v predlogo.
Ključi v slovarju, se morajo ujemati z imeni spremenljivk v predlogi. O posameznih primerih metode si lahko preberete v
razdelku :ref:'_ref-poskusi-sestaviti'.



Parameter število nalog
########################
Prav tako ima vsaka naloga parameter `število nalog` (``st_nalog``) s katerim določamo koliko primerov posamezne naloge želimo imeti.
Privzeta vrednost je en primer. Če želimo več primerov pa moramo podati naravno številsko vrednost, koliko primerov želimo.

Naslednja koda, bi ustvarila test, z dvema enakima nalogama. Prva naloga ima samo 1 primer računa, druga naloga pa 5 primerov (glej sliko).


.. code-block:: python

    >>>sestavi_vse_teste([kompleksna_stevila.Mnozenje(), kompleksna_stevila.Mnozenje(st_nalog=5)])

.. figure:: slike/st_nalog.png
    :align: center

    Izpis naloge z enim primerom in s 5 primeri.


Dodatni parametri
##############################
Ostali parametri so specifični za vsako nalogo. Z njimi lahko uravnavamo zahtevnost naloge ali kako lepe so številske
rešitve. Včasih pa je lahko zelo podobna naloga primerna za različne stopnje znanja in s parametri lahko določimo
na kateri stopnji znanja so učenci. Vsi podani parametri imajo podane privzete vrednosti, tako da jih ni potrebno
določati, če tega ne želimo.

V nadaljevanju bo predstavljenih nekaj zanimivih primerov nalog.

Pri nalogi ``DeliteljVeckratnik`` mora učenc izračunati najmanjši skupni večkratnik in največji skupni delitelj dveh števil.
S parametrom ``do`` lahko določamo kako veliki sta lahko števili in tako omejimo kako zahtevno bo računanje.
Privzeta vrednost so števila do 200. S parametrom ``najvecje_prastevilo`` pa določimo kaj je navečje praštevilo, ki se lahko pojavi v praštevilskem razcepu števil. Privzeta vrednost je 17.

.. code-block:: python

    >>> naravna_stevila.DeliteljVeckratnik().primer()
    Slovar posameznega primera: {'stevilo1': 130, 'stevilo2': 121, 'najvecji_delitelj': 1, 'najmanjsi_veckratnik': 15730}
    Besedilo posameznega primera: Določi največji skupni delitelj in najmanjši skupni večkratnik števil $130$ in $121$.
    Slovar naloge z več primeri: [{'stevilo1': 130, 'stevilo2': 121, 'najvecji_delitelj': 1, 'najmanjsi_veckratnik': 15730}, {'stevilo1': 165, 'stevilo2': 121, 'najvecji_delitelj': 11, 'najmanjsi_veckratnik': 1815}, {'stevilo1': 64, 'stevilo2': 110, 'najvecji_delitelj': 2, 'najmanjsi_veckratnik': 3520}]
    Besedilo naloge z več primeri: Določi največji skupni delitelj in najmanjši skupni večkratnik števil:
        \begin{enumerate}

        \item $130$ in $121$

        \item $165$ in $121$

        \item $64$ in $110$

        \end{enumerate}

    >>> naravna_stevila.DeliteljVeckratnik(do=500,najvecje_prastevilo=41).primer()
    Slovar posameznega primera: {'stevilo1': 272, 'stevilo2': 198, 'najvecji_delitelj': 2, 'najmanjsi_veckratnik': 26928}
    Besedilo posameznega primera: Določi največji skupni delitelj in najmanjši skupni večkratnik števil $272$ in $198$.
    Slovar naloge z več primeri: [{'stevilo1': 272, 'stevilo2': 198, 'najvecji_delitelj': 2, 'najmanjsi_veckratnik': 26928}, {'stevilo1': 396, 'stevilo2': 261, 'najvecji_delitelj': 9, 'najmanjsi_veckratnik': 11484}, {'stevilo1': 91, 'stevilo2': 385, 'najvecji_delitelj': 7, 'najmanjsi_veckratnik': 5005}]
    Besedilo naloge z več primeri: Določi največji skupni delitelj in najmanjši skupni večkratnik števil:
        \begin{enumerate}

        \item $272$ in $198$

        \item $396$ in $261$

        \item $91$ in $385$

        \end{enumerate}

Naloga ``SistemDvehEnacb`` iz poglavja linearne funkcija ima lahko različno zahtevne številske rešitve. Običajno nam je
lažje izračunati celoštevilske rešitve. Če pa določimo parameter ``racionalne_resitve=True``, pa bo naloga bolj raznolika,
saj bodo lahko rešitve tako celoštevilske kot tudi racionalne. Na tak način lahko dosežemo tudi večjo raznolikost nalog.

.. code-block:: python

    >>> linearna_funkcija.SistemDvehEnacb().primer()
    Slovar posameznega primera: {'enacba1': Eq(-x - 5*y, 8), 'enacba2': Eq(5*x - y, -14), 'x': -3, 'y': -1}
    Besedilo posameznega primera: Reši sistem enačb $- x - 5 y = 8$ in $5 x - y = -14$.
    Slovar naloge z več primeri: [{'enacba1': Eq(-x - 5*y, 8), 'enacba2': Eq(5*x - y, -14), 'x': -3, 'y': -1}, {'enacba1': Eq(3*x + 2*y, -4), 'enacba2': Eq(4*x + 5*y, 4), 'x': -4, 'y': 4}, {'enacba1': Eq(2*x - 3*y, 1), 'enacba2': Eq(5*x - 3*y, 16), 'x': 5, 'y': 3}]
    Besedilo naloge z več primeri: Reši sistem enačb:
        \begin{enumerate}

        \item $- x - 5 y = 8$, $5 x - y = -14$

        \item $3 x + 2 y = -4$, $4 x + 5 y = 4$

        \item $2 x - 3 y = 1$, $5 x - 3 y = 16$

        \end{enumerate}


    >>> linearna_funkcija.SistemDvehEnacb(racionalne_resitve=True).primer()
    Slovar posameznega primera: {'enacba1': Eq(-4*x - 5*y, -1), 'enacba2': Eq(-5*x - y, -3), 'x': 2/3, 'y': -1/3}
    Besedilo posameznega primera: Reši sistem enačb $- 4 x - 5 y = -1$ in $- 5 x - y = -3$.
    Slovar naloge z več primeri: [{'enacba1': Eq(-4*x - 5*y, -1), 'enacba2': Eq(-5*x - y, -3), 'x': 2/3, 'y': -1/3}, {'enacba1': Eq(-x + 2*y, -3/2), 'enacba2': Eq(5*x - 3*y, -3), 'x': -3/2, 'y': -3/2}, {'enacba1': Eq(-2*x + 5*y, -29), 'enacba2': Eq(4*x - 3*y, 23), 'x': 2, 'y': -5}]
    Besedilo naloge z več primeri: Reši sistem enačb:
        \begin{enumerate}

        \item $- 4 x - 5 y = -1$, $- 5 x - y = -3$

        \item $- x + 2 y = - \frac{3}{2}$, $5 x - 3 y = -3$

        \item $- 2 x + 5 y = -29$, $4 x - 3 y = 23$

        \end{enumerate}


Podobno lahko tudi računanje prvih členov zaporedja naredimo malo računsko zahtevnejših, če lahko za prvi člen in
diferenco določimo racionalna števila namesto celih.

.. code-block:: python

    >>> zaporedja.PrviCleniAritmeticnega().primer()
    Slovar posameznega primera: {'cleni': [-2, -5, -8, -11, -14], 'a1': -2, 'd': -3, 'splosni': -3*(n - 1) - 2}
    Besedilo posameznega primera: Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1=-2$
             in diferenco $d=-3$.
    Slovar naloge z več primeri: [{'cleni': [-2, -5, -8, -11, -14], 'a1': -2, 'd': -3, 'splosni': -3*(n - 1) - 2}, {'cleni': [11, 9, 7, 5, 3], 'a1': 11, 'd': -2, 'splosni': 11 - 2*(n - 1)}, {'cleni': [-9, -10, -11, -12, -13], 'a1': -9, 'd': -1, 'splosni': -(n - 1) - 9}]
    Besedilo naloge z več primeri: Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1$ in diferenco $d$:
        \begin{enumerate}

        \item $a_1=-2$, $d=-3$

        \item $a_1=11$, $d=-2$

        \item $a_1=-9$, $d=-1$

        \end{enumerate}

    >>> zaporedja.PrviCleniAritmeticnega(racionalne_vrednosti=True).primer()
    Slovar posameznega primera: {'cleni': [-1, 0, 1, 2, 3], 'a1': -1, 'd': 1, 'splosni': n - 1 - 1}
    Besedilo posameznega primera: Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1=-1$
             in diferenco $d=1$.
    Slovar naloge z več primeri: [{'cleni': [-1, 0, 1, 2, 3], 'a1': -1, 'd': 1, 'splosni': n - 1 - 1}, {'cleni': [-1/2, -2/3, -5/6, -1, -7/6], 'a1': -1/2, 'd': -1/6, 'splosni': -(n - 1)/6 - 1/2}, {'cleni': [-2/3, -7/6, -5/3, -13/6, -8/3], 'a1': -2/3, 'd': -1/2, 'splosni': -(n - 1)/2 - 2/3}]
    Besedilo naloge z več primeri: Zapiši prvih pet členov in splošni člen aritmetičnega zaporedja s prvim členom $a_1$ in diferenco $d$:
        \begin{enumerate}

        \item $a_1=-1$, $d=1$

        \item $a_1=- \frac{1}{2}$, $d=- \frac{1}{6}$

        \item $a_1=- \frac{2}{3}$, $d=- \frac{1}{2}$

        \end{enumerate}

Pri računanju ničel polinoma se zahtevnost hitro povečuje z višanjem stopnje polinoma. Zato je pomembno, da lahko
s parametroma ``min_stopnja``, ki določa najmanjšo možno stopnjo polinoma, in ``max_stopnja``, ki določa
najvišjo možno stopnjo polinoma, uravnavamo polinomom kakšnih stopenj bomo iskali ničle. Ker lahko določamo zgornjo
in spodnjo mejo stopenj, tako obstaja nek razpon stopenj, da so naloge lahko raznolike. S parametroma
``min_nicla`` in ``max_nicla`` pa lahko določimo s kako velikimi vrednostmi bomo računali.

.. code-block:: python

    >>> polinomska_racionalna_funkcija.NiclePolinoma().primer()
    Slovar posameznega primera: {'polinom': 3*x**3 - 21*x**2 - 12*x + 84, 'nicle': [-2, 2, 7]}
    Besedilo posameznega primera: Poišči ničle polinoma $p(x)=3 x^{3} - 21 x^{2} - 12 x + 84$.
    Slovar naloge z več primeri: [{'polinom': 3*x**3 - 21*x**2 - 12*x + 84, 'nicle': [-2, 2, 7]}, {'polinom': -x**3 - 4*x**2 + 17*x + 60, 'nicle': [-5, -3, 4]}, {'polinom': -3*x**3 - 36*x**2 - 63*x + 294, 'nicle': [-7, -7, 2]}]
    Besedilo naloge z več primeri: Poišči ničle sledečih polinomov:
            \begin{enumerate}

            \item $p(x)=3 x^{3} - 21 x^{2} - 12 x + 84$

            \item $p(x)=- x^{3} - 4 x^{2} + 17 x + 60$

            \item $p(x)=- 3 x^{3} - 36 x^{2} - 63 x + 294$

            \end{enumerate}

    >>> polinomska_racionalna_funkcija.NiclePolinoma(max_stopnja=5, min_nicla=0, max_nicla=10).primer()
    Slovar posameznega primera: {'polinom': 3*x**4 - 39*x**3 + 138*x**2 - 144*x, 'nicle': [0, 2, 3, 8]}
    Besedilo posameznega primera: Poišči ničle polinoma $p(x)=3 x^{4} - 39 x^{3} + 138 x^{2} - 144 x$.
    Slovar naloge z več primeri: [{'polinom': 3*x**4 - 39*x**3 + 138*x**2 - 144*x, 'nicle': [0, 2, 3, 8]}, {'polinom': -3*x**5 + 99*x**4 - 1212*x**3 + 6636*x**2 - 15120*x + 9600, 'nicle': [1, 4, 8, 10, 10]}, {'polinom': x**5 - 22*x**4 + 161*x**3 - 428*x**2 + 288*x, 'nicle': [0, 1, 4, 8, 9]}]
    Besedilo naloge z več primeri: Poišči ničle sledečih polinomov:
            \begin{enumerate}

            \item $p(x)=3 x^{4} - 39 x^{3} + 138 x^{2} - 144 x$

            \item $p(x)=- 3 x^{5} + 99 x^{4} - 1212 x^{3} + 6636 x^{2} - 15120 x + 9600$

            \item $p(x)=x^{5} - 22 x^{4} + 161 x^{3} - 428 x^{2} + 288 x$

            \end{enumerate}

Zahtevnost naloge lahko spreminjamo tudi z zahtevnostjo predpisa. Pri zapisu elementov izpeljane množice
lahko podamo preprost predpis za :math:`n`
:math:`\{n ; 1 < n < 5\}` ali pa malo zahtevnejši z linearno kombinacijo :math:`\{ 3 \cdot n -2 ; 1 < n < 5\}`.
Ravno to spreminja parameter ``linearna_kombinacija`` naloge ``ElementiMnozice``.

.. code-block:: python

    >>> mnozice.ElementiMnozice().primer()
    Slovar posameznega primera: {'n': 3*n, 'pogoj': '<', 'stevilo': 7, 'mnozica': {3, 6, 9, 12, 15, 18}}
    Besedilo posameznega primera: Zapiši elemente množice $ \mathcal{A} =\{ 3 n;
        (n \in \mathbb{N}) \land (n< 7 ) \} $.
    Slovar naloge z več primeri: [{'n': 3*n, 'pogoj': '<', 'stevilo': 7, 'mnozica': {3, 6, 9, 12, 15, 18}}, {'n': n, 'pogoj': '|', 'stevilo': 37, 'mnozica': {1, 37}}, {'n': n - 1, 'pogoj': '|', 'stevilo': 37, 'mnozica': {36}}]
    Besedilo naloge z več primeri: Zapiši elemente množic:
        \begin{enumerate}

        \item $ \mathcal{A} =\{ 3 n;
        (n \in \mathbb{N}) \land (n< 7 ) \} $

        \item $ \mathcal{A} =\{ n;
        (n \in \mathbb{N}) \land (n| 37 ) \} $

        \item $ \mathcal{A} =\{ n - 1;
        (n \in \mathbb{N}) \land (n| 37 ) \} $

        \end{enumerate}

    >>> mnozice.ElementiMnozice(linearna_kombinacija=True).primer()
    Slovar posameznega primera: {'n': n - 2, 'pogoj': '|', 'stevilo': 24, 'mnozica': {1, 2, 4, 6, 10, 22}}
    Besedilo posameznega primera: Zapiši elemente množice $ \mathcal{A} =\{ n - 2;
        (n \in \mathbb{N}) \land (n| 24 ) \} $.
    Slovar naloge z več primeri: [{'n': n - 2, 'pogoj': '|', 'stevilo': 24, 'mnozica': {1, 2, 4, 6, 10, 22}}, {'n': 2*n - 2, 'pogoj': '|', 'stevilo': 30, 'mnozica': {2, 4, 8, 10, 18, 28, 58}}, {'n': 2*n + 2, 'pogoj': '<', 'stevilo': 9, 'mnozica': {2, 4, 6, 8, 10, 12, 14, 16, 18}}]
    Besedilo naloge z več primeri: Zapiši elemente množic:
        \begin{enumerate}

        \item $ \mathcal{A} =\{ n - 2;
        (n \in \mathbb{N}) \land (n| 24 ) \} $

        \item $ \mathcal{A} =\{ 2 n - 2;
        (n \in \mathbb{N}) \land (n| 30 ) \} $

        \item $ \mathcal{A} =\{ 2 n + 2;
        (n \in \mathbb{N}) \land (n< 9 ) \} $

        \end{enumerate}

Težavnost naloge lahko povečamo, če uvedemo dodaten korak ali znanje, ki je potrebno za rešitev naloge.
Pri reševanju eksponentnih enačb, kjer nastopata dve različni osnovi, je pogosto potrebno samo izpostaviti
vsako osnovo na svoji strani in izenačiti eksponenta. Vendar pa lahko nalogo napišemo tako, da je vsaka osnova pomnožena
s potenco druge osnove. Tako moramo pri reševanju dodati še korak deljenja.

.. code-block:: python

    >>> eksponentna_funkcija.Enacba2osnovi().primer()
    Slovar posameznega primera: {'enacba': Eq(5*3**x - 5*7**x, 14*3**x/3 - 34*7**x/7), 'resitev': 1}
    Besedilo posameznega primera: Reši enačbo $5 \cdot 3^{x} - 5 \cdot 7^{x} = \frac{14 \cdot 3^{x}}{3} - \frac{34 \cdot 7^{x}}{7}$.
    Slovar naloge z več primeri: [{'enacba': Eq(5*3**x - 5*7**x, 14*3**x/3 - 34*7**x/7), 'resitev': 1}, {'enacba': Eq(-10*2**x + 12*3**x, -9*2**x + 11*3**x), 'resitev': 0}, {'enacba': Eq(-100000*10**x + 192*2**x, -90000*10**x + 176*2**x), 'resitev': -4}]
    Besedilo naloge z več primeri: Reši enačbe:
        \begin{enumerate}

        \item $5 \cdot 3^{x} - 5 \cdot 7^{x} = \frac{14 \cdot 3^{x}}{3} - \frac{34 \cdot 7^{x}}{7}$.

        \item $- 10 \cdot 2^{x} + 12 \cdot 3^{x} = - 9 \cdot 2^{x} + 11 \cdot 3^{x}$.

        \item $- 100000 \cdot 10^{x} + 192 \cdot 2^{x} = - 90000 \cdot 10^{x} + 176 \cdot 2^{x}$.

        \end{enumerate}


    >>> eksponentna_funkcija.Enacba2osnovi(deli_z_osnovo=True).primer()
    Slovar posameznega primera: {'enacba': Eq(-80*2**x + 27*3**x, -76*2**x + 21*3**x), 'resitev': -1}
    Besedilo posameznega primera: Reši enačbo $- 80 \cdot 2^{x} + 27 \cdot 3^{x} = - 76 \cdot 2^{x} + 21 \cdot 3^{x}$.
    Slovar naloge z več primeri: [{'enacba': Eq(-80*2**x + 27*3**x, -76*2**x + 21*3**x), 'resitev': -1}, {'enacba': Eq(-3*2**x/16 + 4*3**x/27, -3*2**x/64 + 34*3**x/243), 'resitev': 7}, {'enacba': Eq(5*2**x/8 - 2*5**x/15625, 19*2**x/32 - 42*5**x/390625), 'resitev': 8}]
    Besedilo naloge z več primeri: Reši enačbe:
        \begin{enumerate}

        \item $- 80 \cdot 2^{x} + 27 \cdot 3^{x} = - 76 \cdot 2^{x} + 21 \cdot 3^{x}$.

        \item $- \frac{3 \cdot 2^{x}}{16} + \frac{4 \cdot 3^{x}}{27} = - \frac{3 \cdot 2^{x}}{64} + \frac{34 \cdot 3^{x}}{243}$.

        \item $\frac{5 \cdot 2^{x}}{8} - \frac{2 \cdot 5^{x}}{15625} = \frac{19 \cdot 2^{x}}{32} - \frac{42 \cdot 5^{x}}{390625}$.

        \end{enumerate}

Reševanje enačb s kompleksnimi števili lahko naredimo bolj raznolike, če poleg neznanega števila :math:`z` nastopa
še njeno konjugirana vrednost :math:`\overline{z}`. To lahko v nalogi ``Enacba`` določimo s parametrom
``konjugirana_vrednost``.

.. code-block:: python

    >>> kompleksna_stevila.Enacba().primer()
    Slovar posameznega primera: {'enacba': Eq(z*(1 - 4*I), -17), 'resitev': -1 - 4*I, 'imaginarna': -4, 'realna': -1, 'absolutna': sqrt(17)}
    Besedilo posameznega primera: Katero kompleksno število $z$ zadošča enačbi $z \left(1 - 4 i\right) = -17$? Zapiši $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunaj $\left| z \right|$.
    Slovar naloge z več primeri: [{'enacba': Eq(z*(1 - 4*I), -17), 'resitev': -1 - 4*I, 'imaginarna': -4, 'realna': -1, 'absolutna': sqrt(17)}, {'enacba': Eq(z*(2 + 4*I), 12 + 14*I), 'resitev': 4 - I, 'imaginarna': -1, 'realna': 4, 'absolutna': sqrt(17)}, {'enacba': Eq(z*(2 - 2*I), -12 - 4*I), 'resitev': -2 - 4*I, 'imaginarna': -4, 'realna': -2, 'absolutna': 2*sqrt(5)}]
    Besedilo naloge z več primeri: Izračunaj katero število $z$ reši enačbo in zapiši še $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunajte $\left| z \right|$:
        \begin{enumerate}

        \item $z=z \left(1 - 4 i\right) = -17$

        \item $z=z \left(2 + 4 i\right) = 12 + 14 i$

        \item $z=z \left(2 - 2 i\right) = -12 - 4 i$

        \end{enumerate}

    >>> kompleksna_stevila.Enacba(konjugirana_vrednost=True).primer()
    Slovar posameznega primera: {'enacba': Eq(z*(4 + 4*I) + (-2 + 5*I)*conjugate(z), 14 + 69*I), 'resitev': 5 + 4*I, 'imaginarna': 4, 'realna': 5, 'absolutna': sqrt(41)}
    Besedilo posameznega primera: Katero kompleksno število $z$ zadošča enačbi $z \left(4 + 4 i\right) + \left(-2 + 5 i\right) \overline{z} = 14 + 69 i$? Zapiši $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunaj $\left| z \right|$.
    Slovar naloge z več primeri: [{'enacba': Eq(z*(4 + 4*I) + (-2 + 5*I)*conjugate(z), 14 + 69*I), 'resitev': 5 + 4*I, 'imaginarna': 4, 'realna': 5, 'absolutna': sqrt(41)}, {'enacba': Eq(z*(1 + 5*I) + (-3 - 4*I)*conjugate(z), -42 + 19*I), 'resitev': 3 + 4*I, 'imaginarna': 4, 'realna': 3, 'absolutna': 5}, {'enacba': Eq(z*(-2 + 3*I) + (-3 - 3*I)*conjugate(z), -3 - 2*I), 'resitev': 3 - 2*I, 'imaginarna': -2, 'realna': 3, 'absolutna': sqrt(13)}]
    Besedilo naloge z več primeri: Izračunaj katero število $z$ reši enačbo in zapiši še $\operatorname{Re}(z)$ in $\operatorname{Im}(z)$ ter izračunajte $\left| z \right|$:
        \begin{enumerate}

        \item $z=z \left(4 + 4 i\right) + \left(-2 + 5 i\right) \overline{z} = 14 + 69 i$

        \item $z=z \left(1 + 5 i\right) + \left(-3 - 4 i\right) \overline{z} = -42 + 19 i$

        \item $z=z \left(-2 + 3 i\right) + \left(-3 - 3 i\right) \overline{z} = -3 - 2 i$

        \end{enumerate}


Včasih lahko podobne naloge rešujemo z različnimi stopnjami znanja, zato je potrebno nalogo prilagoditi trenutnemu
znanju učencev. V poglavju stožnic se pogosto najprej spozna enačbe v središčni legi, kasneje pa šele v premaknjeni legi.
Zato je smiselno, da lahko pri nalogi ``TemeGorisceEnacba``, kjer določamo teme in gorišča elipse, določimo s parametrom ``premaknjena``,
ki lego elipse.

.. code-block:: python

    >>> stoznice.TemeGorisceEnacba().primer()
    Slovar posameznega primera: {'teme': (0, -1), 'gorisce': (sqrt(3), 0), 'sredisce': (0, 0), 'elipsa': Eq(x**2/4 + y**2, 1)}
    Besedilo posameznega primera: Zapiši enačbo elipse s središčem $S\left( 0, 0\right)$, temenom $T_1\left( 0, -1\right)$ in goriščem $F_1\left( \sqrt{3}, 0\right)$.
    Slovar naloge z več primeri: [{'teme': (0, -1), 'gorisce': (sqrt(3), 0), 'sredisce': (0, 0), 'elipsa': Eq(x**2/4 + y**2, 1)}, {'teme': (-2, 0), 'gorisce': (sqrt(3), 0), 'sredisce': (0, 0), 'elipsa': Eq(x**2/4 + y**2, 1)}, {'teme': (-2, 0), 'gorisce': (0, -2*sqrt(3)), 'sredisce': (0, 0), 'elipsa': Eq(x**2/4 + y**2/16, 1)}]
    Besedilo naloge z več primeri: Zapiši enačbo elipse s središčem $S$, temenom $T_1$ in goriščem $F_1$:
        \begin{enumerate}

        \item $S(\left( 0, 0\right))$, $T_1\left( 0, -1\right)$, $F_1\left( \sqrt{3}, 0\right)$

        \item $S(\left( 0, 0\right))$, $T_1\left( -2, 0\right)$, $F_1\left( \sqrt{3}, 0\right)$

        \item $S(\left( 0, 0\right))$, $T_1\left( -2, 0\right)$, $F_1\left( 0, - 2 \sqrt{3}\right)$

        \end{enumerate}

    >>> stoznice.TemeGorisceEnacba(premaknjena=True).primer()
    Slovar posameznega primera: {'teme': (5, 7), 'gorisce': (sqrt(5) + 5, 5), 'sredisce': (5, 5), 'elipsa': Eq((x/3 - 5/3)**2 + (y/2 - 5/2)**2, 1)}
    Besedilo posameznega primera: Zapiši enačbo elipse s središčem $S\left( 5, 5\right)$, temenom $T_1\left( 5, 7\right)$ in goriščem $F_1\left( \sqrt{5} + 5, 5\right)$.
    Slovar naloge z več primeri: [{'teme': (5, 7), 'gorisce': (sqrt(5) + 5, 5), 'sredisce': (5, 5), 'elipsa': Eq((x/3 - 5/3)**2 + (y/2 - 5/2)**2, 1)}, {'teme': (-4, -5), 'gorisce': (-8, -2), 'sredisce': (-4, -2), 'elipsa': Eq((x/5 + 4/5)**2 + (y/3 + 2/3)**2, 1)}, {'teme': (-1, 1), 'gorisce': (-3 + sqrt(3), 1), 'sredisce': (-3, 1), 'elipsa': Eq((x/2 + 3/2)**2 + (y - 1)**2, 1)}]
    Besedilo naloge z več primeri: Zapiši enačbo elipse s središčem $S$, temenom $T_1$ in goriščem $F_1$:
        \begin{enumerate}

        \item $S(\left( 5, 5\right))$, $T_1\left( 5, 7\right)$, $F_1\left( \sqrt{5} + 5, 5\right)$

        \item $S(\left( -4, -2\right))$, $T_1\left( -4, -5\right)$, $F_1\left( -8, -2\right)$

        \item $S(\left( -3, 1\right))$, $T_1\left( -1, 1\right)$, $F_1\left( -3 + \sqrt{3}, 1\right)$

        \end{enumerate}

V poglavju odvodi učenci postopoma spoznavajo odvode različnih funkcij. Nalogo ``OdvodSestavljene`` s parametrom
``funkcije`` lahko prilagodimo za primerno znanje, oziroma lahko določamo njeno zahtevnost. Izbiramo lahko med
eksponentnimi, logaritemskimi, racionalnimi, polinomskimi ali kotnimi funkcijami. Da program lahko ločuje,
med vrstami funkcijami so imena funkcij določena z razredom ``Funkcija``.

.. literalinclude:: ..\..\odvodi.py
   :pyobject: Funkcija

Funkcije, ki se lahko pojavijo v računu torej določimo s parametrom ``funkcije`` tako da jih naštejemo v seznamu.

Primer: ``funkcije=[odvodi.Funkcija.KOTNA, odvodi.Funkcija.LOGARITEM]``

.. code-block:: python

    >>> odvodi.OdvodSestavljene().primer()
    Slovar posameznega primera: {'funkcija': -2**x + 3**(-x), 'odvod': -3**(-x)*6**x*log(6) - 3**(-x)*(1 - 6**x)*log(3)}
    Besedilo posameznega primera: Določi odvod funkcije $f(x)=- 2^{x} + 3^{- x}$.
    Slovar naloge z več primeri: [{'funkcija': -2**x + 3**(-x), 'odvod': -3**(-x)*6**x*log(6) - 3**(-x)*(1 - 6**x)*log(3)}, {'funkcija': -3**x + tan(2*x), 'odvod': -3**x*log(3) + 2*tan(2*x)**2 + 2}, {'funkcija': (-x**2 - 3*x + 2)*log(-2*x)/(x*(x - 3)), 'odvod': -(2*x + 3)*log(-2*x)/(x*(x - 3)) + (x**2 + 3*x - 2)*log(-2*x)/(x*(x - 3)**2) + (x**2 + 3*x - 2)*log(-2*x)/(x**2*(x - 3)) - (x**2 + 3*x - 2)/(x**2*(x - 3))}]
    Besedilo naloge z več primeri: Določi odvod funkcije $f$:
        \begin{enumerate}

        \item $f(x)=- 2^{x} + 3^{- x}$

        \item $f(x)=- 3^{x} + \tan{\left(2 x \right)}$

        \item $f(x)=\frac{\left(- x^{2} - 3 x + 2\right) \ln{\left(- 2 x \right)}}{x \left(x - 3\right)}$

        \end{enumerate}

    >>> odvodi.OdvodSestavljene(funkcije=[odvodi.Funkcija.KOTNA, odvodi.Funkcija.LOGARITEM]).primer()
    Slovar posameznega primera: {'funkcija': log(-2*x) + cos(x), 'odvod': -sin(x) + 1/x}
    Besedilo posameznega primera: Določi odvod funkcije $f(x)=\ln{\left(- 2 x \right)} + \cos{\left(x \right)}$.
    Slovar naloge z več primeri: [{'funkcija': log(-2*x) + cos(x), 'odvod': -sin(x) + 1/x}, {'funkcija': log(-x) - log(x), 'odvod': 0}, {'funkcija': sin(2*x) + cos(x), 'odvod': -sin(x) + 2*cos(2*x)}]
    Besedilo naloge z več primeri: Določi odvod funkcije $f$:
        \begin{enumerate}

        \item $f(x)=\ln{\left(- 2 x \right)} + \cos{\left(x \right)}$

        \item $f(x)=\ln{\left(- x \right)} - \ln{\left(x \right)}$

        \item $f(x)=\sin{\left(2 x \right)} + \cos{\left(x \right)}$

        \end{enumerate}


Rešitvi kvadratne enačbe sta lahko kompleksni števili, vendar se lahko zgodi, da takih rešitev ne želimo ali
da snovi kompleksnih števil še nismo obravnavali. Zato lahko nalogi ``IzracunajNicle`` s parametrom
``kompleksni_nicli`` določimo ali želimo da sta rešitvi kompleksni ali realni števili.

.. code-block:: python

    >>> kvadratna_funkcija.IzracunajNicle().primer()
    Slovar posameznega primera: {'splosna': 3*x**2 + 3*x/2 - 5/3, 'x1': -1/4 + sqrt(89)/12, 'x2': -sqrt(89)/12 - 1/4}
    Besedilo posameznega primera: Izračunaj ničli kvadratne funkcije $f(x)=3 x^{2} + \frac{3 x}{2} - \frac{5}{3}$.
    Slovar naloge z več primeri: [{'splosna': 3*x**2 + 3*x/2 - 5/3, 'x1': -1/4 + sqrt(89)/12, 'x2': -sqrt(89)/12 - 1/4}, {'splosna': -x**2/3 - 11*x/3 - 2, 'x1': -11/2 - sqrt(97)/2, 'x2': -11/2 + sqrt(97)/2}, {'splosna': 10*x**2/3 + 14*x/3 - 2, 'x1': -7/10 + sqrt(109)/10, 'x2': -sqrt(109)/10 - 7/10}]
    Besedilo naloge z več primeri: Izračunaj ničli naslednjih kvadratnih funkcij:
        \begin{enumerate}

        \item $f(x)=3 x^{2} + \frac{3 x}{2} - \frac{5}{3}$

        \item $f(x)=- \frac{x^{2}}{3} - \frac{11 x}{3} - 2$

        \item $f(x)=\frac{10 x^{2}}{3} + \frac{14 x}{3} - 2$

        \end{enumerate}

    >>> kvadratna_funkcija.IzracunajNicle(kompleksni_nicli=True).primer()
    Slovar posameznega primera: {'splosna': x**2/3 + 2*x + 7/2, 'x1': -3 + sqrt(6)*I/2, 'x2': -3 - sqrt(6)*I/2}
    Besedilo posameznega primera: Izračunaj ničli kvadratne funkcije $f(x)=\frac{x^{2}}{3} + 2 x + \frac{7}{2}$.
    Slovar naloge z več primeri: [{'splosna': x**2/3 + 2*x + 7/2, 'x1': -3 + sqrt(6)*I/2, 'x2': -3 - sqrt(6)*I/2}, {'splosna': -11*x**2/3 - 3*x/2 - 7/2, 'x1': -9/44 - sqrt(1767)*I/44, 'x2': -9/44 + sqrt(1767)*I/44}, {'splosna': 4*x**2/3 + 7*x/2 + 4, 'x1': -21/16 + sqrt(327)*I/16, 'x2': -21/16 - sqrt(327)*I/16}]
    Besedilo naloge z več primeri: Izračunaj ničli naslednjih kvadratnih funkcij:
        \begin{enumerate}

        \item $f(x)=\frac{x^{2}}{3} + 2 x + \frac{7}{2}$

        \item $f(x)=- \frac{11 x^{2}}{3} - \frac{3 x}{2} - \frac{7}{2}$

        \item $f(x)=\frac{4 x^{2}}{3} + \frac{7 x}{2} + 4$

        \end{enumerate}

Pri računanju algebrajskih izrazov, je za na videz podobne naloge potrebno različno znanje. Naloga ``PotencirajVecclenik``
ima zato več parametrov. Parametra ``min_clenov`` in ``max_clenov`` določata ali v nalogi potenciramo dvočlenike,
tročlenike ali malo mešano.  Parametra ``min_potenca`` in ``mix_potenca`` pa določata razpon potenc.
Na ta način lahko dobimo raznolike primere enega tipa naloge.

.. code-block:: python

    >>> izrazi.PotencirajVecclenik().primer()
    Slovar posameznega primera: {'izraz': (y - 10)**2}
    Besedilo posameznega primera: Potenciraj izraz $\left(y - 10\right)^{2}$.
    Slovar naloge z več primeri: [{'izraz': (y - 10)**2}, {'izraz': (z - 1)**3}, {'izraz': (x - 3)**3}]
    Besedilo naloge z več primeri: Potenciraj izraze:
        \begin{enumerate}

        \item$\left(y - 10\right)^{2}$

        \item$\left(z - 1\right)^{3}$

        \item$\left(x - 3\right)^{3}$

        \end{enumerate}


    >>> izrazi.PotencirajVecclenik(max_clenov=2,max_potenca=5).primer()
    Slovar posameznega primera: {'izraz': (x - 4)**3}
    Besedilo posameznega primera: Potenciraj izraz $\left(x - 4\right)^{3}$.
    Slovar naloge z več primeri: [{'izraz': (x - 4)**3}, {'izraz': (t - 4)**5}, {'izraz': (c - 3)**3}]
    Besedilo naloge z več primeri: Potenciraj izraze:
        \begin{enumerate}

        \item$\left(x - 4\right)^{3}$

        \item$\left(t - 4\right)^{5}$

        \item$\left(c - 3\right)^{3}$

        \end{enumerate}

