import tkinter as tk
from tkinter import *
from tkinter import messagebox

def hydroph():
    global e, count19, count18, count17, count16, count15, count14, count13, count12, count11, count10, count9, count8, count7, count6, count5, count4, count3, count2, count1, count0
    string = e.get()
    parse= "".join(string.split())
    print(parse)
    a = list(parse)
    print("Sequence consist of",len(parse),"Amino Acids")
    n = len(parse)

    window = 6
    ala = -0.500
    arg = 3.000
    asn = 0.200
    asp = 3.000
    cys = -1.000
    gln = 0.200
    glu = 3.000
    gly = 0.000
    his = -0.500
    ile = -1.800
    leu = -1.800
    lys = 3.000
    met = -1.300
    phe = -2.500
    pro = 0.000
    ser = 0.300
    thr = -0.400
    trp = -3.400
    tyr = -2.300
    val = -1.500
    j = -1
    k = 5
    hydro = 0
    i = 1
    b = []
    while i <= (n-5):
        print(a[j+1:k+1])
        hydro / window
        print("value =", hydro)
        b[j+1:k+1] = a[j+1:k+1]

        # If  a letter is A add value -0.500
        if (a[j]) == 'A':
            hydro += ala
            count0 = parse.count('A')

            i += 1
            j += 1
            k += 1
            continue

        # If  a letter is C add value -1.000
        if (a[j]) == 'C':
            hydro += cys
            count1 = parse.count('C')

            i += 1
            j += 1
            k += 1
            continue

        # If  a letter is D add value 3.000
        if (a[j]) == 'D':
            hydro += asp
            count2 = parse.count('D')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'E':
            hydro += glu
            count3 = parse.count('E')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'F':
            hydro += phe
            count4 = parse.count('F')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'G':
            hydro += gly
            count5 = parse.count('G')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'H':
            hydro += his
            count6 = parse.count('H')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'I':
            hydro += ile
            count7 = parse.count('I')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'K':
            hydro += lys
            count8 = parse.count('K')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'L':
            hydro += leu
            count9 = parse.count('L')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'M':
            hydro += met
            count10 = parse.count('M')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'N':
            hydro += asn
            count11 = parse.count('N')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'P':
            hydro += pro
            count12 = parse.count('P')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'Q':
            hydro += gln
            count13 = parse.count('Q')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'R':
            hydro += arg
            count14 = parse.count('R')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'S':
            hydro += ser
            count15 = parse.count('S')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'T':
            hydro += thr
            count16 = parse.count('T')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'V':
            hydro += val
            count17 = parse.count('V')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'W':
            hydro += trp
            count18 = parse.count('W')
            i += 1
            j += 1
            k += 1
            continue

        if (a[j]) == 'Y':
            hydro += tyr
            count19 = parse.count('Y')
            i += 1
            j += 1
            k += 1
            continue

    i += 1
    j += 1
    k += 1
    print("Frequency of Occurrence of \n A =", count0, "\n C =", count1, "\n D =", count2, "\n E =", count3, "\n F =",count4, "\n G =", count5)
    print("Overall protein hydrophilicity value is =", hydro / n)
    print("Protein seq is: ", parse)


def startgame():
    pass


mw = tk.Tk()
var = IntVar()
mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "white")

mw.title('Protein Antigenicity Finder')
mw.geometry("1300x600")  # You want the size of the app to be 500x500
mw.resizable(0,0)  # Don't allow resizing in the x or y direction

back = tk.Frame(master=mw, bg='black')
back.pack_propagate(0)  # Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

e= tk.Label(master=back, text='Enter Protein', bg="black", fg="white", font=('Times New Roman', 18, 'bold')).grid(row=1, column=1)
e= tk.Label(master=back, text='Sequence', bg="black", fg="white", font=('Times New Roman', 18, 'bold')).grid(row=2, column=1)
e = tk.Entry(master=back,width=150, bg="white", bd=10)
e.pack()
e.focus_set()
info0 = tk.Label(master=back, text='Functionalities', bg="black", fg="lightgreen", font=('Times New Roman', 14, 'bold')) .grid(row=6, column=1)
info1 = tk.Checkbutton(master=back, text="Hydrophilicity", variable=var, bg="black", fg="White").grid(row=7, column=1)
info2 = tk.Checkbutton(master=back, text="Accessibility", variable=var, bg="black", fg="White").grid(row=8, column=1)
info3 = tk.Checkbutton(master=back, text="Flexibility", variable=var, bg="black", fg="White").grid(row=9, column=1)

info4 = tk.Label(master=back, text='Class', bg="black", fg="lightpink",font=('Times New Roman', 14, 'bold')).grid(row=6, column=3)
info5 = tk.Radiobutton(master=back, text="MHC I", bg="black", fg="white").grid(row=7, column=3)
info6 = tk.Radiobutton(master=back, text="MHC II", bg="black", fg="white").grid(row=8, column=3)
info7 = tk.Radiobutton(master=back, text="B CELL", bg="black", fg="white").grid(row=9, column=3)
info8 = tk.Radiobutton(master=back, text="T CELL", bg="black", fg="white").grid(row=10, column=3)

info9 = tk.Button(master=back, text='Submit', bg="green", fg="white", command=hydroph).grid(row=12, column=1)
info = tk.messagebox.showinfo("Antigenicity Result")

info = tk.Label(master=back, text='', bg="black", fg="white").grid(row=13, column=1)
info = tk.Label(master=back, text='Antigenicity Result', bg="black", fg="white",font=('Times New Roman', 15, 'bold')).grid(row=15, column=1)

canvas = tk.Canvas(mw, bg="white", bd=100 )
colors = ('red', 'black', 'green','blue')
canvas.create_line(20, 100, 120, 100, width=4,fill=colors[0])
canvas.pack()

info = tk.Label(master=back, bg="black")

close = tk.Button(master=back, text='Quit', bg="red", fg="white", command=mw.destroy).grid(row=12, column=3)
info.pack()

mw.mainloop()

