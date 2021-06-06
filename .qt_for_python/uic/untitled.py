# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
        Form.resize(429, 503)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background-color: #B154B1\n"
"}\n"
"\n"
"QFrame#titleBar {\n"
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
""
                        "	border-right: 0\n"
"}\n"
"\n"
"QLineEdit#password {\n"
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
        self.titleBar = QFrame(self.widget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setGeometry(QRect(0, 0, 411, 71))
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
        self.layoutWidget.setGeometry(QRect(280, 10, 121, 51))
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

        self.password = QLineEdit(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(20, 250, 371, 41))
        font2 = QFont()
        font2.setFamily(u"MS UI Gothic")
        font2.setPointSize(17)
        self.password.setFont(font2)
        self.password.setEchoMode(QLineEdit.Password)
        self.submit = QPushButton(self.widget)
        self.submit.setObjectName(u"submit")
        self.submit.setGeometry(QRect(110, 310, 181, 41))
        font3 = QFont()
        font3.setFamily(u"Palatino Linotype")
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setWeight(75)
        self.submit.setFont(font3)
        self.restore = QLabel(self.widget)
        self.restore.setObjectName(u"restore")
        self.restore.setGeometry(QRect(50, 370, 341, 31))
        font4 = QFont()
        font4.setFamily(u"MingLiU-ExtB")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.restore.setFont(font4)
        self.appLogo = QLabel(self.widget)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setGeometry(QRect(130, 80, 161, 91))
        self.appLogo.setPixmap(QPixmap(u"logo.png"))
        self.appLogo.setScaledContents(True)
        self.appName = QLabel(self.widget)
        self.appName.setObjectName(u"appName")
        self.appName.setGeometry(QRect(130, 170, 151, 31))
        self.appName.setFont(font)
        self.appName.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"ZahirWallet", None))
        self.logo.setText("")
        self.minimize.setText(QCoreApplication.translate("Form", u"_", None))
        self.close.setText(QCoreApplication.translate("Form", u"X", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"Enter password", None))
        self.submit.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.restore.setText(QCoreApplication.translate("Form", u"Restore from seed key", None))
        self.appLogo.setText("")
        self.appName.setText(QCoreApplication.translate("Form", u"Zahir Wallet", None))
    # retranslateUi

