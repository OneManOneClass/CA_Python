'''Padaryti paleidžiamąjį failą iš 11 paskaitos 4 užduoties (pilna programa su vartotojo sąsaja)
• Programa turi turėti programos lango ikoną ir norimą pavadinimą
• Paleidžiamasis failas turi turėti norimą ikoną'''

# Užduotis nr. 1 ------------------------------------------------------------------------------------------------------
'''Sukurti programą su grafine sąsaja, kuri:
• Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
• Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"
'''
# Užduotis nr. 2 ------------------------------------------------------------------------------------------------------
'''Patobulinti 1 užduoties programą, kad ji:
• Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"
'''
# Užduotis nr. 3 ------------------------------------------------------------------------------------------------------
'''Patobulinti 2 užduoties programą, kad ji turėtų meniu pavadinimu "Meniu", kuriame:
• Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
• Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
• Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
• Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys
'''
# Užduotis nr. 4 ------------------------------------------------------------------------------------------------------
'''
Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:
• Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
• Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
• Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas Nuspaudus klaviatūros mygtuką "Escape", uždarytų 
programos langą
'''

from tkinter import *

root = Tk()  # create new window
root.title("11 Paskaita")  # window title
root.geometry("350x150+800+300")  # window size, position
root.iconbitmap(r'D:\Mokslai\Code Academy\Python\Class projects\paskaitos\13_paskaita\3_uzduotis.ico') # 'r' = string modifier
name = StringVar("")


def say_hello():
    input_name = input_field.get()
    name.set(input_name)
    result["text"] = (f"Labas, {name.get()}!")
    status["text"] = "Sukurta"


def clear():
    result["text"] = ""
    status["text"] = "Išvalyta"


def restore_last():
    result["text"] = (f"Labas, {name.get()}!")
    status["text"] = "Atkurta"


menubar = Menu(root)  # create a menu

frame_top = Frame(root)
frame_bottom = Frame(root)

# Create menu and submenus
main_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Meniu", menu=main_menu)
main_menu.add_command(label="Išvalyti", command=clear)
main_menu.add_command(label="Atkurti", command=restore_last)
main_menu.add_separator()
main_menu.add_command(label="Išeiti", command=root.destroy)

label_input = Label(frame_top, text="Įveskite savo vardą")

input_field = Entry(frame_top)
input_field.focus()

button_confirm = Button(frame_top, text="Patvirtinti")
button_confirm.bind("<Button 1>", lambda say: say_hello())
button_confirm.bind("<Return>", lambda say: say_hello())
root.bind("<Return>", lambda say: say_hello())

result = Label(frame_bottom, text="")

status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)

frame_top.pack()
frame_bottom.pack(side=TOP)
label_input.pack(side=LEFT)
input_field.pack(side=LEFT)
button_confirm.pack()
result.pack()
status.pack(side=BOTTOM, fill=X)

root.config(menu=menubar)
root.mainloop()
