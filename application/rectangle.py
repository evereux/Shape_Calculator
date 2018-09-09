from math import pi

class RectangleCalc:
    def __init__(self, x, y, r):

        self.x = x
        self.y = y
        self.r = r

    def rectangleProperties(self):

        warning = False
        x = self.x
        y = self.y
        r = self.r
        areaSqrCorners = 0
        areaCircle = 0
        cfmSqrCorners = 0
        cfmCircle = 0

        if (x == 0) and (y == 0):
            warning = True

        # area of rectangle
        areaRectangle = x * y
        # circumference of the rectangle
        cfmRectangle = (x * 2) + (y * 2)

        # if we have an input for r
        if r > 0:
            # area of square corners
            areaSqrCorners = (r * r) * 4
            areaCircle = pi * (r ** 2)
            cfmSqrCorners = (r * 2) * 4
            cfmCircle = 2 * pi * r

        area = areaRectangle - areaSqrCorners + areaCircle
        cfm = cfmRectangle - cfmSqrCorners + cfmCircle

        return (x, y, r, area, cfm, warning)

