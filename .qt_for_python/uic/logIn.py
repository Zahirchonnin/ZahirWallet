# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logIn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(429, 433)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#titleBar {\n"
"	border-bottom: 3px solid white;\n"
"	background-color: rgb(161, 76, 161);\n"
"}\n"
"QLabel#logo, QLabel#appLogo {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#title, QLabel#appName {\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	font: 75 20pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QLabel#title::hover, QLabel#appName::hover {\n"
"	color: rgb(53, 53, 53)\n"
"}\n"
"\n"
"QPushButton#close {\n"
"	background-color:  rgb(161, 76, 161);\n"
"	color: red;\n"
"	border: 4px solid white;\n"
"	border-left: 0;\n"
"	border-top: 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#minimize {\n"
"	background-color:  rgb(161, 76, 161);\n"
"	color: green;\n"
"	border: 4px solid white;\n"
"	border-left: 0;\n"
"	border-top: 0;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#minimize::pressed, QPushButton#close::pressed {\n"
"	background-color: rgb(149, 70, 149);\n"
"	border: 4px solid rgb(229, 229, 229);\n"
"	border-bottom: 0;\n"
"	border-right: 0\n"
"}\n"
"\n"
"QLineEdit#password {\n"
""
                        "	border: 3px solid white;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit#password::focus {\n"
"	border-color: #CA8ACA\n"
"}\n"
"\n"
"QPushButton#submit {\n"
"	color: white;\n"
"	border: 3px solid #592859;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#submit::pressed {\n"
"	border-color: rgb(124, 56, 124);\n"
"	background-color: rgb(145, 69, 145);\n"
"	padding-top: 10px;\n"
"	padidng-left: 10px\n"
"}\n"
"\n"
"QLabel#restore {\n"
"	color: rgb(6, 255, 118)\n"
"}\n"
"QLabel#restore::hover {\n"
"	color: rgb(5, 229, 102)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.appLogo = QLabel(self.frame)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setGeometry(QRect(130, 20, 161, 91))
        self.appLogo.setPixmap(QPixmap(u"logo.png"))
        self.appLogo.setScaledContents(True)
        self.appName = QLabel(self.frame)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(140, 130, 151, 31))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.appName.setFont(font)
        self.appName.setLayoutDirection(Qt.LeftToRight)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 190, 371, 41))
        font1 = QFont()
        font1.setFamily(u"MS UI Gothic")
        font1.setPointSize(17)
        self.password.setFont(font1)
        self.password.setEchoMode(QLineEdit.Password)
        self.submit = QPushButton(self.frame)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(110, 260, 181, 41))
        font2 = QFont()
        font2.setFamily(u"Palatino Linotype")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.submit.setFont(font2)
        self.restore = QLabel(self.frame)
        self.restore.setObjectName(u"restore")
        self.restore.setGeometry(QRect(50, 320, 301, 31))
        font3 = QFont()
        font3.setFamily(u"MingLiU-ExtB")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.restore.setFont(font3)

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.appLogo.setText("")
        self.appName.setText(QCoreApplication.translate("Form", u"Zahir Wallet", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"Enter password", None))
        self.submit.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.restore.setText(QCoreApplication.translate("Form", u"Restore from seed key", None))
    # retranslateUi

