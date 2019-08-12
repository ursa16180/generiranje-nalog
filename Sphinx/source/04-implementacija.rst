.. _ref-implementacija:

Implementacija knjižnice in izpis testov
==========================================

Knjižnici nalog je dodana še datoteka ``generiranje.py``, ki vključuje program za izpis testov in razred ``Naloga``,
katerega metode in vrednosti dedujejo posamezne naloge. Dodana je tudi mapa `vzorci`, ki vsebuje vzorce za `LaTeX`
datoteko posameznega test, posameznih rešitev in skupnih rešitev. Slednje lahko po potrebi tudi prilagajmo, vendar
moramo biti pozorni, da ne spreminjamo imena spremenljivk znotraj dvojnih zavitih oklepajev.

****************
Razred Naloga
****************
Vse naloge v knjižnici dedujejo atribute in metode razreda ``Naloga``. Kodo za razred si lahko podrobno ogledate v razdelku :ref:`ref-izvorna-koda`.

.. .. literalinclude:: ..\..\generiranje.py     :pyobject: Naloga

Razred ima 5 atributov

* ``st_nalog``,
* ``besedilo_posamezne``,
* ``besedilo_vecih``,
* ``resitev_posamezne`` in
* ``resitev_vecih``

ter 5 metod

* ``_poskusi_sestaviti``,
* ``sestavi``,
* ``sestavi_vec``,
* ``besedilo`` in
* ``primer``.


.. todo ali je smiselno opisovati atribute

Atributi
#########

Besedila nalog in rešitev
**************************
Razred naloga ima zelo podana splošna besedila, v katere se na mesto spremenljivke vstavi kar celoten slovar,
ki ga vrne metoda ``_poskusi_sestaviti``. Veliko bolj jasno je, če za posamezno nalogo napišemo podrobnejša besedila,
ki primerno razbijejo slovar. Atributi posamezne naloge prepišejo vrednosti teh zelo splošnih atributov.


Število nalog
**************
Atribut ``st_nalog`` določa število posameznih primerov naloge. Njegova privzeta vrednost je ``None`` in pomeni 1 primer.
Če želimo več primerov posamezne naloge, mora biti podano naravno število.

Metode
#######

Metoda ``_poskusi_sestaviti``
*******************************
.. todo tle ni kej napisat

Metoda ``sestavi``
*******************************
Metoda ``sestavi`` vrne slovar z vrednosti posamezne naloge, ki ustrezajo želenim pogojem. To doseže tako, da kliče metodo
``_poskusi_sestaviti``, dokler ne dobi slovarja z želenimi vrednostmi.

Metoda ``sestavi_vec``
*******************************
Metoda ``sestavi_vec`` vrne seznam slovarjev, ki vsebujejo ustrezne vrednosti posameznih primerov naloge. Posamezne
elemente seznama pa dobi tako, da kliče metodo ``sestavi``.


Metoda ``besedilo``
*******************************
Metoda ``besedilo`` spremeni surove nize besedil nalog in rešitev v  ``Jinja2`` predloge (``Jinja2.Template``) in vanje vstavi
konkretne vrednosti naloge ,ki jih dobi s klicem metode ``sestavi`` ali ``sestavi_vec``.
Prva se kliče, če želimo nalogo samo z enim primerom, druga pa če želimo nalogo zveč primeri.
Metoda vrne slovar, ki vsebuje nalogo in rešitev. Slednji sta se spremenili v končen niz besedila z vstavljenimi vrednostmi.

Metoda ``primer``
*******************************
Metoda ``primer`` prikaže, kako bi izgledal slovar z vrednostimi naloge in besedilo naloge z vstavljenimi vrednostimi,
da si uporabnik lažje predstavlja sestavljeno nalogo. Prikaže tako besedilo za nalogo z enim primerom ali nalogo z
večimi primeri.

.. code-block:: python

    >>> naravna_stevila.EvklidovAlgoritem().primer()
    Slovar posamezne: {'stevilo1': 187, 'stevilo2': 996, 'najvecji_delitelj': 1}
    Besedilo posamezne: Z Evklidovim algoritmom poišči največji skupni delitelj števil $187$ in $996$.
    Slovar vecih: [{'stevilo1': 187, 'stevilo2': 996, 'najvecji_delitelj': 1}, {'stevilo1': 89, 'stevilo2': 655, 'najvecji_delitelj': 1}, {'stevilo1': 96, 'stevilo2': 810, 'najvecji_delitelj': 6}]
    Besedilo večih: Z Evklidovim algoritmom poišči največji skupni delitelj števil:
        \begin{enumerate}

        \item $187$, $996$

        \item $89$, $655$

        \item $96$, $810$


*****************************************
Uporaba programa za izpis testov
*****************************************
Za sestavitev testov moramo iz datoteke ``generiranje.py`` klicati funkcijo ``sestavi_vse_teste``, ki ustvari vse teste
in rešitve.

.. code-block:: python

    >>> generiranje.sestavi_vse_teste(
    ...     naloge=[mnozice.PotencnaMnozica(), izrazi.PotencaDvoclenika(st_nalog=3), naravna_stevila.DeliteljVeckratnik()],
    ...     ime_testa='Množice, deljivost in izrazi', datoteka_seznam_dijakov='dijaki.txt', zdruzene_resitve=False)
    Sestavljam test Množice, deljivost in izrazi.
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
    Test Množice, deljivost in izrazi je sestavljen.

