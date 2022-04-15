import tkinter as tk
import random

def main():
    window["bg"] = "#000"
    window.title("Visual Bar Sort")
    canvas.pack()
    barlyst = [canvas.create_rectangle(x*10, 0, x*10-10, 5*x, fill="#fff") for x in range(1, BARS+1)]
    while True:
        scramble(barlyst)
        bubble(barlyst)
    #inorder(barlyst)
    window.mainloop()

def swap(lyst, index_1, index_2):
    lyst[index_1], lyst[index_2] = lyst[index_2], lyst[index_1]
    canvas.itemconfig(lyst[index_1], fill="#f00")
    canvas.itemconfig(lyst[index_2], fill="#0f0")
    window.update()
    canvas.coords(lyst[index_1], index_1*10, 0, index_1*10+10, 5*lyst[index_1])
    canvas.coords(lyst[index_2], index_2*10, 0, index_2*10+10, 5*lyst[index_2])
    canvas.itemconfig(lyst[index_1], fill="#fff")
    canvas.itemconfig(lyst[index_2], fill="#fff")
    window.update()

def scramble(lyst):
    for i in range(len(lyst)):
        swap(lyst, i, random.randint(0, BARS-1))

def inorder(lyst):
    for x in range(len(lyst)-1):
        if lyst[x] > lyst[x+1]:
            #print("flase")
            return False
        else:
            #print("chekc")
            pass
    #print("ture")
    return True

def bubble(lyst):
    while inorder(lyst) is False:
        for x in range(len(lyst)-1):
            if lyst[x] > lyst[x+1]:
                swap(lyst, x, x+1)

if __name__ == "__main__":
    BARS = 128
    window = tk.Tk()
    canvas = tk.Canvas(window, width=BARS*10, height=BARS*5, background="#000", bd=-2)
    main()
