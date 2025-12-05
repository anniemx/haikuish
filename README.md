# haikuish

Sovellus generoi yleiskielen perusteella haikumaisia runoja. 

## Ohjelman käyttö:
* lataa tai kloonaa ohjelma
* lataa tarvittaessa poetry
* aktivoi virtuaaliympäristö
```
$ poetry shell
$ poetry env activate
```
* aja ohjelma 
```
$ python3 src/index.py
```
* anna markovin aste generoidaksesi haikumaisen uutisrunon
* testaukseen:
```
$ poetry add pytest
$ pytest src
```



## Määrittelydokumentti
[Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)

## Toteutusdokumentti
[Toteutusdokumentti](./dokumentaatio/toteutusdokumentti.md)

## Testausraportti
[Testausraportti](./dokumentaatio/testausraportti.md)

## Viikkoraportit
* [Viikkoraportit](./dokumentaatio/viikkoraportit)
* [Viikkoraportti 1](./dokumentaatio/viikkoraportit/viikko1.md)
* [Viikkoraportti 2](./dokumentaatio/viikkoraportit/viikko2.md)
* [Viikkoraportti 3](./dokumentaatio/viikkoraportit/viikko3.md)
* [Viikkoraportti 4](./dokumentaatio/viikkoraportit/viikko4.md)
* [Viikkoraportti 5](./dokumentaatio/viikkoraportit/viikko5.md)



---
Data/mini_corpus.txt: Tavutettu mini-tietoaineisto testiksi: Eino Leinon runoja (Runoja kokoelmien ulkopuolelta) kotimaisten kielten keskuksen avoimesta tietokannasta.
https://kaino.kotus.fi/korpus/klassikot/meta/leino/leino_muita_runoja_rdf.xml
tavutettu käyttäen tavuttajaa: https://joukahainen.puimula.org/hyphenate

Algoritmin opetukseen on käytetty laajana aineistona YLE:n 2018 uutisaineistokorpuksen osittain (https://www.kielipankki.fi/download/YLE/fi/2011-2018-s-vrt/). Aineiston alkuprosessointiin käytetty koodi on data-kansiossa erikseen. Alkuprosessointi tavuttaa aineiston FinnSyll-kirjaston avulla.  