from struct import calcsize

import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import END

#forma kalkulatora
calc = customtkinter.CTk()
calc.title("Kalkulator")
calc.geometry("400x500")
calc.config(bg="black")

#funkcję kalkulatora
def calcclear():
    Wyswietlacz.delete(0, END)
def calcclick(liczba):
    Wyswietlacz.insert(END,liczba)
def calcwynik():
    wyrazenie=Wyswietlacz.get()
    wynik=eval(wyrazenie)
    ans=round(wynik,1)
    Wyswietlacz.delete(0, END)
    Wyswietlacz.insert(0, ans)

#Wyświetlacz
Wyswietlacz = customtkinter.CTkEntry(calc, font=("Terminal", 26), text_color="green", fg_color="black", width=330, height=50, border_color="white", border_width=4)
Wyswietlacz.place(x=35, y=10)

#przyciski
guzik1 = customtkinter.CTkButton(calc, text="1" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(1))
guzik1.place(x=90, y=100)
guzik2 = customtkinter.CTkButton(calc, text="2" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(2))
guzik2.place(x=145, y=100)
guzik3 = customtkinter.CTkButton(calc, text="3" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(3))
guzik3.place(x=200, y=100)

guzik4 = customtkinter.CTkButton(calc, text="4" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(4))
guzik4.place(x=90, y=155)
guzik5 = customtkinter.CTkButton(calc, text="5" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(5))
guzik5.place(x=145, y=155)
guzik6 = customtkinter.CTkButton(calc, text="6" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(6))
guzik6.place(x=200, y=155)

guzik7 = customtkinter.CTkButton(calc, text="7" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(7))
guzik7.place(x=90, y=210)
guzik8 = customtkinter.CTkButton(calc, text="8" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(8))
guzik8.place(x=145, y=210)
guzik9 = customtkinter.CTkButton(calc, text="9" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(9))
guzik9.place(x=200, y=210)

guzik0 = customtkinter.CTkButton(calc, text="0" ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick(0))
guzik0.place(x=145, y=265)

guzikplus = customtkinter.CTkButton(calc, text="+" ,font=("Terminal", 26), text_color="white", fg_color="blue", width=100, height=50, border_color="white", border_width=2, command=lambda :calcclick("+"))
guzikplus.place(x=255, y=100)
guzikminus = customtkinter.CTkButton(calc, text="-" ,font=("Terminal", 26), text_color="white", fg_color="blue", width=100, height=50, border_color="white", border_width=2, command=lambda :calcclick("-"))
guzikminus.place(x=255, y=155)
guzikmnozenie = customtkinter.CTkButton(calc, text="*" ,font=("Terminal", 26), text_color="white", fg_color="blue", width=100, height=50, border_color="white", border_width=2, command=lambda :calcclick("*"))
guzikmnozenie.place(x=255, y=210)
guzikdzielenie = customtkinter.CTkButton(calc, text="/" ,font=("Terminal", 26), text_color="white", fg_color="blue", width=100, height=50, border_color="white", border_width=2, command=lambda :calcclick("/"))
guzikdzielenie.place(x=255, y=265)

guzikclear = customtkinter.CTkButton(calc, text="C" ,font=("Terminal", 26), text_color="white", fg_color="red", width=100, height=50, border_color="white", border_width=2, command=calcclear)
guzikclear.place(x=40, y=265)
guzikrownosci = customtkinter.CTkButton(calc, text="=" ,font=("Terminal", 26), text_color="white", fg_color="purple", width=315, height=50, border_color="white", border_width=2, command=calcwynik)
guzikrownosci.place(x=40, y=320)
guzik0 = customtkinter.CTkButton(calc, text="." ,font=("Terminal", 26), text_color="green", fg_color="black", width=50, height=50, border_color="white", border_width=2, command=lambda :calcclick("."))
guzik0.place(x=200, y=265)

calc.mainloop()