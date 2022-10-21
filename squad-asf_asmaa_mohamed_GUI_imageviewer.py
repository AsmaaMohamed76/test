from PyQt5.QtWidgets import QMainWindow , QApplication,QPushButton,QLabel,QFileDialog
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
 
import sys
class UI(QMainWindow):
    def __init__(self):
        super(UI , self).__init__()
        #load ui file
        uic.loadUi("image_viewer.ui", self)
        #define our widets
        self.button = self.findChild(QPushButton,"pushButton")
        self.label = self.findChild(QLabel,"label")
        #click the box
        self.button.clicked.connect(self.clicker)
        #show App
        self.show()
        
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self,"Open File","c:\\Gui\\images","All Files(*);;PNG Files(*.png);;Jpg Files(*.jpg)")    
        #open the image
        self.pixmap =QPixmap(fname[0])
        #add picture
        self.label.setPixmap(self.pixmap)
#initalize the app    
app = QApplication(sys.argv) 
UIWindow = UI()  

app.exec_()