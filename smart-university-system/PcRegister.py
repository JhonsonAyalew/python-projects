import sys,os

from PySide2 import QtGui, QtWidgets, QtCore
from pathlib import Path
import cv2
from PcRegister_ui import *
from SuperAdmin import *
from simple_facerec import *
import mysql.connector

sfr = SimpleFacerec()
sfr.load_encoding_images("data/")
Pc = "havepc"
counter=0

class PcRegister(QMainWindow):
    
        

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_PcRegister()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.addPhoto.clicked.connect(lambda:self.Face_reco())
        self.ui.save.clicked.connect(lambda:self.Save())
        self.ui.pushButton_6.clicked.connect(lambda:self.close())
        self.ui.back.clicked.connect(lambda:self.back_button())
        self.show_s()

        
        
        
        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
    def back_button(self):
        self.ui.main = SuperAdmin()
        self.ui.main.show()
        self.close()
    def close(self):
        counter =+ 1
        

    def Face_reco(self):
        start=None
        cap = cv2.VideoCapture(0)
        while True:
            ret, image = cap.read()
            face_locations, face_names = sfr.detect_known_faces(image)
            for face_loc, name in zip(face_locations, face_names):
                y1,x1,y2,x2 = face_loc[0],face_loc[1],face_loc[2],face_loc[3]
                print(name)
                if name =="unknown":
                    start=name
                    print(name)
                    
                else:
                    name_split=name.split(".")
                    start,t=[name1.strip() for name1 in name_split]
                    conn=mysql.connector.connect(host="localhost",user="root",password="jhon1995",database="ambo_university",auth_plugin="mysql_native_password")
                    my_cursor=conn.cursor() 
                    sql=my_cursor.execute(f"select first_name from register where username='{start}'")
                    First_name=my_cursor.fetchone()
                    First_name="+".join(First_name)
                    self.ui.first_name.setText(First_name)
                    sql=my_cursor.execute(f"select father_name from register where username='{start}'")
                    Father_name=my_cursor.fetchone()
                    Father_name="+".join(Father_name)
                    self.ui.father_name.setText(Father_name)
                    sql=my_cursor.execute(f"select grandfather_name from register where username='{start}'")
                    GFather_name=my_cursor.fetchone()
                    GFather_name="+".join(GFather_name)
                    self.ui.grandfather_name.setText(GFather_name)
                    sql=my_cursor.execute(f"select age from register where username='{start}'")
                    Age=my_cursor.fetchone()
                    Age="+".join(Age)
                    self.ui.age.setText(Age)
                    sql=my_cursor.execute(f"select DOB from register where username='{start}'")
                    DOB=my_cursor.fetchone()
                    DOB="+".join(DOB)
                    self.ui.DOB.setText(DOB)
                    sql=my_cursor.execute(f"select address from register where username='{start}'")
                    Address=my_cursor.fetchone()
                    Address="+".join(Address)
                    self.ui.address.setText(Address)
                    sql=my_cursor.execute(f"select nationality from register where username='{start}'")
                    Nationality=my_cursor.fetchone()
                    Nationality="+".join(Nationality)
                    self.ui.nationality.setText(Nationality)
                    sql=my_cursor.execute(f"select department from register where username='{start}'")
                    Department=my_cursor.fetchone()
                    Department="+".join(Department)
                    self.ui.department.setText(Department)
                    sql=my_cursor.execute(f"select gender from register where username='{start}'")
                    Gender=my_cursor.fetchone()
                    Gender="+".join(Gender)
                    self.ui.gender.setText(Gender)
                    sql=my_cursor.execute(f"select phone_number from register where username='{start}'")
                    Phone_number=my_cursor.fetchone()
                    Phone_number="+".join(Phone_number)
                    self.ui.phone_number.setText(Phone_number)
                    sql=my_cursor.execute(f"select username from register where username='{start}'")
                    Username=my_cursor.fetchone()
                    Username="+".join(Username)
                    self.ui.username.setText(Username)
                
                
                
     
            cv2.imshow("hghj",image)

            if cv2.waitKey(1)==13 or start != None:
                break
    def Save(self):
        self.db=mysql.connector.connect(host="localhost",user="root",password="jhon1995",database="ambo_university",auth_plugin="mysql_native_password")
        self.cur=self.db.cursor()

        first_name=self.ui.first_name.text()
        Last_name=self.ui.father_name.text()
        Username=self.ui.username.text()
        Grandfather_name=self.ui.grandfather_name.text()
        Pc_name=self.ui.pc_name.text()
        Serial_number=self.ui.serial_number.text()
        Age=self.ui.age.text()
        DOB=self.ui.DOB.text()
        Phone_no=self.ui.phone_number.text()
        Address=self.ui.address.text()
        Department=self.ui.department.text()
        Gender=self.ui.gender.text()
        Nationality=self.ui.nationality.text()
        Username=self.ui.username.text()

        if (first_name==""):
            self.face_reco()
        else:
            
           

            self.cur.execute('''INSERT INTO pcregister (first_name,father_name,grandfather_name,pc_name,serial_number,username,age,DOB,department,gender,phone_number,address) 
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                (first_name,Last_name,Grandfather_name,Pc_name,Serial_number,Username,Age,DOB,Department,Gender,Phone_no,Address))
            self.db.commit()
            name="wow"
            self.cur.execute("update register set pc=%s where username=%s",(name,Username,))
            self.cur.fetchone()
            self.db.commit()
            self.show_s()
                    
                    
            self.statusBar().showMessage("  |  You Are Successfully Added Data  |  ")
    def selectionChanged(self):
        selected_row=self.selectedRowId()
        id_name=self.ui.tableWidget.item(selected_row,0).text()
        first_name=self.ui.tableWidget.item(selected_row,1).text()
        last_name=self.ui.tableWidget.item(selected_row,2).text()
        self.ui.First_name.setText(first_name)
        self.ui.Last_name.setText(last_name)
        
    def selectedRowId(self):
        return self.ui.tableWidget.currentRow()
    def show_s(self):
        
        self.conn=mysql.connector.connect(host="localhost",user="root",password="jhon1995",database="ambo_university",auth_plugin="mysql_native_password")
        self.my_cursor=self.conn.cursor()
        self.my_cursor.execute("select * from pcregister")
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
        
    
        
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
   
    ########################################################################
    ## 
    ########################################################################
    window = PcRegister()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
