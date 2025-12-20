## Ohjelman yleisrakenne
Haikumaisia runoja generoiva ohjelma koostuu Markovin ketjusta ja TRIE-hakupuusta. 

Algoritmin opetukseen käytetty prosessoitu aineisto löytyy data-kansioista nimellä corpus.txt. Aineiston alkuprosessointiin käytetty koodi on data-kansiossa erikseen. Alkuprosessointi tavuttaa FinnSyll-kirjaston avulla YLE:n 2018 uutisaineistokorpuksen (osakorpus). 

Tavutettu tekstiaineisto (korpus) prosessoidaan ensin n-grammeihin, jonka Markovin ketjun k asteen mukaan n=k+1. Käyttäjä määrittää halutun asteen k. Toisin sanoen ohjelma mahdollistaa mielivaltaiset markovin ketjun asteen, mutta käytännössä pienellä korpuksella aste 2 tai 3 on järkevin. Markovin ketjun aste kertoo, kuinka monen edellisen sanan perusteella generoidaan seuraava sana. Markovin ketjun malli muodostetaan markov.py ohjelmassa metodilla build_model, joka muodostaa n-grammit tuplena esim. n=3 (sana1, sana2, sana3) ja (sana2, sana3, sana4). N-grammit jaotellaan mallin sanakirjaan niin, että avaimena on n-grammi (sekvenssi) ja arvona niiden esiintyvyys (frekvenssi) korpuksessa. 

Muodostettu Markovin ketjun malli viedään TRIE-hakupuuhun (trie.py), johon n-grammit tallennetaan. Seuraavien sanojen generointi halutun pituuden mukaisesti käyttää TRIE:n getteriä get_list_words(), joka palauttaa hakupuusta löydetyt seuraavat sanat. TRIE:n haku itsessään käyttää syvyyshakua (dfs). Uusi sanajono arvotaan painotetusti frekvenssien mukaan.

Haikun generointi ja tavujen tarkastus (yhteensä 17-tavua, jaolla 5-7-5) haetaan trie-hakupuusta generoimalla oikeaa muotoa oleva sanajono. Haikumuoto tarkastetaan samalla, kun uusia sanoja generoidaan. Haikurunon tavujakojen rajat (5-12-17) riveittäin tarkastetaan samalla ja mikäli sana tavumäärä on liian pitkä, haetaan kaikki edellisen sanan seuraajat ja valitaan niistä ensimmäinen sopiva. 

Kun sopiva sanajono on muodostettu, haiku tulostetaan riveittäin.

## Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)
TRIE:n haku ja lisäys tapahtuu aikavaativuudella O(n), jossa n on sanajonon pituus. Tämä on tehokkaampi, kuin esimerkiksi listasta sanan etsintä, jossa käydään lineaarisesti vaihtoehdot lävitse. TRIE-hakupuussa voidaan siis etsiä tehokkaammin oikea polku kulkemalla vain toisiinsa liittyvät sanat.

##  Työn mahdolliset puutteet ja parannusehdotukset
Ylen korpuksen käsittelyssä käytetty FinnSyll ei osaa tavuttaa ihan jokaista pitkää sanaa oikein, jolloin se antaa kaksi vaihtoehtoa. Nämä vaihtoehdot jää korpukseen, jolloin joissain tapauksissa sana saattaa toistua kahdesti. Lisäksi joitain numerosarjoja saattaa tulla korpuksessa vastaan.

## Laajojen kielimallien (ChatGPT yms.) käyttö
Olen tarkastanut ja kääntänyt jotain englanninkielisiä termejä ja niiden selityksiä suomeksi TRIE-koodiesimerkkien osalta ChatGPT:n avulla. Olen tarkastanut joitakin yksittäisiä Pythonin perussyntakseja ja virheilmoituksia ChatGPT:stä, sekä etsinyt kerran trien testitiedostosta typoa ja tarkastanut virheiden takia trien haikumuodon koodia.

## Lähteet
* https://fi.wikipedia.org/wiki/Haiku
* https://en.wikipedia.org/wiki/Markov_chain
* https://www.geeksforgeeks.org/nlp/markov-chains-in-nlp/
* https://fitech101.aalto.fi/en/courses/introduction-to-large-language-models/part-2/4-markov-chains-and-n-gram-models
* https://www.geeksforgeeks.org/dsa/trie-insert-and-search/ 