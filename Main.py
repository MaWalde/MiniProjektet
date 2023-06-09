from nltk_setup import setup
from tkinter import *
from tkinter import font
from nltk.corpus import wordnet

def getSynonyms():  #Funktion för att hämta synonymer till inmatat ord
    ord = fönster.intext.get()
    synonymer = set()
    for syn in wordnet.synsets(ord):
        for lemma in syn.lemmas():
            synonymer.add(lemma.name())
    synonymer = [synonym.replace('_', ' ') for synonym in synonymer]
    fönster.resultat.config(text="Synonyms: " + ", ".join(synonymer))
    showResFrame()

def getDefinition():  #Funktion för att hämta definitionen för inmatat ord
    ord = fönster.intext.get()
    definition = wordnet.synsets(ord)
    if definition:
        fönster.resultat.config(text="Definition: " + definition[0].definition())
    else:
        fönster.resultat.config(text="Can not find a definition for the given word.")
    showResFrame()

def getAutonyms():  #Funktion för att hämta autonymer till inmatat ord
    ord = fönster.intext.get()
    autonymer = set()
    synonymer = wordnet.synsets(ord)
    for syn in synonymer:
        for lemma in syn.lemmas():
            if lemma.antonyms():
                autonymer.add(lemma.antonyms()[0].name())
    autonymer = [autonym.replace('_', ' ') for autonym in autonymer]
    fönster.resultat.config(text="Autonyms: " + ", ".join(autonymer))
    showResFrame()

def getWordClass():  #Funktion för att bestämma ordklarr för inmatat ord
    ord = fönster.intext.get()
    synset = wordnet.synsets(ord)
    klass = NONE
    for syn in synset:
        klass = syn.pos()
    if klass == "n":
        klass = "Substantive"
    elif klass == "v":
        klass = "Verb"
    elif klass == "a":
        klass = "Adjective"
    elif klass == "r":
        klass = "Adverb"
    else:
        for syn in synset:
            for lemma in syn.lemmas():
                synset_sat = wordnet.synsets(lemma.name())
                for syn_sat in synset_sat:
                    pos_sat = syn_sat.pos()
                    if pos_sat != "s":
                        klass = pos_sat
                        break
                if klass:
                    break
            if klass:
                break
        if klass:
            if klass == "n":
                klass = "Substantive"
            elif klass == "v":
                klass = "Verb"
            elif klass == "a":
                klass = "Adjective"
            elif klass == "r":
                klass = "Adverb"
        else:
            klass = "Unknown"            
    fönster.resultat.config(text="Word class: " + klass)
    showResFrame()

def showResFrame(): #Öppnar gömt resultatfönster med nedre ram när användaren skickar begäran
    bd_frame.grid()
    bot_frame.grid()

def splash(): #Startskärm som laddar en fiktionell företagslogotyp
    global splash_screen
    splash_screen = Tk()
    splash_screen.title("LeAl Solutions")
    splash_screen.geometry("957x623")
    splash_img = PhotoImage(file="LeAl_logotyp.png", master=splash_screen)
    splash_label = Label(splash_screen, image=splash_img)
    splash_label.image = splash_img
    splash_label.pack()
    splash_screen.after(4000, splash_2)    #Timer för splashscreen
    splash_screen.mainloop()

def splash_2(): #Startskärm nr.2 som stänger föregående bild och laddar programmets egen logotyp 
    global titelbild
    titelbild = Tk()
    titelbild.title("Mattias fantasticly spectacular english encyclopedia")
    titelbild.geometry("957x623")
    titel_img = PhotoImage(file="Programnamn.png", master=titelbild)
    titel_label = Label(titelbild, image=titel_img)
    titel_label.image = titel_img
    titel_label.pack()
    splash_screen.destroy()
    titelbild.after(4000, splash_screen_stäng)    #Timer för splashscreen

def splash_screen_stäng(): #Stänger andra bilden och startar själva huvudprogrammet i eget fönster
    titelbild.destroy()
    startWin()

def startWin(): #Huvudfönstret som lirar mot samtliga funktioner
    global fönster
    global bd_frame
    global bot_frame
    fönster = Tk()
    fönster.title("Mattias fantasticly spectacular english encyclopedia")
    fönster.maxsize(800,500)
    fönster.config(bg="skyblue")
    l_frame = Frame(fönster, width=200, height=480, bg="white", bd = 13)
    l_frame.grid(row=1,column=0, padx=20,pady=20)
    etikett = Label(l_frame, text="Enter a word:")
    fet_font = font.Font(weight="bold")
    etikett.config(fg="#426cb6", bg="white",font=fet_font)
    etikett.grid(row=1,column=1,padx=10,pady=5)
    fönster.intext = Entry(l_frame)
    fönster.intext.config(font=fet_font)
    fönster.intext.grid(row=1,column=3,padx=10,pady=5)
    knapp = Button(l_frame, text="Get synonyms", command= getSynonyms)
    knapp_font = font.Font(weight="bold", size=11)
    knapp.config(bg="skyblue", fg="#426cb6", font=knapp_font, activebackground="white")
    knapp.grid(row=3,column=1,padx=10,pady=10)
    knapp2 = Button(l_frame, text="Get definition", command= getDefinition)
    knapp2.config(bg="skyblue", fg="#426cb6", font=knapp_font, activebackground="white")
    knapp2.grid(row=3,column=3,padx=10,pady=10)
    knapp3 = Button(l_frame, text="Get autonyms", command= getAutonyms)
    knapp3.config(bg="skyblue", fg="#426cb6", font=knapp_font, activebackground="white")
    knapp3.grid(row=4,column=1,padx=10,pady=10)
    knapp4 = Button(l_frame, text="Get class", command= getWordClass)
    knapp4.config(bg="skyblue", fg="#426cb6", font=knapp_font, activebackground="white")
    knapp4.grid(row=4,column=3,padx=10,pady=10)
    bd_frame = Frame(fönster,width=180,height=250, bg="white",bd=5)
    bd_frame.grid(row=5,column=0,padx=10,pady=5)
    bot_frame = Frame(fönster, width=0, height=20, bg="skyblue")
    bot_frame.grid(row=7,column=0)
    fönster.resultat = Label(bd_frame, text=" ", wraplength=300, justify="left")
    fönster.resultat.config(bg="white", fg="#426cb6", font=knapp_font)
    fönster.resultat.grid(row=1,column=0,padx=10,pady=10)
    bd_frame.grid_forget()
    bot_frame.grid_forget()

setup()
splash()