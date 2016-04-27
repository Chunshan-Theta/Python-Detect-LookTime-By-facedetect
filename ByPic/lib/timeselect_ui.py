# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeselect.ui'
#
# Created: Sat Oct 24 18:09:55 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(442, 251)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(30, 30, 131, 81))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.timeEdit_2 = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit_2.setGeometry(QtCore.QRect(250, 30, 121, 81))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 130, 71, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuJj = QtGui.QMenu(self.menubar)
        self.menuJj.setObjectName(_fromUtf8("menuJj"))
        self.menuL = QtGui.QMenu(self.menubar)
        self.menuL.setObjectName(_fromUtf8("menuL"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuJj.addSeparator()
        self.menubar.addAction(self.menuJj.menuAction())
        self.menubar.addAction(self.menuL.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "確定", None))
        self.menuJj.setTitle(_translate("MainWindow", "請選擇時間", None))
        self.menuL.setTitle(_translate("MainWindow", "!", None))

