from PyQt5.QtWidgets import QApplication
import sys
from MainWindow import MainWindow




    
app = QApplication(sys.argv)
QApplication.setApplicationName("Chamodh's Browser")
window = MainWindow()
app.exec_()

