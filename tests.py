
from math import pi

from application.circle import CircleCalc

def test_circle():

    # define circle defaults
    diameter = 8
    area = pi * ((diameter / 2) * (diameter / 2))
    cfm = 2 * pi * (diameter / 2)

    # calculate using diameter
    circle = CircleCalc(diameter, 0, 0)
    circle.properties()
    assert circle.area == area
    assert circle.cfm == cfm

    # calculate using area
    circle = CircleCalc(0, area, 0)
    circle.properties()
    assert circle.dia == diameter
    assert circle.cfm == cfm

    # calculate using cfm
    circle = CircleCalc(0, 0, cfm)
    circle.properties()
    assert circle.dia == diameter
    assert circle.area == area


