.. _ref_uporaba:

Uporaba
============

.. _ref_sestavi_vse_teste:

**************
Izpis testov
**************
Knjižnici je dodana mapa `Primeri testov`, kjer imamo pripravljene 3 primere rabe knjižnice. Ogledali si bomo primer,
kako pripraviti vaje za utrjevanje znanja kompleksnih števil. Najprej ustvarimo novo `Python` datoteko (ime_datoteke.py).
Vedno moramo uvoziti modul `generiranje` in module, ki vsebujejo želene naloge. V našem primeru sta to modula
`kompleksna_stevila` in `kvadratna_funkcija`.

Za izpis testov je potrebno poklicati funkcijo ``sestavi_vse_teste`` iz datoteke ``generiranje.py`` z želenimi parametri.
Sprejme osem parametrov, ki so natančneje opisani kasneje. Uspešno zagnana funkcija ustvari teste ter rešitve kot `LaTeX`
dokumente. Če želimo lahko avtomatično ustvari dokumente tudi v `PDF` formatu.
`LaTeX` dokument je na voljo zato, da vedno lahko kaj naknadno spremenimo ali popravimo.

Recimo, da želimo za vsakega učenca s seznama v datoteki `ucenci.txt` ustvariti test z naslovom `Vaje kompleksna števila`,
ki vsebuje 6 različnih nalog iz računanja s kompleksnimi števili in risanjem v kompleksno ravnino.
Spodaj si lahko ogledamo, kako bi izgledala naša datoteka.

.. code-block:: python

    import generiranje
    import kompleksna_stevila
    import kvadratna_funkcija

    generiranje.sestavi_vse_teste(naloge=[kompleksna_stevila.NarisiTocke(),
                                          kompleksna_stevila.VsotaRazlika(st_nalog=6),
                                          kompleksna_stevila.Mnozenje(st_nalog=6),
                                          kompleksna_stevila.Racunanje(st_nalog=3),
                                          kompleksna_stevila.Enacba(st_nalog=3),
                                          kvadratna_funkcija.IzracunajNicle(kompleksni_nicli=True)],
                                  ime_testa= "Vaje kompleksna števila",
                                  datoteka_seznam_ucencev="ucenci.txt",
                                  zdruzene_resitve=False,
                                  pdf=True,
                                  pot_vzorca_testa="vzorec_testa1.tex",
                                  pot_vzorca_resitev="vzorec_posameznih_resitev1.tex")



Ko program zaženemo, se nam bo izpisala naslednja koda, ki nas za vsakega učenca s seznama obvesti, da zanj sestavlja test in rešitve. Ko
uspešno sestavi vse teste in rešitve nas obvesti, da je `Test Vaje kompleksna števila je sestavljen`.

.. code-block:: console

    Sestavljam test Vaje kompleksna števila.
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
    Test Vaje kompleksna števila je sestavljen.

Program najprej ustvari mapo z enakim imenom kot ime testa in 2 podmapi:

#. Naloge
#. Rešitve

.. figure:: slike/mape.png
    :align: center

    Ustvarjeni mapi za teste in rešitve testov

Mapa `Naloge` vsebuje posamezne zgenerirane teste, mapa `Rešitve` pa rešitve zgeneriranih testov.

Spodaj so prikazane prve strani treh testov. Dejanski primeri pa so v mapi `Primeri testov` programa.

.. figure:: slike/testi-sestavljeni.PNG
    :align: center

    Primeri prvih strani testov

Na slikah se vidi, kako izgledajo rešitve različnih učencev. V celoti so prav tako na voljo v mapi `Primeri testov`.

.. figure:: slike/resitve-sestavljene.png
    :align: center

    Primeri rešitev


Kadar mapa z enakim imenom že obstaja, nas program vpraša, če jo želimo prepisati. Če izberemo možnost `da`, se stara mapa izbriše in ustvari nova.
Če izberemo možnost `ne`, stara mapa ostane nespremenjena hkrati pa se ustvari nova mapa z enakim imenom poleg katerega se izpiše ura nastanka testa..

.. code-block:: console
    :emphasize-lines: 2-3,18

    Sestavljam test Vaje kompleksna števila.
    Mapa z imenom Vaje kompleksna števila že obstaja.
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
    Test Vaje kompleksna števila-18-19-46 je sestavljen.


