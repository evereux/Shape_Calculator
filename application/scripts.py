import os

from decimal import Decimal

def convertUnits(value, unitFrom, unitTo, unit, ureg):
    vP = ""  # value power eg area m**2
    allgood = False
    alist = ['length', 'mass', 'massflow']

    if unit in alist:
        allgood = True
    elif unit == "area":
        vP = "**2"
        unitFrom = unitFrom[:-1]
        unitTo = unitTo[:-1]
        allgood = True
    elif unit == "volume":
        vP = "**3"
        unitFrom = unitFrom[:-1]
        unitTo = unitTo[:-1]
        allgood = True
    elif unit == "density":
        vP = "**3"
        unitFrom = unitFrom[:-1]
        unitTo = unitTo[:-1]
        allgood = True
    elif unit == "mass":
        allgood = True

    # set the output value to 0
    v = 0

    if allgood:
        unitFrom = unitFrom + vP
        unitTo = unitTo + vP
        v = value * ureg.parse_expression(unitFrom)
        v = v.to(ureg.parse_expression(unitTo))
        v = v.magnitude

    v = f_round(v)
    v = convert2float(v)
    return v


def convert2float(input):
    try:
        return float(Decimal(input))
    except:
        return 0


def f_round(value):
    value = float(value)

    value = '{:.10f}'.format(value)

    return value

def get_image(image_name):
    """
    Function to overwrite the ui defined image paths.
    :param image_name:
    :return:
    """
    cwd = os.getcwd()
    path_to_images = r'application/images/'
    image = path_to_images + image_name + '.png'
    image_name = os.path.join(cwd, image)

    if os.path.isfile(image_name):
        return image_name
    else:
        raise Exception("Could not load image.")
