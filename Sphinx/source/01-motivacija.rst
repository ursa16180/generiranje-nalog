Motivacija
============

Pomembno vlogo pri učenju matematike v srednji šoli predstavljajo vaje in utrjevanje naučene snovi. Naloge lahko najdemo
v različnih učbenikih in spletnih bazah nalog, vendar pa je njihovo število omejeno. Učitelji imajo pogosto dostop do
različnih učbenikov, vendar pa če jih želijo deliti z učenci, jih morajo fotokopirati ali celo pretipkati, še posebej
če želijo imeti naloge v elektronski obliki. Spletne baze nalog omogočajo, da lahko ustvarijo preverjanja, vendar pa imajo baze
pogosto premajhno število različnih nalog ali pa niso javno dostopne. :cite:`banka`

Naloge, predvsem take namenjene utrjevanje, imajo pogosto enako navodilo, le vrednosti so različne. Baza nalog, kjer bi lahko
vrednosti generirali naključno, a bi vseeno imeli zagotovljene lepe rezultate, bi lahko na tak način omogočala obširnejši
nabor nalog. Morda celo dovolj, da bi lahko vsak učenec dobil drugačno preverjanje in bi tako zagotovili veliko različnih
primerov s čimer bi preprečili prepisovanje rezultatov ter morda celo povečali motivacijo za samostojno reševanje.
V primeru, da bi bila baza dostopna tudi učencem pa bi jim omogočili samostojno reševanje, kjer bi utrjevali razumevanje
reševanja in ne samo učenje rešitev na pamet.

Sestavljanje nalog s psevdo-generiranimi vrednostmi se da avtomatizirati, vendar moramo ustvariti knjižnico nalog in
zagotoviti, da so rešitve primerne. V nadaljevanju je predstavljena `Python` knjižnica, ki vsebuje 59 nalog
iz snovi srednješolske matematike. Naloge so različno zahtevne. Nekatere so lahko primerne za spoznavanje
konceptov, utrjevanje osnovnih pojmov in računskih postopkov, priprave na maturo ali preverjanja znanja.
Knjižnica vsebuje naloge iz različnih področij:

#. `naravna_stevila` - izračun največjega skupnega delitelja in najmanjšega skupnega večkratnika dveh števil
#. `izrazi` - računanje z algebrajskimi izrazi
#. `mnozice` -  zapis elementov množic in različne operacije z množicami
#. `linearna_funkcija` - graf in lastnosti linearne funkcije ter enačbe premic v ravnini
#. `kvadratna_funkcija` - različne oblike zapisov funkcije, računanje ničel in risanje grafov
#. `kompleksna_stevila` - računske operacije s kompleksnimi števili
#. `eksponentna_funkcija` - reševanje eksponentnih enačb in graf eksponentne funkcije
#. `polinomska_racionalna_funkcija` - računanje ničel, polov, risanje grafov racionalne in polinomske funkcije
#. `stoznice` -  enačbe krožnice in elipse v premaknjeni legi
#. `odvodi` - odvodi elementarnih in sestavljenih funkcij in razumevanje tangente na krivuljo
#. `zaporedja` - določanje splošnega člena poljubnega zaporedja, računanje prvih členov in vsote aritmetičnega ali geometrijskega zaporedja

Ideje za naloge sem črpala iz lastnih pedagoških izkušenj in različnih srednješolskih učbenikov.
:cite:`brilej2004omega1`
:cite:`brilej2005omega2a`
:cite:`brilej2005omega2b`
:cite:`brilej2006omega3`
:cite:`brilej2005omega4`
:cite:`arnus2009matematika1`
:cite:`arnus2010matematika2`
:cite:`bon2011matematika3`
:cite:`bon2012matematika4`
:cite:`alt2006matematika`
:cite:`benko2014matematika`
:cite:`kavka2014matematika`

Knjižnica ima splošen razred ``Naloga`` in več podrazredov, ki predstavljajo posamezne naloge iz snovi srednješolske matematike.

Knjižnici je dodan še program, ki iz izbranih nalog sestavi preverjanje znanja oziroma učni list z vajami ter
rešitve. Program s klicem funkcije ``sestavi_vse_teste`` ustvari `LaTeX` in po želji tudi `PDF` datoteke preverjanj
in rešitev za vsakega učenca s podanega seznama. Vsako preverjanje vsebuje enake naloge, vendar različne
psevdo-generirane vrednosti.

Kadar uporabimo že sestavljene naloge, program ne zahteva veliko razumevanja programiranja. Kogar zanima, pa si lahko
osnove programiranja v jeziku `Python` ogleda na `spletu<https://docs.python.org/3/tutorial/>`_.
