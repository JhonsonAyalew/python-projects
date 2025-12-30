# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PcRegister.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PcRegister(object):
    def setupUi(self, PcRegister):
        if not PcRegister.objectName():
            PcRegister.setObjectName(u"PcRegister")
        PcRegister.resize(1027, 661)
        self.centralwidget = QWidget(PcRegister)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(23, 31, 53);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(238, 238, 238);\n"
"font: 9pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 25))
        self.pushButton_3.setStyleSheet(u"QPushButton{border-style:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 71, 89);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../minimizeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.pushButton_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 25))
        self.pushButton_4.setStyleSheet(u"QPushButton{border-style:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 71, 89);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../maximizeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.pushButton_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(40, 25))
        self.pushButton_5.setStyleSheet(u"QPushButton{border-style:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(187, 73, 51);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../closeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(12, 12))

        self.horizontalLayout_4.addWidget(self.pushButton_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"background-color: rgb(20, 27, 45);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_22 = QWidget(self.widget_5)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.back = QLabel(self.widget_22)
        self.back.setObjectName(u"back")
        self.back.setMaximumSize(QSize(25, 15))
        self.back.setPixmap(QPixmap(u"images/menuicon.png"))
        self.back.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.back)


        self.horizontalLayout_6.addWidget(self.widget_22, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_23 = QWidget(self.widget_5)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy1)
        self.horizontalLayout_31 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_2 = QLabel(self.widget_23)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u"images/computerIcon (1).png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.widget_23)


        self.verticalLayout_2.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.widget_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 200))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(9, -1, -1, 0)
        self.frame_9 = QFrame(self.frame_22)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.addPhoto = QPushButton(self.frame_10)
        self.addPhoto.setObjectName(u"addPhoto")
        self.addPhoto.setMinimumSize(QSize(300, 0))
        self.addPhoto.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(0, 117, 175, 255));\n"
