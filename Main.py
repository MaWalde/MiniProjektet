import nltk_setup
from nltk.corpus import wordnet
from tkinter import *

def getSynonyms():
    ord = intext.get()
    synonymer = []
    for syn in wordnet.synsets(ord):
        for lemma in syn.lemmas():
            synonymer.append(lemma.name())
    resultat.config(text="Synonyms: " + ", ".join(synonymer))

def getDefinition():
    ord = intext.get()
    definition = wordnet.synsets(ord)
    if definition:
        resultat.config(text="Definition: " + definition[0].definition())
    else:
        resultat.config(text="Can not find a definition for the given word.")

def startWin():
    start = Toplevel(fönster)
    start.geometry("200x200")
    label = Label(start, text="Experiment")
    label.pack()

# ordet = "sport"
# synonymer = listaSynonymer(ordet)
# definitionen = getDefinition(ordet)
# print(f"{synonymer} {definitionen}")

fönster = Tk()
fönster.title("Lexicon")
fönster.geometry("500x300")
etikett = Label(fönster, text="Enter a word:")
etikett.pack()
intext = Entry(fönster)
intext.pack()
knapp = Button(fönster, text="Get synonyms", command=getSynonyms)
knapp.pack()
knapp2 = Button(fönster, text="Get definition", command=getDefinition)
knapp2.pack()
resultat = Label(fönster, text=" ")
resultat.pack()
knapp2 = Button(fönster, text="Öppna", command=startWin)
knapp2.place(x=75,y=50)
fönster.mainloop()