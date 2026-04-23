# Szakdolgozat kezdetleges vázlat

## 1. Bevezetés:
*A bevezető/összegző rész elkészítése elegendő a beadási határidő előtt maximum 2 héttel.*

**logikai ív:**
* probléma->megoldás->módszer->eredmény

## 2. Tárgyalás:

**logikai ív:**
* elmélet->eszközök->implementáció->értékelés

### I. Szakirodalmi áttekintés és elméleti háttér (*kb. 4-6 oldal*)

* A természetes nyelvfeldolgozás (NLP) alapjai
* Szentiment analízis megközelítések
* Szövegreprezentáció és klaszterezés

### II. Alkalmazott technológiák és az adatforrás (*kb. 4-5 oldal*)

* Fejlesztői környezet
* Használt könyvtárak
* Publikus adatbázis


### III. Adatelőkészítés és leíró statisztikák (*kb. 5-7 oldal*)

* Adattisztítás
* Mennyiségi jellemzők statisztikája
* Szó- és kifejezésgyakoriságok vizualizációja


### IV. Szentiment analízis megvalósítása (*kb. 5-7 oldal*)

* A polaritás meghatározása: VADER és a TextBlob algoritmusok futtatása
* Pozitív és negatív arányok: compound scores -> elemzése/kategorizálása
* Személyfüggő eltérések: A visszajelzések vizsgálata a felhasználói profilok alapján


### V. Kategóriák és klaszterek kialakítása (*kb. 5-7 oldal*)
*Rejtett mintázatok feltárása.*

* Vektorizáció (scikit-learn): A szövegek átalakítása -> TF-IDF (Term Frequency-Inverse Document Frequency)
* K-means klaszterezés: Az optimális klaszterszám -> algoritmus futtatása.
* A klaszterek értelmezése

### VI. Területek összehasonlítása és szabályszerűségek (*kb. 6-8 oldal*)

* Területek szerinti bontás: A különböző termékkategóriák szentimentjének és gyakori témáinak összevetése
* Szignifikáns különbségek: Hol tapasztalható a legnagyobb eltérés a területek között? 
* Gyakorlati/Üzleti következtetések: Hogyan tudja egy vállalat felhasználni ezeket az interaktív (Bokeh) és statikus diagramokat?
