# Käyttöohje

## Ohjelman käynnistäminen
<pre>Ohjelma löytyy seuraavasta osoitteesta: </pre>
https://ohtu-references.fly.dev/


## Aloitusnäkymä
<pre>Sovellus käynnistyy seuraavanlaiseen näkymään:</pre><br>

![main](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/main.png)<br>

<pre>Aloitusnäkymässä on kaksi valintavaihtoehtoa: sisäänkirjautuminen jo olemassaolevalla käyttäjälle 
ja uuden käyttäjän rekisteröinti</pre>


## Rekisteröinti
<pre>Käyttäjän halutessa rekisteröidä uuden käyttäjätunnuksen, avautuu seuraavanlainen näkymä:</pre><br>

![register](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/register.png)<br>

<pre>Käyttäjältä kysytään seuraavia tietoja: nimi, salasana ja salasanan varmennus. Käyttäjän syöttäessä virheelliset tiedot, 
esimerkiksi salasananat eivät täsmää, sovellukselta tulee tästä ilmoitus. Käyttäjätunnuksen ollessa jo olemassa, 
rekisteröinti epäonnistuu myös tässä tapauksessa</pre><br>

![invalid_register](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/invalid_register.png) <br>

<pre>Onnistuneen rekisteröinnin jälkeen käyttäjä kirjataan automaattisesti sovellukseen, 
jonka jälkeen avautuu seuraavanlainen näkymä: </pre>

![login_success](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/login_success.png) <br>

## Sisäänkirjautuminen

<pre>Käyttäjän valitessa sisäänkirjautumisen avautuu seuraavanlainen näkymä:</pre>

![login](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/login.png) <br>

<pre>Käyttäjän syöttessä virheelliset tiedot, tulee tästä ilmoitus: </pre>

![invalid_credentials](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/invalid_credentials.png) <br>

<pre>Onnistuneen sisäänkirjautumisen jälkeen avautuu seuraava näkymä: </pre>

![login_success](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/login_success.png) <br>

## Viitteiden lisääminen

<pre>Käyttäjä valitsee valitsee pudotusvalikosta haluamansa viitetyypin, jonka jälkeen sovellus tarjoaa oikeantyyppistä 
lomaketta tietojen lisäämiseen </pre>

![add_reference](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/add_reference.png) <br>

## Viitteiden lukeminen
<pre>Kun käyttäjä on onnistuneesti lisännyt viitteen tietokantaan, voidaan sisäänkirjautuneen käyttäjän henkilökohtaiset
viitteet lukea painamalla etusivulla linkkiä click here, jonka jälkeen viitteet ovat luettavissa BibTeX-muotoisina. </pre>

![view_references](https://github.com/roosahut/ohtu-miniprojekti/blob/master/documentation/pictures/view_references.png) <br>

## Uloskirjautuminen ja paluu edelliseen näkymään
<pre>Käyttäjä voi palata takaisin edelliseen näkymään painamalla return-nappia. Painamalla logout-nappia, 
käyttäjä kirjataan sovelluksesta ulos</pre>
