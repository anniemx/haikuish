# TESTAUSRAPORTTI

* Yksikkötestauksen kattavuusraportti.
* Mitä on testattu, miten tämä tehtiin?

## TRIE:n testaus
* Yksikkötestit:
- Yksikkötesti on erityisesti trie-tietorakenteen kannalta olennainen ja yksikkötestit kattavat siten käytännössä n.30% koodista ja 90% triestä.
- Yksikkötestissä muodostetaan trie-luokka ja trie-rakenteelle annetaan listana 3-grammit, joissa 3-grammit ovat tupleina muodossa ("sana", "tavumäärä").
- def test_trie_insert; Trien syötteen lisäys -metodi testataan vertaamalla löytyykö search-metodilla vastaavat annetut 3-grammit tietorakenteesta.
- def test_search_empty_sequence; Trien haku-metodia testataan tyhjällä merkkijonolla.
- def test_search_none; Trien haku-metodia testataan None-tyypillä.
- def test_get_followers; Trien seuraajien getteriä testataan hakemalla annetun hakusekvenssin lapset ja vertaamalla niitä haluttuihin tuloksiin. Samalla testataan tavufilterin toimivuutta, koska filterin tulisi päästää läpi vain rajaan sopivat lapset.

## Markovin ketjun testaus
* Päästä päähän testaus
* tarkastetaan onko generoidun haikurunon sanat löydettävissä peräkkäin alkuperäisestä tekstiaineistosta

## Pylint testaukset:
- vk 3: 7.43/10 -> 8.06/10
