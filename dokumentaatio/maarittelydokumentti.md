## Määrittelydokumentti
Opinto-ohjelma: Matemaattisten tieteiden kandiohjelma, tietojenkäsittelyteorian opintosuunta
Helsingin yliopiston aineopintojen harjoitustyö: Algoritmit ja tekoäly syksyllä 2025.

## Ohjelmointikieli
Projektin ohjelmointikieli on Python. Vertaisarvioinnin tekisin myös Pythonilla. 

## Projektin kieli

Projektin kieli on suomi ja projektin generoinnissa käytetään suomen kieltä, mutta koodi itsessään on englanniksi. Vertaisarviointeja voin tehdä myös englanniksi.

## Projektin toiminnallisuus ja aihe
Projektin aiheena on haikumaisia runoja generoiva malli, joka on opetettu yleiskielellä. Haiku-runossa olennaista on tavujen määrä, joita on yhteensä 17 ja ne jakautuvat kolmelle riville jaolla 5-7-5. Malli siis generoi runon tämän säännön perusteella. Syötteenä malli saa sanan, jonka perusteella se generoi haikumaisen runon. 

Malli pohjautuu Markovin ketjuihin. Ketjuissa mallinnetaan tiloja, joista siirrytään seuraavaan tilaan tietyillä todennäköisyyksillä ja jossa seuraava tila riippuu vain nykyisestä tilasta. Tässä mallissa siis Markovin ketjun muodostaisivat sanat. Rakennetta käytetään luonnollisen kielen prosessoinnissa. 

Aikavaativuus vaikuttaa riippuvan tilojen ja siirtymien määrästä. Aikavaativuudesta en löytänyt tarkkaa tietoa, mutta joissain esimerkeissä on mainittu esimerkiksi O(N^2*T), jossa N on tilojen määrä ja T siirtymien määrä. Tällöin N^2 vastaisi kaikkien tilojen läpikäyntiä matriisirakenteessa ja tämä kerrottaisiin siirtymien määrän mukaan. 


## Lähteet
Lähteenä käytän: 
https://fi.wikipedia.org/wiki/Haiku
https://en.wikipedia.org/wiki/Markov_chain
https://towardsdatascience.com/new-york-seeks-haikus-generating-haikus-from-nyc-government-job-descriptions-c27496a376fd/
https://www.geeksforgeeks.org/nlp/markov-chains-in-nlp/
