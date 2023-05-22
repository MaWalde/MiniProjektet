import nltk_setup
from nltk.corpus import wordnet
from tkinter import *
from tkinter import font

def getSynonyms():
    ord = fönster.intext.get()
    synonymer = []
    for syn in wordnet.synsets(ord):
        for lemma in syn.lemmas():
            synonymer.append(lemma.name())
    fönster.resultat.config(text="Synonyms: " + ", ".join(synonymer))

def getDefinition():
    ord = fönster.intext.get()
    definition = wordnet.synsets(ord)
    if definition:
        fönster.resultat.config(text="Definition: " + definition[0].definition())
    else:
        fönster.resultat.config(text="Can not find a definition for the given word.")

def getAutonyms():
    ord = fönster.intext.get()
    autonymer = []

def splash_screen_stäng(event=None):
    splash_screen.destroy()
    startWin()

def startWin():
    global fönster
    fönster = Tk()
    fönster.title("Lexicon")
    fönster.maxsize(800,500)
    fönster.config(bg="skyblue") #Prototyp bg-färg
    l_frame = Frame(fönster, width=200, height=480, bg="white", bd = 13)
    l_frame.grid(row=1,column=0, padx=20,pady=20)
    etikett = Label(l_frame, text="Enter a word:")
    fet_font = font.Font(weight="bold")
    etikett.config(fg="blue", bg="skyblue",font=fet_font)
    etikett.grid(row=1,column=1,padx=10,pady=5)
    fönster.intext = Entry(l_frame)
    fönster.intext.config(font=fet_font)
    fönster.intext.grid(row=1,column=3,padx=10,pady=5)
    knapp = Button(l_frame, text="Get synonyms", command=getSynonyms)
    knapp_font = font.Font(weight="bold", size=11)
    knapp.config(bg="skyblue", fg="blue", font=knapp_font, activebackground="gold")
    knapp.grid(row=3,column=1,padx=10,pady=10)
    knapp2 = Button(l_frame, text="Get definition", command=getDefinition)
    knapp2.config(bg="skyblue", fg="blue", font=knapp_font, activebackground="gold")
    knapp2.grid(row=3,column=3,padx=10,pady=10)
    bd_frame = Frame(fönster,width=180,height=250, bg="black",bd=1)
    bd_frame.grid(row=5,column=0,padx=10,pady=5)
    frame_res = Frame(bd_frame, width=180,height=250,bg="white",bd=5)
    frame_res.grid(row=5,column=0,padx=1,pady=1)
    fönster.resultat = Label(frame_res, text=" ")
    fönster.resultat.config(bg="skyblue", fg="blue", font=knapp_font)
    fönster.resultat.grid(row=1,column=0,padx=10,pady=10)
    #fönster.mainloop()

splash_screen = Tk()
splash_screen.title("Logotype")
splash_screen.geometry("957x623")
splash_img = PhotoImage(file="LeAl_logotyp.png", master=splash_screen)
splash_label = Label(splash_screen, image=splash_img)
splash_label.image = splash_img
splash_label.pack()
# splash_screen.after(3000, splash_screen_stäng)    Timer för splashscreen
splash_label.bind("<Button-1>", splash_screen_stäng)
splash_screen.bind("<Button-1>", splash_screen_stäng)
splash_screen.mainloop()