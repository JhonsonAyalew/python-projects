import sys,os

from PySide2 import QtGui, QtWidgets, QtCore
from pathlib import Path

from SplashScreen_ui import *
from Login import *

counter=0
class splash(QMainWindow):
    
        

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
       
    

    
        
        
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.Progress)
        

        self.timer.start(60)


        
    def Progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter>=100:
            self.timer.stop()
            self.ui.main = Login()
            self.ui.main.show()

        
        
            self.close()



        if counter==50:
            self.ui.loading_label.setText("Collecting requirment...")
            self.timer.start(1000)
        if counter==51:
            self.ui.loading_label.setText("Ready...")
            self.timer.start(100)
        if counter==80:
            self.ui.loading_label.setText("Ready...")
            self.timer.start(500)
        if counter==85:
            self.ui.loading_label.setText("Ready...")
            self.timer.start(20)
        if counter==98:
            self.ui.loading_label.setText("finishing...")
            self.timer.start(500)

        counter +=1
       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
   
    ########################################################################
    ## 
    ########################################################################
    window = splash()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
