# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SuperAdmin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SuperAdmin(object):
    def setupUi(self, SuperAdmin):
        if not SuperAdmin.objectName():
            SuperAdmin.setObjectName(u"SuperAdmin")
        SuperAdmin.resize(1020, 665)
        self.centralwidget = QWidget(SuperAdmin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_mini_bar = QWidget(self.centralwidget)
        self.left_mini_bar.setObjectName(u"left_mini_bar")
        self.left_mini_bar.setMinimumSize(QSize(0, 0))
        self.left_mini_bar.setMaximumSize(QSize(50, 16777215))
        self.left_mini_bar.setStyleSheet(u"background-color: rgb(31, 41, 64);")
        self.verticalLayout_9 = QVBoxLayout(self.left_mini_bar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 0, 2, 9)
        self.widget_28 = QWidget(self.left_mini_bar)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy)
        self.verticalLayout_8 = QVBoxLayout(self.widget_28)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 5, 2, 9)
        self.home1 = QPushButton(self.widget_28)
        self.home1.setObjectName(u"home1")
        self.home1.setMinimumSize(QSize(0, 35))
        self.home1.setStyleSheet(u"QPushButton{\n"
"background-color: \"#2B5DFF\";\n"
"border-style:none;\n"
"padding:5;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../Untitled82_20240401042441.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home1.setIcon(icon)

        self.verticalLayout_8.addWidget(self.home1)

        self.register1 = QPushButton(self.widget_28)
        self.register1.setObjectName(u"register1")
        self.register1.setMinimumSize(QSize(0, 35))
        self.register1.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:0;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4;\n"
"text-align:center;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/homeIcon.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.register1.setIcon(icon1)
        self.register1.setIconSize(QSize(28, 28))

        self.verticalLayout_8.addWidget(self.register1)

        self.face_recognition1 = QPushButton(self.widget_28)
        self.face_recognition1.setObjectName(u"face_recognition1")
        self.face_recognition1.setMinimumSize(QSize(0, 35))
        self.face_recognition1.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        self.face_recognition1.setIcon(icon)

        self.verticalLayout_8.addWidget(self.face_recognition1)

        self.about1 = QPushButton(self.widget_28)
        self.about1.setObjectName(u"about1")
        self.about1.setMinimumSize(QSize(0, 35))
        self.about1.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:3;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4;\n"
"text-align:center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/info.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.about1.setIcon(icon2)
        self.about1.setIconSize(QSize(28, 28))

        self.verticalLayout_8.addWidget(self.about1)


        self.verticalLayout_9.addWidget(self.widget_28, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_2 = QSpacerItem(117, 344, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.widget_29 = QWidget(self.left_mini_bar)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_16 = QPushButton(self.widget_29)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"text-align:left;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"images/setting.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon3)
        self.pushButton_16.setIconSize(QSize(18, 18))

        self.horizontalLayout_19.addWidget(self.pushButton_16)


        self.verticalLayout_9.addWidget(self.widget_29, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.left_mini_bar, 0, Qt.AlignLeft)

        self.left_bar = QWidget(self.centralwidget)
        self.left_bar.setObjectName(u"left_bar")
        self.left_bar.setMinimumSize(QSize(0, 0))
        self.left_bar.setMaximumSize(QSize(150, 16777215))
        self.left_bar.setStyleSheet(u"background-color:\"#1F2940\";")
        self.verticalLayout = QVBoxLayout(self.left_bar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, -1)
        self.widget_3 = QWidget(self.left_bar)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 5, 2, 9)
        self.home = QPushButton(self.widget_3)
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(0, 35))
        self.home.setStyleSheet(u"QPushButton{\n"
"background-color: \"#2B5DFF\";\n"
"border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:4;\n"
"text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        self.home.setIcon(icon)

        self.verticalLayout_2.addWidget(self.home)

        self.register_3 = QPushButton(self.widget_3)
        self.register_3.setObjectName(u"register_3")
        self.register_3.setMinimumSize(QSize(0, 35))
        self.register_3.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5;\n"
"text-align:left;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../Untitled82_20240401041801.png", QSize(), QIcon.Normal, QIcon.Off)
        self.register_3.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.register_3)

        self.face_recognition = QPushButton(self.widget_3)
        self.face_recognition.setObjectName(u"face_recognition")
        self.face_recognition.setMinimumSize(QSize(0, 35))
        self.face_recognition.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5;\n"
