# TESTAUSRAPORTTI

* Yksikkötestauksen kattavuusraportti.
* Mitä on testattu, miten tämä tehtiin?

## TRIE:n testaus
* Yksikkötestit:
- Yksikkötesti on erityisesti trie-tietorakenteen kannalta olennainen.
- Yksikkötestissä muodostetaan trie-luokka ja trie-rakenteelle annetaan listana 3-grammit, joissa 3-grammit ovat tupleina muodossa ("sana", "tavumäärä").
- def test_str_; testataan alkaako TRIE-rakenne muodostua oikein juuresta. Tulostetaan ensimmäiset lapset merkkijonona ja verrataan niitä haluttuihin lapsiin.
- def test_trie_insert; Trien syötteen lisäys -metodi testataan vertaamalla löytyykö search-metodilla vastaavat annetut 3-grammit tietorakenteesta.
- def test_search_empty_sequence; Trien haku-metodia testataan tyhjällä merkkijonolla.
- def test_search_none; Trien haku-metodia testataan None-tyypillä.
- def test_get_successors; Trien seuraajien getteriä testataan hakemalla annetun hakusekvenssin lapset ja vertaamalla niitä haluttuihin tuloksiin. Samalla testataan tavufilterin toimivuutta, koska filterin tulisi päästää läpi vain rajaan sopivat lapset.

- Trien rakenne testataan tulostamalla syvyyshaun avulla solmut ja lapset. Testauksen tulisi siis todistaa, että rakenne yhdellätoista testisekvenssillä on: 

root
->on
    ->virrannut
        ->lastenlaulukulttuurin
    ->olemassa
	    ->monia
	    ->ainakin
->virrannut
    ->lastenlaulukulttuurin
	    ->uudistamisesta
->lastenlaulukulttuurin
    ->uudistamisesta
	    ->ja
->kokonaan
    ->uusi
	    ->sanajono
        ->uudestaan
->uusi
    ->kokoelma
        ->jonoja
    ->talletus
        ->sanajono
->kokoelma
    ->jonoja
	    ->uusia

Syvyyshaku käy siis solmun kerrallaan lisäten sen lapset tulostettavaan merkkijonoon ja ohittaen jo lisätyt solmut, mikäli ne ovat jonkun sekvenssin alussa lisätty. Merkkijonossa on myös frekvenssit heti sanan perässä. Näin ollen tulostettava merkkijono on: 
"on4-virrannut1-lastenlaulukulttuurin1-olemassa3-monia2-" \
"ainakin1-virrannut1-lastenlaulukulttuurin1-uudistamisesta1-lastenlaulukulttuurin1-" \
"uudistamisesta1-ja1-kokonaan2-uusi2-sanajono1-uudestaan1-uusi2-kokoelma1-jonoja1-talletus1-" \
"sanajono1-kokoelma1-jonoja1-uusia1-"


## Markovin ketjun testaus
* Päästä päähän testaus
* tarkastetaan onko generoidun haikurunon sanat löydettävissä peräkkäin alkuperäisestä tekstiaineistosta
* Generoidut haikurunot on tuotu merkkijonona ja täydennettynä tavumäärillä test_markov.py tiedostoon. Haikurunoista muodostetaan n-grammit, joita verrataan alkuperäisen tekstiaineistoon. 
* Testit menivät lävitse, eli n-grammit säilyvät alkuperäisestä aineistosta generoituun tekstiin.

## Manuaalinen testaus seuraajasanoille testitulostuksilla
Koska haikumuodon rajat ovat melko tiukat, ohjelma voi keskeyttää generoinnin, mikäli sopivia seuraajasanoja ei löydy. Testasin keskeytyneitä generointeja ja tarkastin manuaalisesti ettei tosiaan generointia ole voitu jatkaa.

* Tapaus 1:

Anna Markovin ketjun aste: 2
Rivi 1: [['asiana', 'ja']] tavumäärä: 5 - ok!
hakusanat rivin generoinnin jälkeen: [('asiana', 4), ('ja', 1)] - ok!

Rivi 2: [('sellaisena', 4), ('johon', 2)] tavumäärä: 6 < 7 - ok!

generointi katkeaa

hakusanojen ('sellaisena', 4), ('johon', 2) seuraajiksi palautuu tyhjät listat: ([], [])
Tarkastin hakemalla for-loopilla myös koko korpuksesta sanat peräkkäin ja tulostamaan niitä seuraavat sanat:
('tulee', 2) - tavumäärä > 1, joten seuraaja ei käy.

Näin ollen sopivia seuraajia ei ole.


* Tapaus 2:

Anna Markovin ketjun aste: 2

Rivi 1: [['miljoonaa', 'yli']] tavumäärä: 5 - ok!
hakusanat rivin generoinnin jälkeen: [('miljoonaa', 3), ('yli', 2)]
Rivi 2: [['65-vuotiasta', 'ei', 'käytä']] tavumäärä 7 - ok! (Finnsyll ei laske 65-alkua)
hakusanat rivin generoinnin jälkeen: [('ei', 1), ('käytä', 2)]
Rivi 3: ([('nettiä', 3)]) tavumäärä 3 < 5 ok!

generointi katkeaa

hakusanojen ('käytä', 2), ('nettiä', 3) seuraajiksi palautuu tyhjät listat: ([], [])
Koko korpuksesta etsittässä ei löydy ollenkaan seuraavia sanoja hakusanoilla, koska lause loppuu näihin.
Näin ollen sopivia seuraajia ei ole.

* Tapaus 3:

Anna Markovin ketjun aste: 3

Rivi 1: [['vuoksi', 'maapohja']] tavumäärä: 5 - ok!
hakusanat rivin generoinnin jälkeen: [('vuoksi', 2), ('maapohja', 3)] < 3 - ok!
Rivi 2: [['on', 'kuitenkin', 'pehmeä']] tavumäärä 7 - ok!
hakusanat rivin generoinnin jälkeen: [('on', 1), ('kuitenkin', 3), ('pehmeä', 3)] == 3 - ok!
Rivi 3: ([('joten', 2)])

generointi katkeaa

hakusanojen ('kuitenkin', 3), ('pehmeä', 3), ('joten', 2) seuraajiksi palautuu tyhjät listat: ([], [])
Tarkastin hakemalla for-loopilla myös koko korpuksesta sanat peräkkäin ja tulostamaan niitä seuraavat sanat:
('metsäkoneetkaan', 5) tavumäärä > 3, joten seuraaja ei käy.

Näin ollen sopivia seuraajia ei ole.

## Pylint testaukset:
- vk 3: 7.43/10 -> 8.06/10
