Izpis nalog
============

************************************
Uporaba programa `izpisi_naloge.py`
************************************
Program `izpisi_naloge.py` vsebuje predloge  za teste in rešitve ter več pomožnih fukcij, ki so potrebne za izpis testov.

.. code-block:: python
    :linenos:

    >>> sestavi_vse_teste(
    ...     naloge=[mnozice.PotencnaMnozica(), izrazi.PotencaDvoclenika(st_nalog=3), naravnaStevila.DeliteljVeckratnik()],
    ...     ime_testa='Množice, deljivost in izrazi', datoteka_seznam_dijakov='dijaki.txt', zdruzene_resitve=False)
    Test Množice, deljivost in izrazi je sestavljen.
