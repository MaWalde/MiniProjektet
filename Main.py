import nltk_setup
from nltk.corpus import wordnet
from tkinter import *
# from tkinter import ttk

# dark_mode = {".": {"configure": {"background": "#2d2d2d", "foreground": "white",}},
#              "Tlabel":{"configure":{"foreground": "white",}},
#              "Tbutton":{"configure":{"background":"#3c3f41","foreground":"white",}},
#              "TEntry": {"configure": {"background": "#2d2d2d", "foreground": "white",
#                         "fieldbackground" : "#4d4d4d", "insertcolor": "white",
#                         "bordercolor" : "black", "lightcolor" : "#4d4d4d",
#                         "darkcolor" : "black",}},
#              "TCheckbutton": {"configure": {"foreground": "white", "indicatorbackground" : "white", 
#                               "indicatorforeground" : "black",}},
#              "TCombobox": {"configure": {"background": "#2d2d2d", "foreground": "white",
#                                          "fieldbackground" : "#4d4d4d", "insertcolor": "white",
#                                          "bordercolor" : "black", "lightcolor" : "#4d4d4d",
#                                          "darkcolor" : "black", "arrowcolor" : "white"},},
#              }

# tema = ttk.Style()
# tema.theme_create('dark', parent="clam", settings=dark_mode)
# tema.theme_use('dark')

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

def splash_screen_stäng(event=None):
    splash_screen.destroy()
    startWin()

def startWin():
    global fönster
    global splash_img
    fönster = Tk()
    fönster.protocol("WM_DELETE_WINDOW", fönster.quit)
    fönster.title("Lexicon")
    fönster.geometry("800x500")
    #etikett = ttk.Label(fönster, text="Enter a word:")
    etikett = Label(fönster, text="Enter a word:")
    etikett.pack()
    #fönster.intext = ttk.Entry(fönster)
    fönster.intext = Entry(fönster)
    fönster.intext.pack()
    #knapp = ttk.Button(fönster, text="Get synonyms", command=getSynonyms)
    knapp = Button(fönster, text="Get synonyms", command=getSynonyms)
    knapp.pack()
    #knapp2 = ttk.Button(fönster, text="Get definition", command=getDefinition)
    knapp2 = Button(fönster, text="Get definition", command=getDefinition)
    knapp2.pack()
    #fönster.resultat = ttk.Label(fönster, text=" ")
    fönster.resultat = Label(fönster, text=" ")
    fönster.resultat.pack()
    #fönster.mainloop()

splash_screen = Tk()
splash_screen.title("Logotype")
splash_screen.geometry("961x615")
# style = ttk.Style()
# style.configure("TSplashScreen.TLabel", background="#2d2d2d")
# style.configure("TSplashScreen.TLabel.image", background="#2d2d2d")
splash_img = PhotoImage(file="LeAl_logotyp.png", master=splash_screen)
#splash_label = ttk.Label(splash_screen, image=splash_img, style="TSplashScreen.TLabel",)
splash_label = Label(splash_screen, image=splash_img)
splash_label.image = splash_img
splash_label.pack()
# splash_screen.after(3000, splash_screen_stäng)    Timer för splashscreen
splash_label.bind("<Button-1>", splash_screen_stäng)
splash_screen.bind("<Button-1>", splash_screen_stäng)
splash_screen.mainloop()