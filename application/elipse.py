from math import pi, sqrt


class ElipseCalc:


    def __init__(self, semimajor, semiminor, area, cfm):
        self.semimajor = semimajor
        self.semiminor = semiminor
        self.area = area
        self.cfm = cfm

    def properties(self):

        warning = False

        # inputs for semimajor and semiminor only
        if all([self.semimajor > 0, self.semiminor > 0,
                self.area == 0, self.cfm == 0]):

            self.area = self.get_area(self.semimajor, self.semiminor)
            self.cfm = self.get_circumference(self.semimajor, self.semiminor)

        # inputs for semiminor and area only
        elif all([self.semimajor == 0, self.semiminor > 0,
                  self.area > 0, self.cfm == 0]):

            self.semimajor = self.get_opposite_semi(self.semiminor, self.area)
            self.cfm = self.get_circumference(self.semimajor, self.semiminor)

        # inputs for semiminor and area only
        elif all([self.semimajor > 0, self.semiminor == 0,
                  self.area > 0, self.cfm == 0]):

            self.semiminor = self.get_opposite_semi(self.semimajor, self.area)
            self.cfm = self.get_circumference(self.semimajor, self.semiminor)

        else:

            warning = True

        return self.semimajor, self.semiminor, self.area, self.cfm, warning

    def get_area(self, semimajor, semiminor):
        # excel calcuation = =PI()*(semimajor/2)*(semiminor/2)
        # calculation if we know major or minor axis
        # 2 * ( csa / (pi * ( value / 2)))
        area = pi * (semimajor / 2) * (semiminor / 2)
        return area

    def get_opposite_semi(self, semiminor, area):

        semimajor = 2 * (area / (pi * (semiminor / 2)))

        return semimajor

    def get_circumference(self, semimajor, semiminor):

        # ensure values have been inputted in correct order
        x, y = max(semimajor, semiminor), min(semimajor, semiminor)

        a = x/2
        b = y/2

        # based on an approximation equation by Ramanujan
        h = (pow((a-b), 2))/(pow((a+b), 2))
        l = 1+((3*h)/(10+sqrt(4-3*h)))
        p = pi*(a+b)*l

        return p

