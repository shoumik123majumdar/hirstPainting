from turtle import Turtle
import colorgram
import random
import turtle


turtle.colormode(255)
class HirstGenerator():
    def __init__(self, num_colors, file_path):
        self.hirst = Turtle()
        self.hirst.speed("fast")
        self.hirst.penup()
        self.hirst.shape("circle")
        self.hirst.setpos(-230, -100)
        self.hirst.setheading(0)
        self.num_colors = num_colors
        self.file_path = file_path
        self.colors = colorgram.extract(self.filePath, self.numColors) # extracts the 'num_colors' colors from the image

    # Returns a list of the rgb tuples in 'num_colors'
    def get_colors(self):
        color_tuples = []
        for color in self.colors:
            r = color.rgb[0]
            g = color.rgb[1]
            b = color.rgb[2]
            tup = (r, g, b)
            color_tuples.append(tup)
        return color_tuples  # returns a list of the rgb tuples in 'num_colors'

    # Returns a randomized list of 100 rgb tuples using 'color_tuples'
    def get_rand_colors(self):
        color_tuples = self.get_colors()
        rand_colors = []
        num_colors = self.num_colors
        if(self.num_colors>len(self.colors)):  # if the user's input number is greater than the total number of colors that can be extracted...
                num_colors = len(self.colors)  # set the user's input to the total num of colors extracted.

        for i in range(100):
            randomNum = random.randint(0, num_colors - 1)
            rand_colors.append(color_tuples[randomNum])
        return rand_colors



    def generate_painting(self):
        randColors = self.get_rand_colors()
        counter = 0  # this counter makes sure it iterates through all 100 of the colors in the randomized list
        for i in range(10):
            for z in range(10):
                color = randColors[counter]
                self.hirst.dot(20,color)  # places dot colored dot on the screen
                self.hirst.forward(40)
                counter+=1
            # after every 10 dots, resets the position back 10 spaces and up 1 space to continue moving
            self.hirst.setx(-230)
            self.hirst.sety(self.hirst.ycor()+40)
            self.hirst.ht()  # hides the turtle to only show the dots appearing on the screen



