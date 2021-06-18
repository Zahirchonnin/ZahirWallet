# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Send(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("SEND")
        self.resize(430, 423)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setStyleSheet("QPushButton#back {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: 3px solid white;\n"
"    border-radius: 5px;    \n"
"    font: 75 14pt \"Myanmar Text\";\n"
"}\n"
"\n"
"QPushButton#back::hover {\n"
"    border: 2px solid white\n"
"}\n"
"\n"
"\n"
"QPushButton#back::pressed {\n"
"    background-color:  rgb(163, 77, 163)\n"
"}\n"
"\n"
"QPushButton#send {\n"
"    background-color: rgb(163, 77, 163);\n"
"    border: 3px solid white;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font: 75 10pt \"Verdana\";\n"
"}\n"
"\n"
"QPushButton#send::hover {\n"
"    border: 2px solid white;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton#send::pressed {\n"
"    background-color: rgb(139, 65, 139)\n"
"}\n"
"\n"
"QLabel{\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    color: rgb(238, 238, 238)\n"
"}\n"
"QLineEdit, QSpinBox {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    border: 3px solid white;\n"
"    border-radius: 5px;\n"
"    \n"
"    font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"QLineEdit::focus, QSpinBox::focus {\n"
"    border-color: #CA8ACA\n"
"}")
        self.widget.setObjectName("widget")
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.back.setMinimumSize(QtCore.QSize(40, 30))
        self.back.setMaximumSize(QtCore.QSize(1987, 109000))
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphic/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QtCore.QSize(30, 30))
        self.back.setObjectName("back")
        self.send = QtWidgets.QPushButton(self.widget)
        self.send.setGeometry(QtCore.QRect(240, 170, 151, 51))
        self.send.setObjectName("send")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(90, 280, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.amount = QtWidgets.QSpinBox(self.widget)
        self.amount.setGeometry(QtCore.QRect(20, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.amount.setFont(font)
        self.amount.setObjectName("amount")
        self.To = QtWidgets.QLineEdit(self.widget)
        self.To.setGeometry(QtCore.QRect(20, 100, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.To.setFont(font)
        self.To.setObjectName("To")
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SEND", "SEND"))
        self.send.setText(_translate("SEND", "send"))
        self.label.setText(_translate("SEND", "Send Transaction"))
        self.amount.setSpecialValueText(_translate("SEND", "Amount"))
        self.To.setPlaceholderText(_translate("SEND", "Recipient Address"))
