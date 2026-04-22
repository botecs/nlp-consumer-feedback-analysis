import nltk

def main():
    # NLTK erőforrások letöltése
    for res in ['vader_lexicon', 'punkt', 'stopwords', 'wordnet']:
        nltk.download(res, quiet=True)
    
    print("NLTK erőforrások sikeresen letöltve!")

if __name__ == "__main__":
    main()