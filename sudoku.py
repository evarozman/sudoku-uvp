import tkinter as tk
import random as rnd

class Sudoku:

    def __init__(self):
        self.okno = tk.Tk()
        self.vnosi = []
        self.tezavnost = "lahko"
        tk.Button(self.okno, text="Lahko", command=self.zacni_lahko_igro).grid(row=10,column=10)
        tk.Button(self.okno, text="Srednje", command=self.zacni_srednjo_igro).grid(row=11,column=10)
        tk.Button(self.okno, text="Težko", command=self.zacni_tezko_igro).grid(row=12,column=10)
        self.opozorilo = tk.StringVar()
        tk.Label(textvariable=self.opozorilo, fg="red").grid(row=13,column=10)
        
    def vrednosti(self, seznam):
        s = set()
        for x in seznam:
            if x in s:
                return False
            s.add(x)
        return True

    def preveri_sudoku(self):

        ### po vrsticah
        for x in range(9):
            seznam = []
            for y in range(9):
                if self.vnosi[x][y].get() != "": 
                    seznam.append(self.vnosi[x][y].get())
            if self.vrednosti(seznam) == False:
                return False

        ### po stolpcih
        for x in range(9):
            seznam = []
            for y in range(9):
                if self.vnosi[y][x].get() != "": 
                    seznam.append(self.vnosi[y][x].get())
            if self.vrednosti(seznam) == False:
                return False
            
        ### po kvadrantih
        for i in range(0, 9, 3): 
            for j in range(0, 9, 3):
                seznam = []
                for k in range(i, i + 3): 
                    for l in range(j, j + 3):
                        if self.vnosi[k][l].get() != "": 
                            seznam.append(self.vnosi[k][l].get())
                if self.vrednosti(seznam) == False:
                    return False

        return True

    def po_vnosu(self):
        st_pravilnih = 0
        pravilno = True
        
        for i in range(9):
            for j in range(9):
                if self.vnosi[i][j].get() != "" and int(self.vnosi[i][j].get()) > 9:
                    self.vnosi[i][j].config(fg='red')
                    pravilno=False
                else:
                    self.vnosi[i][j].config(fg='black')

                if self.vnosi[i][j].get() != "" and int(self.vnosi[i][j].get()) <= 9:
                    st_pravilnih += 1
                    
        if self.preveri_sudoku() == False:
            self.opozorilo.set("Napaka pri vnosu!")
        else:
            self.opozorilo.set("")
            if st_pravilnih == 81:
                tk.Label(text="Sudoku rešen!", fg="green").grid(row=14,column=10)
                        
    def sprazni_celice(self, st_celic):
        stevec=0
        while stevec < st_celic:
            randX = rnd.randint(0, 8)
            randY = rnd.randint(0, 8)
            if self.vnosi[randX][randY].get() != "":
                self.vnosi[randX][randY].delete(0, 'end')
                stevec+=1        

    def preberi_iz_datoteke(self):
        self.vnosi = []
        with open("datoteka.txt", "r") as dat:
            for x in range(9):
                self.vnosi.append([])
                line = dat.readline()
                for y in range(9):
                    vnosno_polje = tk.Entry(self.okno, borderwidth=5,
                                            width=2, validate="focusout",
                                            validatecommand=self.po_vnosu)
                    vnosno_polje.insert(0, line[y])
                    self.vnosi[x].append(vnosno_polje)
                    vnosno_polje.grid(row=x, column=y)

    def zacni_lahko_igro(self):
        self.preberi_iz_datoteke()
        self.sprazni_celice(50)

    def zacni_srednjo_igro(self):
        self.preberi_iz_datoteke()
        self.sprazni_celice(60)

    def zacni_tezko_igro(self):
        self.preberi_iz_datoteke()
        self.sprazni_celice(70)

igra = Sudoku()