"padding-top:10;\n"
"padding-bottom:10;\n"
"padding-left:50;\n"
"padding-right:50;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.verticalLayout_3.addWidget(self.addPhoto)


        self.horizontalLayout_7.addWidget(self.frame_10, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_7.addWidget(self.frame_11, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_22)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_13, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.pc_name = QLineEdit(self.frame_22)
        self.pc_name.setObjectName(u"pc_name")
        self.pc_name.setMinimumSize(QSize(300, 30))
        self.pc_name.setMaximumSize(QSize(200, 16777215))
        self.pc_name.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.pc_name)

        self.serial_number = QLineEdit(self.frame_22)
        self.serial_number.setObjectName(u"serial_number")
        self.serial_number.setMinimumSize(QSize(300, 30))
        self.serial_number.setMaximumSize(QSize(200, 16777215))
        self.serial_number.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.serial_number)

        self.frame_17 = QFrame(self.frame_22)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_18.addWidget(self.frame_18, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_23)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_18.addWidget(self.frame_23, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.frame_8 = QFrame(self.frame_22)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_15, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_8)


        self.horizontalLayout_10.addWidget(self.frame_22, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_8 = QWidget(self.widget_3)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_8)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_11 = QVBoxLayout(self.widget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_19.addWidget(self.label_3)

        self.first_name = QLabel(self.widget_11)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_19.addWidget(self.first_name)


        self.verticalLayout_11.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_9)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_4 = QLabel(self.widget_12)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_20.addWidget(self.label_4)

        self.father_name = QLabel(self.widget_12)
        self.father_name.setObjectName(u"father_name")
        self.father_name.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_20.addWidget(self.father_name)


        self.verticalLayout_11.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_9)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_5 = QLabel(self.widget_13)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_21.addWidget(self.label_5)

        self.grandfather_name = QLabel(self.widget_13)
        self.grandfather_name.setObjectName(u"grandfather_name")
        self.grandfather_name.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_21.addWidget(self.grandfather_name)


        self.verticalLayout_11.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_9)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_6 = QLabel(self.widget_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_22.addWidget(self.label_6)

        self.age = QLabel(self.widget_14)
        self.age.setObjectName(u"age")
        self.age.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_22.addWidget(self.age)


        self.verticalLayout_11.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_8 = QLabel(self.widget_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_24.addWidget(self.label_8)

        self.DOB = QLabel(self.widget_15)
        self.DOB.setObjectName(u"DOB")
        self.DOB.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_24.addWidget(self.DOB)


        self.verticalLayout_11.addWidget(self.widget_15)

        self.widget_21 = QWidget(self.widget_9)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_14 = QLabel(self.widget_21)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_30.addWidget(self.label_14)

        self.username = QLabel(self.widget_21)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_30.addWidget(self.username)


        self.verticalLayout_11.addWidget(self.widget_21)


        self.horizontalLayout_12.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_14 = QVBoxLayout(self.widget_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_17 = QWidget(self.widget_10)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_10 = QLabel(self.widget_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_26.addWidget(self.label_10)

        self.address = QLabel(self.widget_17)
        self.address.setObjectName(u"address")
        self.address.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_26.addWidget(self.address)


        self.verticalLayout_14.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.widget_10)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_9 = QLabel(self.widget_16)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_25.addWidget(self.label_9)

        self.nationality = QLabel(self.widget_16)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_25.addWidget(self.nationality)


        self.verticalLayout_14.addWidget(self.widget_16)

        self.widget_19 = QWidget(self.widget_10)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_12 = QLabel(self.widget_19)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_28.addWidget(self.label_12)

        self.department = QLabel(self.widget_19)
        self.department.setObjectName(u"department")
        self.department.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_28.addWidget(self.department)


        self.verticalLayout_14.addWidget(self.widget_19)

        self.widget_18 = QWidget(self.widget_10)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_11 = QLabel(self.widget_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_27.addWidget(self.label_11)

        self.gender = QLabel(self.widget_18)
        self.gender.setObjectName(u"gender")
        self.gender.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_27.addWidget(self.gender)


        self.verticalLayout_14.addWidget(self.widget_18)

        self.widget_20 = QWidget(self.widget_10)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_13 = QLabel(self.widget_20)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_29.addWidget(self.label_13)

        self.phone_number = QLabel(self.widget_20)
        self.phone_number.setObjectName(u"phone_number")
        self.phone_number.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_29.addWidget(self.phone_number)


        self.verticalLayout_14.addWidget(self.widget_20)


        self.horizontalLayout_12.addWidget(self.widget_10)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.widget_7 = QWidget(self.widget_3)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.widget_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout_4.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.widget_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"\n"
"border-radius:10")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setSpacing(40)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.save = QPushButton(self.frame_16)
        self.save.setObjectName(u"save")
        self.save.setStyleSheet(u"background-color: rgb(30, 41, 70);\n"
"color: rgb(208, 208, 208);\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"border-radius:17;\n"
"font: 10pt \"arial\";")

        self.horizontalLayout_13.addWidget(self.save)

        self.pushButton_6 = QPushButton(self.frame_16)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"background-color: rgb(30, 41, 70);\n"
"color: rgb(208, 208, 208);\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"border-radius:17;\n"
"font: 10pt \"arial\";")

        self.horizontalLayout_13.addWidget(self.pushButton_6)

        self.delete_2 = QPushButton(self.frame_16)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setStyleSheet(u"background-color: rgb(30, 41, 70);\n"
"color: rgb(208, 208, 208);\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"border-radius:17;\n"
"font: 10pt \"arial\";")

        self.horizontalLayout_13.addWidget(self.delete_2)


        self.verticalLayout_4.addWidget(self.frame_16)


        self.verticalLayout_2.addWidget(self.widget_7, 0, Qt.AlignBottom)


        self.horizontalLayout_5.addWidget(self.widget_3, 0, Qt.AlignLeft)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.frame_20 = QFrame(self.widget_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_20)
        self.verticalLayout_12.setSpacing(50)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_20)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 0))
        self.frame_24.setStyleSheet(u"margin:0;\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_97 = QFrame(self.frame_24)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_97)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(50, 50))
        self.label_55.setMaximumSize(QSize(50, 50))
        self.label_55.setStyleSheet(u"border-radius:25;\n"
"border-style:solid;\n"
"border-width:1;\n"
"border-color: rgb(255, 255, 255);\n"
"padding:6;")
        self.label_55.setPixmap(QPixmap(u"images/amboLogo.PNG"))
        self.label_55.setScaledContents(True)

        self.horizontalLayout_54.addWidget(self.label_55)

        self.frame_93 = QFrame(self.frame_97)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_93)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(9, 0, -1, 5)
        self.frame_94 = QFrame(self.frame_93)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 0))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_94)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_94)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 10pt \"arial black\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.verticalLayout_46.addWidget(self.label_35)

        self.label_51 = QLabel(self.frame_94)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"font: 10pt \"arial\";\n"
"margin:0;")

        self.verticalLayout_46.addWidget(self.label_51)


        self.verticalLayout_43.addWidget(self.frame_94)


        self.horizontalLayout_54.addWidget(self.frame_93)


        self.horizontalLayout_17.addWidget(self.frame_97)

        self.frame_83 = QFrame(self.frame_24)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_53.setSpacing(15)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 15, 0)
        self.lineEdit_2 = QLineEdit(self.frame_83)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(250, 0))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(30, 41, 70);\n"
