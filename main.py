from HirstGenerator import HirstGenerator
from turtle import Screen
from tkinter import*
import requests
from colorDisplay import colorDisplay
from PIL import Image

screen = Screen()
window = Tk()
window.title("Hirst Painting Generator")
window.minsize(width = 300,height=300)


filePathLabel = Label(window,text="Enter the web image url you want to extract from")
filePathLabel.pack()
entry1 = Entry(window)
entry1.pack()

global BUTTON_2_WAS_CLICKED
BUTTON_2_WAS_CLICKED = False
def button2Clicked():
    global BUTTON_2_WAS_CLICKED
    BUTTON_2_WAS_CLICKED = True
    useLastImageButton.config(text="Clicked")

useLastImageButton = Button(window,text="Use the last used image",command = button2Clicked)
useLastImageButton.pack()

fileNameLabel = Label(window,text="Enter file type (add .jpg if using last image)")
fileNameLabel.pack()
entry3 = Entry(window)
entry3.pack()

numColorLabel = Label(window,text="Enter the number of colors you want to extract from")
numColorLabel.pack()
entry2 = Entry(window)
entry2.pack()


def resize(filePath):
    input_name = filePath
    output_width = 300  # set the output size
    img = Image.open(input_name)
    wpercent = (output_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((output_width, hsize), Image.Resampling.LANCZOS)
    img.save(filePath)



def buttonClicked():
    global numColors
    numColors = int(entry2.get())
    pathName = f"hirstImage{entry3.get()}"
    resize(pathName)

    global BUTTON_2_WAS_CLICKED
    if BUTTON_2_WAS_CLICKED == True:
        hirst = HirstGenerator(numColors,"hirstimage.jpg")
        BUTTON_2_WAS_CLICKED = False
    else:
        global filePath
        filePath = requests.get(entry1.get())
        with open(pathName, 'wb') as f:
            f.write(filePath.content)
        hirst = HirstGenerator(numColors,pathName)

    hirst.generatePainting()

    generateButton.config(text="Regenerate")
    useLastImageButton.config(text = "Use last image")


    display = colorDisplay(pathName, 12, numColors)
    display.plot()


generateButton = Button(window,text="Click to generate Painting",fg="green", width = 30, height = 5, command = buttonClicked)
generateButton.pack()

window.mainloop()
