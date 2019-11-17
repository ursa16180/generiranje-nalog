.. _ref-implementacija:

Implementacija knjižnice in izpis testov
==========================================

Knjižnici nalog je dodana še datoteka ``generiranje.py``, ki vključuje program za izpis testov in razred ``Naloga``,
katerega metode in vrednosti dedujejo posamezne naloge. Dodani sta mapa `vzorci`, ki vsebuje vzorce za `LaTeX`
datoteke posameznega test, posameznih rešitev in skupnih rešitev in mapa `Primeri testov`, ki vsebuje nekaj primerov
rabe programa.

****************
Razred Naloga
****************
Vse naloge v knjižnici dedujejo atribute in metode razreda ``Naloga``.

.. literalinclude:: ../../generiranje.py
    :pyobject: Naloga
    :lines: 1-42

.. todo preveri da vključene prave vrstice

Razred ima 5 atributov

#. ``st_nalog``,
#. ``besedilo_posamezne``,
#. ``besedilo_vecih``,
#. ``resitev_posamezne`` in
#. ``resitev_vecih``

ter 5 metod

#. ``_poskusi_sestaviti``,
#. ``sestavi``,
#. ``sestavi_vec``,
#. ``besedilo`` in
#. ``primer``.


Besedila nalog in rešitev
#############################
Razred naloga ima podana zelo splošna besedila, v katere se na mesto spremenljivke vstavi kar celoten slovar,
ki ga vrne metoda ``_poskusi_sestaviti``. Veliko bolj jasno je, če za posamezno nalogo napišemo podrobnejša besedila,
ki primerno razbijejo slovar. Atributi posamezne naloge prepišejo vrednosti teh zelo splošnih atributov.


Število nalog
#############################
Atribut ``st_nalog`` določa število posameznih primerov naloge. Njegova privzeta vrednost je ``None`` in pomeni 1 primer.
Če želimo več primerov posamezne naloge, mora biti podano naravno število.

.. _ref_poskusi_sestaviti:

Metoda ``_poskusi_sestaviti``
###############################
Vsaka posamezna naloga mora imeti metodo ``_poskusi_sestaviti``, drugače naloga nima nobene vsebine. V primeru, da
posamezna naloga nima definirane metode, kliče metodo nadrazreda, ki opozori, da metoda še ni bila implementirana in
da jo še potrebno napisati.

.. literalinclude:: ../../generiranje.py
    :pyobject: Naloga._poskusi_sestaviti

Metoda ``sestavi``
#############################
Metoda ``sestavi`` vrne slovar z vrednostmi posamezne naloge, ki ustrezajo želenim pogojem. To doseže tako, da kliče metodo
``_poskusi_sestaviti``, dokler ne dobi slovarja z želenimi vrednostmi.

.. literalinclude:: ../../generiranje.py
    :pyobject: Naloga.sestavi

Metoda ``sestavi_vec``
#############################
Metoda ``sestavi_vec`` vrne seznam slovarjev, ki vsebujejo ustrezne vrednosti posameznih primerov naloge. Posamezne
elemente seznama pa dobi tako, da kliče metodo ``sestavi``.

.. literalinclude:: ../../generiranje.py
    :pyobject: Naloga.sestavi_vec


Metoda ``besedilo``
#############################
Metoda ``besedilo`` spremeni surove nize besedil nalog in rešitev v  ``Jinja2`` predloge (``Jinja2.Template``) in vanje vstavi
konkretne vrednosti naloge, ki jih dobi s klicem metode ``sestavi`` ali ``sestavi_vec``.
Prva se kliče, če želimo nalogo samo z enim primerom, druga pa če želimo nalogo z več primeri.
Metoda vrne slovar, ki vsebuje nalogo in rešitev. Slednji sta se spremenili v končen niz besedila z vstavljenimi vrednostmi.

.. literalinclude:: ../../generiranje.py
    :pyobject: Naloga.besedilo

