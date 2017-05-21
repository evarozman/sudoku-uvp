import tkinter as tk
import random as rnd




okno=tk.Tk()

vnosi = []

def unique_values(seznam):
    s = set()
    for x in seznam:
        if x in s:
            return False
        s.add(x)
    return True

def preveriSudoku():

    ### preverjanje pravilnosti sudokuja za vrstice
    for x in range(9):
        seznam=[]
        for y in range(9):
            if vnosi[x][y].get() != "": 
                seznam.append(vnosi[x][y].get())
        if unique_values(seznam) == False:
            return False

    ### preverjanje pravilnosti sudokuja za stolpce
    for x in range(9):
        seznam=[]
        for y in range(9):
            if vnosi[y][x].get() != "": 
                seznam.append(vnosi[y][x].get())
        if unique_values(seznam) == False:
            return False
        
    return True

def izpis():
    print(preveriSudoku(), end="--- CEL \n")
##    for row in vnosi:
##        for column in row:
##            print(column.get(), end=" ")
##        print(end="\n")

def poVnosu():
     print(preveriSudoku())

for x in range(9):
    vnosi.append([])
    for y in range(9):
        vnosnoPolje=tk.Entry(okno, borderwidth=5, width=2, validate="focusout", validatecommand=poVnosu)
        vnosi[x].append(vnosnoPolje)
        #temp = tk.Button(okno, text= texti[x][y],bg="red", command=lambda: izpis())
        vnosnoPolje.grid(row=x,column=y)


tk.Button(okno, text="Izpis",bg="red", command=izpis).grid(row=1,column=10)

randX=rnd.randint(0, 8)
randY=rnd.randint(0, 8)
#gumbi[0][0]['text']=0
    
##stevec=1
##for x in range(3):
##    for y in range(3):
##        temp = tk.Button(okno, text=stevec,bg="gray")
##        temp.grid(row=x,column=y+15)
##        stevec+=1


