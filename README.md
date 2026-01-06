# haikuish

Sovellus generoi yleiskielen perusteella haikumaisia runoja. 

## Ohjelman käyttö:
* lataa tai kloonaa ohjelma
* lataa tarvittaessa poetry
* aktivoi virtuaaliympäristö (jompi kumpi)
```
$ poetry shell
$ poetry env activate
```
* varmista index.py polku korpustiedostoon on oikein
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
* [Viikkoraportti 6](./dokumentaatio/viikkoraportit/viikko6.md)



---
Algoritmin opetukseen on käytetty laajana aineistona YLE:n 2018 uutisaineistokorpuksen osittain (https://www.kielipankki.fi/download/YLE/fi/2011-2018-s-vrt/). Alkuprosessoinnissa ohjelman ulkopuolella on tavutettu ja siistitty aineisto FinnSyll-kirjaston avulla.  