V mapi `Primeri testov` si lahko ogledamo primere za kontrolno nalogo, popravni izpit ali utrjevanje. V posamezni mapi
sta poleg `Python` datoteke tudi želena vzorca in seznam učencev, čeprav to ni nujno potrebno, saj lahko za vrednosti
parametrov ``datoteka_seznam_ucencev``, ``pot_vzorca_testa`` in ``pot_vzorca_resitev``  napišemo kar celo poti do želenih datotek.


Seznam nalog
#############

Parameter ``naloge`` je seznam nalog iz knjižnice, ki jih želimo na posameznem testu. Na seznamu lahko podamo poljubno
število nalog, ne sme pa biti prazen. Če je seznam prazen ali vsebuje neobstoječe naloge,
nas program na to opozori.

.. code-block:: python

    naloge=[kompleksna_stevila.NarisiTocke(),
              kompleksna_stevila.VsotaRazlika(st_nalog=6),
              kompleksna_stevila.Mnozenje(st_nalog=6),
              kompleksna_stevila.Racunanje(st_nalog=3),
              kompleksna_stevila.Enacba(st_nalog=3),
              kvadratna_funkcija.IzracunajNicle(kompleksni_nicli=True)]


Knjižnica vsebuje naloge z različnih področij. Naloge iz različnih področij imajo lahko enaka imena,
zato moramo vedno nalogo klicati tako, da najprej napišemo ime poglavja in nato ime naloge. Naloge imajo različne
parametre, ki so pojasnjeni v razdelku :numref:'ref-parametri'.

``ime_poglavja.ime_naloge(parametri)``.

Primera:

``kvadratna_funkcija.Neenacba(st_nalog=3)``

``linearna_funkcija.Neenacba()``

Ime testa
############
Parameter ``ime_testa`` je niz želenega imena testa. Izbrano ime je lahko poljubno in lahko vsebuje tudi presledke,
šumnike in druge znake. Pozorni moramo biti le, da ne uporabljamo posebnih `LaTeX` in `Jinja2` znakov, kot so recimo podčrtaj `_`, znak za
dolar `$` ali zavita oklepaja `{}`. Ime testa se izpiše na vrhu posameznega testa in rešitev. Enako ime ima tudi na novo ustvarjena
mapa, ki vsebuje teste in rešitve. Če imena testa ne podamo, se namesto njega izpiše današnji datum.

Primer:

``ime_testa='Vaje kompleksna števila'``


.. _ref-semena:

Seznam učencev
################
Seznam učencev napišemo v ločeni tekstovni datoteki (`ime_seznama.txt`), tako da so podatki posameznega učenca v svoji vrstici.
Podatki učenca so lahko poljubni: ime, priimek, vpisna številka ... Namesto podatkov učencev lahko podamo tudi na primer
imena skupin A in B.

Podatek v posamezni vrstici predstavlja podnaslov našega testa in ime datoteke posameznega testa ali rešitve.

.. figure:: slike/ucenci.png
    :align: center
    :width: 50%

    Primer tekstovne datoteke s seznamom učencev

.. figure:: slike/testi.png
    :align: center
    :width: 50%

    Primer mape z generiranimi testi.

Če datoteka s seznamom ni podana, bo program ustvaril samo 1 test s privzetim podnaslovom `Matematika`.


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
Testi in rešitve so `LaTeX` dokumenti, kar zagotavlja da imamo možnost spreminjanja in popravljanja. Ker pa za končno uporabo običajno
potrebujemo `PDF` datoteke, nam jih lahko program avtomatično ustvari. Privzeto je ustvarjanje `PDF` datotek, vendar to
poveča časovno zahtevnost programa. Če ne želimo avtomatično generiranih `PDF` datotek, moramo nastaviti ``pdf=False``.

.. _ref-parametri:

Vzorci testov
##############
V mapi `vzorci` so štiri različne predloge oziroma vzorci testov. Uporabnik se odloči, kateri je najprimernejši zanj in nastavi
spremenljivko `pot_vzorca_testa` kot niz do želene predloge. Privzeta je predloga `vzorec_testa1.tex`.

Primer: ``pot_vzorca_testa=vzorci/vzorec_testa2.tex``

