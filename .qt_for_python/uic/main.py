# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        Form.resize(424, 424)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#account_options {\n"
"	background-color: rgb(148, 67, 148);\n"
"	border: 3px solid white;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLabel {\n"
"	color: white;\n"
"	\n"
"	font: 75 16pt \"Myanmar Text\";\n"
"}\n"
"\n"
"QLabel::hover {\n"
"	color: rgb(234, 234, 234)\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent\n"
"}\n"
"\n"
"QPushButton#import_2, QPushButton#send, QPushButton#create {\n"
"	border: 3px solid white;\n"
"	color: black;\n"
"	border-radius: 5px;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton#import_2::hover, QPushButton#send::hover, QPushButton#create::hover {\n"
"	background-color: rgb(141, 63, 141)\n"
"}\n"
"\n"
"QPushButton#import_2::pressed, QPushButton#send::pressed, QPushButton#create::pressed {\n"
"	background-color: rgb(130, 58, 130);\n"
"	padding-left: 3px;\n"
"	paddind-top: 3px\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"	width: 198px;\n"
"	height: 20px;\n"
"	padding-bottom: 5px;\n"
"	color: white;\n"
"	font: 75 14pt \"Urdu Typesetting\";\n"
"}\n"
"\n"
"QTabBa"
                        "r:tab:!selected {\n"
"	border: 3px solid black;\n"
"	border-bottom: 0;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(165, 78, 165)\n"
"}\n"
"\n"
"QTabBar:tab:!selected::hover {\n"
"	background-color: rgb(150, 71, 150)\n"
"}\n"
"\n"
"QPushButton#add_token {\n"
"	height: 20px;\n"
"	\n"
"	font: 12pt \"Myanmar Text\";\n"
"	background-color: rgb(0, 255, 191);\n"
"	border: white;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QPushButton#add_token::hover {\n"
"	background-color: rgb(0, 240, 176)	\n"
"}\n"
"\n"
"QPushButton#add_token::pressed {\n"
"	background-color: rgb(0, 234, 172)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 120, 411, 291))
        self.transaction = QWidget()
        self.transaction.setObjectName(u"transaction")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transaction.sizePolicy().hasHeightForWidth())
        self.transaction.setSizePolicy(sizePolicy)
        self.transaction.setBaseSize(QSize(44, 0))
        self.verticalLayout_3 = QVBoxLayout(self.transaction)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scrollArea = QScrollArea(self.transaction)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 385, 238))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.transaction, "")
        self.tokens = QWidget()
        self.tokens.setObjectName(u"tokens")
        self.verticalLayout_2 = QVBoxLayout(self.tokens)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_token = QPushButton(self.tokens)
        self.add_token.setObjectName(u"add_token")

        self.verticalLayout_2.addWidget(self.add_token)

        self.scrollArea_2 = QScrollArea(self.tokens)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 385, 212))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tokens, "")
        self.account_options = QFrame(self.frame)
        self.account_options.setObjectName(u"account_options")
        self.account_options.setGeometry(QRect(-1, -1, 411, 111))
        self.account_options.setFrameShape(QFrame.StyledPanel)
        self.account_options.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.account_options)
        self.gridLayout.setObjectName(u"gridLayout")
        self.account_name = QLabel(self.account_options)
        self.account_name.setObjectName(u"account_name")

        self.gridLayout.addWidget(self.account_name, 0, 0, 1, 1)

        self.import_2 = QPushButton(self.account_options)
        self.import_2.setObjectName(u"import_2")

        self.gridLayout.addWidget(self.import_2, 0, 2, 1, 1)

        self.account_address = QLabel(self.account_options)
        self.account_address.setObjectName(u"account_address")

        self.gridLayout.addWidget(self.account_address, 1, 0, 1, 1)

        self.create = QPushButton(self.account_options)
        self.create.setObjectName(u"create")

        self.gridLayout.addWidget(self.create, 1, 2, 1, 1)

        self.balance = QLabel(self.account_options)
        self.balance.setObjectName(u"balance")

        self.gridLayout.addWidget(self.balance, 2, 0, 1, 1)

        self.send = QPushButton(self.account_options)
        self.send.setObjectName(u"send")

        self.gridLayout.addWidget(self.send, 2, 2, 1, 1)

        self.copy = QPushButton(self.account_options)
        self.copy.setObjectName(u"copy")
        icon = QIcon()
        icon.addFile(u"copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copy.setIcon(icon)

        self.gridLayout.addWidget(self.copy, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.import_2, self.create)
        QWidget.setTabOrder(self.create, self.send)
        QWidget.setTabOrder(self.send, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.copy)
        QWidget.setTabOrder(self.copy, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.scrollArea_2)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transaction), QCoreApplication.translate("Form", u"transaction", None))
        self.add_token.setText(QCoreApplication.translate("Form", u"+ Add Token", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tokens), QCoreApplication.translate("Form", u"Tokens", None))
        self.account_name.setText(QCoreApplication.translate("Form", u"name", None))
        self.import_2.setText(QCoreApplication.translate("Form", u"import", None))
        self.account_address.setText(QCoreApplication.translate("Form", u"address", None))
        self.create.setText(QCoreApplication.translate("Form", u"create", None))
        self.balance.setText(QCoreApplication.translate("Form", u"balance", None))
        self.send.setText(QCoreApplication.translate("Form", u"Send", None))
#if QT_CONFIG(tooltip)
        self.copy.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.copy.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.copy.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.copy.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.copy.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.copy.setText("")
    # retranslateUi

