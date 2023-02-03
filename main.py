from HirstGenerator import HirstGenerator
from turtle import Screen
from tkinter import*
from turtle import Turtle
import colorgram
import random
import turtle


screen = Screen()
window = Tk()
window.title("Hirst Painting Generator")
window.minsize(width = 300,height=300)


filePathLabel = Label(window,text="Enter the image url you want to extract from")
filePathLabel.pack()
entry1 = Entry(window)
entry1.pack()


numColorLabel = Label(window,text="Enter the number of colors you want to extract from \n If greater than the total number of colors extracted, it will extract the maximum number of colors")
numColorLabel.pack()
entry2 = Entry(window)
entry2.pack()

def buttonClicked():
    global filePath
    filePath = entry1.get()
    #filePath = 'monaLisa.jpg'
    global numColors
    numColors = int(entry2.get())
    hirst = HirstGenerator(numColors,filePath)
    hirst.generatePainting()



generateButton = Button(window,text="Click to generate Painting",command = buttonClicked)
generateButton.pack()

window.mainloop()