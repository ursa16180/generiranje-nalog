.. _ref_uporaba:

Uporaba
============

Program za generiranje nalog je sestavljen iz knjižnice nalog iz različnih področij srednješolske matematike in programa
za sestavljanje testov. Ko zaženemo program z želenimi parametri nam ustvari teste in rešitve v `LaTeX` datotekah ter po
želji tudi v `PDF` datotekah.

********
Naloge
********
Vsebuje 60 takih nalog iz teh področij
.. todo katere naloge

**************
Izpis testov
**************
Za izpis testov je potrebno poklicati funkcijo ``sestavi_vse_teste`` iz datoteke ``generiranje.py``. Funkcija sprejme pet parametrov

#. seznam nalog
#. ime testa
#. datoteko, ki vsebuje seznam učencev
#. izbira združenih ali ločenih rešitev
#. izbira za avtomatično generiranje PDF datotek

in ustvari teste ter rešitve kot `LaTeX` dokumente. Če želimo lahko avtomatično ustvari dokumente tudi v `PDF` formatu.
`LaTeX` dokument je na voljo zato, da vedno lahko kaj naknadno spremenimo alii popravimo.

.. code-block:: python

    >>>sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3),
                                          izrazi.RazstaviRazliko(min_potenca=3),
                                          naravna_stevila.DeliteljVeckratnik()],
                                  ime_testa='Izrazi in deljivost', datoteka_seznam_učencev='ucenci.txt',
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
                                  ime_testa='Izrazi in deljivost', datoteka_seznam_ucencev='ucenci.txt',
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
Parameter ``ime_testa`` je niz željenega imena testa. Izbrano ime je lahko poljubno in lahko vsebuje tudi presledke,
šumnike in druge znake. Ime testa se izpiše na vrhu posameznega testa in rešitev. Enako ime ima tudi na novo ustvarjena
mapa, ki vsebuje teste in rešitve. Če imena testa ne podamo, se namesto njega izpiše današnji datum.

Primer:

``ime_testa='Izrazi in deljivost'``

.. TODO ali želim tudi tukaj ponoviti kaj se zgodi če ime že obstaja

Seznam učencev
################
Seznam učencev napišemo v ločeni tekstovni datoteki (`.txt`), tako da so podatki posameznega učenca v svoji vrstici.
Podatki učenca so lahko poljubni: ime, priimek, vpisna številka... Namesto podatkov učencev lahko podamo tudi naprimer imena skupin: A in B.
Podatek v posamezni vrstici predstavlja podnaslov našega testa in ime datoteke posameznega testa ali rešitve.

.. figure:: slike/ucenci.png
    :align: center

    Primer tekstovne datotetke

.. figure:: slike/testi.png
    :align: center

    Primer mape z generiranimi testi.

Če datoteka s seznamom ni podana, bo program ustvaril samo 1 test s privzetim podnaslovom `Matematika`.

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

    >>> sestavi_vse_teste(
        naloge=[izrazi.PotencaDvoclenika(st_nalog=3),izrazi.RazstaviRazliko(min_potenca=3),
        naravna_stevila.DeliteljVeckratnik()],
        ime_testa='Izrazi in deljivost',
        zdruzene_resitve=True)
    Sestavljam test Izrazi in deljivost.
    Izpisujem test: Matematika
    Izpisujem skupne rešitve za test Izrazi in deljivost.
    Test Izrazi in deljivost je sestavljen.


.. _ref-parametri:

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
S parametrim ``do`` lahko določamo kako veliki sta lahko števili in tako omejimo kako zahtevno bo računanje.
Privzeta vrednost so števila do 200. S parametrom ``najvecje_prastevilo`` pa določimo kaj je navečje praštevilo, ki se lahko pojavi v praštevilskem razcepu števil. Privzeta vrednost je 17.

.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: DeliteljVeckratnik

Naloga ``SistemDvehEnacb`` iz poglanja linearn funkcija ima lahko različno zahtevne številske rešitve. Običajno nam je
lažje izručunati celoštevilske rešitve. Če pa določimo parameter ``racionalne_resitve=True``, pa bo naloga bolj raznolika,
saj bodo lahko rešitve tako celoštevilske kot tudi racionalne. Na tak način lahko dosežemo tudi večjo raznolikost nalog.

.. literalinclude:: ..\..\linearna_funkcija.py
   :pyobject: SistemDvehEnacb

Podobno lahko tudi računanje prvih členov zaporedja naredimo malo računsko zahtevnejših, če lahko za prvi člen in
diferenco določimo racionalna števila namesto celih.

.. literalinclude:: ..\..\zaporedja.py
   :pyobject: PrviCleniAritmeticnega

