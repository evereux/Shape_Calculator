from math import atan, cos, pi, tan, radians, sin

class TaperCalc:
    def __init__(self, angle, dia1, dia2, length):
        self.dia1 = dia1
        self.dia2 = dia2
        self.angle = angle
        self.length = length

    def properties(self):

        warning = False

        if all([self.dia1 > 0, self.dia2 > 0, self.angle > 0]) and (self.length == 0):
            self.length = self.get_taper_length()
        elif all([self.dia1 > 0, self.dia2 > 0, self.length > 0]) and (self.angle == 0):
            self.angle = self.get_taper_angle()
        elif all([self.dia2 > 0, self.length > 0, self.angle > 0]) and (self.dia1 == 0):
            self.dia1 = self.get_taper_dia(self.dia1, self.dia2)
        elif all([self.dia1 > 0, self.length > 0, self.angle > 0]) and (self.dia2 == 0):
            self.dia2 = self.get_taper_dia(self.dia1, self.dia2)
        else:
            warning = True

        return self.angle, self.dia1, self.dia2, self.length, warning

    def get_taper_length(self):
        # get the opposite length
        opp = self.dia1 - self.dia2
        # convert input angle to radians
        radians = self.angle * pi / 180
        cot = 1 / (tan(radians))
        length = opp / 2 * cot
        return abs(length)

    def get_taper_angle(self):
        # get the opposite length
        opp = (self.dia1 - self.dia2) / 2
        adj = self.length
        tangent = opp / adj
        arc_tangent = atan(tangent)
        angle = arc_tangent * (180 / pi)

        return abs(angle)

    def get_taper_dia(self, dia1, dia2):

        if dia1 == 0:
            dia = dia2
        elif dia2 == 0:
            dia = dia1

        angle = self.angle
        length = self.length

        # get hypotenuse
        _radians = radians(angle)
        _cosa = cos(_radians)
        hyp = length / _cosa

        # get opposite
        _sin = sin(_radians)
        opp = _sin * hyp

        if dia1 == 0:
            oDia = dia + (opp * 2)
        elif dia2 == 0:
            oDia = dia - (opp * 2)

        return (abs(oDia))