"text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../Untitled82_20240401041259.png", QSize(), QIcon.Normal, QIcon.Off)
        self.face_recognition.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.face_recognition)

        self.about = QPushButton(self.widget_3)
        self.about.setObjectName(u"about")
        self.about.setMinimumSize(QSize(0, 35))
        self.about.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:3;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5;\n"
"text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        self.about.setIcon(icon2)
        self.about.setIconSize(QSize(28, 28))

        self.verticalLayout_2.addWidget(self.about)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_4 = QWidget(self.left_bar)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_5 = QPushButton(self.widget_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"text-align:left;\n"
"")
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.pushButton_5)


        self.verticalLayout.addWidget(self.widget_4, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.left_bar, 0, Qt.AlignLeft)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setStyleSheet(u"background-color: \"#141B2D\";")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_5)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.widget_8)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7;\n"
"}\n"
"")
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.menu_button)


        self.horizontalLayout_3.addWidget(self.widget_8, 0, Qt.AlignLeft|Qt.AlignTop)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 2, 0)
        self.pushButton_7 = QPushButton(self.widget_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(40, 25))
        self.pushButton_7.setMaximumSize(QSize(40, 25))
        self.pushButton_7.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:5;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../minimizeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(18, 12))

        self.horizontalLayout_5.addWidget(self.pushButton_7, 0, Qt.AlignTop)

        self.pushButton_8 = QPushButton(self.widget_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(40, 25))
        self.pushButton_8.setMaximumSize(QSize(40, 25))
        self.pushButton_8.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:5;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../maximizeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.pushButton_8, 0, Qt.AlignTop)

        self.close = QPushButton(self.widget_9)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(40, 25))
        self.close.setMaximumSize(QSize(40, 25))
        self.close.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:3;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(179, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../closeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon8)
        self.close.setIconSize(QSize(12, 10))

        self.horizontalLayout_5.addWidget(self.close, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.widget_9, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.widget_5, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboardstack = QWidget()
        self.dashboardstack.setObjectName(u"dashboardstack")
        self.horizontalLayout_20 = QHBoxLayout(self.dashboardstack)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.dashboard = QWidget(self.dashboardstack)
        self.dashboard.setObjectName(u"dashboard")
        sizePolicy.setHeightForWidth(self.dashboard.sizePolicy().hasHeightForWidth())
        self.dashboard.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.dashboard)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_10 = QWidget(self.dashboard)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_97 = QFrame(self.widget_10)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_97)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(50, 50))
        self.label_56.setMaximumSize(QSize(50, 50))
        self.label_56.setStyleSheet(u"border-radius:25;\n"
"border-style:solid;\n"
"border-width:1;\n"
"border-color: rgb(243, 243, 243);\n"
"padding:6;")
        self.label_56.setPixmap(QPixmap(u"images/amboLogo.PNG"))
        self.label_56.setScaledContents(True)

        self.horizontalLayout_55.addWidget(self.label_56)

        self.frame_95 = QFrame(self.frame_97)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_95)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(9, 0, -1, 5)
        self.frame_96 = QFrame(self.frame_95)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 0))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_96)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_96)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 11pt \"arial black\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.verticalLayout_47.addWidget(self.label_36)

        self.label_53 = QLabel(self.frame_96)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"font: 10pt \"arial\";\n"
"margin:0;")

        self.verticalLayout_47.addWidget(self.label_53)


        self.verticalLayout_44.addWidget(self.frame_96)


        self.horizontalLayout_55.addWidget(self.frame_95)


        self.horizontalLayout_7.addWidget(self.frame_97, 0, Qt.AlignTop)

        self.lineEdit_2 = QLineEdit(self.widget_10)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(250, 0))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(20, 27, 45);\n"
