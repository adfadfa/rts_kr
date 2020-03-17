# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\wigettest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


self.lnEditCurrentNS = QtGui.QLineEdit(self) # This is my QLineEdit

my_string = 'none'
self.lnEditCurrentNS.textChanged.connect(self.onSelectedValue)

def onSelectedValue(self):
    selectedValue = self.txtEditCurrentNS.displayText()
    my_string = selectedValue
    sys.exit(app.exec_())

    

