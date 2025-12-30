# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(547, 587)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(20, 27, 45);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(23, 31, 53);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 20))
        self.label_5.setPixmap(QPixmap(u"images/amboLogo.PNG"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_5)

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
        self.minimize = QPushButton(self.frame_6)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(40, 25))
        self.minimize.setStyleSheet(u"QPushButton{border-style:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 71, 89);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../minimizeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize.setIcon(icon)
        self.minimize.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.minimize, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.restore_down = QPushButton(self.frame_6)
        self.restore_down.setObjectName(u"restore_down")
        self.restore_down.setMinimumSize(QSize(40, 25))
        self.restore_down.setStyleSheet(u"QPushButton{border-style:none;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 71, 89);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../maximizeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restore_down.setIcon(icon1)
        self.restore_down.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.restore_down, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.close = QPushButton(self.frame_6)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(40, 25))
        self.close.setStyleSheet(u"QPushButton{border-style:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(187, 73, 51);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../closeIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close.setIcon(icon2)
        self.close.setIconSize(QSize(12, 12))

        self.horizontalLayout_4.addWidget(self.close, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../Capture.PNG"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 87 12pt \"Arial Black\";\n"
"color: rgb(179, 179, 179);")

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(25)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.username = QLineEdit(self.frame_7)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(350, 0))
        self.username.setMaximumSize(QSize(450, 16777215))
        self.username.setStyleSheet(u"border-color: rgb(0, 170, 255);\n"
"color: rgb(211, 211, 211);\n"
"border-style:solid;\n"
"border-width:1;\n"
"border-radius:7;\n"
"padding:7")

        self.verticalLayout_4.addWidget(self.username)

        self.password = QLineEdit(self.frame_7)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(350, 0))
        self.password.setMaximumSize(QSize(450, 16777215))
        self.password.setStyleSheet(u"border-color: rgb(0, 170, 255);\n"
"color: rgb(211, 211, 211);\n"
"border-style:solid;\n"
"border-width:1;\n"
"border-radius:7;\n"
"padding:7")
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_4.addWidget(self.password)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.error = QLabel(self.frame_3)
        self.error.setObjectName(u"error")
        self.error.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.error, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.signup = QPushButton(self.frame_8)
        self.signup.setObjectName(u"signup")
        self.signup.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(0, 117, 175, 255));\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:50;\n"
"padding-right:50;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:14\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.verticalLayout_5.addWidget(self.signup)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 75 11pt \"Arial\";\n"
"color: rgb(0, 170, 255);")

        self.verticalLayout_5.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.frame_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{border-style:none;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(0, 117, 175, 255));\n"
"padding-top:7;\n"
"padding-bottom:7;\n"
"padding-left:50;\n"
"padding-right:50;\n"
"font: 75 9pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:14\n"
"}\n"
"QPushButton::hover{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(0, 130, 195, 255), stop:1 rgba(0, 100, 147, 255));\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout_2.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label_5.setText("")
        self.label.setText(QCoreApplication.translate("Login", u"Hachalu Hundesa Campus Gate Detection", None))
        self.minimize.setText("")
        self.restore_down.setText("")
        self.close.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Login", u"Login Page", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Login", u"Username...", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Login", u"Password...", None))
        self.error.setText("")
        self.signup.setText(QCoreApplication.translate("Login", u"Sign Up", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"or", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"Sign Up with Face", None))
    # retranslateUi