"padding:10;\n"
"padding-left:20;\n"
"border-radius:17;\n"
"color: rgb(255, 255, 255);\n"
"border-style:none;\n"
"border-width:1;\n"
"border-color: rgb(220, 220, 220);")
        self.lineEdit_2.setText(u"Search by content")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_53.addWidget(self.lineEdit_2, 0, Qt.AlignRight)


        self.horizontalLayout_17.addWidget(self.frame_83, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_21)
        if (self.tableWidget.columnCount() < 14):
            self.tableWidget.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"\n"
"\n"
"\n"
"QHeaderView::section{\n"
"height:40px;\n"
"	\n"
"	background-color: rgb(17, 24, 40);\n"
"border-top:0px solid 4181C0;\n"
"border-bottom:0px solid 4181C0;\n"
"border-right:0px solid 4181C0;\n"
"border-left:0px solid 4181C0;\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"arial\";\n"
"\n"
"}\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border:0px solid;\n"
"background-color: rgb(30, 41, 70);\n"
"border-radius:0;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"margin:0;\n"
"")

        self.horizontalLayout_15.addWidget(self.tableWidget)


        self.verticalLayout_12.addWidget(self.frame_21)


        self.horizontalLayout_16.addWidget(self.frame_20)


        self.horizontalLayout_5.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        PcRegister.setCentralWidget(self.centralwidget)

        self.retranslateUi(PcRegister)

        QMetaObject.connectSlotsByName(PcRegister)
    # setupUi

    def retranslateUi(self, PcRegister):
        PcRegister.setWindowTitle(QCoreApplication.translate("PcRegister", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("PcRegister", u"Hachalu Hundesa Campus Gate Detection", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.back.setText("")
        self.label_2.setText("")
        self.addPhoto.setText(QCoreApplication.translate("PcRegister", u"Add Photo", None))
        self.pc_name.setPlaceholderText(QCoreApplication.translate("PcRegister", u"Enter Pc Name", None))
        self.serial_number.setPlaceholderText(QCoreApplication.translate("PcRegister", u"Enter Serial Number", None))
        self.label_3.setText(QCoreApplication.translate("PcRegister", u"First Name :", None))
        self.first_name.setText("")
        self.label_4.setText(QCoreApplication.translate("PcRegister", u"Father Name :", None))
        self.father_name.setText("")
        self.label_5.setText(QCoreApplication.translate("PcRegister", u"G/father Name :", None))
        self.grandfather_name.setText("")
        self.label_6.setText(QCoreApplication.translate("PcRegister", u"Age:", None))
        self.age.setText("")
        self.label_8.setText(QCoreApplication.translate("PcRegister", u"DOB:", None))
        self.DOB.setText("")
        self.label_14.setText(QCoreApplication.translate("PcRegister", u"Username :", None))
        self.username.setText("")
        self.label_10.setText(QCoreApplication.translate("PcRegister", u"Adress:", None))
        self.address.setText("")
        self.label_9.setText(QCoreApplication.translate("PcRegister", u"Nationality:", None))
        self.nationality.setText("")
        self.label_12.setText(QCoreApplication.translate("PcRegister", u"Department:", None))
        self.department.setText("")
        self.label_11.setText(QCoreApplication.translate("PcRegister", u"Gender:", None))
        self.gender.setText("")
        self.label_13.setText(QCoreApplication.translate("PcRegister", u"Phone Number:", None))
        self.phone_number.setText("")
        self.save.setText(QCoreApplication.translate("PcRegister", u"Save", None))
        self.pushButton_6.setText(QCoreApplication.translate("PcRegister", u"Update", None))
        self.delete_2.setText(QCoreApplication.translate("PcRegister", u"Delete", None))
        self.label_55.setText("")
        self.label_35.setText(QCoreApplication.translate("PcRegister", u"Face Recognition and other", None))
        self.label_51.setText(QCoreApplication.translate("PcRegister", u"Face Recognition and other", None))
        self.lineEdit_2.setInputMask("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PcRegister", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PcRegister", u"First Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PcRegister", u"Father Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PcRegister", u"G/father Name", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PcRegister", u"PC Name", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PcRegister", u"Serial Number", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PcRegister", u"Username", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PcRegister", u"Age", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("PcRegister", u"DOB", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("PcRegister", u"Department", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("PcRegister", u"Gender", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("PcRegister", u"Photo", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("PcRegister", u"Phone Number", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("PcRegister", u"Address", None));
    # retranslateUi

