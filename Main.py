import nltk_setup
from nltk.corpus import wordnet

def listaSynonymer(ord):
    synonymer = []
    for syn in wordnet.synsets(ord):
        for lemma in syn.lemmas():
            synonymer.append(lemma.name())
    return synonymer

ordet = "sport"
synonymer = listaSynonymer(ordet)
print(f"{synonymer}")