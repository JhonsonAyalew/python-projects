import sys,os

from PySide2 import QtGui, QtWidgets, QtCore
from pathlib import Path

from CarRegister_ui import *


counter=0
class carRegister(QMainWindow):
    
        

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_CarRegister()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
       
    

    
        
        
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

      
       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
   
    ########################################################################
    ## 
    ########################################################################
    window = carRegister()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
