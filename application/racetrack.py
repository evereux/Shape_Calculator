
from math import pi

from .circle import CircleCalc

class RacetrackCalc:
    def __init__(self, x, y, area, cfm):
        self.x = x
        self.y = y
        self.area = area
        self.cfm = cfm

    def racetrackProperties(self):

        # simply vars to make rest of function more readable.
        width = self.x
        height = self.y
        area = self.area
        circumference = self.cfm

        warning = False

        # inputs for width and height
        if all([width > 0, height > 0, area == 0, circumference == 0]):
            self.area, self.circumference = self.getAreaCFM()
        # inputs for height and area.
        elif all([width == 0, height > 0, area > 0, circumference == 0]):
            # get width
            circleArea = pi * ((height / 2) ** 2)
            rectangleArea = area - circleArea
            self.x = rectangleArea / height
            # get circumference
            circleCircumference = 2 * pi * (height / 2)
            rectangleEdgesCircumference = self.x * 2
            self.cfm = circleCircumference + rectangleEdgesCircumference
        # inputs for height and circumference.
        elif all([width == 0, height > 0, area == 0, circumference > 0]):
            # get width
            circleCircumference = 2 * pi * (height / 2)
            self.x = (circumference - circleCircumference) / 2
            # get area
            circleArea = pi * ((height / 2) ** 2)
            rectangleArea = height * self.x
            self.area = circleArea + rectangleArea

        else:

            warning = True

        return self.x, self.y, self.area, self.cfm, warning

    def getAreaCFM(self):
        # get the csa of the square portion
        csasqr = self.x * self.y
        # get the csa of the rounded ends
        circleList = CircleCalc(self.y, 0, 0).circleProperties()
        self.area = circleList[1] + csasqr
        self.cfm = circleList[2] + (self.x * 2)
        return self.area, self.cfm

