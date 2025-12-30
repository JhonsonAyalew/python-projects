# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Outdoor_Face_recognition.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Outdoor_Face_recognition(object):
    def setupUi(self, Outdoor_Face_recognition):
        if not Outdoor_Face_recognition.objectName():
            Outdoor_Face_recognition.setObjectName(u"Outdoor_Face_recognition")
        Outdoor_Face_recognition.resize(1073, 602)
        self.centralwidget = QWidget(Outdoor_Face_recognition)
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


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"background-color: rgb(20, 27, 47);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_12 = QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(20, 0, 20, 0)
        self.All_camera = QPushButton(self.widget_8)
        self.All_camera.setObjectName(u"All_camera")
        self.All_camera.setMinimumSize(QSize(0, 0))
        self.All_camera.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: rgb(33, 44, 76);\n"
"padding-top:10;\n"
"padding-bottom:10;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_25.addWidget(self.All_camera)

        self.weapon_camera = QPushButton(self.widget_8)
        self.weapon_camera.setObjectName(u"weapon_camera")
        self.weapon_camera.setMinimumSize(QSize(0, 0))
        self.weapon_camera.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: rgb(33, 44, 76);\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_25.addWidget(self.weapon_camera)

        self.vechile_camera = QPushButton(self.widget_8)
        self.vechile_camera.setObjectName(u"vechile_camera")
        self.vechile_camera.setMinimumSize(QSize(0, 0))
        self.vechile_camera.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: rgb(33, 44, 76);\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_25.addWidget(self.vechile_camera)

        self.pc_camera = QPushButton(self.widget_8)
        self.pc_camera.setObjectName(u"pc_camera")
        self.pc_camera.setMinimumSize(QSize(0, 0))
        self.pc_camera.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: rgb(33, 44, 76);\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_25.addWidget(self.pc_camera)

        self.face_cmera = QPushButton(self.widget_8)
        self.face_cmera.setObjectName(u"face_cmera")
        self.face_cmera.setMinimumSize(QSize(0, 0))
        self.face_cmera.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: rgb(33, 44, 76);\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_25.addWidget(self.face_cmera)


        self.verticalLayout_12.addWidget(self.widget_8, 0, Qt.AlignTop)

        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_7)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy1.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy1)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy2)
        self.widget_20.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.face_recognition_widget = QWidget(self.widget_20)
        self.face_recognition_widget.setObjectName(u"face_recognition_widget")
        self.face_recognition_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_19 = QVBoxLayout(self.face_recognition_widget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_36 = QWidget(self.face_recognition_widget)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy2.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy2)
        self.widget_36.setStyleSheet(u"border-style:solid;\n"
"border-color: rgb(33, 44, 76);\n"
"border-width:3;\n"
"border-radius:15")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_36)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMaximumSize(QSize(330, 200))
        self.label_12.setStyleSheet(u"border-style:none;\n"
"background-color:none;\n"
"border-radius:15")

        self.horizontalLayout_31.addWidget(self.label_12)


        self.verticalLayout_19.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.face_recognition_widget)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"background-color: rgb(15, 20, 36);")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.label_11 = QLabel(self.widget_37)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(147, 147, 147);\n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_29.addWidget(self.label_11)

        self.comboBox = QComboBox(self.widget_37)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(90, 0))
        self.comboBox.setMaximumSize(QSize(90, 16777215))
        self.comboBox.setStyleSheet(u"border-styel:none;\n"
"background-color: rgb(33, 44, 76);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(222, 222, 222);")

        self.horizontalLayout_29.addWidget(self.comboBox)


        self.verticalLayout_19.addWidget(self.widget_37, 0, Qt.AlignLeft)


        self.verticalLayout_14.addWidget(self.face_recognition_widget)

        self.vechile_recognition_widget = QWidget(self.widget_20)
        self.vechile_recognition_widget.setObjectName(u"vechile_recognition_widget")
        self.vechile_recognition_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_20 = QVBoxLayout(self.vechile_recognition_widget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.widget_39 = QWidget(self.vechile_recognition_widget)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy2.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy2)
        self.widget_39.setStyleSheet(u"border-style:solid;\n"
"border-color: rgb(33, 44, 76);\n"
"border-width:3;\n"
"border-radius:15")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_39)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setMaximumSize(QSize(330, 200))
        self.label_13.setStyleSheet(u"border-style:none;\n"
"background-color:none;\n"
"border-radius:15")

        self.horizontalLayout_32.addWidget(self.label_13)


        self.verticalLayout_20.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.vechile_recognition_widget)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setStyleSheet(u"background-color: rgb(15, 20, 36);")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.label_15 = QLabel(self.widget_40)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(147, 147, 147);\n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_33.addWidget(self.label_15)

        self.comboBox_3 = QComboBox(self.widget_40)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(90, 0))
        self.comboBox_3.setMaximumSize(QSize(90, 16777215))
        self.comboBox_3.setStyleSheet(u"border-styel:none;\n"
"background-color: rgb(33, 44, 76);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(222, 222, 222);")

        self.horizontalLayout_33.addWidget(self.comboBox_3)


        self.verticalLayout_20.addWidget(self.widget_40, 0, Qt.AlignLeft)


        self.verticalLayout_14.addWidget(self.vechile_recognition_widget)


        self.horizontalLayout_11.addWidget(self.widget_20)

        self.widget_22 = QWidget(self.widget_19)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy2.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy2)
        self.verticalLayout_15 = QVBoxLayout(self.widget_22)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pc_recognition_widget = QWidget(self.widget_22)
        self.pc_recognition_widget.setObjectName(u"pc_recognition_widget")
        self.pc_recognition_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_16 = QVBoxLayout(self.pc_recognition_widget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.pc_recognition_widget)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy2.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy2)
        self.widget_23.setStyleSheet(u"border-style:solid;\n"
"border-color: rgb(33, 44, 76);\n"
"border-width:3;\n"
"border-radius:15")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_16 = QLabel(self.widget_23)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMaximumSize(QSize(330, 200))
        self.label_16.setStyleSheet(u"border-style:none;\n"
"background-color:none;\n"
"border-radius:15")

        self.horizontalLayout_28.addWidget(self.label_16)


        self.verticalLayout_16.addWidget(self.widget_23)

        self.widget_29 = QWidget(self.pc_recognition_widget)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setStyleSheet(u"background-color: rgb(15, 20, 36);")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.widget_29)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(147, 147, 147);\n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_26.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.widget_29)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(90, 0))
        self.comboBox_2.setMaximumSize(QSize(90, 16777215))
        self.comboBox_2.setStyleSheet(u"border-styel:none;\n"
"background-color: rgb(33, 44, 76);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(222, 222, 222);")

        self.horizontalLayout_26.addWidget(self.comboBox_2)


        self.verticalLayout_16.addWidget(self.widget_29, 0, Qt.AlignLeft)


        self.verticalLayout_15.addWidget(self.pc_recognition_widget)

        self.weapon_detection_widget = QWidget(self.widget_22)
        self.weapon_detection_widget.setObjectName(u"weapon_detection_widget")
        self.weapon_detection_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_17 = QVBoxLayout(self.weapon_detection_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = QWidget(self.weapon_detection_widget)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy2.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy2)
        self.widget_31.setStyleSheet(u"border-style:solid;\n"
"border-color: rgb(33, 44, 76);\n"
"border-width:3;\n"
"border-radius:15")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_17 = QLabel(self.widget_31)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMaximumSize(QSize(330, 200))
        self.label_17.setStyleSheet(u"border-style:none;\n"
"background-color:none;\n"
"border-radius:15")

        self.horizontalLayout_34.addWidget(self.label_17)


        self.verticalLayout_17.addWidget(self.widget_31)

        self.widget_32 = QWidget(self.weapon_detection_widget)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setStyleSheet(u"background-color: rgb(15, 20, 36);")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.widget_32)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(147, 147, 147);\n"