Metoda ``primer``
#############################
Metoda ``primer`` prikaže, kako bi izgledal slovar z vrednostmi naloge in besedilo naloge z vstavljenimi vrednostmi,
da si uporabnik lažje predstavlja sestavljeno nalogo. Prikaže seznam s tremi primeri ter besedilo za nalogo z enim
(prvim) primerom in besedilo naloge z več primeri.

.. runblock:: pycon

    >>> import sys
    >>> sys.path.append('../')
    >>> import naravna_stevila
    >>> naravna_stevila.EvklidovAlgoritem().primer()


.. literalinclude:: ../../generiranje.py
    :pyobject: Naloga.primer

************************
Razred NapacnaNaloga
************************
Razred ``NapacnaNaloge`` je podrazred izjem (`Exception`). Razred izjem pomaga pri opozarjanju na napake.
Več si lahko o njem preberete na spletu.
.. todo link https://docs.python.org/3/library/exceptions.html

Izjema `NapacnaNaloga` se sproži kadar sestavljene vrednosti niso ustrezne.


.. literalinclude:: ../../generiranje.py
    :pyobject: NapacnaNaloga

************************
Funkcija preveri
************************
Funkcija `preveri` sproži izjemo `NapacnaNaloga`, kadar vrednosti niso ustrezne. S funkcijo preveri zagotavljamo, da so
rešitve smiselne in ustrezajo vsem želenim parametrom. Včasih pa funkcija pomaga zagotoviti lepše rešitve.

.. literalinclude:: ../../generiranje.py
    :pyobject: preveri

*****************************************
Implementacija programa za izpis testov
*****************************************
Za sestavo testov moramo iz datoteke ``generiranje.py`` klicati funkcijo ``sestavi_vse_teste``, ki ustvari vse teste
in rešitve s klici drugih pomožnih funkcij.

.. code-block:: python

    >>> generiranje.sestavi_vse_teste(naloge=[zaporedja.SplosniClenAritmeticnegaZaporedja(od=-10, do=0),
                                          zaporedja.SplosniClenAritmeticnegaEnacbi(),
                                          zaporedja.VsotaAritmeticnega(podan_splosni_clen=False),
                                          zaporedja.SplosniClenGeometrijskegaEnacbi(),
                                          zaporedja.VsotaGeometrijskeVrste(lazji_podatki=False)],
                                  ime_testa="3. kontrolna naloga - Zaporedja",
                                  datoteka_seznam_ucencev="skupine.txt",
                                  zdruzene_resitve=False,
                                  pdf=True,
                                  pot_vzorca_testa="vzorci/vzorec_testa2.tex",
                                  pot_vzorca_resitev="vzorci/vzorec_skupnih_resitev2.tex")
    Sestavljam test 3. kontrolna naloga - Zaporedja.
    Izpisujem test: A
    Izpisujem rešitve: A
    Izpisujem test: B
    Izpisujem rešitve: B
    Test 3. kontrolna naloga - Zaporedja je sestavljen.



Funkcija ``napisi_test``
################################
Funkcija ``napisi_test`` sprejme 7 argumentov

* ``ime_testa``,
* ``seznam_nalog``,
* ``ucenec``,
* ``pot_naloge`` in
* ``pdf``
* ``pot_vzorca_testa``
* ``tocke``

ter ustvari posamezen test za učenca.

V podmapi `Naloge` ustvari `LaTeX` datoteko z imenom argumenta ``ucenec`` (`ucenec.tex`). Datoteka je ustvarjena iz predloge za
posamezen test, katerega podamo z nizom ``pot_vzorca_testa``. Nekaj primerov predlog najdemo v mapi `vzorci`. Vzorec se
spremeni v `Jinja2.Template` v katero se na mesta spremenljivk vstavijo ustrezne naloge iz seznama `seznam_nalog` in
vrednosti možnih točk, kadar so podane.

