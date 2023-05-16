import nltk_setup
from nltk.corpus import wordnet
import tkinter

def getSynonyms(ord):
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

# ordet = "sport"
# synonymer = listaSynonymer(ordet)
# definitionen = getDefinition(ordet)
# print(f"{synonymer} {definitionen}")

fönster = tkinter.Tk()
fönster.title("Lexicon")
etikett = tkinter.Label(fönster, text="Enter a word:")
etikett.pack()
intext = tkinter.Entry(fönster)
intext.pack()
knapp = tkinter.Button(fönster, text="Get synonyms", command=getSynonyms)
knapp.pack()
knapp2 = tkinter.Button(fönster, text="Get definition", command=getDefinition)
knapp2.pack()
resultat = tkinter.Label(fönster, text=" ")
resultat.pack()
fönster.mainloop()