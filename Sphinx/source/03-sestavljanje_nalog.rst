Sestavljanje nalog
======================================================

Vsaka naloga v knjižnici je svoj razred, vse pa dedujejo lastnosti iz razreda ``Naloga``, ki je podrobneje predstavljen v poglaju 4.
.. Todo (glej točko 4)


Če želimo sestaviti novo nalogo, jo lahko dodamo v katero od obstoječih poglavij ali pa ustvarimo popolnoma novo datoteko.
Na novo ustvarjeno poglavje nalog mora najprej uvoziti razred ``Naloga``  in metodo ``preveri`` iz ``generiranje.py``.
Za naključno generirane vrednosti moramo uvoziti še paket ``random``. Paket ``sympy`` pa nam omogoča simbolno računanje.

.. literalinclude:: ..\..\eksponentna_funkcija.py
   :lines: 1-3

Da bomo naloge lahko dodajali v teste, moramo na koncu našo novo ustvarjeno poglavje uvoziti še v program ``izpisi_naloge.py``.


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


Posamezen niz se bo kasneje pretvoril v ``Jinja2.Template`` in nato v `LaTeX`-ov dokument. Zato je verjetno najlažje, da so nizi 'surovi',
saj se tako izognemo težavam pri zapisu posameznih posebnih simbolov, kot je recimo poševnica nazaj.

.. TODO Kaj je raw niz

Niz ``besedilo_posamezne`` je navodilo za reševanje naloge, ki ustreza vsem primerom sestavljene naloge. Namesto
konkretnih primerov pa napišemo ``Jinja2`` spremenljivke. `Jinja2` za označevanje spremenljivk uporablja
dvojne zavite oklepaje. Spremenljivke, ki bodo v `LaTeX`-u zapisane v matematičnem načinu moramo obdati z znakom '$'.
Na mesto spremenljivke se bo kasneje dodala vrednost, ki jo bo sestavila metoda `_`poskusi_sestaviti``.
Na enak način zapišemo tudi preostale nize. Niz ``resitev_posamezne`` je niz za izpis rešitev.

.. code-block:: python

    besedilo_posamezne = r'''Nariši graf {{naloga.ime_funkcije}} funkcije ${{naloga.matematicno_zapisana_spremenljivka}}$.''

Knjižnica ``sympy`` s klicem funkcije ``latex`` pretvori python matematični zapis v latexov matematični zapis.
Za lažjo uporabo, sem ``sympy`` funkciji  ``latex``  in ``expand`` dodala med funkcije, ki jih ``Jinja2`` prepozna.

.. Todo dodaj sklic na kodo v generiranju ki doda funkciji ali sklic na dodatek B

.. literalinclude:: ..\..\eksponentna_funkcija.py
   :pyobject: Enacba
   :lines: 14, 22


Niza ``besedilo_vecih`` in ``resitev_vecih`` sta za izpis besedila oziroma rešitev naloge z več primeri.
Običajno je navodilo samo eno, nato pa sledi (oštevilčeni) seznam primerov. Testi se izpisujejo v obliki ``LaTeX`` dokumentov,
zato je najpogosteje smiselno, da v nizu pripravimo izpis ``LaTeX`` seznama. To naredimo tako, da uporabimo okolje ``itemize`` za neoštevilčeni seznam ali okolje ``enumerate`` za oštevilčeni seznam. Pred posamezno točko seznama kličemo element `\item`.
..TODO vir za latex sezname
Program nam več primerov izpiše z pomočjo `for` zanke. Primer `Jinja` zanke spremenljivke:

.. code-block:: python

	{% for element in seznam %}
    {{element.spremenljivka}}
    {% endfor %}

.. todo vir za jinja zanko.

.. literalinclude:: ..\..\eksponentna_funkcija.py
   :pyobject: Enacba
   :lines: 15-21, 23-29


*********************************************
Metoda ``_poskusi_sestaviti``
*********************************************
Metoda ``_poskusi_sestaviti`` sestavi posamezen primer za nalogo in vrne slovar vrednosti, ki jih metoda ``generiranje.besedilo``
vstavi na mesta spremenljivk v predlogah besedil in rešitev. Metoda ``_poskusi_sestaviti`` vedno vrne samo en primer.
Če želimo nalogo z več primeri, program večkrat pokliče metodo ``generiranje.besedilo`` in tako vstavi vrednosti posameznih primerov znotraj naloge.

.. TODO ali ta del paše sem ali bolje v opis impelementacije knjižnice

Lepe rešitve najlažje zagotovimo tako, da rešitve naloge izberemo vnaprej in nato okoli tega sestavimo nalogo ali pa da jih
preverimo s metodo ``preveri``. Funkcija ``preveri`` zagotovi, da program zavrne naloge, ki ne ustrezajo pogoju. Na ta način
lahko zagotovimo lepši rezultat ali pa preprečimo nesmiselne naloge.

Vnaprej izbrana rešitev:

.. literalinclude:: ..\..\kompleksna_stevila.py
   :pyobject: Enacba._poskusi_sestaviti
   :emphasize-lines: 4

Funkcija `preveri` zagotovi lepši rezultat:

..TODO najdi primer eksponentna.enacba2osnovi? al je tole vredu

.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: EvklidovAlgoritem._poskusi_sestaviti
   :emphasize-lines: 4-5

Funkcija `preveri` zagotovi smiseln rezultat.

.. literalinclude:: ..\..\linearna_funkcija.py
   :pyobject: PremicaSkoziTocki._poskusi_sestaviti
   :emphasize-lines: 6

Raznolikost primerov zagotovimo tako, da v sestavljanje naloge vključimo naključnost. Najpogosteje sem uporabila funkcije:

* ``random.randint``, ki vrne naključno celo število
* ``random.choice``, ki izbere element s seznama
* ``random.sample``, ki iz seznama izbere določeno število različnih elementov.

.. todo sklic na random dokumentacijo

.. literalinclude:: ..\..\naravna_stevila.py
   :pyobject: DeliteljVeckratnik._poskusi_sestaviti
   :emphasize-lines: 2-3










