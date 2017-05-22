import tkinter as tk


okno = tk.Tk()

vnosi = []


def vrednosti(seznam):
    s = set()
    for x in seznam:
        if x in s:
            return False
        s.add(x)
    return True


def preveri_sudoku():

    ### po vrsticah
    for x in range(9):
        seznam = []
        for y in range(9):
            if vnosi[x][y].get() != "": 
                seznam.append(vnosi[x][y].get())
        if vrednosti(seznam) == False:
            return False

    ### po stolpcih
    for x in range(9):
        seznam = []
        for y in range(9):
            if vnosi[y][x].get() != "": 
                seznam.append(vnosi[y][x].get())
        if vrednosti(seznam) == False:
            return False
    return True


def po_vnosu():
     print(preveri_sudoku())


for x in range(9):
    vnosi.append([])
    for y in range(9):
        vnosno_polje = tk.Entry(okno, borderwidth = 5, width = 2,
                                validate = "focusout",
                                validatecommand = po_vnosu)
        vnosi[x].append(vnosno_polje)
        vnosno_polje.grid(row = x, column = y)
