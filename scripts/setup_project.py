import os
import nltk
import spacy
import pandas as pd

def initialize_project():
    print("*** Projekt inicializálása... ***")

    # 1. Kötelező mappák létrehozása
    folders = ['data', 'notebooks', 'outputs', 'scripts']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"  📁 Létrehozva: {folder}")

    # 2. NLTK adatok letöltése
    print("*** NLTK adatok letöltése... ***")
    nltk_data = ['vader_lexicon', 'punkt', 'stopwords', 'wordnet']
    for data in nltk_data:
        nltk.download(data, quiet=True)
    print("  ✅ NLTK kész.")

    # 3. spaCy modell ellenőrzése
    print("*** spaCy modell ellenőrzése... ***")
    try:
        nlp = spacy.load("en_core_web_sm")
        print("  ✅ spaCy (en_core_web_sm) kész.")
    except OSError:
        print("  ❌ Hiba: A spaCy modellt nem található. Futtasd a korábbi 'uv add <link>' parancsot!")

    # 4. Pandas alapbeállítások
    pd.set_option('display.max_colwidth', None)
    
    print("\n=== Minden készen áll a munkára! ===")

if __name__ == "__main__":
    initialize_project()