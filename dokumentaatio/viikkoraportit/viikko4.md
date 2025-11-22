# Viikkoraportti 4

Tällä viikolla olen keskittynyt tekstin generointiin. Tein TRIE:n generointimetodin, joka käyttää getteriä ja syvyyshakua uusien sanojen hakemiseen. Tämän lisäksi kirjoitin toteutusdokumenttia ohjelman kehittymisen perusteella tarkemmaksi. Lisäsin myös yksikkötestejä TRIE:n osalta. 

Tällä viikolla minitekstiaineiston ongelmat tulivat esille. Olen aikaisemmin käyttänyt pientä ja mahdollisimman kevyttä tekstiaineistoa, jotta pystyn nopeasti testaamaan koodia kehittäessä toimiiko se haluamallani tavalla. Nyt generoinnin ja testauksen osalta huomasin sen olevan riittämätön. Yritin rakentaa jo haiku-muodon testausta haikuohjelmaan, mutta mikäli triestä ei löydy sopivaa muotoa, ohjelma keskeytyy. Tarvitsen siis siihen isomman testiaineiston, jolla voisin havaita paremmin haikumuodon tarkastuksen toimivuuden. Myös sanajonoja generoidessa pienellä aineistolla tosiaan käy niin, että generoidut sanat ovat kopiota tekstistä. Myöskään testauksella en siten pysty arvioimaan pienellä korpuksella, tuottaako algoritmi uusia yhdistelmiä vai vain kopioita. Tämän viikon suurin oppi oli ehkä juuri tämä aineiston koon konkretisoituminen ja toisaalta myös haaste algoritmin toimivuuden kannalta.

Kommentoin keskeneräisen haikutarkastuksen koodista tässä välissä vielä pois (ellen kerkeä sitä ratkaisemaan vielä ennen arviointeja), sillä ajattelin, että vertaisarvioinnin kannalta jotain tuottava koodi on mukavampi.

Seuraavaksi jatkan generoivan algoritmin ja haikumuodon tarkastuksen hienosäätöä isommalla aineistolla. Aion osallistua testauksesta kertovalle luennolle, jonka perusteella jatkan testien rakentamista ja itse testaamista. 

Mikään yksittäinen asia ei ehkä ole ollut tässä vaiheessa ylitsepääsemätön, vaan enemmänkin yritän nyt saada testattua toimivuutta ja rakentaa testejä eteenpäin.

Etsin myös sopivaa opetusaineistoa ja latasin YLE:n uutisaineistoja, joita olen testaillut vielä erillään projektista. Löysin myös python-kirjaston FinnSyll, joka tavuttaa tekstiä. Voisiko tätä käyttää hyödyksi tekstiaineiston tavutukseen, koska se ei ole algoritmin pääasiallinen tarkoitus, vaan koskisi vain aineiston prosessointia algoritmille sopivaksi? 

Viikon työtunnit: xxh.