"font: 87 8pt \"Arial Black\";")

        self.horizontalLayout_27.addWidget(self.label_9)

        self.comboBox_4 = QComboBox(self.widget_32)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(90, 0))
        self.comboBox_4.setMaximumSize(QSize(90, 16777215))
        self.comboBox_4.setStyleSheet(u"border-styel:none;\n"
"background-color: rgb(33, 44, 76);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(222, 222, 222);")

        self.horizontalLayout_27.addWidget(self.comboBox_4)


        self.verticalLayout_17.addWidget(self.widget_32, 0, Qt.AlignLeft)


        self.verticalLayout_15.addWidget(self.weapon_detection_widget)


        self.horizontalLayout_11.addWidget(self.widget_22)


        self.horizontalLayout_23.addWidget(self.widget_19)


        self.verticalLayout_12.addWidget(self.widget_7)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout_6.addWidget(self.widget_6)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(300, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_9)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u"images/carIcon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.widget_10, 0, Qt.AlignTop)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.widget_11)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 200))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_22)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_10, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.frame_11, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_22)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_12, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_9.addWidget(self.frame_13, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.widget_12 = QWidget(self.frame_22)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.verticalLayout_11 = QVBoxLayout(self.widget_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_3 = QLabel(self.widget_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_19.addWidget(self.label_3)

        self.first_name = QLabel(self.widget_14)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_19.addWidget(self.first_name)


        self.verticalLayout_11.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_4 = QLabel(self.widget_15)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_20.addWidget(self.label_4)

        self.father_name = QLabel(self.widget_15)
        self.father_name.setObjectName(u"father_name")
        self.father_name.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_20.addWidget(self.father_name)


        self.verticalLayout_11.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.widget_13)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_5 = QLabel(self.widget_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_21.addWidget(self.label_5)

        self.grandfather_name = QLabel(self.widget_16)
        self.grandfather_name.setObjectName(u"grandfather_name")
        self.grandfather_name.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_21.addWidget(self.grandfather_name)


        self.verticalLayout_11.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_13)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_6 = QLabel(self.widget_17)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_22.addWidget(self.label_6)

        self.age = QLabel(self.widget_17)
        self.age.setObjectName(u"age")
        self.age.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_22.addWidget(self.age)


        self.verticalLayout_11.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_13)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_8 = QLabel(self.widget_18)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(180, 180, 180);\n"
