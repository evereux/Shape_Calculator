from math import pi

from .circle import CircleCalc


class RacetrackCalc:
    def __init__(self, x, y, area, cfm):
        self.x = x
        self.y = y
        self.z = 0
        self.circumference = 0
        self.area = area
        self.cfm = cfm

    def properties(self):

        # simplify vars to make rest of function more readable.
        width = self.x
        height = self.y
        area = self.area
        circumference = self.cfm

        warning = False

        # inputs for width and height
        if all([width > 0, height > 0, area == 0, circumference == 0]):
            self.area, self.circumference = self.get_area_cfm()
        # inputs for height and area.
        elif all([width == 0, height > 0, area > 0, circumference == 0]):
            # get width
            circle_area = pi * ((height / 2) ** 2)
            rectangle_area = area - circle_area
            self.x = rectangle_area / height
            # get circumference
            circle_circumference = 2 * pi * (height / 2)
            rectangle_edges_circumference = self.x * 2
            self.cfm = circle_circumference + rectangle_edges_circumference
        # inputs for height and circumference.
        elif all([width == 0, height > 0, area == 0, circumference > 0]):
            # get width
            circle_circumference = 2 * pi * (height / 2)
            self.x = (circumference - circle_circumference) / 2
            # get area
            circle_area = pi * ((height / 2) ** 2)
            rectangle_area = height * self.x
            self.area = circle_area + rectangle_area

        else:

            warning = True

        self.z = self.y * 2 + self.x

        return self.x, self.y, self.z, self.area, self.cfm, warning

    def get_area_cfm(self):
        # get the csa of the square portion
        csasqr = self.x * self.y
        # get the csa of the rounded ends
        circle_list = CircleCalc(self.y, 0, 0).properties()
        self.area = circle_list[1] + csasqr
        self.cfm = circle_list[2] + (self.x * 2)
        return self.area, self.cfm