Predloga `vzorec_testa1.tex` je verjetno najprimernejša za utrjevanje znanja. Na vrhu je napisano ime testa, pod njim
podnaslov, ki ga program prebere iz seznama učencev, in datum nastanka testa. Nato so brez večjih razmakov naštete vse naloge.

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


Vzorci združenih rešitev
###########################

V mapi `vzorci` so tudi predloge oziroma vzorci za rešitve. Pozorni moramo biti, ali smo se odločili za združene
rešitve ali ne, saj se predloge za njih razlikujejo.
V primeru združenih rešitev program sestavi samo eno datoteko z vsemi rešitvami. Privzeta nastavitev je predloga
`vzorec_skupnih_resitev1.tex`. Za vsakega učenca se rešitve začnejo na novi strani, ki ima naštete samo rešitve.

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

Vzorci posameznih rešitev
############################

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
avtomatično izpišejo ob posamezni nalogi oziroma rešitvah, moramo kot parameter `tocke` podati seznam možnih točk. Privzeta
vrednost je prazen seznam - v tem primeru je namesto točk le prazen prostor. Pri podajanju parametra je pomemben
vrstni red, saj prva vrednost na seznamu predstavlja število možnih točk pri prvi
nalogi. Če na primer podamo `tocke=[6,3,9]`, pomeni da je prva naloga vredna 6 točk, druga 3 točke, tretja pa 9 točk.

Pomembno je, da je seznam nalog `naloge` enako dolg kot seznam točk `tocke`. V nasprotnem primeru nas program na to
opozori.

Včasih lahko zahtevnost naloge določimo šele, ko vidimo dejanske vrednosti v nalogi in ne prej. V tem primeru najprej
zaženemo program brez podanega seznama točk in šele ko vemo koliko bodo posamezne naloge vredne, ponovno zaženemo
program s podanim parametrom `tocke`. Semena (opisana v razdelku :numref:`ref-semena`.) nam zagotavljajo, da bomo v obeh
primerih dobili enake vrednosti.


***********************
Spreminjanje parametrov
***********************
Naloge imajo različne parametre. Vse naloge imajo parametre, ki določajo besedilo nalog in besedila rešitev ter koliko
primerov naj vsebuje posamezna naloga.
Nekatere pa imajo tudi dodatne parametre s katerimi lahko prilagajamo zahtevnost naloge, kompleksnost rešitev ali tip naloge.

Parametri za besedilo nalog in rešitev
########################################
Vsaka naloga ima 4 parametre, ki so predloge za:

* besedilo naloge z enim primerom - ``besedilo_posamezne``
* besedilo naloge z več primeri - ``besedilo_vecih``
* besedilo rešitve naloge z enim primerom - ``resitev_posamezne``
* besedilo rešitve naloge z več primeri - ``resitev_vecih``

Za vsako nalogo želimo imeti prilagojeno besedilo, ki pravzaprav najpogosteje predstavlja navodilo za reševanje.
Pri vsaki nalogi tako lahko prilagodimo navodila. Na enak način lahko prilagodimo tudi izpis rešitev.

Naloge se pojavljajo v dveh oblikah - naloga z enim primerom ali naloga z več primeri. Ker se v takih primerih
navodila pogosto razlikujejo imamo 2 različna parametra.

Besedila so surovi nizi, ki se pretvorijo v predloge `Python` knjižnice `Jinja2` (``Jinja2.Template``).
V predlogo se na mesta spremenljivk označenih z dvojnimi zaviti oklepaji kasneje vstavijo posamezne vrednosti naloge.

.. literalinclude:: ../../naravna_stevila.py
   :pyobject: DeliteljVeckratnik
   :lines: 16

Metoda ``_poskusi_sestaviti``, ki si jo bomo kasneje ogledali v razdelku :numref:`ref_poskusi_sestaviti`, vrne slovar vrednosti,
ki se vstavijo na manjkajoča mesta v predlogo. Ključi v slovarju, se morajo ujemati z imeni spremenljivk v predlogi.
Če spreminjamo predlogo, moramo paziti, da obdržimo enaka imena spremenljivk, saj so vezana na ključe slovarja.



