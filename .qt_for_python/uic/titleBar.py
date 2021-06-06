# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'titleBar.ui'
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
        Form.resize(430, 499)
        self.contanier = QWidget(Form)
        self.contanier.setObjectName(u"contanier")
        self.contanier.setGeometry(QRect(0, 70, 431, 431))
        self.contanier.setStyleSheet(u"QWidget {\n"
"	background-color: #B154B1\n"
"}")
        self.titleBar = QFrame(Form)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 431, 71))
        self.titleBar.setStyleSheet(u"QFrame#titleBar {\n"
"	border-bottom: 3px solid white;\n"
"	background-color: rgb(161, 76, 161);\n"
"}\n"
"QLabel#logo {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#title {\n"
"	background-color: transparent;\n"
"	color: black;\n"
"	font: 75 20pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QLabel#title::hover{\n"
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
"")
        self.titleBar.setFrameShape(QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.titleBar)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(70, 20, 151, 41))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.title.setFont(font)
        self.logo = QLabel(self.titleBar)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(-30, 0, 141, 71))
        self.logo.setPixmap(QPixmap(u"logo.png"))
        self.logo.setScaledContents(True)
        self.layoutWidget = QWidget(self.titleBar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(290, 10, 131, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize = QPushButton(self.layoutWidget)
        self.minimize.setObjectName(u"minimize")
        font1 = QFont()
        font1.setFamily(u"Permanent Marker")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.minimize.setFont(font1)

        self.horizontalLayout_2.addWidget(self.minimize)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")
        self.close.setFont(font1)

        self.horizontalLayout_2.addWidget(self.close)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"ZahirWallet", None))
        self.logo.setText("")
        self.minimize.setText(QCoreApplication.translate("Form", u"_", None))
        self.close.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

