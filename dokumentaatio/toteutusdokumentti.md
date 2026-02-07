## Ohjelman yleisrakenne
Haikumaisia runoja generoiva ohjelma koostuu Markovin ketjusta ja TRIE-hakupuusta. 

Esimerkiksi generoitu runo;
***************************
- Uutishaiku -
***************************
pyörivä tuuli
jonka takia piispat
keskeyttävät
***************************

Algoritmin opetukseen käytetty prosessoitu osa-aineisto/pienehkö testiaineisto löytyy data-kansioista nimellä test_corpus.txt. Osakorpus on alkuprosessointu ja tavutettu FinnSyll-kirjaston avulla YLE:n 2018 uutisaineistokorpuksesta. Aineisto koostuu yleiskielisistä lauseista.

Index.py-tiedostossa käynnistetään sovellus ja kutsutaan korpuksen prosessointi process_data.py, jossa tekstitiedosto avataan ja prosessoidaan lauseittain listaan. Haiku.py ohjaa koko runon muodostamista. Ensin kysytään käyttäjältä haluttu Markovin ketjun aste. Annettua syötettä on rajoitettu nollan ja kymmenen väliin. Toisin sanoen ohjelma mahdollistaisi mielivaltaiset markovin ketjun asteen, mutta käytännössä pienellä korpuksella aste 2 tai 3 on järkevin. Korpuslistan lauseista muodostetaan n-grammit Markovin ketjun k-asteen mukaan n=k+1, jotka talletetaan trie-tietorakenteeseen. Markovin ketjun aste kertoo, kuinka monen edellisen sanan perusteella generoidaan seuraava sana. 

Trieen tallennetaan ja lasketaan samalla myös esiintyvyys korpuksessa. Esiintyvyyden perusteella voidaan arpoa seuraava sana. Haikua muodostetaan riveittäin. Haikun generointi ja tavujen tarkastus (yhteensä 17-tavua, jaolla 5-7-5) haetaan trie-hakupuusta generoimalla oikeaa muotoa oleva sanajono. Haiku.py muodostetaan markovin ketjua niin, että hakusekvenssiksi aletaan keräämään sanalistaa tyhjästä listasta. Hakulistaan lisätään ja poistetaan sanoja niin, että se pysyy k-asteen mukaisena. Triestä haetaan seuraava sana hakulistan sanojen perusteella ja trien getteri palauttaa vain haiku-runon rivin tavumäärään sopivat seuraajasanat. Tavuraja annetaan trielle parametrinä limit. Löydetyistä hyväksytyistä seuraajasanoista arvotaan haiku.py metodissa lottery seuraava sana painotetusti frekvenssien mukaan. Kun kaikki kolme riviä on tällä tavalla generoitu, haiku tulostetaan riveittäin.

## Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)
TRIE:n haku ja lisäys tapahtuu aikavaativuudella O(n), jossa n on sanajonon pituus. Tämä on tehokkaampi, kuin esimerkiksi listasta sanan etsintä, jossa käydään lineaarisesti vaihtoehdot lävitse. TRIE-hakupuussa voidaan siis etsiä tehokkaammin oikea polku kulkemalla vain toisiinsa liittyvät sanat.
def trie_insert(self, ngram): aikavaativuus O(n), tilavaativuus O(n)
def trie_get_followers(self, search_words, limit): aikavaativuus O(n), tilavaativuus O(1)


##  Työn mahdolliset puutteet ja parannusehdotukset
Ylen korpuksen käsittelyssä käytetty FinnSyll ei osaa tavuttaa ihan jokaista pitkää sanaa oikein, jolloin se antaa kaksi vaihtoehtoa. Nämä vaihtoehdot jäävät korpukseen, jolloin joissain tapauksissa sana saattaa toistua kahdesti. Lisäksi joitain numerosarjoja saattaa tulla korpuksessa vastaan. Haikumuodon tavurajat ovat myös aika tarkkoja, joten runoa ei voida aina generoida. Tulokset voisivat olla parempia, jos itse korpus koostuisi haikurunoista, joissa tavumäärät jo lähtökohtaisesti täsmäisivät haikumuotoon.

## Laajojen kielimallien (ChatGPT yms.) käyttö
Olen tarkastanut ja kääntänyt jotain englanninkielisiä termejä ja niiden selityksiä suomeksi TRIE-koodiesimerkkien osalta ChatGPT:n avulla. Olen tarkastanut joitakin yksittäisiä Pythonin perussyntakseja ja virheilmoituksia ChatGPT:stä, sekä etsinyt trien testitiedostosta typoa.

## Lähteet
* https://fi.wikipedia.org/wiki/Haiku
* https://en.wikipedia.org/wiki/Markov_chain
* https://www.geeksforgeeks.org/nlp/markov-chains-in-nlp/
* https://fitech101.aalto.fi/en/courses/introduction-to-large-language-models/part-2/4-markov-chains-and-n-gram-models
* https://www.geeksforgeeks.org/dsa/trie-insert-and-search/ 