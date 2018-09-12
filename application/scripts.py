import os

from decimal import Decimal


def convert_units(value, unit_from, unit_to, unit, ureg):
    v_p = ""  # value power eg area m**2
    allgood = False
    alist = ['length', 'mass', 'massflow']

    if unit in alist:
        allgood = True
    elif unit == "area":
        v_p = "**2"
        unit_from = unit_from[:-1]
        unit_to = unit_to[:-1]
        allgood = True
    elif unit == "volume":
        v_p = "**3"
        unit_from = unit_from[:-1]
        unit_to = unit_to[:-1]
        allgood = True
    elif unit == "density":
        v_p = "**3"
        unit_from = unit_from[:-1]
        unit_to = unit_to[:-1]
        allgood = True
    elif unit == "mass":
        allgood = True

    # set the output value to 0
    v = 0

    if allgood:
        unit_from = unit_from + v_p
        unit_to = unit_to + v_p
        v = value * ureg.parse_expression(unit_from)
        v = v.to(ureg.parse_expression(unit_to))
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

    try:
        cwd = sys._MEIPASS
    except Exception:
        cwd = os.path.abspath(".")

    path_to_images = r'application/images/'
    image = path_to_images + image_name + '.png'
    image_name = os.path.join(cwd, image)

    if os.path.isfile(image_name):
        return image_name
    else:
        raise Exception("Could not load image.")