Parameter število nalog
########################
Prav tako ima vsaka naloga parameter `število nalog` (``st_nalog``) s katerim določamo koliko primerov posamezne naloge želimo imeti.
Privzeta vrednost je en primer. Če želimo več primerov pa moramo podati naravno številsko vrednost, koliko primerov želimo.

Naslednja koda, bi ustvarila test, z dvema enakima nalogama. Prva naloga ima samo 1 primer računa, druga naloga pa 5 primerov.


.. code-block:: python

    >>>sestavi_vse_teste([kompleksna_stevila.Mnozenje(), kompleksna_stevila.Mnozenje(st_nalog=5)])

.. figure:: slike/st_nalog.png
    :align: center

    Izpis naloge z enim primerom in s petimi primeri


Dodatni parametri
##############################
Ostali parametri so specifični za vsako nalogo posebej. Z njimi lahko uravnavamo zahtevnost naloge ali kako lepe so številske
rešitve. Včasih je lahko zelo podobna naloga primerna za različne stopnje znanja in s parametri lahko določimo
na kateri stopnji znanja so učenci. Vsi podani parametri imajo podane privzete vrednosti, tako da jih ni potrebno
določati, če tega ne želimo.

V nadaljevanju bo predstavljenih nekaj zanimivih primerov nalog. Za vsako nalogo sta podana 2 primera nalog - prvi s privzetimi
vrednostmi, drugi pa s spremenjenimi.

Pri nalogi ``DeliteljVeckratnik`` mora učenec izračunati najmanjši skupni večkratnik in največji skupni delitelj dveh števil.
S parametrom ``do`` lahko določamo velikost števil in tako omejimo zahtevnost računanja.
Privzeta vrednost so števila do 200. S parametrom ``najvecje_prastevilo`` pa določimo kaj je največje praštevilo,
ki se lahko pojavi v praštevilskem razcepu števil. Privzeta vrednost je 17.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import naravna_stevila
    >>> naravna_stevila.DeliteljVeckratnik().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import naravna_stevila
    >>> naravna_stevila.DeliteljVeckratnik(najvecje_prastevilo=41, do=1000).primer()

Pri računanju ničel polinoma se zahtevnost hitro povečuje z višanjem stopnje polinoma. Zato je pomembno, da lahko
s parametroma ``min_stopnja``, ki določa najmanjšo možno stopnjo polinoma, in ``max_stopnja``, ki določa
najvišjo možno stopnjo polinoma, uravnavamo polinomom katerih stopenj bomo iskali ničle. Ker lahko določamo zgornjo
in spodnjo mejo stopenj, tako obstaja nek razpon stopenj, da so naloge lahko raznolike. S parametroma
``min_nicla`` in ``max_nicla`` pa lahko določimo s kako visokimi vrednostmi bomo računali.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import polinomska_racionalna_funkcija
    >>> polinomska_racionalna_funkcija.NiclePolinoma().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import polinomska_racionalna_funkcija
    >>> polinomska_racionalna_funkcija.NiclePolinoma(max_stopnja=5, min_nicla=0, max_nicla=10).primer()

Zahtevnost naloge lahko spreminjamo tudi z zahtevnostjo predpisa. Pri zapisu elementov izpeljane množice
lahko podamo preprost predpis za :math:`n`
:math:`\{n ; 1 < n < 5\}` ali pa malo zahtevnejši z linearno kombinacijo :math:`\{ 3 \cdot n -2 ; 1 < n < 5\}`.
Ravno to spreminja parameter ``linearna_kombinacija`` naloge ``ElementiMnozice``.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import mnozice
    >>> mnozice.ElementiMnozice().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import mnozice
    >>> mnozice.ElementiMnozice(linearna_kombinacija=True).primer()

Težavnost naloge lahko povečamo, če uvedemo dodaten korak ali znanje, ki je potrebno za reševanje naloge.
Pri reševanju eksponentnih enačb, kjer nastopata dve različni osnovi, je pogosto potrebno samo izpostaviti
vsako osnovo na svoji strani in izenačiti eksponenta. Vendar pa lahko nalogo napišemo tako, da je vsaka osnova pomnožena
s potenco druge osnove. Tako moramo pri reševanju dodati še korak deljenja.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import eksponentna_funkcija
    >>> eksponentna_funkcija.Enacba2osnovi().primer()


