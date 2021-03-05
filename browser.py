from PyQt5.QtWidgets import QApplication
import sys
from MainWindow import MainWindow




    
app = QApplication(sys.argv)
QApplication.setApplicationName("ChaBrow")
window = MainWindow()
app.exec_()