Funkcija ``sestavi_vse_teste``
################################

Funkcija sprejme 5 argumentov:

* ``naloge``
* ``ime_testa``
* ``datoteka_seznam_dijakov``
* ``zdruzene_resitve``
* ``pdf``

Najprej ustvari mapo z imenom testa in 2 podmapi za naloge in rešitve. Če ime ni določeno, uporabi trenutni datum.
V primeru da mapa z imenom testa že obstaja, nas program vpraša, če jo želimo prepisati. Če izberemo "da", izbriše staro
mapo in ustvari novo, drugače pa samo ustvari novo mapo z enakim imenom, ki mu doda trenutno uro.
Nato za vsakega učenca s seznama, ki nastane iz leksikografsko urejene datoteke ``datoteka_seznam_dijakov``,
ustvari seznam nalog in rešitev. Slednje dobi tako, da za naloge s seznama ``naloge`` kliče metodo ``besedilo``.
Če je seznam učencev ni podan, ustvari samo en test s podnaslovom `Matematika`.

.. todo a hočemo tukaj pojasniti semena?

Argument ``naloge`` je seznam nalog, ki jih želimo imeti v testu. Če je seznam prazen ali vsebuje neobstoječe naloge,
nas program na to opozori.
Program nato pokliče funkcijo ``napisi_test``, ki ustvari posamezne teste.
Kadar želimo za vsakega učenca samostojne rešitve kliče še funkcijo ``napisi_posamezno_resitev``, ki sestavi posamezne
rešitve. V primeru, da želimo eno datoteko z združenimi rešitvami za vse dijake, pa najprej naredi seznam vseh učencev
in pripadajočih rešitev, nato pa kliče funkcijo ``napisi_skupno_resitev``. Argument ``pdf`` je ``Bool`` vrednost, ki
določa, če želimo že avtomatično ustvariti teste in rešitve tudi v `PDF`
obliki. Če argument nastavimo na ``False``, bo program ustvaril samo `LaTeX` datoteke, če pa pustimo vrednost
nastavljeno na `True`, bo ustvaril tudi `PDF` dokumente.

.. literalinclude:: ..\..\generiranje.py
    :pyobject: sestavi_vse_teste

Funkcija ``napisi_test``
################################
Funkcija ``napisi_test`` sprejme 5 argumentov

* ``ime_testa``,
* ``seznam_nalog``,
* ``ucenec``,
* ``pot_naloge`` in
* ``pdf``

ter ustvari posamezen test za učenca.

V podmapi `Naloge` ustvari `LaTeX` datoteko z imenom arguemnta ``ucenec`` (`ucenec.tex`). Datoteka je ustvarjena iz predloge za
posamezen test `vzorec_testa.txt`, ki jo najdemo v mapi `vzorci`. Vzorec se spremeni v `Jinja2.Template` v katero se
na mesta spremenljivk vstavijo ustrezne naloge iz seznama `seznam_nalog`.
.. todo kako rečeš da v LaTeXu ni težav? kako rečeš da zaženeš LaTeX?

Kadar je argument ``pdf`` nastavljen na vrednost ``True``, program zažene `LaTeX` datoteko testa. Če v njej ni `LaTeX`
napak, program v isti mapi ustvari še `PDF` datoteko (`ucenec.pdf`) in izbriše datoteki `ucenec.log` ter `ucenec.aux`.
Drgače pa javi napako, o kateri si uporabnik lahko več prebere v datoteki `ucenec.log`.


.. literalinclude:: ..\..\generiranje.py
    :pyobject: napisi_test

Funkcija ``napisi_posamezno_resitev``
########################################

Funkcija ``napisi_posamezno_resitev`` deluje zelo podobno kot funkcija ``napisi_test``. V podmapi `Rešitve` ustvari
datoteko z imenom arguemnta ``ucenec`` in dodatkom `-resitve` (`ucenec-resitve.tex`). Na podlagi vzorca za rešitve
posameznika (`vzorec_posameznih_resitev.txt` )nato ustvari `LaTeX` datoteko z vstavljenimi rešitvami s seznama
``seznam_resitev``. Če je argument ``pdf`` nastavljen na vrednost ``True``, poskusi v isti mapi ustvariti še `PDF`
datoteko rešitev (`ucenec-resitve.pdf`).


.. literalinclude:: ..\..\generiranje.py
    :pyobject: napisi_posamezno_resitev

Funkcija ``napisi_skupno_resitev``
#####################################
Funkcija ``napisi_skupno_resitev`` v podmapi `Rešitve` ustvari `LaTeX` datoteko `Resitve.tex`. Datoteka je ustvarjena iz
predloge `vzorec_skupnih_resitev.txt`. Na ustrezna mesta spremenljivk se vstavijo imena učencev in njihovim nalogam
pripadajoče rešitve s seznama seznamov rešitev ``seznam_vseh_resitev``. Rešitve vsakega učenca se začnejo na novi
strani, vrstni red pa je določen z abecednim redom učencev. Če je argument ``pdf`` nastavljen na vrednost ``True``,
poskusi v isti mapi ustvariti še `PDF` datoteko rešitev (`Resitve.pdf`)

.. literalinclude:: ..\..\generiranje.py
    :pyobject: napisi_skupno_resitev