.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import eksponentna_funkcija
    >>> eksponentna_funkcija.Enacba2osnovi(deli_z_osnovo=True).primer()

Reševanje enačb s kompleksnimi števili lahko naredimo bolj raznoliko, če poleg neznanega števila :math:`z` nastopa
še njegova konjugirana vrednost :math:`\overline{z}`. To lahko v nalogi ``Enacba`` določimo s parametrom
``konjugirana_vrednost``.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import kompleksna_stevila
    >>> kompleksna_stevila.Enacba().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import kompleksna_stevila
    >>> kompleksna_stevila.Enacba(konjugirana_vrednost=True).primer()


Včasih lahko podobne naloge rešujemo z različnimi stopnjami znanja, zato je potrebno nalogo prilagoditi trenutnemu
znanju učencev. V poglavju stožnic se pogosto najprej spozna enačbe v središčni legi, kasneje pa šele v premaknjeni legi.
Zato je smiselno, da lahko pri nalogi ``TemeGorisceEnacba``, kjer določamo teme in gorišča elipse, določimo lego elipse
s parametrom ``premaknjena``.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import stoznice
    >>> stoznice.TemeGorisceEnacba().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import stoznice
    >>> stoznice.TemeGorisceEnacba(premaknjena=True).primer()

V poglavju odvodi učenci postopoma spoznavajo odvode različnih funkcij. Nalogo ``OdvodSestavljene`` s parametrom
``funkcije`` lahko prilagodimo za primerno znanje, oziroma lahko določamo njeno zahtevnost. Izbiramo lahko med
eksponentnimi, logaritemskimi, racionalnimi, polinomskimi ali kotnimi funkcijami. Da program lahko ločuje
med vrstami funkcij, so imena funkcij določena s posebnim razredom ``Funkcija``.

.. literalinclude:: ../../odvodi.py
   :pyobject: Funkcija

Funkcije, ki se lahko pojavijo v računu torej določimo s parametrom ``funkcije`` tako da jih naštejemo v seznamu.

Primer: ``funkcije=[odvodi.Funkcija.KOTNA, odvodi.Funkcija.LOGARITEM]``

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import odvodi
    >>> odvodi.OdvodSestavljene().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import odvodi
    >>> odvodi.OdvodSestavljene(funkcije=[odvodi.Funkcija.KOTNA, odvodi.Funkcija.LOGARITEM]).primer()


Rešitvi kvadratne enačbe sta lahko kompleksni števili, vendar se lahko zgodi, da takih rešitev ne želimo ali
da snovi kompleksnih števil še nismo obravnavali. Zato lahko nalogi ``IzracunajNicle`` s parametrom
``kompleksni_nicli`` določimo ali želimo da sta rešitvi kompleksni ali realni števili.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import kvadratna_funkcija
    >>> kvadratna_funkcija.IzracunajNicle().primer()

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import kvadratna_funkcija
    >>> kvadratna_funkcija.IzracunajNicle(kompleksni_nicli=True).primer()

Pri računanju algebrajskih izrazov, je za na videz podobne naloge potrebno različno znanje. Naloga ``PotencirajVecclenik``
ima zato več parametrov. Parametra ``min_clenov`` in ``max_clenov`` določata ali v nalogi potenciramo dvočlenike,
tročlenike ali malo mešano.  Parametra ``min_potenca`` in ``mix_potenca`` pa določata razpon potenc.
Na ta način lahko dobimo raznolike primere posameznega tipa naloge.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import izrazi
    >>> izrazi.PotencirajVecclenik().primer()


.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import izrazi
    >>> izrazi.PotencirajVecclenik(max_clenov=2,max_potenca=5).primer()

**********************************************
Sestavljanje predlog za teste in rešitve
**********************************************

Predloge za teste in rešitve lahko sestavimo tudi sami. Za to potrebujemo osnovno znanje `LaTeX`-a
in razumevanje, kako se vrednosti vstavijo v predloge.
Predloge so `LaTeX` datoteke, ki imajo namesto konkretnih vrednosti napisane spremenljive. Na mesta
slednjih se s pomočjo paketa ``Jinja2`` vstavijo želene vrednosti.
``Jinja2`` za označevanje spremenljivk uporablja
dvojne zavite oklepaje in znotraj ime spremenljivke.


