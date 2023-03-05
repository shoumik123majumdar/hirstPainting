from HirstGenerator import HirstGenerator
from turtle import Screen
from tkinter import *
import requests
from ColorDisplay import ColorDisplay
from PIL import Image

# Creates the screen for the painting as well as the window for the GUI
screen = Screen()
window = Tk()
window.title("Hirst Painting Generator")
window.minsize(width=300, height=300)

# Creates the label and entry box for the file path in the GUI
file_path_label = Label(window, text="Enter the web image url you want to extract from")
file_path_label.pack()
entry1 = Entry(window)
entry1.pack()

global image_button_was_clicked
image_button_was_clicked = False


# Creates the command for the button that allows the user to 'Use the last used image' in the GUI
def use_image_button():
    global image_button_was_clicked
    image_button_was_clicked = True
    use_last_image_button.config(text="Clicked")


use_last_image_button = Button(window, text="Use the last used image", command=use_image_button)
use_last_image_button.pack()

# Creates the label and entry box for the file type in the GUI
file_name_label = Label(window, text="Enter file type (enter.jpg if using last image)")
file_name_label.pack()
entry3 = Entry(window)
entry3.pack()

# Creates the label and entry box for the number of colors in the GUI
num_color_label = Label(window, text="Enter the number of colors you want to extract from")
num_color_label.pack()
entry2 = Entry(window)
entry2.pack()


# This function resizes the file
def resize(filePath):
    output_width = 300  # set the output size
    img = Image.open(filePath)  # opens the image
    wpercent = (output_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))  # Calculates the new size to resize it to
    img = img.resize((output_width, hsize), Image.Resampling.LANCZOS)  # Resizes the image
    img.save(filePath)  # saves the new resized image in the same place


# This function handles the command for the generate button
def generate_button_clicked():
    global image_button_was_clicked
    error_caught = False
    try:
        num_colors = int(entry2.get())  # gets the number of colors from the user's entry in the GUI
    except ValueError:
        num_color_label.config(text="NUMBER OF COLORS REQUIRED")
        error_caught = True
    path_name = f"hirstImage" + str(entry3.get())   # gets the user's input on whether it is a .jpg or .png

    try: resize(path_name)  # resizes the image
    except FileNotFoundError:
        file_name_label.config(text="PLEASE INPUT '.jpg'")
        error_caught = True


    if image_button_was_clicked == True:  # if the 'use last image' button was clicked, then use 'hirstimage.jpg' (contains the old image)
        try: hirst = HirstGenerator(num_colors, "hirstimage.jpg")
        except UnboundLocalError:
            error_caught = True
        image_button_was_clicked = False # set this boolean back to false for the next iteration of the program
    else:  # this case handles when a user inputs a new image file url to generate from
        try:
            file_path = requests.get(entry1.get())  # gets the image from the web and saves the file path into this variable
            with open(path_name, 'wb') as f:
                f.write(file_path.content)  # downloads the web image locally on the computer in the file 'hirstimage'
            resize(path_name)  # resizes the image again (this is for iterations of the function after the first one)
            hirst = HirstGenerator(num_colors, path_name)
        except requests.exceptions.MissingSchema:
            file_path_label.config(text="FILE PATH REQUIRED")
            error_caught = True

    try: hirst.generate_painting()  # generates the painting using the HirstGenerator object's function
    except UnboundLocalError:
        error_caught = True
    # Renames these buttons to be clicked for the next iteration of the program
    if error_caught == False:
        generate_button.config(text="Regenerate")
        use_last_image_button.config(text="Use last image")
        num_color_label.config(text="Enter the number of colors you want to extract from")
        file_name_label.config(text="Enter file type (add .jpg if using last image)")
        file_path_label.config(text="Enter the web image url you want to extract from")
        # Creates a colorDisplay object and plots it: shows the user a donut chart of the image's colors
        display = ColorDisplay(path_name, 12, num_colors)
        display.plot()
    else:
        use_last_image_button.config(text = "Use the last used image")




# This button generates the painting when the user clicks it on the GUI using the function above
generate_button = Button(window, text="Click to generate Painting", fg="green", width=30, height=5,
                         command=generate_button_clicked)
generate_button.pack()

window.mainloop()  # closes windows

