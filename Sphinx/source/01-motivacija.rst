Motivacija
============

Pomembno vlogo pri učenju matematike v srednji šoli predstavljajo vaje in utrjevanje naučene snovi. Naloge lahko najdemo
v različnih učbenikih in spletnih bazah nalog, vendar pa je njihovo število omejeno. Učitelji imajo pogosto dostop do
različnih učbenikov, vendar pa če jih želijo deliti z učenci, morajo fotokopirati ali celo pretipkati, še posebej
če želijo imeti naloge v elektronski obliki. Spletne baze nalog omogočajo, da lahko ustvarijo preverjanja, vendar pa imajo baze
pogosto premajhno število različnih nalog ali pa niso javno dostopne. :cite:`banka`

Naloge, predvsem za take namenjene utrjevanje, imajo pogosto enako navodilo, le vrednosti so različne. Baza nalog, kjer bi lahko
vrednosti generirali naključno, a bi vseeno imeli zagotovljene lepe rezultate, bi lahko na tak način omogočala obširnejši
nabor nalog. Morda celo dovolj, da bi lahko vsak učenec dobil drugačno preverjanje in bi tako zagotovili veliko različnih
primerov s čimer bi preprečili prepisovanje rezultatov ter morda celo povečali motivacijo za samostojno reševanje.
V primeru, da bi bila baza dostopna tudi učencem pa bi jim omogočili samostojno reševanje, kjer bi utrjevali razumevanje
reševanja in ne samo učenje rešitev na pamet.

Sestavljanje nalog s psevdo-generiranimi vrednostmi se da avtomatizirati, vendar moramo ustvariti knjižnico nalog in
zagotoviti, da so rešitve primerne. V nadaljevanju je predstavljena `Python` knjižnica, ki vsebuje 59 nalog
iz snovi srednješolske matematike. Večina nalog je namenjena učenju in utrjevanju osnovnih pojmov in računskih
postopkov, nekatere pa so primerne tudi za preverjanja znanja in priprave na maturo. Knjižnica ima splošen razred
``Naloga`` in več podrazredov, ki predstavljajo posamezne naloge iz snovi srednješolske matematike.

Knjižnici je dodan še program, ki iz izbranih nalog sestavi preverjanje znanja oziroma učni list z vajami ter
rešitve. Program s klicem funkcije ``sestavi_vse_teste.py`` ustvari `LaTeX` in po želji tudi `PDF` datoteke preverjanj
in rešitev za vsakega učenca s podanega seznama. Vsako preverjanje vsebuje enake naloge, vendar različne
psevdo-generirane vrednosti.
