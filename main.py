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

fileNameLabel = Label(window,text="Enter file type (add .jpg/.png)")
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
    pathName = f"hirstImage{entry3.get()}"
    with open(pathName,'wb') as f:
        f.write(filePath.content)
    global numColors
    numColors = int(entry2.get())
    hirst = HirstGenerator(numColors,pathName)
    hirst.generatePainting()
    generateButton.config(text="Regenerate")





generateButton = Button(window,text="Click to generate Painting",fg="green", width = 30, height = 5, command = buttonClicked)
generateButton.pack()

window.mainloop()