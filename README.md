# haikuish

Application generates haikuish poems from news corpus. 

## Use:
* load or clone application
* load poetry if needed
* activate virtual environment (depending the version;)
```
$ poetry shell
$ poetry env activate
```
* write index.py path to corpus as wanted (you can thus use another corpus in case you want as long as it is sentences row by row with syllables as numbers after each word)
* run program 
```
$ python3 src/index.py
```
* give Markov chain k-order to generate a news haiku
* to test:
```
$ poetry add pytest
```
Test trie:
```
$ pytest src/tests/test_trie.py
```

Test markov:
```
$ python3 src/tests/markov_test.py
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
Corpus used partially: (https://www.kielipankki.fi/download/YLE/fi/2011-2018-s-vrt/). Preprocessing with counting syllables has been done outside the programm with the help of FinnSyll-library.  