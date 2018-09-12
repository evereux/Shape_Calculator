from math import pi, sqrt

class CircleCalc:
    def __init__(self, dia, area, cfm):

        self.dia = dia
        self.area = area
        self.cfm = cfm

    def properties(self):

        warning = False

        if all([self.dia > 0, self.area == 0, self.cfm == 0]):

            self.area = self.f_area(self.dia)
            self.cfm = self.f_cfm(self.area)

        elif all([self.area > 0, self.dia == 0, self.cfm == 0]):

            self.cfm = self.f_cfm(self.area)
            self.dia = self.f_dia(self.cfm)

        elif all([self.cfm > 0, self.dia == 0, self.area == 0]):

            self.dia = self.f_dia(self.cfm)
            self.area = self.f_area(self.dia)

        else:

            warning = True

        return self.dia, self.area, self.cfm, warning

    # calculate the dia based on cfm
    def f_dia(self, cfm):
        dia = cfm / pi
        return dia

    # calculate the cross sectional area based on dia
    def f_area(self, dia):
        area = pi * (dia / 2) ** 2
        return area

    # calculate the circumference based on area
    def f_cfm(self, area):
        cfm = sqrt(area * 4 * pi)
        return cfm
