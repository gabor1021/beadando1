# beadando1
A szövegfájlban tárolt adatok sorrendben: városnév, ország(ha nem magyarországi), kontinens(ha nem európai), szélességi és hosszúsági koordináták, utazási idő(ahol / jel van,
ott repülővel és autóval is megadva)

beolvas(): beadando.txt beolvasása

vehicle(Enum): az enum, ami a jármű megadásához kell

rad_convert(): fokokat átvált radiánra

tavolsag(): kiszámítja egy bekért város Pécstől vett távolságát (légvonalban, kis pontatlanságokkal)

mile_convert(): mérföldre átváltja a kilométerben megadott adatot

ido_calc(): Kiszámítja az összes utazási időt Pécstől a városig, járműtől függően.

melyik_orszag, melyik kontinens: kiírja és visszaadja a város országát, kontinensét

file_write_...: fájlkiírás

feltolt(): példányosításhoz használt függvény; a Varos classba kerülnek a magyar városok, az Europai_varos-ba minden más európai város, a Masik_kontinens_varos-ba a nem európai városok. globals() segítségével a városnevet adja meg objektumnévnek, így például a "Pécs.nev" hibát ír, de hiba nélkül lefut. Ide bekerül minden txt-ből beolvasott adat, és a város helyétől függően az enum segítségével járművet is ad hozzá.

beker(): bekér a felhasználótól egy mértékegységet és egy városnevet, és utána kiírja és fájlba írja az eredményt (tavolsagok.txt), ehhez metódusokat használ
