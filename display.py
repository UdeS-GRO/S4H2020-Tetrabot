from tkinter import *
from simulation import GUI

fenetre = Tk()

label = Label(fenetre, text="TETRABOT PROJECT", font="Helvetica 20")
label.pack()


# canvas
# canvas = Canvas(fenetre, width=150, height=220, background='red')
# ligne1 = canvas.create_line(75, 0, 75, 120)
# ligne2 = canvas.create_line(0, 60, 150, 60)
# txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
# canvas.pack()


l = 800
h = 400
lt = 100 # l tetrabot

canvas1 = Canvas(fenetre, width=l, height=h, bg='gray')
gui = GUI(fenetre, canvas1)
gui.animate_walk()
# gui = GUI(fenetre, width=l, height=h, bg='gray')

bouton1  = Button(fenetre, text ='Start').pack(side=LEFT, padx=30, pady=10)
bouton2 = Button(fenetre, text ='Stop').pack(side=LEFT, padx=30, pady=10)
bouton3 = Button(fenetre, text="Close", command=fenetre.quit)
bouton3.pack(side=RIGHT, padx=30, pady=10)




fenetre.mainloop()