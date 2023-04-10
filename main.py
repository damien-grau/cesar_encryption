from tkinter import Tk, Label, CENTER, W, StringVar, Entry, LEFT, S, Button, E
from random import randint

"""
Chiffrage Cesar
Auteur : Damien
"""

table = [
    "\\", "\t", "\n", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9",
    ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z", "[", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", " ", "\xA1", "\xA2", "\xA3",
    "\xA4", "\xA5",
    "\xA6", "\xA7", "\xA8", "\xA9", "\xAA", "\xAB", "\xAC", "\xAD", "\xAE", "\xAF", "\xB0", "\xB1", "\xB2", "\xB3",
    "\xB4",
    "\xB5", "\xB6", "\xB7", "\xB8", "\xB9", "\xBA", "\xBB", "\xBC", "\xBD", "\xBE", "\xBF", "\xC0", "\xC1", "\xC2",
    "\xC3",
    "\xC4", "\xC5", "\xC6", "\xC7", "\xC8", "\xC9", "\xCA", "\xCB", "\xCC", "\xCD", "\xCE", "\xCF", "\xD0", "\xD1",
    "\xD2",
    "\xD3", "\xD4", "\xD5", "\xD6", "\xD7", "\xD8", "\xD9", "\xDA", "\xDB", "\xDC", "\xDD", "\xDE", "\xDF", "\xE0",
    "\xE1",
    "\xE2", "\xE3", "\xE4", "\xE5", "\xE6", "\xE7", "\xE8", "\xE9", "\xEA", "\xEB", "\xEC", "\xED", "\xEE", "\xEF",
    "\xF0",
    "\xF1", "\xF2", "\xF3", "\xF4", "\xF5", "\xF6", "\xF7", "\xF8", "\xF9", "\xFA", "\xFB", "\xFC", "\xFD", "\xFE",
    "\xFF",
    "\u0100", "\u0101", "\u0102", "\u0103", "\u0104", "\u0105", "\u0106", "\u0107", "\u0108", "\u0109", "\u010A",
    "\u010B",
    "\u010C", "\u010D", "\u010E", "\u010F", "\u0110", "\u0111", "\u0112", "\u0113", "\u0114", "\u0115", "\u0116",
    "\u0117",
    "\u0118", "\u0119", "\u011A", "\u011B", "\u011C", "\u011D", "\u011E", "\u011F", "\u0120", "\u0121", "\u0122",
    "\u0123",
    "\u0124", "\u0125", "\u0126", "\u0127", "\u0128", "\u0129", "\u012A", "\u012B", "\u012C", "\u012D", "\u012E",
    "\u012F",
    "\u0130", "\u0131", "\u0132", "\u0133", "\u0134", "\u0135", "\u0136", "\u0137", "\u0138", "\u0139", "\u013A",
    "\u013B",
    "\u013C", "\u013D", "\u013E", "\u013F", "\u0140", "\u0141", "\u0142", "\u0143", "\u0144", "\u0145", "\u0146",
    "\u0147",
    "\u0148", "\u0149", "\u014A", "\u014B", "\u014C", "\u014D", "\u014E", "\u014F", "\u0150", "\u0151", "\u0152",
    "\u0153",
    "\u0154", "\u0155", "\u0156", "\u0157", "\u0158", "\u0159", "\u015A", "\u015B", "\u015C", "\u015D", "\u015E",
    "\u015F",
    "\u0160", "\u0161", "\u0162", "\u0163", "\u0164", "\u0165", "\u0166", "\u0167", "\u0168", "\u0169", "\u016A",
    "\u016B",
    "\u016C", "\u016D", "\u016E", "\u016F", "\u0170", "\u0171", "\u0172", "\u0173", "\u0174", "\u0175", "\u0176",
    "\u0177",
    "\u0178", "\u0179", "\u017A", "\u017B", "\u017C", "\u017D", "\u017E", "\u017F", "\u0192", "\u02C6", "\u02C7",
    "\u02C9",
    "\u02D8", "\u02D9", "\u02DA", "\u02DB", "\u02DC", "\u02DD", "\u0311", "\u0384", "\u0385", "\u0386", "\u0388",
    "\u0389",
    "\u038A", "\u038C", "\u038E", "\u038F", "\u0390", "\u0391", "\u0392", "\u0393", "\u0394", "\u03A9", "\u03BC",
    "\u03C0",
    "\u2013", "\u2014", "\u2015", "\u2018", "\u2019", "\u201A", "\u201C", "\u201D", "\u201E", "\u2020", "\u2021",
    "\u2022",
    "\u2026", "\u2030", "\u2039", "\u203A", "\u2044", "\u2070", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078",
    "\u2079",
    "\u2080", "\u2081", "\u2082", "\u2083", "\u2084", "\u2085", "\u2086", "\u2087", "\u2088", "\u2089", "\u20AC",
    "\u20AE",
    "\u20B4", "\u20B9", "\u2113", "\u2116", "\u2122", "\u2126", "\u212E", "\u2153", "\u2154", "\u2155", "\u2156",
    "\u2157",
    "\u2158", "\u2159", "\u2202", "\u2206", "\u220F", "\u2211", "\u2219", "\u221A", "\u221E", "\u222B", "\u2248",
    "\u2260",
    "\u2264", "\u2265"
]


def process(M):
    global table
    cryptage = decryptage = str = error = False
    decalage = char = decalage1 = a = 0
    if M == 'D':
        decalage = decalageSAISIE1.get()
        char = texteSAISIE1.get()
        decryptage = True
        if decalage.isdigit() or not decalage:
            if decalage.isdigit() and int(decalage) % 409 == 0:
                error = True
            elif not decalage:
                error = True
                decalageSAISIE1.set('Error')

        elif decalage == 'Error':
            decalageSAISIE1.set('Error')
            error = True
        else:
            str = True
            decalage = list(decalage)

    elif M == 'C':
        decalage = decalageSAISIE.get()
        char = texteSAISIE.get()
        cryptage = True
        if decalage.isdigit() or not decalage:
            if decalage.isdigit() and int(decalage) % 409 == 0:
                error = True
            elif not decalage:
                error = True
                decalageSAISIE.set('Error')

        elif decalage == 'Error':
            decalageSAISIE.set('Error')
            error = True

        else:
            str = True
            decalage = list(decalage)

    if not error:
        if not str:
            decalage = int(decalage)
        char = list(char)

        for i in range(len(char)):
            if str:
                if a == len(decalage):
                    a = 0
                try:
                    decalage1 = table.index(decalage[i])
                except IndexError:
                    decalage1 = table.index(decalage[a])
                    a += 1
            indexage = table.index(char[i])
            if not str:
                decalage1 = decalage % 409
            verif = True
            if cryptage:
                while verif:
                    try:
                        char[i] = table[(indexage + decalage1) % 409]
                    except IndexError:
                        decalage1 %= 409
                    else:
                        verif = False
            elif decryptage:
                while verif:
                    try:
                        char[i] = table[(indexage - decalage1) % 409]
                    except IndexError:
                        decalage1 %= 409
                    else:
                        verif = False

        char = "".join(char)
        if cryptage:
            crypte.set(char)
        else:
            crypte1.set(char)




def randkey():
    global table
    key = ''
    for i in range(15):
        key += table[randint(0, 409)]
    decalageSAISIE.set(key)


fenetre = Tk()
fenetre.title('Cesar Encryption')
fenetre.geometry('339x300+600+300')
fenetre.maxsize(width=339, height=300)
fenetre.minsize(width=339, height=300)
fenetre.config(bg='#F2B33D')

# label du tire
titre = Label(fenetre, text='Cesar Encryption', font=('Arial', 14), justify=CENTER, bg='#F2B33D', )
titre.grid(row=0, columnspan=1, padx=100)

# création du label à côté de la zone de saise de décalage
labelDECALAGE = Label(fenetre, text='Key', font=('Arial', 11), width=10, bg='#F2B33D')
labelDECALAGE.grid(row=1, column=0, sticky=W)

# Zone de saisie de décalage
decalageSAISIE = StringVar()
decalageBOX = Entry(fenetre, textvariable=decalageSAISIE, font=('Arial', 12),
                    width=10)
decalageBOX.grid(row=2, column=0, sticky=W)

# Label texte
labelTEXTE = Label(fenetre, text='Text to encrypt', font=('Arial', 11), width=12, bg='#F2B33D', justify=LEFT)
labelTEXTE.grid(row=1, sticky=S)

# zone de saisie texte
texteVAR = StringVar()
texteSAISIE = Entry(fenetre, textvariable=texteVAR, font=('Arial', 11), width=12, justify=LEFT)
texteSAISIE.grid(row=2)

# Bouton de chiffrage
valider = Button(fenetre, width=12, text='Encrypt', font=('Arial', 8), justify=CENTER, command=lambda: process('C'))
valider.grid(row=2, column=0, sticky=E)

# Aléatoire key
random = Button(fenetre, width=12, text='Random key', font=('Arial', 8), justify=CENTER, command=lambda: randkey())
random.grid(row=3, column=0, sticky=W)

# label indication texte chiffré
indicationCrypte = Label(fenetre, text='Text encrypted', font=('Arial', 11), bg='#F2B33D')
indicationCrypte.grid(row=3, pady=10)

# texte chiffré
crypte = StringVar()
zonecrypte = Entry(fenetre, textvariable=crypte, font=('Arial', 10), width=48, justify=LEFT)
zonecrypte.grid(row=4, sticky=W)

vide = Label(fenetre, bg='#F2B33D')
vide.grid(row=5)
# création du label à côté de la zone de saise de décalage
labelDECALAGE1 = Label(fenetre, text='Key', font=('Arial', 11), width=10, bg='#F2B33D')
labelDECALAGE1.grid(row=6, column=0, sticky=W)

# Zone de saisie de décalage
decalageSAISIE1 = StringVar()
decalageBOX1 = Entry(fenetre, validate="key", textvariable=decalageSAISIE1, font=('Arial', 12), width=10)
decalageBOX1.grid(row=7, column=0, sticky=W)

# Label texte
labelTEXTE1 = Label(fenetre, text='Text to decrypt', font=('Arial', 11), width=12, bg='#F2B33D', justify=LEFT)
labelTEXTE1.grid(row=6, sticky=S)

# zone de saisie texte
texteVAR1 = StringVar()
texteSAISIE1 = Entry(fenetre, textvariable=texteVAR1, font=('Arial', 11), width=12, justify=LEFT)
texteSAISIE1.grid(row=7)

# Bouton de déchiffrage
valider1 = Button(fenetre, width=12, text='Decrypt', font=('Arial', 8), justify=CENTER, command=lambda: process('D'))
valider1.grid(row=7, column=0, sticky=E)

# label indication texte déchiffré
indicationCrypte1 = Label(fenetre, text='Text decrypted', font=('Arial', 11), bg='#F2B33D')
indicationCrypte1.grid(row=8, pady=10)

# texte déchiffré
crypte1 = StringVar()
zonecrypte1 = Entry(fenetre, textvariable=crypte1, font=('Arial', 10), width=48, justify=LEFT)
zonecrypte1.grid(row=9, sticky=W)


fenetre.mainloop()
