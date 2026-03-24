import sys
from PyQt6 import QtWidgets, uic  # For PyQt6: from PyQt6 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    WVL1_val = None
    WVL2_val = None
    Resolution_val = None

    def __init__(self):
        super().__init__()
        # Load the .ui file
        uic.loadUi("OSA.ui", self)

        # Default values
        self.WVL1_val = self.WVL1.value()
        self.WVL2_val = self.WVL2.value()
        self.Resolution_val = self.Resolution.value()
        self.Nb_Points_Set()

        # Connect button click to a method
        self.WVL1_Button.clicked.connect(self.WVL1_set)
        self.WVL2_Button.clicked.connect(self.WVL2_set)
        self.Resolution_Button.clicked.connect(self.Resolution_set)


    def WVL1_set(self):
        self.WVL1_val = self.WVL1.value()  # récupérer la valeur
        QtWidgets.QMessageBox.information(
            self,
            "Action Triggered",
            "Start Wavelength set to {:.0f}.".format(self.WVL1_val)
        )
        self.Nb_Points_Set()
    def WVL2_set(self):
        self.WVL2_val = self.WVL2.value()  # récupérer la valeur
        QtWidgets.QMessageBox.information(
            self,
            "Action Triggered",
            "End Wavelength set to {:.0f}.".format(self.WVL2_val)
        )
        self.Nb_Points_Set()
    def Resolution_set(self):
        self.Resolution_val = self.Resolution.value()  # récupérer la valeur
        QtWidgets.QMessageBox.information(
            self,
            "Action Triggered",
            "End Wavelength set to {:.2f}.".format(self.Resolution_val)
        )
        self.Nb_Points_Set()
    def Nb_Points_Set(self):
        if self.WVL1_val == self.WVL2_val or self.Resolution_val == 0: return

        N_Points = (self.WVL2_val - self.WVL1_val)/self.Resolution_val
        self.NbPoints.display(N_Points)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # For PyQt6: sys.exit(app.exec())
