"""
This program is meant to be an interface for an old OSA, and will act as a digital replacement
using PascalCase for classes
using camelCase for variables, methods and functions
"""
import sys, pyqtgraph as pg, numpy as np
from PyQt6 import QtWidgets, uic  # For PyQt6: from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    """
    Qt interface, using Qt Designer .ui file
    Contain the OSA parameters and allow to interact with them as if using the physical one.
    """
    startWavelength = None
    endWavelength = None
    resolution = None
    isYAxisLog: bool = True

    def __init__(self):
        """
        Initialize the interface
        """
        super().__init__()
        # Load the .ui file
        uic.loadUi("OSA.ui", self)

        # Default values
        self.startWavelength = self.startWavelengthValue.value()
        self.endWavelength = self.endWavelengthValue.value()
        self.resolution = self.resolutionValue.value()
        self.isYAxisLog = True
        self.updatePointsNumber()
        # Default setup
        self.setupGraph()
        self.updateXAxis()
        self.updateYAxis()

        # Connect button click to a method
        self.startWavelengthButton.clicked.connect(self.setStartWavelength)
        self.endWavelengthButton.clicked.connect(self.setEndWavelength)
        self.resolutionButton.clicked.connect(self.setResolution)
        self.isYAxisLogButton.clicked.connect(self.updatePowerScale)


    # Methods
    def setStartWavelength(self):
        """
        Set the local startWavelength with the Interface's startWavelengthValue value,
        update the graph bound and the number of points,
        tell the user with a popup
        :return: Nothing
        """
        # getting interface value
        self.startWavelength = self.startWavelengthValue.value()
        # notifying the user
        QtWidgets.QMessageBox.information(self,"Update",
                                          "Start Wavelength set to {:.0f}.".format(self.startWavelength))
        # update the number of points and graph x-axis
        self.updatePointsNumber()
        self.updateXAxis()
    def setEndWavelength(self):
        """
        Set the local endWavelength with the Interface's endWavelengthValue value,
        update the graph bound and the number of points,
        tell the user with a popup
        :return: Nothing
        """
        # getting interface value
        self.endWavelength = self.endWavelengthValue.value()
        # notifying the user
        QtWidgets.QMessageBox.information(self, "Update",
                                          "Start Wavelength set to {:.0f}.".format(self.endWavelength))
        # update the number of points and graph x-axis
        self.updatePointsNumber()
        self.updateXAxis()
    def setResolution(self):
        """
        Set the local resolution with the Interface's resolutionValue value,
        tell the user with a popup
        :return: Nothing
        """
        # getting interface value
        self.resolution = self.resolutionValue.value()
        # notifying the user
        QtWidgets.QMessageBox.information(self,"Update",
                                          "Resolution set to {:.2f}.".format(self.resolution))
        self.updatePointsNumber()
    def updatePointsNumber(self):
        """
        Calculate the Number of point using the interval and resolution,
        tell the user with a popup
        :return: Nothing
        """
        # exiting if the interval is null of if division by zero
        if self.startWavelength == self.endWavelength or self.resolution == 0: return
        # n_points = interval / period between points
        pointsNumber = (self.endWavelength - self.startWavelength) / self.resolution
        self.pointsNumberValue.display(pointsNumber)
    def setupGraph(self):
        """
        Set up the graph
        :return: Nothing
        """
        self.spectre.setBackground("k")  # darK background
        pen = pg.mkPen(color=(101,255,0)) # orange (251,153,2) or green (101,255,0) curves
        self.spectre.setTitle("Spectrum")
        self.spectre.setLabel("left", "Power [dBm]")
        self.spectre.setLabel("bottom", "Wavelength [nm]")

        # test curve
        x = np.linspace(400, 410, 1000)
        y = 30 + 20 * np.sin((x - 400) * 2 * np.pi)
        self.curve = self.spectre.plot(x,y,pen = pen)
    def updateXAxis(self):
        """
        Update the X Axis of the spectrum graph (nm range)
        :return: nothing
        """
        self.spectre.setXRange(self.startWavelength, self.endWavelength)
    def updateYAxis(self):
        """
        Update the Y Axis of the spectrum graph (dBm range or pW / µW / mW)
        :return: nothing
        """
        if self.isYAxisLog:
            # Log mode (dBm)
            #self.spectre.setYRange(-210, 10)
            self.spectre.setLogMode(y = True)

            self.spectre.setLabel("left", "Power (dBm)")

        else:
            # Lin mode (Watts)
            #self.spectre.setYRange(0, 1e-3)
            self.spectre.setLogMode(y = False)
            self.spectre.setLabel("left", "Power (W)")
    def updatePowerScale(self):
        """
        Allow the user to update the power scale of the spectrum graph with a toggle (Log/Lin)
        :return: nothing
        """
        self.isYAxisLog = not self.isYAxisLog
        if self.isYAxisLog: self.isYAxisLogButton.setText("Press to change to Lin scale")
        else : self.isYAxisLogButton.setText("Press to change to Log scale")
        self.updateYAxis()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    print(window.isYAxisLog)
    sys.exit(app.exec())
