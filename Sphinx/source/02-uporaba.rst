Uporaba
============

Program za generiranje nalog je sestavljen iz knjižnice nalog iz različnih področij srednješolske matematike in programa za sestavljanje testov.. Ko zaženemo program z željenimi parametri nam ustvari testov in rešitve v `PDF` in `LaTeX` obliki.

********
Naloge
********
Vsebuje 60 takih nalog iz teh področij

**************
Izpis testov
**************
Za izpis testov je potrebno poklicati funkcijo ``sestavi_vse_teste`` iz programa ``izpisi_naloge.py``.

..TODO: autorun požene na licu mesta conf.py in ne tm k program dejansko je, zato je treba mal okol kodo napisat (recimo datoteko za dijake kliče drugače). Ne prenese šumnikov (niti v nizu). pazi na presledek # ignore

.. runblock:: pycon

    >>> import sys # ignore
    >>> sys.path.append('../') # ignore
    >>> from izpisi_naloge import * # ignore
    ... sestavi_vse_teste(naloge=[mnozice.PotencnaMnozica(), izrazi.PotencaDvoclenika(st_nalog=3), naravna_stevila.DeliteljVeckratnik()], ime_testa='Mnozice, deljivost in izrazi', datoteka_seznam_dijakov='../dijaki.txt', zdruzene_resitve=False)
