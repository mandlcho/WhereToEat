# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wheretoeat.ui'
#
# Created: Sun Dec  2 16:39:27 2018
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(279, 190)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btn_Tellme = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Tellme.sizePolicy().hasHeightForWidth())
        self.btn_Tellme.setSizePolicy(sizePolicy)
        self.btn_Tellme.setObjectName(_fromUtf8("btn_Tellme"))
        self.verticalLayout_2.addWidget(self.btn_Tellme)
        self.btn_Surpriseme = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Surpriseme.sizePolicy().hasHeightForWidth())
        self.btn_Surpriseme.setSizePolicy(sizePolicy)
        self.btn_Surpriseme.setMaximumSize(QtCore.QSize(227, 32))
        self.btn_Surpriseme.setFlat(False)
        self.btn_Surpriseme.setObjectName(_fromUtf8("btn_Surpriseme"))
        self.verticalLayout_2.addWidget(self.btn_Surpriseme)
        self.Le_showresult = QtGui.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.Le_showresult.setFont(font)
        self.Le_showresult.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Le_showresult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Le_showresult.setAlignment(QtCore.Qt.AlignCenter)
        self.Le_showresult.setReadOnly(True)
        self.Le_showresult.setObjectName(_fromUtf8("Le_showresult"))
        self.verticalLayout_2.addWidget(self.Le_showresult)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Where To Eat", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Tellme.setText(QtGui.QApplication.translate("MainWindow", "Tell Me", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Surpriseme.setText(QtGui.QApplication.translate("MainWindow", "Surprise Me", None, QtGui.QApplication.UnicodeUTF8))
        self.Le_showresult.setText(QtGui.QApplication.translate("MainWindow", "display result here", None, QtGui.QApplication.UnicodeUTF8))