"padding:10;\n"
"border-radius:17;\n"
"color: rgb(255, 255, 255);\n"
"border-style:solid;\n"
"border-width:1;\n"
"border-color: rgb(167, 167, 167);")
        self.lineEdit_2.setText(u"Search by content")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_7.addWidget(self.lineEdit_2, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.dashboard)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 90))
        self.widget_11.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setSpacing(25)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_13 = QWidget(self.widget_11)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_16 = QWidget(self.widget_13)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_5 = QVBoxLayout(self.widget_16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.widget_24 = QWidget(self.widget_16)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_24)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 10pt \"arial black\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.horizontalLayout_16.addWidget(self.label_37)

        self.label_38 = QLabel(self.widget_24)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 10pt \"arial\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.horizontalLayout_16.addWidget(self.label_38)


        self.verticalLayout_5.addWidget(self.widget_24, 0, Qt.AlignLeft)

        self.label_52 = QLabel(self.widget_16)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"font: 8pt \"arial\";\n"
"margin:0;")

        self.verticalLayout_5.addWidget(self.label_52)


        self.horizontalLayout_9.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_13)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(50, 50))
        self.widget_17.setMaximumSize(QSize(60, 60))
        self.widget_17.setStyleSheet(u"background-color: rgb(43, 93, 255);\n"
"border-radius:5")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.label_2 = QLabel(self.widget_17)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../../Untitled82_20240401041801.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_2)


        self.horizontalLayout_9.addWidget(self.widget_17, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_11)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:5")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_25 = QWidget(self.widget_14)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_6 = QVBoxLayout(self.widget_25)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.widget_26)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font:10pt \"arial black\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.horizontalLayout_17.addWidget(self.label_39)

        self.label_40 = QLabel(self.widget_26)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 10pt \"arial\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.horizontalLayout_17.addWidget(self.label_40)


        self.verticalLayout_6.addWidget(self.widget_26, 0, Qt.AlignLeft)

        self.label_54 = QLabel(self.widget_25)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"font: 9pt \"arial\";\n"
"margin:0;")

        self.verticalLayout_6.addWidget(self.label_54)


        self.horizontalLayout_10.addWidget(self.widget_25)

        self.widget_19 = QWidget(self.widget_14)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(50, 50))
        self.widget_19.setMaximumSize(QSize(50, 50))
        self.widget_19.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-radius:5")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(15, 9, 15, 9)
        self.label_3 = QLabel(self.widget_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../Untitled82_20240401041259.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.label_3)


        self.horizontalLayout_10.addWidget(self.widget_19, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_11)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:5")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.widget_18 = QWidget(self.widget_15)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_7 = QVBoxLayout(self.widget_18)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.widget_27 = QWidget(self.widget_18)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.widget_27)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 10pt \"arial black\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.horizontalLayout_18.addWidget(self.label_41)

        self.label_42 = QLabel(self.widget_27)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(204, 204, 204);\n"
"font: 10pt \"arial\";\n"
"margin:0;\n"
"color: rgb(182, 182, 182);")

        self.horizontalLayout_18.addWidget(self.label_42)


        self.verticalLayout_7.addWidget(self.widget_27, 0, Qt.AlignLeft)

        self.label_55 = QLabel(self.widget_18)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: rgb(154, 154, 154);\n"
