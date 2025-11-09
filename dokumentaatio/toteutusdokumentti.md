## Ohjelman yleisrakenne
Ohjelma koostuu Markovin ketjusta ja TRIE-hakupuusta. 

Tavutettu tekstiaineisto prosessoidaan ensin n-grammeihin, joissa n=3. 3-grammit eli muotoa (sana1, sana2, sana3) ja (sana2, sana3, sana4) viedään Markovin ketjuihin (markov.py). 3-grammit jaotellaan sanakirjaan niin, että avaimena on sanapari ja arvona kaikki mahdolliset paria seuraavat mahdolliset sanat ja niiden todennäköisyydet. Markovin ketjun aste on siten k=2, koska tunnemme kaksi edellistä sanaa, eli tilaa seuraavan sanan generointia varten. 

Muodostettu Markovin ketjun malli viedään TRIE-hakupuuhun (trie.py), jossa 3-grammit tallennetaan tavuittain.
Haikun generointi aloitetaan käyttäjän antamasta tavutetusta sanasta. TRIE-hakupuusta arvotaan painotetusti annetun aloitussanan perusteella haikumuotoon sopivat seuraavat sanat.

Haiku tulostetaan riveittäin.

## Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)

## Suorituskyky- ja O-analyysivertailu (mikäli sopii työn aiheeseen)

##  Työn mahdolliset puutteet ja parannusehdotukset

## Laajojen kielimallien (ChatGPT yms.) käyttö
Olen tarkastanut ja kääntänyt jotain englanninkielisiä termejä ja niiden selityksiä suomeksi TRIE-koodiesimerkkien osalta ChatGPT:n avulla ja tarkastanut joitakin yksittäisiä Pythonin perussyntakseja ChatGPT:stä.

## Lähteet
* https://fi.wikipedia.org/wiki/Haiku
* https://en.wikipedia.org/wiki/Markov_chain
* https://www.geeksforgeeks.org/nlp/markov-chains-in-nlp/
* https://fitech101.aalto.fi/en/courses/introduction-to-large-language-models/part-2/4-markov-chains-and-n-gram-models
* https://www.geeksforgeeks.org/dsa/trie-insert-and-search/ 