Na mesto spremenljivke lahko `Python` program vstavi konkretne vrednosti. Podan mora
biti slovar, ki ima za ključ točno ime spremenljivke, za vrednost pa vrednost te spremenljivke.
Zato je pomembno, da v predlogo točno zapišemo imena spremenljivk.

Primer:

.. code-block:: latex

    Lepo pozdravljeni {{ime_priimek}}!

.. code-block:: python

    {'ime_priimek' : 'Marjan Novak'}

.. code-block:: latex

    Lepo pozdravljeni Marjan Novak!

V primeru, da bo spremenljivka v `LaTeX`-u obdana z okoljem, ki ga določamo z zavitimi oklepaji, moramo biti pozorni, da
naredimo presledek med oklepaji okolja in oklepajema spremenljivke.

.. literalinclude:: ../../vzorci/vzorec_testa1.tex
   :lines: 14-15

`Jinja` pozna tudi `if` stavek in `for` zanko, ki nam pogosto prideta prav in ju lahko tudi kombiniramo.

.. code-block:: latex

    {% for element in seznam %}
        {{element.spremenljivka}}
    {% endfor %}

.. code-block:: latex

    {% if pogoj %}
        To se izpiše, če je pogoj izpolnjen.
    {% else %}
        To se izpiše, če pogoj ni izpolnjen.
    {% endif%}

V naslednjem primeru si lahko ogledamo primer `for` zanke, ki za vsako nalogo iz seznama nalog, doda
nov element na `LaTeX` seznam in če seznam točk obstaja (ima dolžino), doda še vrednost točk s seznama točk
z enakim indeksom kot ga ima `for` zanka za naloge.
Uporabimo lahko tudi nekatere funkcije, ki jih ima `Jinja` vgrajene.
Več o uporabi paketa `Jinja` si lahko preberte v
`spletni dokumentaciji Jinja <https://jinja.palletsprojects.com/en/2.10.x/>`_.

.. literalinclude:: ../../vzorci/vzorec_testa1.tex
   :lines: 17-25

Ko sestavljamo svojo predlogo za teste ali rešitve, moramo poznati imena spremenljivk, ki jih
vrne funkcija `sestavi_vse_teste`. Ustvarimo `LaTeX` dokument in sestavimo želeno obliko testa.
Namesto konkretnih vrednosti pa zapišemo `Jinja` spremenljivke.
Ime testa je podano s spremenljivko ``ime_testa``, ime učenca ali skupine pa s spremenljivko
``ucenec``. Seznam nalog za posameznega učenca je podan z imenom
``naloge`` pripadajoči seznam točk pa s spremenljivko ``tocke``.

.. literalinclude:: ../../vzorci/vzorec_testa1.tex

Pri sestavljanju predlog za rešitve moramo ločiti kadar imamo skupne rešitve vseh učencev v eni
datoteki ali posamezen dokument rešitev za vsakega učenca.

V primeru skupnih rešitev ustvarimo eno `LaTeX` datoteko in nato naredimo `for` zanko, ki za vsakega
učenca s seznama ``seznam`` naredi svoj del dokumenta. Spremenljivki ``ime_testa`` in ``tocke`` sta za vse učence enake.
Posamezni elementi seznama ``seznam`` so slovarji, ki vsebujejo ime učenca ``ucenec``, seznam nalog za tega učenca
``naloge`` in pripadajoče rešitve ``resitve``.

.. literalinclude:: ../../vzorci/vzorec_skupnih_resitev1.tex

Kadar sestavljamo posamezne rešitve, ustvarimo `LaTeX` dokument v katerega lahko zapišemo ime testa ``ime_testa`` in
ime učenca ``ucenec``. Seznam nalog je podan s spremenljivko ``naloge``, seznam rešitev s spremenljivko ``resitve`` in
seznam točk s spremenljivko ``tocke``. Da jih lahko zapišemo posamezno, uporabimo `for` zanko.
Ujemanje indeksov nalog, rešitev in točk najlažje dosežemo tako, da naredimo zanko po enem od
seznamov in za ostale kličemo samo element z istim indeksom s pomočjo števca ``loop.index0``.

.. literalinclude:: ../../vzorci/vzorec_posameznih_resitev2.tex

