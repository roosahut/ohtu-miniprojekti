# Käyttöohje

## Ohjelman käynnistäminen
Ohjelma käynnistyy komennolla:
<pre>poetry run invoke start</pre>

## Aloitusnäkymä
Sovellus käynnistyy seuraavanlaiseen näkymään: <br>
![start](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/aloitus.png) <br>
Käyttäjä voi lisätä uuden viitteen komennolla lisaa, tulostaa jo lisätyt viitteet komennolla lue ja lopettaa ohjelman komennolla lopeta

## Lisää viite
Käyttäjän kirjottessa terminaaliin komennon lisää, avautuu seuraavanlainen näkymä: <br>
![add](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/lisaa.png) <br>
Käyttäjältä kysytään seuraavia tietoja: viiteavain, kirjoittaja, teoksen nimi, vuosi ja julkaisija. <br>
Jos käyttäjä yrittää lisätä viitteavaimen, joka on jo olemassa, ohjelma herjaa tästä seuraavanlaisella tavalla: <br>
![error](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/olemassa.png) <br>
Käyttäjän jättäessä viiteavaimen tyhjäksi, ohjelma herjaa tästä seuraavalla tavalla: <br>
![error](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/viite_tyhja.png) <br>

## Lue viitteet
Käyttäjä voi lukea lisäämänsä viitteet kirjoittamalla terminaaliin komennon lue <br>
![read](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/lue.png) <br>
