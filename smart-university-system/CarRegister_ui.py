# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CarRegister.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CarRegister(object):
    def setupUi(self, CarRegister):
        if not CarRegister.objectName():
            CarRegister.setObjectName(u"CarRegister")
        CarRegister.resize(1036, 578)
        self.centralwidget = QWidget(CarRegister)
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
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u"images/carIcon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_2)


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

        self.car_id = QLineEdit(self.frame_22)
        self.car_id.setObjectName(u"car_id")
        self.car_id.setMinimumSize(QSize(300, 30))
        self.car_id.setMaximumSize(QSize(200, 16777215))
        self.car_id.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.car_id)

        self.carple_number = QLineEdit(self.frame_22)
        self.carple_number.setObjectName(u"carple_number")
        self.carple_number.setMinimumSize(QSize(300, 30))
        self.carple_number.setMaximumSize(QSize(200, 16777215))
        self.carple_number.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.carple_number)

        self.car_type = QLineEdit(self.frame_22)
        self.car_type.setObjectName(u"car_type")
        self.car_type.setMinimumSize(QSize(300, 30))
        self.car_type.setMaximumSize(QSize(200, 16777215))
        self.car_type.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.car_type)

        self.owner = QLineEdit(self.frame_22)
        self.owner.setObjectName(u"owner")
        self.owner.setMinimumSize(QSize(300, 30))
        self.owner.setMaximumSize(QSize(200, 16777215))
        self.owner.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.owner)

        self.owner_id = QLineEdit(self.frame_22)
        self.owner_id.setObjectName(u"owner_id")
        self.owner_id.setMinimumSize(QSize(300, 30))
        self.owner_id.setMaximumSize(QSize(200, 16777215))
        self.owner_id.setStyleSheet(u"border-style:none;\n"
"background-color: rgb(30, 41, 70);\n"
"padding:9;\n"
"padding-left:15;\n"
"font: 9pt \"arial\";\n"
"color: rgb(140, 140, 140);\n"
"border-radius:7\n"
"")

        self.verticalLayout_13.addWidget(self.owner_id)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_21)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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

        CarRegister.setCentralWidget(self.centralwidget)

        self.retranslateUi(CarRegister)

        QMetaObject.connectSlotsByName(CarRegister)
    # setupUi

    def retranslateUi(self, CarRegister):
        CarRegister.setWindowTitle(QCoreApplication.translate("CarRegister", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("CarRegister", u"Hachalu Hundesa Campus Gate Detection", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.label_2.setText("")
        self.car_id.setPlaceholderText(QCoreApplication.translate("CarRegister", u"Enter Carplet Number", None))
        self.carple_number.setPlaceholderText(QCoreApplication.translate("CarRegister", u"Enter Carplet Number", None))
        self.car_type.setPlaceholderText(QCoreApplication.translate("CarRegister", u"Enter car Type", None))
        self.owner.setPlaceholderText(QCoreApplication.translate("CarRegister", u"Enter owner", None))
        self.owner_id.setPlaceholderText(QCoreApplication.translate("CarRegister", u"Enter Owner Id", None))
        self.save.setText(QCoreApplication.translate("CarRegister", u"Save", None))
        self.pushButton_6.setText(QCoreApplication.translate("CarRegister", u"Update", None))
        self.delete_2.setText(QCoreApplication.translate("CarRegister", u"Delete", None))
        self.label_55.setText("")
        self.label_35.setText(QCoreApplication.translate("CarRegister", u"Face Recognition and other", None))
        self.label_51.setText(QCoreApplication.translate("CarRegister", u"Face Recognition and other", None))
        self.lineEdit_2.setInputMask("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CarRegister", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CarRegister", u"Car_id", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CarRegister", u"Carplet Number", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CarRegister", u"Car Type", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CarRegister", u"Owner Id", None));
    # retranslateUi

