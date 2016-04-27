# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created: Wed Aug 12 20:45:22 2015
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
        MainWindow.resize(442, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        
        self.lbl = QtGui.QLabel(self)
        self.qle = QtGui.QLineEdit(self)        
        self.qle.setGeometry(QtCore.QRect(30, 20, 171, 31))
        self.lbl.setGeometry(QtCore.QRect(210, 30, 171, 31))
        self.qle.textChanged[str].connect(self.onChanged)
        self.qle.setText("00:00:00:00-23:59:59:59")   
        self.lbl.adjustSize();
        
        self.selectbutton_1 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_1.setGeometry(QtCore.QRect(30, 90, 171, 31))
        self.selectbutton_1.setText(_fromUtf8(""))
        self.selectbutton_1.setObjectName(_fromUtf8("selectbutton_1"))
        self.selectbutton_2 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_2.setGeometry(QtCore.QRect(30, 120, 171, 31))
        self.selectbutton_2.setText(_fromUtf8(""))
        self.selectbutton_2.setObjectName(_fromUtf8("selectbutton_2"))
        self.selectbutton_3 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_3.setGeometry(QtCore.QRect(30, 150, 171, 31))
        self.selectbutton_3.setText(_fromUtf8(""))
        self.selectbutton_3.setObjectName(_fromUtf8("selectbutton_3"))
        self.selectbutton_4 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_4.setGeometry(QtCore.QRect(30, 180, 171, 31))
        self.selectbutton_4.setText(_fromUtf8(""))
        self.selectbutton_4.setObjectName(_fromUtf8("selectbutton_4"))
        self.selectbutton_5 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_5.setGeometry(QtCore.QRect(30, 210, 171, 31))
        self.selectbutton_5.setText(_fromUtf8(""))
        self.selectbutton_5.setObjectName(_fromUtf8("selectbutton_5"))
        self.selectbutton_6 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_6.setGeometry(QtCore.QRect(210, 90, 171, 31))
        self.selectbutton_6.setText(_fromUtf8(""))
        self.selectbutton_6.setObjectName(_fromUtf8("selectbutton_6"))
        self.selectbutton_7 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_7.setGeometry(QtCore.QRect(210, 120, 171, 31))
        self.selectbutton_7.setText(_fromUtf8(""))
        self.selectbutton_7.setObjectName(_fromUtf8("selectbutton_7"))
        self.selectbutton_8 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_8.setGeometry(QtCore.QRect(210, 150, 171, 31))
        self.selectbutton_8.setText(_fromUtf8(""))
        self.selectbutton_8.setObjectName(_fromUtf8("selectbutton_8"))
        self.selectbutton_9 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_9.setGeometry(QtCore.QRect(210, 180, 171, 31))
        self.selectbutton_9.setText(_fromUtf8(""))
        self.selectbutton_9.setObjectName(_fromUtf8("selectbutton_9"))
        self.selectbutton_10 = QtGui.QPushButton(self.centralwidget)
        self.selectbutton_10.setGeometry(QtCore.QRect(210, 210, 171, 31))
        self.selectbutton_10.setText(_fromUtf8(""))        
        self.selectbutton_10.setObjectName(_fromUtf8("selectbutton_10"))

        self.nextbutton = QtGui.QPushButton(self.centralwidget)
        self.nextbutton.setGeometry(QtCore.QRect(390, 250, 31, 31))        
        self.nextbutton.setObjectName(_fromUtf8("nextbutton"))

        self.neffbutton = QtGui.QPushButton(self.centralwidget)
        self.neffbutton.setGeometry(QtCore.QRect(30, 250, 31, 31))        
        self.neffbutton.setObjectName(_fromUtf8("neffbutton"))
        self.neffbutton.setText(_fromUtf8("←"))

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # WangChunShan
        self.button =[]
        self.button.append(self.selectbutton_1)
        self.button.append(self.selectbutton_2)
        self.button.append(self.selectbutton_3)
        self.button.append(self.selectbutton_4)
        self.button.append(self.selectbutton_5)
        self.button.append(self.selectbutton_6)
        self.button.append(self.selectbutton_7)
        self.button.append(self.selectbutton_8)
        self.button.append(self.selectbutton_9)
        self.button.append(self.selectbutton_10)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "分析數據，請選擇日期或關閉視窗", None))
        self.nextbutton.setText(_translate("MainWindow", "→", None))
        
    def onChanged(self, text):        
        self.lbl.setText('input timeform: '+text)        
        self.lbl.setStyleSheet('color: red')
        #self.lbl.adjustSize()    
    
