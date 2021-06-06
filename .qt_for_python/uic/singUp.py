# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'singUp.ui'
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
        Form.resize(427, 431)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel#appName {\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	font: 75 20pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QLabel#appName::hover {\n"
"	color: rgb(53, 53, 53)\n"
"}\n"
"\n"
"QLineEdit#password, QLineEdit#password_conf {\n"
"	background-color: transparent;\n"
"	border: 3px solid white;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit#password::focus, QLineEdit#password_conf::focus {\n"
"	border-color: #CA8ACA\n"
"}\n"
"\n"
"QPushButton#create {\n"
"	color: white;\n"
"	border: 3px solid #592859;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton#create::pressed {\n"
"	border-color: rgb(124, 56, 124);\n"
"	background-color: rgb(145, 69, 145);\n"
"	padding-top: 10px;\n"
"	padidng-left: 10px\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.appLogo = QLabel(self.frame)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setGeometry(QRect(120, 10, 191, 101))
        self.appLogo.setPixmap(QPixmap(u"logo.png"))
        self.appLogo.setScaledContents(True)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 190, 371, 41))
        font = QFont()
        font.setFamily(u"MS UI Gothic")
        font.setPointSize(17)
        self.password.setFont(font)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_conf = QLineEdit(self.frame)
        self.password_conf.setObjectName(u"password_conf")
        self.password_conf.setGeometry(QRect(20, 240, 371, 41))
        self.password_conf.setFont(font)
        self.password_conf.setEchoMode(QLineEdit.Password)
        self.create = QPushButton(self.frame)
        self.create.setObjectName(u"create")
        self.create.setGeometry(QRect(110, 320, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Palatino Linotype")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.create.setFont(font1)
        self.appName = QLabel(self.frame)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(140, 110, 151, 31))
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.appName.setFont(font2)
        self.appName.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.appLogo.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"New Password (min 8 chars)", None))
        self.password_conf.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.create.setText(QCoreApplication.translate("Form", u"Create", None))
        self.appName.setText(QCoreApplication.translate("Form", u"Zahir Wallet", None))
    # retranslateUi

