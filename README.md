# Keltaisen ryhmän Ohtu -miniprojekti repo

[Raportti](https://docs.google.com/document/d/1yJQMCieVxRdCBH6c7ABhcSlrO3FX6fW6NKSTdfrQ_Yw/edit?usp=sharing)

[Product backlog](https://docs.google.com/spreadsheets/d/e/2PACX-1vTBRvMHFcpm47yrNZhur4q50_rPGXJ9hRW-U_Ia8FFg1hVNZNbn1Q6GyrQVcuvJ6rLPPdnbpsfF2DFl/pubhtml)

[Linkki sovellukseen](https://ohtu-references.fly.dev/)
 
## Definition of Done

Koodin toiminnallisuus vastaa yhdessä sovittuja kirjoitettuja hyväksymiskriteerejä

Koodin ylläpitäminen on hyvää:
- Järkevä nimeäminen
- Selkeä arkkitehtuuri
- Koodi on jatkuvasti asiakkaan nähtävissä ja testien tila ilmenee CI-palvelun välityksellä

Kohtuullinen testikattavuus
- yksikkötestejä n. 70% kattavuudella sekä robot-testejä soveltuvilta osin
 
![GHA workflow badge](https://github.com/roosahut/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/roosahut/ohtu-miniprojekti/branch/master/graph/badge.svg?token=Um66kxj2Ox)](https://codecov.io/gh/roosahut/ohtu-miniprojekti)

## Dokumentaatio
- [Testikattavuusraportti](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/coverage_report.png)
- [Käyttöohje](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/instructions.md)<br>
- [Retrospektiivi sprintti 1](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/retro1.md)<br>
- [Retrospektiivi sprintti 2](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/retro2.md)<br>


## Komentorivitoiminnot
<h2>Huom!</h2> 
<h3><pre>Käyttäessä ohjelmaa paikallisesti omalla koneella, tulee tietokannan osoite määritellä .env-ympäristömuuttujaan, muuten
ohjelma ei toimi.</pre></h3>

## Sovelluksen asennus
- Riippuvuudet asennetaan komennolla: <h3><pre>poetry install</pre></h3>

- Ohjelma käynnistyy komennolla: <h3><pre>poetry run invoke start</pre></h3>
