# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/tokenExcutor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Excutor(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setObjectName("Excutor")
        self.resize(426, 430)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("QLineEdit, #_value {\n"
"    background-color: transparent;\n"
"    border: 3px solid white;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font: 75 12pt \"Myanmar Text\";\n"
"    height: 25px\n"
"}\n"
"\n"
"QLineEdit:focus, #_value::focus, #methods::focus {\n"
"    border-color: rgb(209, 99, 209);\n"
"    border-radius: 6px\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white;\n"
"    background-color: #B154B1;\n"
"    border: 1px solid rgb(197, 93, 197);\n"
"    border-radius: 5px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: #CA8ACA;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border-color: white\n"
"}\n"
"\n"
"#methods {\n"
"    background-color: transparent;\n"
"    border: 4px solid white;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font: 75 14pt \"Verdana\";\n"
"}\n"
"\n"
"#result {\n"
"    background-color: rgba(189, 129, 189, 100);color: white;\n"
"    border: 3px solid #CA8ACA;\n"
"    border-radius: 5px;\n"
"    font: 75 25pt \"Verdana\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.methods = QtWidgets.QComboBox(self.frame)
        self.methods.setGeometry(QtCore.QRect(10, 60, 391, 31))
        self.methods.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.methods.setObjectName("methods")
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")
        self.methods.addItem("")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphic/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName("back")
        self.result = QtWidgets.QLabel(self.frame)
        self.result.setGeometry(QtCore.QRect(10, 290, 391, 101))
        self.result.setObjectName("result")
        self._from = QtWidgets.QLineEdit(self.frame)
        self._from.setGeometry(QtCore.QRect(10, 110, 391, 41))
        self._from.setObjectName("_from")
        self._to = QtWidgets.QLineEdit(self.frame)
        self._to.setGeometry(QtCore.QRect(10, 160, 391, 41))
        self._to.setObjectName("_to")
        self._value = QtWidgets.QSpinBox(self.frame)
        self._value.setGeometry(QtCore.QRect(11, 220, 251, 51))
        self._value.setObjectName("_value")
        self.excute = QtWidgets.QPushButton(self.frame)
        self.excute.setGeometry(QtCore.QRect(274, 220, 121, 51))
        self.excute.setObjectName("excute")
        self.horizontalLayout.addWidget(self.frame)
        self._from.hide()
        self._to.hide()
        self._value.hide()
        self.result.hide()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Excutor", "Excutor"))
        self.methods.setItemText(0, _translate("Excutor", "totalSupply"))
        self.methods.setItemText(1, _translate("Excutor", "transfer"))
        self.methods.setItemText(2, _translate("Excutor", "transferFrom"))
        self.methods.setItemText(3, _translate("Excutor", "approve"))
        self.methods.setItemText(4, _translate("Excutor", "balanceOf"))
        self.methods.setItemText(5, _translate("Excutor", "allowance"))
        self.result.setText(_translate("Excutor", "TextLabel"))
        self.excute.setText(_translate("Excutor", "Excute"))
