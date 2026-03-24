import sys
from PyQt6 import QtWidgets, uic  # For PyQt6: from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the .ui file
        uic.loadUi("OSA.ui", self)

        # Connect button click to a method
        self.WVL1_Button.clicked.connect(self.WVL1_set)
        self.WVL2_Button.clicked.connect(self.WVL2_set)
        self.Resolution_Button.clicked.connect(self.Resolution_set)


    def WVL1_set(self):
        val = self.WVL1.value()  # récupérer la valeur
        QtWidgets.QMessageBox.information(
            self,
            "Action Triggered",
            "Start Wavelength set to {}.".format(val)
        )
        self.Nb_Points_Set()
    def WVL2_set(self):
        val = self.WVL2.value()  # récupérer la valeur
        QtWidgets.QMessageBox.information(
            self,
            "Action Triggered",
            "End Wavelength set to {}.".format(val)
        )
        self.Nb_Points_Set()
    def Resolution_set(self):
        val = self.Resolution.value()  # récupérer la valeur
        QtWidgets.QMessageBox.information(
            self,
            "Action Triggered",
            "End Wavelength set to {}.".format(val)
        )
        self.Nb_Points_Set()
    def Nb_Points_Set(self):
        WVL1_value = self.WVL1.value()
        WVL2_value = self.WVL2.value()
        Resolution_value = self.Resolution.value()
        if not WVL1_value == WVL2_value or Resolution_value == 0:
            N_Points = (WVL2_value - WVL1_value)/Resolution_value
            self.NbPoints.display(N_Points)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # For PyQt6: sys.exit(app.exec())
