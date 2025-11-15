# Viikkoraportti 3

Viikolla kolme olen jatkanut algoritmin työstöä ja samalla laittanut ylös tarvittavia testejä. Vaihdoin ohjeistuksen mukaisesti Markovin ketjun asteen vapaasti valittavaksi ja siten myös n-grammien muodostuksen riippumaan halutusta Markovin ketjun asteesta. Markovin ketjun ja TRIE:n yhdistäminen on edennyt niin, että Markovin ketjusta saadaan tieto sekvensseistä ja niiden frekvensseistä, jotka tallennetaan TRIE-hakupuuhun.

Opin miten saan yhdistettyä Markovin ketjun ja TRIE:n yhteen. Olen myös oppinut soveltamaan TRIE:n perusteita algoritmini käyttötarkoitukseen. Luin myös testaamisesta ja olen oppinut unittesteistä enemmän, mutta en ole ehtinyt vielä kunnolla rakentamaan omia testejäni. Erotin myös sekvenssien muodostamisen markov.py luokan alle, jolloin process_data.py tehtävä on vain ladata data-aineisto ja siistiä se Markovin ketjun mallia varten.  

Olin ajatellut ehtiväni tällä viikolla keskittymään enemmän myös testien laatimiseen, mutta Markovin ketjun ja TRIE:n yhdistämisessä meni enemmän aikaa, kuin olin ajatellut. Lisäksi testien kehitys on tuntunut hieman haastavalta, on helppo keksiä perustoimivuuteen testejä eri metodeille, mutta vaikeaa määritellä tarpeellisuus ja kattavuuus. Olen kuitenkin tehnyt muistiinpanoja koko ajan, mitä asioita olisi hyvä testata. 

On myös ollut haastavaa tarkastaa, toimiiko TRIE:n solmujen muodostus oikein. Ensi viikon aikana voisin rakentaa testejä, jotka auttaisivat myös näiden tarkastuksessa ja kehityksessä.

Seuraavaksi teen TRIE:n haun ja getterin loppuun, yritän syventyä testaamiseen ja mahdollisesti haiku-muodon muodostamiseen.

Viikon työtunnit: 10.25+h.