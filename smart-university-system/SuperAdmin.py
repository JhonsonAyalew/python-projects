import sys,os

from PySide2 import QtGui, QtWidgets, QtCore
from pathlib import Path

from SuperAdmin_ui import *

from Register import *
from PcRegister import *

class SuperAdmin(QMainWindow):
    
        

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_SuperAdmin()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.home.clicked.connect(lambda:self.home())
        self.ui.register_3.clicked.connect(lambda:self.register())
        self.ui.face_recognition.clicked.connect(lambda:self.face_recognition())
        self.ui.register_button.clicked.connect(lambda:self.register_student())
        self.ui.PC_button.clicked.connect(lambda:self.register_pc())
        self.ui.close.clicked.connect(lambda:self.close_button())
        self.shadow=QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(35)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(5)
        self.shadow.setColor(QColor(20, 27, 45,250))
        self.ui.vehicle_button.setGraphicsEffect(self.shadow)
        #shadow _one
        self.shadow_one=QGraphicsDropShadowEffect(self)
        self.shadow_one.setBlurRadius(35)
        self.shadow_one.setXOffset(0)
        self.shadow_one.setYOffset(5)
        self.shadow_one.setColor(QColor(20, 27, 45,250))
        self.ui.register_button.setGraphicsEffect(self.shadow_one)
        #shadow _two
        self.shadow_two=QGraphicsDropShadowEffect(self)
        self.shadow_two.setBlurRadius(35)
        self.shadow_two.setXOffset(0)
        self.shadow_two.setYOffset(5)
        self.shadow_two.setColor(QColor(20, 27, 45,250))
        self.ui.Admin_button.setGraphicsEffect(self.shadow_two)
        #shadow _three
        self.shadow_three=QGraphicsDropShadowEffect(self)
        self.shadow_three.setBlurRadius(35)
        self.shadow_three.setXOffset(0)
        self.shadow_three.setYOffset(5)
        self.shadow_three.setColor(QColor(20, 27, 45,250))
        self.ui.fasting_button.setGraphicsEffect(self.shadow_three)
        #shadow _one
        self.shadow_four=QGraphicsDropShadowEffect(self)
        self.shadow_four.setBlurRadius(35)
        self.shadow_four.setXOffset(0)
        self.shadow_four.setYOffset(5)
        self.shadow_four.setColor(QColor(20, 27, 45,250))
        self.ui.fasting_button.setGraphicsEffect(self.shadow_four)
        #shadow _three
        self.shadow_five=QGraphicsDropShadowEffect(self)
        self.shadow_five.setBlurRadius(35)
        self.shadow_five.setXOffset(0)
        self.shadow_five.setYOffset(5)
        self.shadow_five.setColor(QColor(20, 27, 45,250))
        self.ui.PC_button.setGraphicsEffect(self.shadow_five)
        #shadow _one
        self.shadow_six=QGraphicsDropShadowEffect(self)
        self.shadow_six.setBlurRadius(35)
        self.shadow_six.setXOffset(0)
        self.shadow_six.setYOffset(5)
        self.shadow_six.setColor(QColor(20, 27, 45,250))
        self.ui.servant_button.setGraphicsEffect(self.shadow_six)
        
        
       
    

    
        
        
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        self.ui.menu_button.clicked.connect(lambda:self.main())
        self.ui.left_mini_bar.setMaximumSize(QSize(0, 16777215))
        self.ui.left_bar.setMaximumSize(QSize(150, 16777215))
    global one
    def close_button(self):
        self.close()
    def mousePressEvent(self, event):
        self.oldPosition=event.globalPos()
    def mouseMoveEvent(self,event):
        delta=QPoint(event.globalPos()-self.oldPosition)
        self.move(self.x()+delta.x(),self.y()+delta.y())
        self.oldPosition=event.globalPos()
    def main(self):
        width = self.ui.left_mini_bar.width()
        left_width = self.ui.left_bar.width()
        print(width)

        if width == 50:
            self.ui.left_mini_bar.setMaximumSize(QSize(0, 16777215))
            self.ui.left_bar.setMaximumSize(QSize(150, 16777215))
            newWidth = 0
            newleft_width = 150
        else:
            self.ui.left_mini_bar.setMaximumSize(QSize(50, 16777215))
            self.ui.left_bar.setMaximumSize(QSize(0, 16777215))
            newWidth = 50
            newleft_width = 0
        self.animation = QPropertyAnimation(self.ui.left_mini_bar, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def home(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def register(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def face_recognition(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def register_student(self):
        self.ui.main = Register()
        self.ui.main.show()
        self.close()
    def register_pc(self):
        self.ui.main = PcRegister()
        self.ui.main.show()
        self.close()

            
            

        




       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
   
    ########################################################################
    ## 
    ########################################################################
    window = SuperAdmin()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
