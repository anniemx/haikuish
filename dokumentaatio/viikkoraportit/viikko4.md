# Viikkoraportti 4

Tällä viikolla lisäsin trieen str-metodin ja testaukseen vertaamaan juureen talletettuja lapsia. En tiedä onko tämä riittävä, vai tulisiko siis vielä jonkun muun solmun lapset tarkastaa tällä testillä?

Testasin myös kommentoidusti runon generoimisen pysähtymisen "manuaalisesti" tarkastelemalla keskeytynyttä suoritusta vertaamalla hakusekvenssiä sekä triestä haettuihin seuraajiin että koko aineistoon peilaten. Tämä vahvisti olettamustani, että haiku-muodon tavurajat ovat sen verran tiukat, että runon generointi keskeytyy useasti siihen, ettei sopivia seuraajia yksinkertaisesti ole. Kirjoitin testaukset kolmesta tapauksesta auki testausraporttiin.

Testailin Markovin ketjun muodostamista vertaamalla kahden generoidun runon n-grammeja alkuperäisen tekstiaineistosta muodostettuihin n-grammeihin. Testit onnistuivat pienen tarkennuksen jälkeen ja raportoin niistä testausraporttiin. Testin muodollisesta oikeellisuudesta en oikein tiedä. 

Korjasin myös joitain muotoiluja ja pikkubugeja koodista.

Työtunnit 6.25h