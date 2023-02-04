from HirstGenerator import HirstGenerator
from turtle import Screen
from tkinter import*
import requests


screen = Screen()
window = Tk()
window.title("Hirst Painting Generator")
window.minsize(width = 300,height=300)


filePathLabel = Label(window,text="Enter the web image url you want to extract from")
filePathLabel.pack()
entry1 = Entry(window)
entry1.pack()

fileNameLabel = Label(window,text="Enter the name you want for the file")
fileNameLabel.pack()
entry3 = Entry(window)
entry3.pack()

numColorLabel = Label(window,text="Enter the number of colors you want to extract from \n If greater than the total number of colors extracted, it will extract the maximum number of colors")
numColorLabel.pack()
entry2 = Entry(window)
entry2.pack()

def buttonClicked():
    global filePath
    filePath = requests.get(entry1.get())
    pathName = "hirstImage"
    with open(pathName,'wb') as f:
        f.write(filePath.content)
    global numColors
    numColors = int(entry2.get())
    hirst = HirstGenerator(numColors,pathName)
    hirst.generatePainting()



generateButton = Button(window,text="Click to generate Painting",command = buttonClicked)
generateButton.pack()

window.mainloop()