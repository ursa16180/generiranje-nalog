import generiranje
import naravna_stevila
import mnozice
import izrazi
import linearna_funkcija
import kompleksna_stevila
import kvadratna_funkcija
import eksponentna_funkcija
import polinomska_racionalna_funkcija
import stoznice
import zaporedja
import odvodi

# generiranje.sestavi_vse_teste([
#     mnozice.IzpeljaneMnozice(),mnozice.IzpeljaneMnozice(st_nalog=3),
#     mnozice.UnijaPresekRazlika(),mnozice.UnijaPresekRazlika(st_nalog=3),
#     mnozice.PotencnaMnozica(),mnozice.PotencnaMnozica(st_nalog=5),
#     mnozice.ElementiMnozice(linearna_kombinacija=False),mnozice.ElementiMnozice(st_nalog=5),
#     kompleksna_stevila.NarisiTocke(),kompleksna_stevila.NarisiTocke(st_nalog=3),
#     kompleksna_stevila.Racunanje(),kompleksna_stevila.Racunanje(st_nalog=3),
#     kompleksna_stevila.Ulomek(nicelna_komponenta_stevca=True),kompleksna_stevila.Ulomek(st_nalog=3),
#     kompleksna_stevila.VsotaRazlika(),kompleksna_stevila.VsotaRazlika(st_nalog=3),
#     kompleksna_stevila.Mnozenje(),kompleksna_stevila.Mnozenje(st_nalog=3),
#     kompleksna_stevila.Enacba(konjugirana_vrednost=True), kompleksna_stevila.Enacba(st_nalog=4),
#     polinomska_racionalna_funkcija.DolociNiclePoleAsimptotoRacionalne(), polinomska_racionalna_funkcija.DolociNiclePoleAsimptotoRacionalne(st_nalog=3),
#     polinomska_racionalna_funkcija.NiclePolinoma(),polinomska_racionalna_funkcija.NiclePolinoma(st_nalog=3),
#     polinomska_racionalna_funkcija.GrafPolinoma(),polinomska_racionalna_funkcija.GrafPolinoma(st_nalog=3),
#     polinomska_racionalna_funkcija.DvojnaNicla(),polinomska_racionalna_funkcija.DvojnaNicla(st_nalog=3),
#     polinomska_racionalna_funkcija.ParametraDvojna(),polinomska_racionalna_funkcija.ParametraDvojna(st_nalog=3),
#     polinomska_racionalna_funkcija.GrafRacionalne(),#polinomska_racionalna_funkcija.GrafRacionalne(st_nalog=2),
#     kvadratna_funkcija.TemenskaOblika(), kvadratna_funkcija.TemenskaOblika(st_nalog=3),
#     kvadratna_funkcija.Neenacba(primerjava_stevilo=False), kvadratna_funkcija.Neenacba(st_nalog=3),
#     kvadratna_funkcija.Presecisce(),kvadratna_funkcija.Presecisce(st_nalog=5),
#     kvadratna_funkcija.IzracunajNicle(kompleksni_nicli=True), kvadratna_funkcija.IzracunajNicle(st_nalog=3),
#     kvadratna_funkcija.NarisiGraf(),kvadratna_funkcija.NarisiGraf(st_nalog=5),
#     kvadratna_funkcija.SkoziTocke(nakljucne_tocke=True),kvadratna_funkcija.SkoziTocke(st_nalog=3),
#     linearna_funkcija.PremicaSkoziTocki(),linearna_funkcija.PremicaSkoziTocki(st_nalog=2),
#     linearna_funkcija.RazdaljaMedTockama(),linearna_funkcija.RazdaljaMedTockama(st_nalog=2),
#     linearna_funkcija.OblikeEnacbPremice(),linearna_funkcija.OblikeEnacbPremice(st_nalog=3),
#     linearna_funkcija.PremiceTrikotnik(),linearna_funkcija.PremiceTrikotnik(st_nalog=2),
#     linearna_funkcija.NarisiLinearnoFunkcijo(), #linearna_funkcija.NarisiLinearnoFunkcijo(st_nalog=5),
#     linearna_funkcija.VrednostiLinearne(),linearna_funkcija.VrednostiLinearne(st_nalog=3),
#     linearna_funkcija.SistemDvehEnacb(racionalne_resitve=True),linearna_funkcija.SistemDvehEnacb(st_nalog=3),
#     linearna_funkcija.SistemTrehEnacb(manjsi_koeficienti=False),linearna_funkcija.SistemTrehEnacb(st_nalog=3),
#     linearna_funkcija.Neenacba(kvadratna=True), linearna_funkcija.Neenacba(st_nalog=3),
#     izrazi.PotencaDvoclenika(linearna_kombinacija=False),izrazi.PotencaDvoclenika(st_nalog=3),
#     izrazi.PotencaTroclenika(linearna_kombinacija=False),izrazi.PotencaTroclenika(st_nalog=3),
#     izrazi.RazstaviVieta(vodilni_koeficient=True),izrazi.RazstaviVieta(st_nalog=2),
#     izrazi.RazstaviRazliko(linearna_kombinacija=True), izrazi.RazstaviRazliko(st_nalog=3),
#     izrazi.PotencirajVecclenik(linearna_kombinacija=True),izrazi.PotencirajVecclenik(st_nalog=2),
#     naravna_stevila.EvklidovAlgoritem(), naravna_stevila.EvklidovAlgoritem(st_nalog=3),
#     #naravna_stevila.DolociStevko(),naravna_stevila.DolociStevko(st_nalog=3),
#     naravna_stevila.DeliteljVeckratnik(), naravna_stevila.DeliteljVeckratnik(st_nalog=3),
#     eksponentna_funkcija.GrafEksponentne(cela_osnova=False),
#     eksponentna_funkcija.Enacba(vsota=True), eksponentna_funkcija.Enacba(st_nalog=3),
#     eksponentna_funkcija.Enacba2osnovi(deli_z_osnovo=True), eksponentna_funkcija.Enacba2osnovi(st_nalog=3),
#     zaporedja.SplosniClenZaporedja(),zaporedja.SplosniClenZaporedja(zamik_alternirajoce=True, st_nalog=5),
#     zaporedja.SplosniClenAritmeticnegaZaporedja(),zaporedja.SplosniClenAritmeticnegaZaporedja(st_nalog=3),
#     zaporedja.SplosniClenAritmeticnegaEnacbi(),zaporedja.SplosniClenAritmeticnegaEnacbi(st_nalog=3),
#     zaporedja.VsotaAritmeticnega(st_nalog=3), zaporedja.VsotaAritmeticnega(podan_splosni_clen=False),
#     zaporedja.PrviCleniAritmeticnega(), zaporedja.PrviCleniAritmeticnega(st_nalog=3),
#     zaporedja.PrviCleniGeometrijskega(), zaporedja.PrviCleniGeometrijskega(st_nalog=3),
#     zaporedja.SplosniClenGeometrijskega(), zaporedja.SplosniClenGeometrijskega(st_nalog=3),
#     zaporedja.SplosniClenGeometrijskegaEnacbi(), zaporedja.SplosniClenGeometrijskegaEnacbi(st_nalog=3),
#     zaporedja.VsotaGeometrijskega(podan_splosni_clen=False), zaporedja.VsotaGeometrijskega(st_nalog=3),
#     zaporedja.VsotaGeometrijskeVrste(lazji_podatki=False), zaporedja.VsotaGeometrijskeVrste(st_nalog=3),
#     odvodi.KotMedPremicama(abscisna_os=False), odvodi.KotMedPremicama(st_nalog=3),
#     odvodi.OdvodElementarne(kompozitum=False), odvodi.OdvodElementarne(st_nalog=3),
#     odvodi.OdvodSestavljene(), odvodi.OdvodSestavljene(st_nalog=3),
#     odvodi.KotMedGrafoma(),odvodi.KotMedGrafoma(st_nalog=3),
#     odvodi.Tangenta(),odvodi.Tangenta(st_nalog=2),
#     stoznice.NarisiKrivuljo(),stoznice.NarisiKrivuljo(st_nalog=3),
#     stoznice.PreseciscaKroznic(),stoznice.PreseciscaKroznic(st_nalog=3),
#     stoznice.TemeGorisceEnacba()
#
# ],
#     "Tester")#, "dijaki.txt", zdruzene_resitve=False)
#
generiranje.sestavi_vse_teste(naloge=[izrazi.PotencaDvoclenika(st_nalog=3),
                                      izrazi.RazstaviRazliko(min_potenca=3),
                                      naravna_stevila.DeliteljVeckratnik()],
                              ime_testa='Izrazi in deljivost',
                              datoteka_seznam_dijakov="dijaki.txt",
                              zdruzene_resitve=True)

# generiranje.sestavi_vse_teste([kompleksna_stevila.Mnozenje(), kompleksna_stevila.Mnozenje(st_nalog=5)], "dijaki.txt",  zdruzene_resitve=True)

# eksponentna_funkcija.Enacba().primer()
