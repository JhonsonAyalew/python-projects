# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(566, 325)
        SplashScreen.setStyleSheet(u"background-color: transparent;")
        self.Main = QWidget(SplashScreen)
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"background-color:transparent;\n"
"border-radius:15")
        self.horizontalLayout = QHBoxLayout(self.Main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_Body = QFrame(self.Main)
        self.Main_Body.setObjectName(u"Main_Body")
        self.Main_Body.setStyleSheet(u"background-color: rgb(20, 27, 45);\n"
"border-radius:10")
        self.Main_Body.setFrameShape(QFrame.StyledPanel)
        self.Main_Body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_Body)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.Main_Body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"color: rgb(0, 170, 255);")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 87 14pt \"Arial Black\";\n"
"color: rgb(200, 200, 200);")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_3 = QFrame(self.Main_Body)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 150))
        self.label_2.setPixmap(QPixmap(u"../Capture.jpg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.Main_Body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(20, 27, 45);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 15))
        self.progressBar.setMaximumSize(QSize(16777215, 15))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color: rgb(25, 35, 44);\n"
"    color:white;\n"
"border-radius:7;\n"
"border-style:none;\n"
"text-align:center;\n"
"margin-right:10\n"
"\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(0, 117, 175, 255));\n"
"border-radius:7;\n"
"border-style:none;\n"
"\n"
"}")
        self.progressBar.setValue(24)

        self.horizontalLayout_3.addWidget(self.progressBar, 0, Qt.AlignBottom)

        self.loading_label = QLabel(self.frame_2)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setMinimumSize(QSize(90, 0))
        self.loading_label.setStyleSheet(u"font: 8pt \"Arial\";\n"
"color: rgb(213, 213, 213);\n"
"background-color: rgb(20, 27, 45);\n"
"border-style:none;\n"
"margin-left:10")

        self.horizontalLayout_3.addWidget(self.loading_label)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.Main_Body)

        SplashScreen.setCentralWidget(self.Main)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("SplashScreen", u"Hachalu Hundesa", None))
        self.label.setText(QCoreApplication.translate("SplashScreen", u" Campus Gate Detection", None))
        self.label_2.setText("")
        self.loading_label.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
    # retranslateUi

