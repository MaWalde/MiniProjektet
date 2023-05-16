import nltk_setup
from nltk.corpus import wordnet

def listaSynonymer(ord):
    synonymer = []
    for syn in wordnet.synsets(ord):
        for lemma in syn.lemmas():
            synonymer.append(lemma.name())
    return synonymer

def getDefinition(ord):
    definition = wordnet.synsets(ord)
    if definition:
        return definition[0].definition()
    else:
        return "Can not find a definition for the given word."

ordet = "sport"
synonymer = listaSynonymer(ordet)
definitionen = getDefinition(ordet)
print(f"{synonymer} {definitionen}")