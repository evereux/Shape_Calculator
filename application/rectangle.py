from math import pi

class RectangleCalc:
    def __init__(self, x, y, r):

        self.x = x
        self.y = y
        self.r = r

    def properties(self):

        warning = False
        x = self.x
        y = self.y
        r = self.r
        area_sqr_corners = 0
        area_circle = 0
        cfm_sqr_corners = 0
        cfm_circle = 0

        if (x == 0) and (y == 0):
            warning = True

        # area of rectangle
        area_rectangle = x * y
        # circumference of the rectangle
        cfm_rectangle = (x * 2) + (y * 2)

        # if we have an input for r
        if r > 0:
            # area of square corners
            area_sqr_corners = (r * r) * 4
            area_circle = pi * (r ** 2)
            cfm_sqr_corners = (r * 2) * 4
            cfm_circle = 2 * pi * r

        area = area_rectangle - area_sqr_corners + area_circle
        cfm = cfm_rectangle - cfm_sqr_corners + cfm_circle

        return (x, y, r, area, cfm, warning)

