from application import ElipseCalc

semimajor = 200
semiminor = 80
area = 15
cfm = 8

EC = ElipseCalc(semimajor, semiminor, False, False)

_, _, area, cfm, _ = EC.elipse_properties()
print("Area: {}, CFM: {}".format(area, cfm))