Kadar je argument ``pdf`` nastavljen na vrednost ``True``, program zažene `LaTeX` datoteko testa. Če uspešno prevede
`LaTeX` datoteko, program v isti mapi ustvari še `PDF` datoteko (`ucenec.pdf`) in izbriše datoteki `ucenec.log` ter `ucenec.aux`.
Drugače pa javi napako, o kateri si uporabnik lahko več prebere v datoteki `ucenec.log`.


.. literalinclude:: ../../generiranje.py
    :pyobject: napisi_test

Funkcija ``napisi_posamezno_resitev``
########################################

Funkcija ``napisi_posamezno_resitev`` deluje zelo podobno kot funkcija ``napisi_test``. V podmapi `Rešitve` ustvari
datoteko z imenom argumenta ``ucenec`` in dodatkom `-resitve` (`ucenec-resitve.tex`). Na podlagi izbranega vzorca za rešitve
posameznika podanega s potjo ``pot_vzorca_resitev`` (na primer `vzorci/vzorec_posameznih_resitev2.txt` ) nato ustvari
`LaTeX` datoteko z vstavljenimi rešitvami s seznama
``seznam_resitev``. Kadar želimo, da se pred rešitvami izpišejo tudi naloge, moramo za to izbrati primerno predlogo, v
katero se nato vstavijo vrednosti s seznama ``seznam_nalog``. Če je argument ``pdf`` nastavljen na vrednost ``True``,
poskusi program v isti mapi ustvariti še `PDF`
datoteko rešitev (`ucenec-resitve.pdf`).


.. literalinclude:: ../../generiranje.py
    :pyobject: napisi_posamezno_resitev

Funkcija ``napisi_skupno_resitev``
#####################################
Funkcija ``napisi_skupno_resitev`` v podmapi `Rešitve` ustvari eno `LaTeX` datoteko `Resitve.tex`. Datoteka je ustvarjena iz
predloge podane s potjo ``pot_vzorca_resitev``. Na ustrezna mesta spremenljivk se vstavijo imena učencev in njihovim nalogam
pripadajoče rešitve s seznama seznamov nalog in rešitev ``seznam_vseh_nalog_resitev``. Kadar želimo, da se pred rešitvijo izpiše
tudi naloga, moramo izbrati za to ustrezno predlogo, v katero se vstavijo tudi naloge s seznama ``seznam_vseh_nalog_resitev``.
Vrstni red rešitev je določen z abecednim
redom učencev. Če je argument ``pdf`` nastavljen na vrednost ``True``, program
poskusi v isti mapi ustvariti še `PDF` datoteko rešitev (`Resitve.pdf`)

.. literalinclude:: ../../generiranje.py
    :pyobject: napisi_skupno_resitev

Funkcija ``sestavi_vse_teste``
################################
Kaj funkcija naredi in kako vplivajo vrednosti parametrov, smo že predstavili (glej :ref:`ref_sestavi_vse_teste`).

Funkcija sprejme 8 argumentov:

* ``naloge``
* ``ime_testa``
* ``datoteka_seznam_ucencev``
* ``zdruzene_resitve``
* ``pdf``
* ``pot_vzorca_testa``
* ``pot_vzorca_resitev``
* ``tocke``

Najprej preveri, če so vrednosti parametrov smiselne in nastavi privzete vrednosti, kadar niso določene.
Če so vrednosti parametrov veljavne, funkcija pokliče funkcijo ``napisi_test``, ki ustvari posamezen test, sicer javi napako.

Kadar želimo za vsakega učenca samostojne rešitve kliče še funkcijo ``napisi_posamezno_resitev``, ki sestavi posamezne
rešitve. V primeru, da želimo eno datoteko z združenimi rešitvami za vse učence, pa najprej naredi seznam vseh učencev
in pripadajočih rešitev, nato pa kliče funkcijo ``napisi_skupno_resitev``.


.. literalinclude:: ../../generiranje.py
    :pyobject: sestavi_vse_teste

