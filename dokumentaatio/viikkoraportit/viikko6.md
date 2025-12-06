# Viikkoraportti 6

Tällä viikolla sairastuin flunssaan alkuviikosta, joten viikon työmäärä jäi vähäisemmäksi.

Prossesoin kuitenkin uuden korpuksen käytettäväksi, jossa sanan tavumäärä on laskettu jo valmiiksi. Muokkasin vastaavasti markovin ketjua huomioimaan korpuksen rakenteen. Lisäksi työstin TRIE:n haiku-muodon tarkastusta. Haikumuodon tarkastus jäi vielä sen verran kesken, että suoritus katkeaa vaihtelevasti eri suorituksilla. Kuitenkin jollain ajoilla sain oikeassa muodossa generoidun runon. En vielä ehtinyt selvittämään, johtuuko vaihtelevuus aineistosta vai koodista. 

Täytyypä dokumentoida tähän vielä itseäni huvittanut ensimmäinen onnistunut uutishaiku:
[('lo.ke.roin.nis.ta', 5)]
[('e.nää', 2), ('niin', 1), ('kyl.mi.ä', 3), ('kuin', 1)]
[('tä.hän', 2), ('o.li', 2), ('se', 1)]

Haastavalta on tuntunut TRIEstä generoitaessa uutta sanajono huomioda kaikki tarvittavat ehdot. Haikun muodon tarkastuksen 5-7-5 tavujaon takia tarkastuksen koodi tuntuu työläältä ja pitkältä, toivottavasti saan sitä selkeytettyä vielä. 

Seuraavaksi joudun edelleen työstämään haikutarkastusta ja täydentämään testausta. 

Työtunnit yht. 10.00h