"font: 75 9pt \"Cambria\";")

        self.horizontalLayout_24.addWidget(self.label_8)

        self.DOB = QLabel(self.widget_18)
        self.DOB.setObjectName(u"DOB")
        self.DOB.setStyleSheet(u"color: rgb(220, 220, 220);")

        self.horizontalLayout_24.addWidget(self.DOB)


        self.verticalLayout_11.addWidget(self.widget_18)

        self.widget_21 = QWidget(self.widget_13)
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


        self.horizontalLayout_12.addWidget(self.widget_13)


        self.verticalLayout_13.addWidget(self.widget_12)

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


        self.horizontalLayout_10.addWidget(self.frame_22, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.frame_19 = QFrame(self.widget_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"\n"
"border-radius:10")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setSpacing(30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)

        self.verticalLayout_3.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.widget_9)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"\n"
"border-radius:10")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setSpacing(30)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.addPhoto_10 = QPushButton(self.frame_20)
        self.addPhoto_10.setObjectName(u"addPhoto_10")
        self.addPhoto_10.setMinimumSize(QSize(0, 0))
        self.addPhoto_10.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_17.addWidget(self.addPhoto_10)

        self.addPhoto_9 = QPushButton(self.frame_20)
        self.addPhoto_9.setObjectName(u"addPhoto_9")
        self.addPhoto_9.setMinimumSize(QSize(0, 0))
        self.addPhoto_9.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: rgb(33, 44, 76);\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:20;\n"
"padding-right:20;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.horizontalLayout_17.addWidget(self.addPhoto_9)


        self.verticalLayout_3.addWidget(self.frame_20)

        self.widget_26 = QWidget(self.widget_9)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_9 = QVBoxLayout(self.widget_26)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.widget_26)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"\n"
"border-radius:10")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_14.setSpacing(40)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)

        self.verticalLayout_9.addWidget(self.frame_16)


        self.verticalLayout_3.addWidget(self.widget_26, 0, Qt.AlignBottom)


        self.horizontalLayout_13.addWidget(self.widget_9)


        self.horizontalLayout_5.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.widget_2)

        Outdoor_Face_recognition.setCentralWidget(self.centralwidget)

        self.retranslateUi(Outdoor_Face_recognition)

        QMetaObject.connectSlotsByName(Outdoor_Face_recognition)
    # setupUi

    def retranslateUi(self, Outdoor_Face_recognition):
        Outdoor_Face_recognition.setWindowTitle(QCoreApplication.translate("Outdoor_Face_recognition", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Hachalu Hundesa Campus Gate Detection", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.All_camera.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"All Camera", None))
        self.weapon_camera.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Weapon", None))
        self.vechile_camera.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Vechile", None))
        self.pc_camera.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"car", None))
        self.face_cmera.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Face", None))
        self.label_12.setText("")
        self.label_11.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Face Recognnition", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Outdoor_Face_recognition", u"Please select camera options", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 0", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 1", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 2", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 3", None))

        self.label_13.setText("")
        self.label_15.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Face Recognnition", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Outdoor_Face_recognition", u"Please select camera options", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 0", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 1", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 2", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 3", None))

        self.label_16.setText("")
        self.label_7.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Weapon Detection", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Outdoor_Face_recognition", u"Please select camera options", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 0", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 1", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 2", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 3", None))

        self.label_17.setText("")
        self.label_9.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Pc Recognition", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("Outdoor_Face_recognition", u"Please select camera options", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 0", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 1", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 2", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("Outdoor_Face_recognition", u"From camera 3", None))

        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"First Name :", None))
        self.first_name.setText("")
        self.label_4.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Father Name :", None))
        self.father_name.setText("")
        self.label_5.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"G/father Name :", None))
        self.grandfather_name.setText("")
        self.label_6.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Age:", None))
        self.age.setText("")
        self.label_8.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"DOB:", None))
        self.DOB.setText("")
        self.label_14.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Username :", None))
        self.username.setText("")
        self.addPhoto_10.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Face", None))
        self.addPhoto_9.setText(QCoreApplication.translate("Outdoor_Face_recognition", u"Face", None))
    # retranslateUi

