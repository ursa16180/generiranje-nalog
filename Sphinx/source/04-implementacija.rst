Implementacija - Izpis nalog
=============================

Knjižnici nalog je dodana še datoteka ``generiranje.py``, ki vključuje program za izpis testov in razred ``Naloga``,
katerega metode in vrednosti dedujejo posamezne naloge.

****************
Razred Naloga
****************
Vse naloge v knjižnici dedujejo atribute in metode razreda ``Naloga``.
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
Metoda ``sestavi`` vrne slovar z vrednosti posamezne naloge, ki ustrezajo želenim pogojem. To doseže tako da kliče metodo
``_poskusi_sestaviti``, dokler ne dobi slovarja z želenimi vrednostimi.

Metoda ``sestavi_vec``
*******************************
Metoda ``sestavi_vec`` vrne seznam slovarjev, ki vsebujejo ustrezne vrednosti posameznih primerov naloge. Posamezne
elemente seznama pa dobi tako, da kliče metodo ``sestavi``.


Metoda ``besedilo``
*******************************
Metoda ``besedilo`` spremeni surove nize besedil nalog in rešitev v  predloge (``Jinja2.Template``) in vanje vstavi
konkretne vrednosti naloge ,ki jih dobi s klicem metode ``sestavi`` ali ``sestavi_vec``.
Prva se kliče, če želimo nalogo samo z enim primerom, druga pa če želimo nalogo z
več primeri.
Metoda vrne slovar, ki vsebuje nalogo in rešitev. Slednji sta se spremenili v končen niz besedila z vstavljenimi vrednostmi.

Metoda ``primer``
*******************************




*****************************************
Uporaba programa za izpis testov
*****************************************
Za sestavitev testov moramo iz datoteke ``generiranje.py`` klicati funkcijo ``sestavi_vse_teste``, ki ustvari vse teste.

.. code-block:: python
    :linenos:

    >>> sestavi_vse_teste(naloge=[mnozice.PotencnaMnozica(), izrazi.PotencaDvoclenika(st_nalog=3), naravnaStevila.DeliteljVeckratnik()], ime_testa='Množice, deljivost in izrazi', datoteka_seznam_dijakov='dijaki.txt', zdruzene_resitve=False)
    Test Množice, deljivost in izrazi je sestavljen.


Funkcija ``sestavi_vse_teste``
################################

Funkcija najprej ustvari mapo z imenom testa in 2 podmapi za naloge in rešitve. Nato za vsakega učenca s seznama
``datoteka_seznam_dijakov`` kliče funkcijo ``napisi_test``, ki sestavi posamezen test. Če želimo za vsakega učenca
samostojne rešitve kliče še funkcijo ``napisi_posamezno_resitev``, ki sestavi posamezne rešitve. V primeru združenih
rešitev pa najprej naredi seznam vseh učencev in pripadajočih rešitev, nato pa kliče funkcijo ``napisi_skupno_resitev``.

.. literalinclude:: ..\..\generiranje.py
    :pyobject: sestavi_vse_teste


Funkcija ``napisi_test``
################################

.. literalinclude:: ..\..\generiranje.py
    :pyobject: napisi_test

Funkcija ``napisi_posamezno_resitev``
########################################

.. literalinclude:: ..\..\generiranje.py
    :pyobject: napisi_posamezno_resitev

Funkcija ``napisi_skupno_resitev``
#####################################

.. literalinclude:: ..\..\generiranje.py
    :pyobject: napisi_skupno_resitev


