Sestavljanje nalog
======================================================

Vsaka naloga v knjižnici je svoj razred, vse pa dedujejo lastnosti iz razreda ``Naloga``, ki je podrobneje predstavljen v poglavju 4.
.. Todo (glej točko 4)


Če želimo sestaviti novo nalogo, jo lahko dodamo v katero od obstoječih poglavij ali pa ustvarimo popolnoma novo datoteko.
Na novo ustvarjeno poglavje nalog mora najprej uvoziti razred ``Naloga``  in metodo ``preveri`` iz ``generiranje.py``.
Za naključno generirane vrednosti moramo uvoziti še paket ``random``. Paket ``sympy`` pa nam omogoča simbolno računanje.

.. literalinclude:: ../../eksponentna_funkcija.py
   :lines: 1-3

Da bomo naloge lahko dodajali v teste, moramo na koncu našo novo ustvarjeno poglavje uvoziti še v program ``generiranje.py``.

.. code-block:: python

    import novo_poglavje

Sedaj smo pripravljeni, da napišemo svojo nalogo, sestavljeno iz dveh glavnih delov:

* predlog za besedilo naloge in rešitev
* metode ``_poskusi_sestaviti``

V dodatku C je pripravljena predloga za novo nalogo.
.. TODO sklic na vzorčno v C


*********************************************
Predloge za besedilo in rešitev naloge
*********************************************
Potrebno je sestaviti 4 nize:

* ``besedilo_posamezne``,
* ``besedilo_večih``,
* ``rešitev_posamezne`` in
* ``rešitev_večih``.


Posamezen niz se bo kasneje pretvoril v ``Jinja2.Template`` in nato v `LaTeX`-ov dokument. Zato je verjetno najlažje,
da so nizi surovi (ang. raw string),
saj se tako izognemo težavam pri zapisu posameznih posebnih `Python` simbolov, kot je recimo poševnica nazaj.

.. TODO Kaj je raw niz

Niz ``besedilo_posamezne`` je navodilo za reševanje naloge, ki ustreza vsem primerom sestavljene naloge. Namesto
konkretnih primerov pa napišemo ``Jinja2`` spremenljivke. ``Jinja2`` za označevanje spremenljivk uporablja
dvojne zavite oklepaje in znotraj ime spremenljivke. Spremenljivke, ki bodo v `LaTeX`-u zapisane v matematičnem načinu
moramo obdati z znakom '$'.
Na mesto spremenljivke se bo kasneje dodala vrednost, ki jo bo sestavila metoda ``_poskusi_sestaviti``.
Na enak način zapišemo tudi preostale nize. Niz ``resitev_posamezne`` je niz za izpis rešitev naloge z enim primerom.