"font: 9pt \"arial\";\n"
"margin:0;")

        self.verticalLayout_7.addWidget(self.label_55)


        self.horizontalLayout_11.addWidget(self.widget_18)

        self.widget_21 = QWidget(self.widget_15)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(50, 50))
        self.widget_21.setMaximumSize(QSize(50, 50))
        self.widget_21.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"border-radius:5")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label = QLabel(self.widget_21)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../../Untitled82_20240401043012.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.label)


        self.horizontalLayout_11.addWidget(self.widget_21, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.widget_15)


        self.verticalLayout_4.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.dashboard)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_22 = QWidget(self.widget_12)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:10")

        self.horizontalLayout_12.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_12)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:10")

        self.horizontalLayout_12.addWidget(self.widget_23)


        self.verticalLayout_4.addWidget(self.widget_12)


        self.horizontalLayout_20.addWidget(self.dashboard)

        self.stackedWidget.addWidget(self.dashboardstack)
        self.register_2 = QWidget()
        self.register_2.setObjectName(u"register_2")
        self.horizontalLayout_21 = QHBoxLayout(self.register_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.register_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_22.setSpacing(40)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.widget_30 = QWidget(self.widget_6)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setStyleSheet(u"QWidget{background-color: rgb(31, 41, 64);\n"
"border-radius:15;\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_30)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(30, -1, 30, 20)
        self.widget_36 = QWidget(self.widget_30)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setStyleSheet(u"border-style:none;")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_4 = QLabel(self.widget_36)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setPixmap(QPixmap(u"../../Untitled82_20240401043012.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_4)


        self.verticalLayout_11.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.widget_30)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"border-style:none;")
        self.verticalLayout_12 = QVBoxLayout(self.widget_37)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_5 = QLabel(self.widget_37)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.label_6 = QLabel(self.widget_37)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(206, 206, 206);")

        self.verticalLayout_12.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.widget_37, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.register_button = QPushButton(self.widget_30)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setMinimumSize(QSize(0, 35))
        self.register_button.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color: rgb(31, 41, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6;\n"
"}\n"
"QPushButton::hover{\n"
"border-style:solid;\n"
"border-width:1;\n"
"	border-color: rgb(148, 148, 148);\n"
"}\n"
"")

        self.verticalLayout_11.addWidget(self.register_button)


        self.horizontalLayout_22.addWidget(self.widget_30)

        self.widget_46 = QWidget(self.widget_6)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setStyleSheet(u"QWidget{background-color: rgb(31, 41, 64);\n"
"border-radius:15;\n"
"}\n"
"")
        self.verticalLayout_32 = QVBoxLayout(self.widget_46)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(30, -1, 30, 20)
        self.widget_64 = QWidget(self.widget_46)
        self.widget_64.setObjectName(u"widget_64")
        self.widget_64.setStyleSheet(u"border-style:none;")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_13 = QLabel(self.widget_64)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(100, 100))
        self.label_13.setPixmap(QPixmap(u"images/carIcon.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_13)


        self.verticalLayout_32.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.widget_46)
        self.widget_65.setObjectName(u"widget_65")
        self.widget_65.setStyleSheet(u"border-style:none;")
        self.verticalLayout_33 = QVBoxLayout(self.widget_65)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_14 = QLabel(self.widget_65)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_33.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.widget_65)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(206, 206, 206);")

        self.verticalLayout_33.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.verticalLayout_32.addWidget(self.widget_65, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.vehicle_button = QPushButton(self.widget_46)
        self.vehicle_button.setObjectName(u"vehicle_button")
        self.vehicle_button.setMinimumSize(QSize(0, 35))
        self.vehicle_button.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color: rgb(31, 41, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6;\n"
"}\n"
"QPushButton::hover{\n"
"border-style:solid;\n"
"border-width:1;\n"
"	border-color: rgb(148, 148, 148);\n"
"}\n"
"")

        self.verticalLayout_32.addWidget(self.vehicle_button)


        self.horizontalLayout_22.addWidget(self.widget_46)

        self.widget_42 = QWidget(self.widget_6)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setStyleSheet(u"QWidget{background-color: rgb(31, 41, 64);\n"
"border-radius:15;\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.widget_42)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(30, -1, 30, 20)
        self.widget_43 = QWidget(self.widget_42)
        self.widget_43.setObjectName(u"widget_43")
        self.widget_43.setStyleSheet(u"border-style:none;")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_10 = QLabel(self.widget_43)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(100, 100))
        self.label_10.setPixmap(QPixmap(u"images/setting.PNG"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_10)


        self.verticalLayout_17.addWidget(self.widget_43)

        self.widget_45 = QWidget(self.widget_42)
        self.widget_45.setObjectName(u"widget_45")
        self.widget_45.setStyleSheet(u"border-style:none;")
        self.verticalLayout_18 = QVBoxLayout(self.widget_45)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_11 = QLabel(self.widget_45)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.widget_45)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(206, 206, 206);")

        self.verticalLayout_18.addWidget(self.label_12, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.widget_45, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.Admin_button = QPushButton(self.widget_42)
        self.Admin_button.setObjectName(u"Admin_button")
        self.Admin_button.setMinimumSize(QSize(0, 35))
        self.Admin_button.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color: rgb(31, 41, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6;\n"
"}\n"
"QPushButton::hover{\n"
"border-style:solid;\n"
"border-width:1;\n"
"	border-color: rgb(148, 148, 148);\n"
"}\n"
"")

        self.verticalLayout_17.addWidget(self.Admin_button)


        self.horizontalLayout_22.addWidget(self.widget_42)


        self.verticalLayout_10.addWidget(self.widget_6)

        self.widget_20 = QWidget(self.widget_2)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_23.setSpacing(40)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.widget_38 = QWidget(self.widget_20)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setStyleSheet(u"QWidget{background-color: rgb(31, 41, 64);\n"
"border-radius:15;\n"
"}\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.widget_38)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(30, -1, 30, 20)
        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setStyleSheet(u"border-style:none;")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_7 = QLabel(self.widget_39)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 100))
        self.label_7.setPixmap(QPixmap(u"images/computerIcon (1).png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_7)


        self.verticalLayout_13.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setStyleSheet(u"border-style:none;")
        self.verticalLayout_14 = QVBoxLayout(self.widget_40)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.widget_40)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.widget_40)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(206, 206, 206);")

        self.verticalLayout_14.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.widget_40, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.PC_button = QPushButton(self.widget_38)
        self.PC_button.setObjectName(u"PC_button")
        self.PC_button.setMinimumSize(QSize(0, 35))
        self.PC_button.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color: rgb(31, 41, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6;\n"
"}\n"
"QPushButton::hover{\n"
"border-style:solid;\n"
"border-width:1;\n"
"	\n"
"	border-color: rgb(199, 199, 199);\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.PC_button)


        self.horizontalLayout_23.addWidget(self.widget_38)

        self.widget_54 = QWidget(self.widget_20)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setStyleSheet(u"QWidget{background-color: rgb(31, 41, 64);\n"
"border-radius:15;\n"
"}\n"
"")
        self.verticalLayout_25 = QVBoxLayout(self.widget_54)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(30, -1, 30, 20)
        self.widget_55 = QWidget(self.widget_54)
        self.widget_55.setObjectName(u"widget_55")
        self.widget_55.setStyleSheet(u"border-style:none;")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_25 = QLabel(self.widget_55)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(100, 100))
        self.label_25.setPixmap(QPixmap(u"../../Untitled82_20240401043012.png"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_25)


        self.verticalLayout_25.addWidget(self.widget_55)

        self.widget_66 = QWidget(self.widget_54)
        self.widget_66.setObjectName(u"widget_66")
        self.widget_66.setStyleSheet(u"border-style:none;")
        self.verticalLayout_26 = QVBoxLayout(self.widget_66)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_26 = QLabel(self.widget_66)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_26.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.label_27 = QLabel(self.widget_66)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(206, 206, 206);")

        self.verticalLayout_26.addWidget(self.label_27, 0, Qt.AlignHCenter)


        self.verticalLayout_25.addWidget(self.widget_66, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.fasting_button = QPushButton(self.widget_54)
        self.fasting_button.setObjectName(u"fasting_button")
        self.fasting_button.setMinimumSize(QSize(0, 35))
        self.fasting_button.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color: rgb(31, 41, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6;\n"
"}\n"
"QPushButton::hover{\n"
"border-style:solid;\n"
"border-width:1;\n"
"	\n"
"	border-color: rgb(199, 199, 199);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.fasting_button)


        self.horizontalLayout_23.addWidget(self.widget_54)

        self.widget_41 = QWidget(self.widget_20)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setStyleSheet(u"QWidget{background-color: rgb(31, 41, 64);\n"
"border-radius:15;\n"
"}\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.widget_41)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(30, -1, 30, 20)
        self.widget_44 = QWidget(self.widget_41)
        self.widget_44.setObjectName(u"widget_44")
        self.widget_44.setStyleSheet(u"border-style:none;")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_16 = QLabel(self.widget_44)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(100, 100))
        self.label_16.setPixmap(QPixmap(u"../../Untitled82_20240401043012.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_16)


        self.verticalLayout_19.addWidget(self.widget_44)

        self.widget_47 = QWidget(self.widget_41)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setStyleSheet(u"border-style:none;")
        self.verticalLayout_20 = QVBoxLayout(self.widget_47)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_17 = QLabel(self.widget_47)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_20.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.widget_47)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(206, 206, 206);")

        self.verticalLayout_20.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_19.addWidget(self.widget_47, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.servant_button = QPushButton(self.widget_41)
        self.servant_button.setObjectName(u"servant_button")
        self.servant_button.setMinimumSize(QSize(0, 35))
        self.servant_button.setStyleSheet(u"\n"
"\n"
"QPushButton{background-color: rgb(31, 41, 64);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6;\n"
"}\n"
"QPushButton::hover{\n"
"border-style:solid;\n"
"border-width:1;\n"
"	\n"
"	border-color: rgb(199, 199, 199);\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.servant_button)


        self.horizontalLayout_23.addWidget(self.widget_41)


        self.verticalLayout_10.addWidget(self.widget_20)


        self.horizontalLayout_21.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.register_2)
        self.facerecognition = QWidget()
        self.facerecognition.setObjectName(u"facerecognition")
        self.horizontalLayout_32 = QHBoxLayout(self.facerecognition)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.widget_32 = QWidget(self.facerecognition)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_27 = QVBoxLayout(self.widget_32)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_34 = QWidget(self.widget_32)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setStyleSheet(u"background-color: rgb(31, 41, 64);")
        self.verticalLayout_28 = QVBoxLayout(self.widget_34)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_35 = QWidget(self.widget_34)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.widget_35)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(234, 234, 234);")

        self.horizontalLayout_33.addWidget(self.label_28)


        self.verticalLayout_28.addWidget(self.widget_35)


        self.verticalLayout_27.addWidget(self.widget_34, 0, Qt.AlignTop)

        self.widget_33 = QWidget(self.widget_32)
        self.widget_33.setObjectName(u"widget_33")
        sizePolicy.setHeightForWidth(self.widget_33.sizePolicy().hasHeightForWidth())
        self.widget_33.setSizePolicy(sizePolicy)
        self.verticalLayout_29 = QVBoxLayout(self.widget_33)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_56 = QWidget(self.widget_33)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.widget_59 = QWidget(self.widget_56)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.widget_58 = QWidget(self.widget_59)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(50, 0, 50, 0)
        self.widget_62 = QWidget(self.widget_58)
        self.widget_62.setObjectName(u"widget_62")
        self.widget_62.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:10;")
        self.verticalLayout_15 = QVBoxLayout(self.widget_62)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_34 = QLabel(self.widget_62)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(100, 100))
        self.label_34.setPixmap(QPixmap(u"../../Untitled82_20240401043012.png"))
        self.label_34.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_34, 0, Qt.AlignHCenter)

        self.pushButton_6 = QPushButton(self.widget_62)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{font: 75 9pt \"Arial\";\n"
"color: rgb(238, 238, 238);\n"
"background-color: rgb(44, 59, 91);\n"
"padding:7;\n"
"padding-left:25;\n"
"padding-right:25;\n"
"border-radius:4;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 68, 104);\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.pushButton_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_36.addWidget(self.widget_62)


        self.horizontalLayout_40.addWidget(self.widget_58)

        self.widget_63 = QWidget(self.widget_59)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setStyleSheet(u"")
        self.verticalLayout_30 = QVBoxLayout(self.widget_63)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_30 = QLabel(self.widget_63)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"font: 75 10pt \"Arial\";\n"
"color: rgb(222, 222, 222);")

        self.verticalLayout_30.addWidget(self.label_30, 0, Qt.AlignTop)

        self.label_29 = QLabel(self.widget_63)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_30.addWidget(self.label_29)

        self.label_31 = QLabel(self.widget_63)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_30.addWidget(self.label_31)

        self.label_32 = QLabel(self.widget_63)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_30.addWidget(self.label_32)

        self.label_33 = QLabel(self.widget_63)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_30.addWidget(self.label_33)


        self.horizontalLayout_40.addWidget(self.widget_63)


        self.horizontalLayout_34.addWidget(self.widget_59)


        self.verticalLayout_29.addWidget(self.widget_56)

        self.widget_57 = QWidget(self.widget_33)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.widget_60 = QWidget(self.widget_57)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(50, 0, 50, 0)
        self.widget_68 = QWidget(self.widget_60)
        self.widget_68.setObjectName(u"widget_68")
        self.widget_68.setStyleSheet(u"background-color: rgb(31, 41, 64);\n"
"border-radius:10;")
        self.verticalLayout_16 = QVBoxLayout(self.widget_68)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_35 = QLabel(self.widget_68)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(100, 100))
        self.label_35.setPixmap(QPixmap(u"../../Untitled82_20240401043012.png"))
        self.label_35.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.label_35, 0, Qt.AlignHCenter)

        self.pushButton_15 = QPushButton(self.widget_68)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"QPushButton{font: 75 9pt \"Arial\";\n"
"color: rgb(238, 238, 238);\n"
"background-color: rgb(44, 59, 91);\n"
"padding:7;\n"
"padding-left:25;\n"
"padding-right:25;\n"
"border-radius:4;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 68, 104);\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.pushButton_15, 0, Qt.AlignHCenter)


        self.horizontalLayout_43.addWidget(self.widget_68)


        self.horizontalLayout_35.addWidget(self.widget_60)

        self.widget_61 = QWidget(self.widget_57)
        self.widget_61.setObjectName(u"widget_61")
        self.verticalLayout_31 = QVBoxLayout(self.widget_61)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_46 = QLabel(self.widget_61)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 75 10pt \"Arial\";\n"
"color: rgb(222, 222, 222);\n"
"text-align:right;")

        self.verticalLayout_31.addWidget(self.label_46)

        self.label_47 = QLabel(self.widget_61)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_31.addWidget(self.label_47)

        self.label_44 = QLabel(self.widget_61)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_31.addWidget(self.label_44)

        self.label_45 = QLabel(self.widget_61)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_31.addWidget(self.label_45)

        self.label_43 = QLabel(self.widget_61)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: rgb(138, 138, 138);")

        self.verticalLayout_31.addWidget(self.label_43)


        self.horizontalLayout_35.addWidget(self.widget_61, 0, Qt.AlignLeft)


        self.verticalLayout_29.addWidget(self.widget_57)


        self.verticalLayout_27.addWidget(self.widget_33)


        self.horizontalLayout_32.addWidget(self.widget_32)

        self.stackedWidget.addWidget(self.facerecognition)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_10 = QPushButton(self.widget_7)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton{border-style:none;\n"
"padding:10;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(42, 57, 88);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_10)


        self.verticalLayout_3.addWidget(self.widget_7, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.widget)

        SuperAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(SuperAdmin)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SuperAdmin)
    # setupUi

    def retranslateUi(self, SuperAdmin):
        SuperAdmin.setWindowTitle(QCoreApplication.translate("SuperAdmin", u"MainWindow", None))
        self.home1.setText("")
        self.register1.setText("")
        self.face_recognition1.setText("")
        self.about1.setText("")
        self.pushButton_16.setText("")
        self.home.setText(QCoreApplication.translate("SuperAdmin", u"Home", None))
        self.register_3.setText(QCoreApplication.translate("SuperAdmin", u"Register", None))
        self.face_recognition.setText(QCoreApplication.translate("SuperAdmin", u"Face Recognition", None))
        self.about.setText(QCoreApplication.translate("SuperAdmin", u"Image Detection", None))
        self.pushButton_5.setText(QCoreApplication.translate("SuperAdmin", u"Quit", None))
        self.menu_button.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.close.setText("")
        self.label_56.setText("")
        self.label_36.setText(QCoreApplication.translate("SuperAdmin", u"Face Recognition and other", None))
        self.label_53.setText(QCoreApplication.translate("SuperAdmin", u"Face Recognition and other", None))
        self.lineEdit_2.setInputMask("")
        self.label_37.setText(QCoreApplication.translate("SuperAdmin", u"Male : ", None))
        self.label_38.setText(QCoreApplication.translate("SuperAdmin", u"20152", None))
        self.label_52.setText(QCoreApplication.translate("SuperAdmin", u"Number male of student", None))
        self.label_2.setText("")
        self.label_39.setText(QCoreApplication.translate("SuperAdmin", u"Female : ", None))
        self.label_40.setText(QCoreApplication.translate("SuperAdmin", u"20152", None))
        self.label_54.setText(QCoreApplication.translate("SuperAdmin", u"Number male of student", None))
        self.label_3.setText("")
        self.label_41.setText(QCoreApplication.translate("SuperAdmin", u"All : ", None))
        self.label_42.setText(QCoreApplication.translate("SuperAdmin", u"20152", None))
        self.label_55.setText(QCoreApplication.translate("SuperAdmin", u"Number male of student", None))
        self.label.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("SuperAdmin", u"Register Students", None))
        self.label_6.setText(QCoreApplication.translate("SuperAdmin", u"Register new students", None))
        self.register_button.setText(QCoreApplication.translate("SuperAdmin", u"Register", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("SuperAdmin", u"Register Vehicle", None))
        self.label_15.setText(QCoreApplication.translate("SuperAdmin", u"Register new vehicle", None))
        self.vehicle_button.setText(QCoreApplication.translate("SuperAdmin", u"vehicle", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("SuperAdmin", u"Register Admin", None))
        self.label_12.setText(QCoreApplication.translate("SuperAdmin", u"Register cafeand OutDoorAdmin", None))
        self.Admin_button.setText(QCoreApplication.translate("SuperAdmin", u"Register Admin", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("SuperAdmin", u"Register Pc", None))
        self.label_9.setText(QCoreApplication.translate("SuperAdmin", u"Register new Pc", None))
        self.PC_button.setText(QCoreApplication.translate("SuperAdmin", u"Pc Register", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("SuperAdmin", u"Register Fasting", None))
        self.label_27.setText(QCoreApplication.translate("SuperAdmin", u"Register Fasting Student", None))
        self.fasting_button.setText(QCoreApplication.translate("SuperAdmin", u"Fasting", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("SuperAdmin", u"Register servant", None))
        self.label_18.setText(QCoreApplication.translate("SuperAdmin", u"Register new servant", None))
        self.servant_button.setText(QCoreApplication.translate("SuperAdmin", u"Servant", None))
        self.label_28.setText(QCoreApplication.translate("SuperAdmin", u"Cafe And OutDoor Security", None))
        self.label_34.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("SuperAdmin", u"Open", None))
        self.label_30.setText(QCoreApplication.translate("SuperAdmin", u"OutDoor Security System", None))
        self.label_29.setText(QCoreApplication.translate("SuperAdmin", u"Student Face Recognition", None))
        self.label_31.setText(QCoreApplication.translate("SuperAdmin", u"Weapon Detection", None))
        self.label_32.setText(QCoreApplication.translate("SuperAdmin", u"Vechile Detection", None))
        self.label_33.setText(QCoreApplication.translate("SuperAdmin", u"Pc Detection", None))
        self.label_35.setText("")
        self.pushButton_15.setText(QCoreApplication.translate("SuperAdmin", u"Open", None))
        self.label_46.setText(QCoreApplication.translate("SuperAdmin", u"OutDoor Security System", None))
        self.label_47.setText(QCoreApplication.translate("SuperAdmin", u"Student Face Recognition", None))
        self.label_44.setText(QCoreApplication.translate("SuperAdmin", u"Weapon Detection", None))
        self.label_45.setText(QCoreApplication.translate("SuperAdmin", u"Vechile Detection", None))
        self.label_43.setText(QCoreApplication.translate("SuperAdmin", u"Pc Detection", None))
        self.pushButton_10.setText(QCoreApplication.translate("SuperAdmin", u"PushButton", None))
    # retranslateUi

