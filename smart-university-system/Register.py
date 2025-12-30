import sys,os
import cv2
from PySide2 import QtGui, QtWidgets, QtCore
from pathlib import Path

from Register_ui import *

import mysql.connector

class Register(QMainWindow):
    
        

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.show_s()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.save.clicked.connect(lambda:self.save())
        self.ui.addPhoto.clicked.connect(lambda:self.photo())
        self.ui.tableWidget.itemSelectionChanged.connect(self.selectionChanged)
        
       
    

    
        
        
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
    def photo(self):
        Username=username=self.ui.username.text()
        face_Classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_Classifier.detectMultiScale(gray,1.1,3)
            for(x,y,w,h) in faces:
                face_cropped=img[y:y+h,x:x+w]
                return face_cropped
        cap=cv2.VideoCapture(0)
        img_id=0
        while True:
            ret,my_frame=cap.read()
            if face_cropped(my_frame) is not None:
                global file_name_path
                img_id+=1
                face=cv2.resize(face_cropped(my_frame),(450,450))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path="data/student/"+f"{Username}.{img_id}"+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.imshow("crooped Face",face)
            if cv2.waitKey(1)==13 or int(img_id)==1:
                break
        cap.release()
        cv2.destroyAllWindows()

    def show_s(self):
        
        self.conn=mysql.connector.connect(host="localhost",user="root",password="jhon1995",database="ambo_university",auth_plugin="mysql_native_password")
        self.my_cursor=self.conn.cursor()
        self.my_cursor.execute("select * from register")
        data1=self.my_cursor.fetchall()

        

        if data1:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.insertRow(0)
            for row, form in enumerate(data1):
                self.ui.tableWidget.insertRow(row)
                for column, item in enumerate(form):
                    self.ui.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
                    column+=1
                row_position=self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_position)


    def save(self):

        self.db=mysql.connector.connect(host="localhost",user="root",password="jhon1995",database="ambo_university",auth_plugin="mysql_native_password")
        self.cur=self.db.cursor()

        first_name=self.ui.First_name.text()
        Last_name=self.ui.Last_name.text()
        Username=self.ui.username.text()
        Grandfather_name=self.ui.grandfather_name.text()
        Age=self.ui.age.text()
        DOB=self.ui.DOB.text()
        Phone_no=self.ui.phone_number.text()
        Address=self.ui.address.text()
        Department=self.ui.department.currentText()
        Gender=self.ui.gender.currentText()
        Nationality=self.ui.nationality.text()
        photo=file_name_path
        
        
        if (first_name==""):
            self.face_reco()
        else:
            
           

            self.cur.execute('''INSERT INTO register (first_name,father_name,grandfather_name,username,age,DOB,department,gender,photo,phone_number,nationality,address) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                (first_name,Last_name,Grandfather_name,Username,Age,DOB,Department,Gender,photo,Phone_no,Nationality,Address))
            self.db.commit()
            self.statusBar().showMessage("  |  You Are Successfully Added Data  |  ")
            
            
        

            self.show_s()

    def selectionChanged(self):
        selected_row=self.selectedRowId()
        id_name=self.ui.tableWidget.item(selected_row,0).text()
        first_name=self.ui.tableWidget.item(selected_row,1).text()
        last_name=self.ui.tableWidget.item(selected_row,2).text()
        self.ui.First_name.setText(first_name)
        self.ui.Last_name.setText(last_name)
        
    def selectedRowId(self):
        return self.ui.tableWidget.currentRow()

        
      



       
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
   
    ########################################################################
    ## 
    ########################################################################
    window = Register()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
