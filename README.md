# Fogyasztói visszajelzések elemzése természetes nyelvfeldolgozási módszerekkel

## A projekt céljai:

A dolgozat célja, hogy publikusan elérhető adatbázisok esetében automatizált eszközökkel elemezze a fogyasztók (vásárlók, felhasználók) visszajelzéseit. A természetes nyelvfeldolgozás eszközeit felhasználva készíteni kell a mennyiségi jellemzőkre vonatkozóan leíró statisztikákat. Vizsgálni kell, hogy mennyiben pozitív vagy negatív visszajelzésről van szó (szentiment analízis). Meg kell próbálni kategóriákat, klasztereket kialakítani, továbbá elemezni, hogy a különféle területekről érkező visszajelzések esetében milyen szabályszerűségek, szignifikáns különbségek figyelhetők meg.

## Technológia Stack:

* **Csomagkezelő:** [uv](https://astral.sh/uv) 
* **Adatkezelés:** pandas
* **NLP:** spaCy
* **Szövegreprezentáció:** scikit-learn -> TF-IDF , K-means
* **Szentiment analízis:** VADER(nltk), TextBlob
* **Vizualizáció:** Seaborn, Matplotlib, Bokeh, WordCloud

## Adatbázis:

* **Amazon fogyasztói visszajelzések:** [link](https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews)

## Útmutató:

* **1. Környezet és függőségek telepítése:**

````
uv sync
````

* **2.  NLP modellek és erőforrások letöltése:**

````
uv run scripts/setup_project.py
````


## Készítette: Demján Botond - SOZGAL