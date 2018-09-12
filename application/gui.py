import os
import string
import sys

import num2words
import pint
from PyQt4 import QtGui, QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

from application.pyqt_ui import uiFormTabs
from .circle import CircleCalc
from .elipse import ElipseCalc
from .racetrack import RacetrackCalc
from .rectangle import RectangleCalc
from .scripts import convert2float, convert_units, f_round, get_image
from .taper import TaperCalc
from .version import email, title, version


class CalculateApp(QtGui.QMainWindow, uiFormTabs.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CalculateApp, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("{}".format(title))
        self.label.setText("{}".format(title))

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("windowsxp"))



        # override the images defined in ui
        self.imageCircle.setPixmap(QtGui.QPixmap(_fromUtf8(get_image(image_name="circle"))))
        self.imageTaper.setPixmap(QtGui.QPixmap(_fromUtf8(get_image(image_name="taper"))))
        self.imageRacetrack.setPixmap(QtGui.QPixmap(_fromUtf8(get_image(image_name="racetrack"))))
        self.imageElipse.setPixmap(QtGui.QPixmap(_fromUtf8(get_image(image_name="elipse"))))
        self.imageRectangle.setPixmap(QtGui.QPixmap(_fromUtf8(get_image(image_name="rectangle"))))
        self.setWindowIcon(QtGui.QIcon(get_image(image_name="logo")))
        icon_exit = QtGui.QIcon()
        icon_exit.addPixmap(QtGui.QPixmap(_fromUtf8(get_image(image_name="exit"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon_exit)



        # if the user clicked the calculate buttons
        self.btnReset.clicked.connect(self.resetFormFields)
        self.btnTaper.clicked.connect(self.calculateTaper)
        self.btnCircles.clicked.connect(self.calculateCircles)
        self.btnRacetrack.clicked.connect(self.calculate_racetrack)
        self.btnElipses.clicked.connect(self.calculateElipses)
        self.btnConvert.clicked.connect(self.calculateConversions)
        self.btnRectangle.clicked.connect(self.calculateRectangle)

        # stored copy of definitions to fix py2exe problems I had with text files
        # removed from defining this in function to convert units as it slowed app down.
        cwd = os.getcwd()
        def_file = r'application/includes/defaultdefinition.txt'
        def_file = os.path.join(cwd, def_file)
        self.ureg = pint.UnitRegistry(def_file)

        # if the user wants to exit
        self.actionExit.triggered.connect(self.fileExit)
        self.actionAbout.triggered.connect(self.fileAbout)

        # define error font's
        self.errorFont = [
            "QLineEdit { background-color: red }",
            "QLineEdit { background-color: white; color: black }"]

        self.show()

    def fileExit(self):

        sys.exit()

    def fileAbout(self):

        text = """<h1>{}</h1>
<p>version: {}</p>
<p>Created by Paul Bourne. Contact: <a href="mailto:{}">{}</a><br>
Source code available at: <a href="https://github.com/evereux/Shape_Calculator">Github</a></p>
<p>Uses python3, PyQt4, num2words and pint.</p>
""".format(title, version, email, email)

        msgBox = QtGui.QMessageBox.about(self, "About {}".format(title), text)

    # zero all form fields.
    def resetFormFields(self):
        self.txtTA_Angle.clear()
        self.txtTA_Diameter1.clear()
        self.txtTA_Diameter2.clear()
        self.txtTA_Length.clear()
        self.txtCLS_Diamter.clear()
        self.txtCLS_Area.clear()
        self.txtCLS_Circumference.clear()
        self.txtRTRK_x.clear()
        self.txtRTRK_y.clear()
        self.txtRTRK_csa.clear()
        self.txtRTRK_cfm.clear()
        self.txtElipses_semimajor.clear()
        self.txtElipses_semiminor.clear()
        self.txtElipses_csa.clear()
        self.txtElipses_circumference.clear()
        self.txtRectangleX.clear()
        self.txtRectangleY.clear()
        self.txtRectangleR.clear()
        self.txtRectangleArea.clear()
        self.txtRectangleCfm.clear()
        self.lineEditInputLength.clear()
        self.lineEditInputArea.clear()
        self.lineEditInputVolume.clear()
        self.lineEditInputMass.clear()
        self.lineEditInputDensity.clear()
        self.lineEditInputMassFlow.clear()

    def calculateTaper(self):

        # convert inputs to float
        angle = convert2float(self.txtTA_Angle.text())
        dia1 = convert2float(self.txtTA_Diameter1.text())
        dia2 = convert2float(self.txtTA_Diameter2.text())
        length = convert2float(self.txtTA_Length.text())

        taperObject = TaperCalc(angle, dia1, dia2, length)
        taperList = taperObject.properties()

        qtTextList = [self.txtTA_Angle, self.txtTA_Diameter1, self.txtTA_Diameter2, self.txtTA_Length]

        if taperList[4] == True:

            requirements = [3, 4]
            warning_box(self, requirements)
            [i.setStyleSheet(self.errorFont[0]) for i in qtTextList]
        else:
            [i.setStyleSheet(self.errorFont[1]) for i in qtTextList]

        self.txtTA_Angle.setText(str(f_round(taperList[0])))
        self.txtTA_Diameter1.setText(str(f_round(taperList[1])))
        self.txtTA_Diameter2.setText(str(f_round(taperList[2])))
        self.txtTA_Length.setText(str(f_round(taperList[3])))

    def calculateCircles(self):

        # convert inputs to float
        dia = convert2float(self.txtCLS_Diamter.text())
        area = convert2float(self.txtCLS_Area.text())
        cfm = convert2float(self.txtCLS_Circumference.text())

        circleObject = CircleCalc(dia, area, cfm)
        circleList = circleObject.properties()

        qtTextList = [self.txtCLS_Diamter, self.txtCLS_Area, self.txtCLS_Circumference]

        if circleList[3] == True:
            requirements = [1, 3]
            warning_box(self, requirements)
            [i.setStyleSheet(self.errorFont[0]) for i in qtTextList]
        else:
            [i.setStyleSheet(self.errorFont[1]) for i in qtTextList]

        qtTextList[0].setText(str(f_round(circleList[0])))
        qtTextList[1].setText(str(f_round(circleList[1])))
        qtTextList[2].setText(str(f_round(circleList[2])))

    def calculate_racetrack(self):

        # convert inputs to floats
        x = convert2float(self.txtRTRK_x.text())
        y = convert2float(self.txtRTRK_y.text())
        area = convert2float(self.txtRTRK_csa.text())
        cfm = convert2float(self.txtRTRK_cfm.text())

        racetrackObject = RacetrackCalc(x, y, area, cfm)
        racetrackList = racetrackObject.properties()

        qtTextList = [self.txtRTRK_x, self.txtRTRK_y, self.txtRTRK_csa, self.txtRTRK_cfm]

        if racetrackList[4] == True:
            requirements = [2, 4]
            warning_box(self, requirements)
            [i.setStyleSheet(self.errorFont[0]) for i in qtTextList]
        else:
            [i.setStyleSheet(self.errorFont[1]) for i in qtTextList]

        self.txtRTRK_x.setText(str(f_round(racetrackList[0])))
        self.txtRTRK_y.setText(str(f_round(racetrackList[1])))
        self.txtRTRK_z.setText(str(f_round(racetrackList[2])))
        self.txtRTRK_csa.setText(str(f_round(racetrackList[3])))
        self.txtRTRK_cfm.setText(str(f_round(racetrackList[4])))

    def calculateElipses(self):

        # convert inputs to floats
        semimajor = convert2float(self.txtElipses_semimajor.text())
        semiminor = convert2float(self.txtElipses_semiminor.text())
        area = convert2float(self.txtElipses_csa.text())
        cfm = convert2float(self.txtElipses_circumference.text())

        elipseObject = ElipseCalc(semimajor, semiminor, area, cfm)
        elipseList = elipseObject.properties()

        qtTextList = [self.txtElipses_semimajor, self.txtElipses_semiminor,
                      self.txtElipses_csa]

        if elipseList[4] == True:
            requirements = [2, 3]
            warning_box(self, requirements)
            [i.setStyleSheet(self.errorFont[0]) for i in qtTextList]
        else:
            [i.setStyleSheet(self.errorFont[1]) for i in qtTextList]

        self.txtElipses_semimajor.setText(str(f_round(elipseList[0])))
        self.txtElipses_semiminor.setText(str(f_round(elipseList[1])))
        self.txtElipses_csa.setText(str(f_round(elipseList[2])))
        self.txtElipses_circumference.setText(str(f_round(elipseList[3])))

    def calculateRectangle(self):

        # convert inputs to floats
        rectangleX = convert2float(self.txtRectangleX.text())
        rectangleY = convert2float(self.txtRectangleY.text())
        rectangleR = convert2float(self.txtRectangleR.text())

        rectangleObject = RectangleCalc(rectangleX, rectangleY, rectangleR)
        rectangleList = rectangleObject.properties()

        qtTextList = [self.txtRectangleX, self.txtRectangleY,
                      self.txtRectangleR]

        if rectangleList[5] == True:
            requirements = [2, 3]
            warning_box(self, requirements)
            [i.setStyleSheet(self.errorFont[0]) for i in qtTextList]
        else:
            [i.setStyleSheet(self.errorFont[1]) for i in qtTextList]

        self.txtRectangleX.setText(str(f_round(rectangleList[0])))
        self.txtRectangleY.setText(str(f_round(rectangleList[1])))
        self.txtRectangleR.setText(str(f_round(rectangleList[2])))
        self.txtRectangleArea.setText(str(f_round(rectangleList[3])))
        self.txtRectangleCfm.setText(str(f_round(rectangleList[4])))

    def calculateConversions(self):

        # get inputs from conversion form tab
        # length
        iLength = convert2float(self.lineEditInputLength.text())
        iLengthFrom = self.comboBoxFromLength.currentText()
        iLengthTo = self.comboBoxToLength.currentText()

        # area
        iArea = convert2float(self.lineEditInputArea.text())
        iAreaFrom = self.comboBoxFromArea.currentText()
        iAreaTo = self.comboBoxToLength_2.currentText()

        # volume
        iVolume = convert2float(self.lineEditInputVolume.text())
        iVolumeFrom = self.comboBoxFromVolume.currentText()
        iVolumeTo = self.comboBoxToVolume.currentText()

        # mass
        iMass = convert2float(self.lineEditInputMass.text())
        iMassFrom = self.comboBoxFromMass.currentText()
        iMassTo = self.comboBoxToMass.currentText()

        # density
        iDensity = convert2float(self.lineEditInputDensity.text())
        iDensityFrom = self.comboBoxFromDensity.currentText()
        iDensityTo = self.comboBoxToDensity.currentText()

        # massflow
        iMassFlow = convert2float(self.lineEditInputMassFlow.text())
        iMassFlowFrom = self.comboBoxFromMassFlow.currentText()
        iMassFlowTo = self.comboBoxToMassFlow.currentText()

        # pass inputs to quantities calculator class

        oLength = convert_units(iLength, iLengthFrom, iLengthTo, "length", self.ureg)
        oArea = convert_units(iArea, iAreaFrom, iAreaTo, "area", self.ureg)
        oVolume = convert_units(iVolume, iVolumeFrom, iVolumeTo, "volume", self.ureg)
        oMass = convert_units(iMass, iMassFrom, iMassTo, "mass", self.ureg)
        oDensity = convert_units(iDensity, iDensityFrom, iDensityTo, "density", self.ureg)
        oMassFlow = convert_units(iMassFlow, iMassFlowFrom, iMassFlowTo, "massflow", self.ureg)

        self.lineEditOutputLength.setText(str(oLength))
        self.lineEditOutputArea.setText(str(oArea))
        self.lineEditOutputVolume.setText(str(oVolume))
        self.lineEditOutputMass.setText(str(oMass))
        self.lineEditOutputDensity.setText(str(oDensity))
        self.lineEditOutputMassFlow.setText(str(oMassFlow))


def warning_box(widget, requirements=[0, 0]):
    title = "Input Warning"
    item = []
    item.append(string.capwords(num2words(requirements[0])))
    item.append(num2words(requirements[1]))
    tabIndex = (QtGui.QTabWidget.currentIndex(widget.btnConversions))
    if tabIndex == 3:

        text = ("{} of the {} inputs must have values.\n\n"
                "Y must always have a value.\n"
                "\nThe remaing inputs must be set to 0.").format(item[0], item[1])

    else:
        text = ("{} of the {} inputs must have values.\n\n"
                "The remaing inputs must be set to 0.").format(item[0], item[1])

    warning = QtGui.QMessageBox.warning(widget,
                                       "About {}".format(title),
                                       text)
    return warning

