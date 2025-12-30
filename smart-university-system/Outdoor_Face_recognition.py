import sys,os

from PySide2 import QtGui, QtWidgets, QtCore
from pathlib import Path
import cv2
from Outdoor_Face_recognition_ui import *
from button_control import *

class Outdoor_Face_recognition(QMainWindow):
    
        

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Outdoor_Face_recognition()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.All_camera.setStyleSheet(u"QPushButton{border-style:solid;\n""border-color: rgb(0, 128, 192);\n""border-width:1;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n"
"padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
    
        self.ui.All_camera.clicked.connect(lambda:self.All())
        self.ui.weapon_camera.clicked.connect(lambda:self.weapon())
        self.ui.pc_camera.clicked.connect(lambda:self.pc())
        self.ui.vechile_camera.clicked.connect(lambda:self.vechile())
        self.ui.face_cmera.clicked.connect(lambda:self.face())

        
       
    

    
        
        
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        self.face_recog()
    def All(self):
        width = self.ui.face_recognition_widget.width()
        width1 = self.ui.pc_recognition_widget.width()
        width2 = self.ui.vechile_recognition_widget.width()
        width3 = self.ui.weapon_detection_widget.width()
        if width == 0:
            self.ui.face_recognition_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.pc_recognition_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.vechile_recognition_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.weapon_detection_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.widget_20.setMaximumSize(QSize(54358452, 54358452))
            self.ui.widget_22.setMaximumSize(QSize(54358452, 54358452))
            self.ui.All_camera.setStyleSheet(u"QPushButton{border-style:solid;\n""border-color: rgb(0, 128, 192);\n""border-width:1;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n"
"padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
    
   
        else:
            self.ui.face_recognition_widget.setMaximumSize(QSize(0, 0))
            self.ui.pc_recognition_widget.setMaximumSize(QSize(0, 0))
            self.ui.vechile_recognition_widget.setMaximumSize(QSize(0, 0))
            self.ui.weapon_detection_widget.setMaximumSize(QSize(0, 0))
            self.ui.widget_20.setMaximumSize(QSize(0, 0))
            self.ui.widget_22.setMaximumSize(QSize(0, 0))
            self.ui.All_camera.setStyleSheet(u"QPushButton{border-style:none;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n""padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
             
    def weapon(self):
        width3 = self.ui.weapon_detection_widget.width()
        if width3 == 0:
            self.ui.weapon_detection_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.widget_22.setMaximumSize(QSize(5845, 5454))

            self.ui.weapon_camera.setStyleSheet(u"QPushButton{border-style:solid;\n""border-color: rgb(0, 128, 192);\n""border-width:1;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n"
"padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
        else:
            width2 = self.ui.pc_recognition_widget.width()
            if width2 == 0:
                self.ui.widget_22.setMaximumSize(QSize(0, 0))
            else:
                pass

            self.ui.weapon_detection_widget.setMaximumSize(QSize(0, 0))

            self.ui.weapon_camera.setStyleSheet(u"QPushButton{border-style:none;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n""padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")

    def pc(self):
        width3 = self.ui.pc_recognition_widget.width()
        if width3 == 0:
            self.ui.pc_recognition_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.widget_22.setMaximumSize(QSize(5845, 5454))

            self.ui.pc_camera.setStyleSheet(u"QPushButton{border-style:solid;\n""border-color: rgb(0, 128, 192);\n""border-width:1;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n"
"padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
        else:
            width2 = self.ui.weapon_detection_widget.width()
            if width2 == 0:
                self.ui.widget_22.setMaximumSize(QSize(0, 0))
            else:
                pass

            self.ui.pc_recognition_widget.setMaximumSize(QSize(0, 0))

            self.ui.pc_camera.setStyleSheet(u"QPushButton{border-style:none;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n""padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")

    def vechile(self):
        width3 = self.ui.vechile_recognition_widget.width()
        if width3 == 0:
            self.ui.vechile_recognition_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.widget_20.setMaximumSize(QSize(5845, 5454))

            self.ui.vechile_camera.setStyleSheet(u"QPushButton{border-style:solid;\n""border-color: rgb(0, 128, 192);\n""border-width:1;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n"
"padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
        else:
            width2 = self.ui.face_recognition_widget.width()
            if width2 == 0:
                self.ui.widget_20.setMaximumSize(QSize(0, 0))
            else:
                pass

            self.ui.vechile_recognition_widget.setMaximumSize(QSize(0, 0))

            self.ui.vechile_camera.setStyleSheet(u"QPushButton{border-style:none;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n""padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")

    def face(self):
        width3 = self.ui.face_recognition_widget.width()
        if width3 == 0:
            self.ui.face_recognition_widget.setMaximumSize(QSize(5465, 5465))
            self.ui.widget_20.setMaximumSize(QSize(5845, 5454))

            self.ui.face_cmera.setStyleSheet(u"QPushButton{border-style:solid;\n""border-color: rgb(0, 128, 192);\n""border-width:1;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n"
"padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")
        else:
            width2 = self.ui.vechile_recognition_widget.width()
            if width2 == 0:
                self.ui.widget_20.setMaximumSize(QSize(0, 0))
            else:
                pass

            self.ui.face_recognition_widget.setMaximumSize(QSize(0, 0))

            self.ui.face_cmera.setStyleSheet(u"QPushButton{border-style:none;\n""background-color: rgb(33, 44, 76);\n""padding-top:7;\n""padding-bottom:7;\n""padding-left:20;\n""padding-right:20;\n""font: 75 9pt \"Arial\";\n""color: rgb(255, 255, 255);\n""border-radius:4\n""}\n""QPushButton::hover{\n""background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n""}")

    

    

    





    def face_recog(self):
        
        
        cap1 = cv2.VideoCapture(0)
        cap2 = cv2.VideoCapture(0)
        while True:
            ret1, self.image = cap1.read()
            ret2, self.image1 = cap1.read()
            ret2, self.image2 = cap1.read()
            ret2, self.image3 = cap1.read()
            
            
            self.setPhoto(self.image)
            self.setPhoto1(self.image1)
            self.setPhoto2(self.image2)
            self.setPhoto3(self.image3)
            
     
            

            if cv2.waitKey(1)==13:
                break
        
    def setPhoto(self,image):
        
        
        self.tmp=image

        
            
            
        


        frame=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        newframe = cv2.resize(frame,(100,100))
        
        image=QImage(newframe,newframe.shape[1],newframe.shape[0],newframe.strides[0],QImage.Format_RGB888)
        self.ui.label_12.setPixmap(QtGui.QPixmap.fromImage(image))
    def setPhoto1(self,image1):
        
        
        self.tmp=image1
        
            
            
        


        frame1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
        
        image1=QImage(frame1,frame1.shape[1],frame1.shape[0],frame1.strides[0],QImage.Format_RGB888)
        self.ui.label_13.setPixmap(QtGui.QPixmap.fromImage(image1))

    def setPhoto2(self,image2):
        
        
        self.tmp=image2
        
            
            
        


        frame2=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
        
        image2=QImage(frame2,frame2.shape[1],frame2.shape[0],frame2.strides[0],QImage.Format_RGB888)
        self.ui.label_16.setPixmap(QtGui.QPixmap.fromImage(image2))

    def setPhoto3(self,image3):
        
        
        self.tmp=image3
        
            
            
        


        frame3=cv2.cvtColor(image3,cv2.COLOR_BGR2RGB)
        
        image3=QImage(frame3,frame3.shape[1],frame3.shape[0],frame3.strides[0],QImage.Format_RGB888)
        self.ui.label_17.setPixmap(QtGui.QPixmap.fromImage(image3))

   

       
if __name__ == "__main__":
    app = QApplication(sys.argv)
   
    ########################################################################
    ## 
    ########################################################################
    window = Outdoor_Face_recognition()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