.. code-block:: python

    besedilo_posamezne = r'''Nariši graf {{naloga.ime_funkcije}} funkcije ${{naloga.matematicno_zapisana_spremenljivka}}$.''

Knjižnica ``sympy`` s klicem funkcije ``latex`` pretvori python matematični zapis v latex-ov matematični zapis.
Za lažjo uporabo, sem ``sympy`` funkciji  ``latex``  in ``expand`` dodala med funkcije, ki jih ``Jinja2`` prepozna.

.. Todo dodaj sklic na kodo v generiranju ki doda funkciji ali sklic na dodatek B

.. literalinclude:: ../../eksponentna_funkcija.py
   :pyobject: Enacba
   :lines: 14, 22


Niza ``besedilo_vecih`` in ``resitev_vecih`` sta za izpis besedila oziroma rešitev naloge z več primeri.
Običajno je navodilo samo eno, nato pa sledi (oštevilčeni) seznam primerov. Testi se izpisujejo v obliki ``LaTeX`` dokumentov,
zato je najpogosteje smiselno, da v nizu pripravimo izpis ``LaTeX`` seznama. To naredimo tako, da uporabimo okolje
``itemize`` za neoštevilčeni seznam ali okolje ``enumerate`` za oštevilčeni seznam. Pred posamezno točko seznama kličemo
element `\item`.
..TODO vir za latex sezname
Program nam več primerov izpiše z pomočjo `for` zanke. Primer `Jinja` zanke spremenljivke:

.. code-block:: python

	{% for element in seznam %}
    {{element.spremenljivka}}
    {% endfor %}

.. todo vir za jinja zanko.

.. literalinclude:: ../../eksponentna_funkcija.py
   :pyobject: Enacba
   :lines: 15-21, 23-29

.. _ref-poskusi-sestaviti:

*********************************************
Metoda ``_poskusi_sestaviti``
*********************************************
Metoda ``_poskusi_sestaviti`` sestavi posamezen primer za nalogo in vrne slovar vrednosti, ki jih metoda ``generiranje.besedilo``
vstavi na mesta spremenljivk v predlogah besedil in rešitev. Imena spremenljivk se morajo ujemati s ključi slovarja,
vrednosti slovarja pa so dejanske vrednosti naloge. Metoda ``_poskusi_sestaviti`` vedno vrne samo en primer.

Če želimo nalogo z več primeri, bo za to poskrbela metoda `generiranje.besedilo``, ki za vsak primer pokliče metodo
``_poskusi_sestaviti``. Podrobnosti, o tem si lahko preberete v :ref:`ref-implementacija`.
.. todo sklic  na poglavje 4

Naključnost
#############

Raznolikost primerov zagotovimo tako, da v sestavljanje naloge vključimo naključnost. To nam omogoča Python knjižnica
``Random``, ki generira psevdo-naključne vrednosti. Knjižnica vsebuje funkcije, ki lahko psevdo-naključno premešajo
vrstni red, izberejo vzorec s seznam, izberejo število in še mnogo več. Če želimo, da so rezultati ponovljivi lahko
določimo seme generatorja s funkcijo ``random.seed``. Več si lahko o knjižnici preberete v uradni dokumentaciji na spletu.

..TODO vir random https://docs.python.org/3/library/random.html

Najpogosteje sem uporabila funkcije:

* ``random.randint``, ki vrne naključno celo število
* ``random.choice``, ki izbere element s seznama
* ``random.sample``, ki iz seznama izbere določeno število različnih elementov.


.. literalinclude:: ../../naravna_stevila.py
   :pyobject: DeliteljVeckratnik._poskusi_sestaviti
   :emphasize-lines: 2-3

Pri sestavljanju nalog iz srednješolske matematike, je za različne naloge potrebno izbrati enak objekte. V knjižnici
nalog lahko najdemo nekaj pomožnih funkcij, ki vračajo željene naključne objekte.

V poglavjih, ki obravnavajo posamezne funkcije ali odvode, najdemo generatorje željenih funkcij.

.. literalinclude:: ../../kvadratna_funkcija.py
   :pyobject: splosna_oblika

Lahko tudi v različnih oblikah.

.. literalinclude:: ../../kvadratna_funkcija.py
   :pyobject: nicelna_oblika

Funkcije lahko generirajo tudi drugačne željene objekte.

.. literalinclude:: ../../mnozice.py
   :pyobject: izberi_mnozico

Naključno izbrani operatoji
****************************
Včasih lahko raznolikost nalog dosežemo tudi tako, da namesto samo naključno generiranih vrednosti, tudi operacije med
vrednostmi izberemo naključno.

.. literalinclude:: ../../odvodi.py
    :pyobject: OdvodSestavljene._poskusi_sestaviti
    :emphasize-lines: 34-40


Simbolno računanje
###################
Za računanje z neznankami, mora program podpirati simbolno računanje. V ta namen je uporabljena knjižnica ``sympy``, ki
omogoča da določimo nek niz kot simbol in ga lahko uporabimo v matematičnih operacijah. Knjižnica ima tudi veliko
različnih objektov kot so polinomi (``Poly``), stožnice (``Circle``, ``Ellipse``), racionalna števila (``Rational``),…
Na znanih objektih je možno uporabiti veliko funkcij in tako izračunati vrednosti izrazov, poenostaviti ali celo
pretvoriti v niz v `LaTeX` obliki.

.. literalinclude:: ../../stoznice.py
    :pyobject: PreseciscaKroznic._poskusi_sestaviti
    :emphasize-lines: 2, 3, 13, 14, 15, 18, 19

Lepe rešitve in funkcija preveri
###################################
Naključno izbrane vrednosti, nam še ne zagotavljajo, da bodo tudi rešitve lepe vrednosti.  Da bodo tudi rešitve lepe,
najlažje zagotovimo tako, da rešitve naloge izberemo vnaprej in nato okoli tega sestavimo nalogo ali pa da jih
preverimo s metodo ``preveri``. Funkcija ``preveri`` zagotovi, da program zavrne naloge, ki ne ustrezajo pogoju. Na ta način
lahko zagotovimo lepši rezultat ali pa preprečimo nesmiselne naloge.

Vnaprej izbrana rešitev:

.. literalinclude:: ../../kompleksna_stevila.py
   :pyobject: Enacba._poskusi_sestaviti
   :emphasize-lines: 4

Funkcija `preveri` zagotovi lepši rezultat:

.. literalinclude:: ../../kvadratna_funkcija.py
   :pyobject: NarisiGraf._poskusi_sestaviti
   :emphasize-lines: 6

Funkcija `preveri` zagotovi smiseln rezultat.

.. literalinclude:: ../../linearna_funkcija.py
   :pyobject: PremicaSkoziTocki._poskusi_sestaviti
   :emphasize-lines: 6


Grafi
######
V naloge oziroma njihove rešitve lahko vključujemo tudi grafe. To nam omogoča `LaTeX` paket `pgfplots`, ki avtomatično
generira slike grafov. Pomembno je, da grafe podamo v obliki, ki jo `pgfplots` zna razbrati. Funkcije, ki jih želimo
narisati, moramo najprej s funkcijo `sympy.latex` spremeniti v nize, ki jih `LaTeX` generator zna prevesti. Vendar
moramo biti pozorni na oznako za potence. V matematičnem načinu zapišemo potence z oznako `**`, za risanje grafov pa
jih moramo zapisati z znakom `^`.

.. literalinclude:: ../../eksponentna_funkcija.py
    :pyobject: GrafEksponentne._poskusi_sestaviti
    :emphasize-lines: 7-8

Včasih je zato lažje, da funkcijo za risanje podamo kot produkt faktorjev (na primer v ničelni obliki).

.. literalinclude:: ../../kvadratna_funkcija.py
    :pyobject: NarisiGraf._poskusi_sestaviti
    :emphasize-lines: 3,8

Zahtevnost naloge
###################
S podajanjem parametrov, lahko nalogo spremenimo v lažjo ali težjo. Primeri, kako lahko s parametri spreminjamo
zahtevnost nalog, so predstavljeni v poglavju :ref:`ref_uporaba`
Če želimo prilagodljivo zahtevnost mora biti tudi metoda ``_poskusi_sestaviti`` prilagojena. Lahko s funkcijo ``preveri``
zagotovimo primerno težke rešitve.

.. literalinclude:: ../../kvadratna_funkcija.py
   :pyobject: IzracunajNicle._poskusi_sestaviti

Lahko pa že metodo napišemo razdeljeno za različno zahtevnost.

.. literalinclude:: ../../eksponentna_funkcija.py
   :pyobject: Enacba2osnovi._poskusi_sestaviti


.. TODO  zanimivi primeri ?





