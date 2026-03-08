# haikuish

Generoi uutishaikuja.

## Käyttö:
* lataa tai kloonaa ohjelma
* lataa poetry jos tarpeen
* aktivoi virtualinen ympäristö (riippuen versiosta;)
```
$ poetry shell
$ poetry env activate
```
* voit vaihtaa korpuksen haluamaksesi vaihtamalla polun index.py, kunhan se noudattaa samaa rakennetta testikorpuksen kanssa
* käynnistä ohjelma 
```
$ python3 src/index.py
```
* Anna Markovin ketjun k-aste (1-10 sallitaan, mutta järkevin tulos asteilla 2 tai 3).
* Ohjelma kokeilee generoida runoa 25 kertaa ja tulostaa generointiprosessin, sekä generoidun runon.
* Testaus:
```
$ poetry add pytest
```
Testaa trie yksikkötesteillä:
```
$ pytest src/tests/test_trie.py
```

Testaa markovin ketjua päästä päähän-testillä:
```
$ python3 src/tests/markov_test.py
```
