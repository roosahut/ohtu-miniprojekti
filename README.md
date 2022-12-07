# Keltaisen ryhmän Ohtu -miniprojekti repo

[Product backlog](https://docs.google.com/spreadsheets/d/e/2PACX-1vTBRvMHFcpm47yrNZhur4q50_rPGXJ9hRW-U_Ia8FFg1hVNZNbn1Q6GyrQVcuvJ6rLPPdnbpsfF2DFl/pubhtml)

[Linkki sovellukseen (ei vielä täysin toimiva)](https://ohtu-references.fly.dev/)
 
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
- [Käyttöohje](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/instructions.md)<br>

## Sovelluksen asennus
- Riippuvuudet asennetaan komennolla: <h3><pre>poetry install</pre></h3>

## Komentorivitoiminnot
- Ohjelma käynnistyy komennolla: <h3><pre>poetry run invoke start</pre></h3>
- Testit voi jaa komennoilla: <h3><pre>poetry run invoke test</pre></h3> <h3><pre>poetry run invoke robot-test</pre></h3>
- Testikattavuusraportin saa komennolla: <h3><pre>poetry run invoke coverage-report</pre></h3>