Pri računanju ničel polinoma se zahtevnost hitro povečuje z višanjem stopnje polinoma. Zato je pomembno, da lahko
s parametroma ``min_stopnja``, ki določa najmanjšo možno stopnjo polinoma, in ``max_stopnja``, ki določa
najvišjo možno stopnjo polinoma, uravnavamo polinomom kakšnih stopenj bomo iskali ničle. Ker lahko določamo zgornjo
in spodnjo mejo stopenj, tako obstaja nek razpon stopenj, da so naloge lahko raznolike. S parametroma
``min_nicla`` in ``max_nicla`` pa lahko določimo s kako velikimi vrednostimi bomo računali.

.. literalinclude:: ..\..\polinomska_racionalna_funkcija.py
   :pyobject: NiclePolinoma

Zahtevnost naloge lahko spreminjamo tudi z zahtevnostjo predpisa. Pri zapisu elementov izpeljane množice
lahko podamo preprost predpis za :math:`n`
:math:`\{n ; 1 < n < 5\}` ali pa malo zahtevnejši z linearno kombinacijo :math:`\{ 3 \cdot n -2 ; 1 < n < 5\}`.
Ravno to spreminja parameter ``linearna_kombinacija`` naloge ``ElementiMnozice``.

.. literalinclude:: ..\..\mnozice.py
   :pyobject: ElementiMnozice

Težavnost naloge lahko povečamo, če uvedemo dodaten korak ali znanje, ki je potrebno za rešitev naloge.
Pri reševanju eksponentnih enačb, kjer nastopata dve različni osnovi, je pogosto potrebno samo izpostaviti
vsako osnovo na svoji strani in izenačiti eksponenta. Vendar pa lahko nalogo napišemo tako, da je vsaka osnova pomnožena
s potenco druge osnove. Tako moramo pri reševanju dodati še korak deljenja.

.. literalinclude:: ..\..\eksponentna_funkcija.py
   :pyobject: Enacba2osnovi

Reševanje enačb s kompleksnimi števili lahko naredimo bolj raznolike, če poleg neznanega števila :math:`z` nastopa
še njego konjugirana vrednost :math:`\overline{z}`. To lahko v nalogi ``Enacba`` določimo s parametrom
``konjugirana_vrednost``.

.. literalinclude:: ..\..\kompleksna_stevila.py
   :pyobject: Enacba

Včasih lahko podobne naloge rešujemo z različnimi stopnjami znanja, zato je potrebno nalogo prilagoditi trenutnemu
znanju učencev. V poglavju stožnic se pogosto najprej spozna enačbe v središčni legi, kasneje pa šele v premaknjeni legi.
Zato je smiselno, da lahko pri nalogi ``TemeGorisceEnacba``, kjer določamo teme in gorišča elipse, določimo s parametrom ``premaknjena``,
ki lego elipse.


.. literalinclude:: ..\..\stoznice.py
   :pyobject: TemeGorisceEnacba

V poglavju odvodi učenci postopoma spoznavajo odvode različnih funkcij. Nalogo ``OdvodSestavljene`` s parametrom
``funkcije`` lahko prilagodimo za primerno znanje, oziroma lahko določamo njeno zahtevnost. Izbiramo lahko med
eksponentnimi, logaritemskimi, racionalnimi, polinomskimi ali kotnimi funkcijami. Da program lahko ločuje,
med vrstami funkcijami so imena funkcij določena z razredom ``Funkcija``.

.. literalinclude:: ..\..\odvodi.py
   :pyobject: Funkcija

Funkcije, ki se lahko pojavijo v računu torej določimo s parametrom ``funkcije`` tako da jih naštejemo v seznamu.

Primer: ``funkcije=[Funkcija.KOTNA, Funkcija.LOGARITEM]``

.. literalinclude:: ..\..\odvodi.py
   :pyobject: OdvodSestavljene

Rešitvi kvadratne enačbe sta lahko kompleksni števili, vendar se lahko zgodi, da takih rešitev ne želimo ali
da snovi kompleksnih števil še nismo obravnavali. Zato lahko nalogi ``IzracunajNicle`` s parametrom
``kompleksni_nicli`` določimo ali želimo da sta rešitvi kompleksni ali realni števili.

.. literalinclude:: ..\..\kvadratna_funkcija.py
   :pyobject: IzracunajNicle

Pri računanju algebrajskih izrazov, je za na videz podobne naloge potrebno različno znanje. Naloga ``PotencirajVecclenik``
ima zato več parametrov. Parametra ``min_clenov`` in ``max_clenov`` določata ali v nalogi potenciramo dvočlenike,
tročlenike ali malo mešano.  Parametra ``min_potenca`` in ``mix_potenca`` pa določata razpon potenc.
Na ta način lahko dobimo raznolike primere enega tipa naloge.

.. literalinclude:: ..\..\izrazi.py
   :pyobject: PotencirajVecclenik

