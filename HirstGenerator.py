from turtle import Turtle
import colorgram
import random
import turtle
from turtle import Screen


turtle.colormode(255)
class HirstGenerator():
    def __init__(self,numColors,filePath):
        self.hirst = Turtle()
        self.hirst.speed("fast")
        self.hirst.penup()
        self.hirst.shape("circle")
        self.hirst.setpos(-230, -100)
        self.hirst.setheading(0)
        self.numColors = numColors
        self.filePath = filePath
        self.colors = colorgram.extract(self.filePath, self.numColors)
        self.maxColors = len(self.colors)
    def getColors(self):
        colorTuples = []
        for color in self.colors:
            r = color.rgb[0]
            g = color.rgb[1]
            b = color.rgb[2]
            tup = (r, g, b)
            colorTuples.append(tup)
        return colorTuples


    def getRandColors(self):
        colorTuples = self.getColors()
        randColors = []
        numColors = self.numColors
        if(self.numColors>len(self.colors)):
                numColors = len(self.colors)
        for i in range(100):
            randomNum = random.randint(0, numColors - 1)
            randColors.append(colorTuples[randomNum])
        return randColors



    def generatePainting(self):
        colors = self.getRandColors()
        counter = 0
        for i in range(10):
            for z in range(10):
                color = colors[counter]
                self.hirst.dot(20,color)
                self.hirst.forward(40)
                counter+=1
            self.hirst.setx(-230)
            self.hirst.sety(self.hirst.ycor()+40)
            self.hirst.ht()



