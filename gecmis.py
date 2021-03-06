# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gecmis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gecmis(object):
    def setupUi(self, Gecmis):
        Gecmis.setObjectName("Gecmis")
        Gecmis.resize(885, 463)
        Gecmis.setMinimumSize(QtCore.QSize(800, 350))
        Gecmis.setMaximumSize(QtCore.QSize(1300, 750))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Gecmis.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Gecmis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.isimara_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.isimara_lineEdit.setFont(font)
        self.isimara_lineEdit.setObjectName("isimara_lineEdit")
        self.horizontalLayout_2.addWidget(self.isimara_lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tcara_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tcara_lineEdit.setFont(font)
        self.tcara_lineEdit.setObjectName("tcara_lineEdit")
        self.horizontalLayout_2.addWidget(self.tcara_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.garama_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.garama_pushButton.setFont(font)
        self.garama_pushButton.setAutoRepeat(False)
        self.garama_pushButton.setAutoDefault(False)
        self.garama_pushButton.setObjectName("garama_pushButton")
        self.horizontalLayout_2.addWidget(self.garama_pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gecmis_cikis_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gecmis_cikis_pushButton.setFont(font)
        self.gecmis_cikis_pushButton.setObjectName("gecmis_cikis_pushButton")
        self.horizontalLayout_2.addWidget(self.gecmis_cikis_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(1250, 750))
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 865, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gecmis_bilgi_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.gecmis_bilgi_label.setMinimumSize(QtCore.QSize(740, 0))
        self.gecmis_bilgi_label.setText("")
        self.gecmis_bilgi_label.setObjectName("gecmis_bilgi_label")
        self.verticalLayout_2.addWidget(self.gecmis_bilgi_label)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toplamgelir_lable = QtWidgets.QLabel(self.centralwidget)
        self.toplamgelir_lable.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toplamgelir_lable.setFont(font)
        self.toplamgelir_lable.setLineWidth(1)
        self.toplamgelir_lable.setObjectName("toplamgelir_lable")
        self.horizontalLayout_3.addWidget(self.toplamgelir_lable)
        self.toplamkisi_label = QtWidgets.QLabel(self.centralwidget)
        self.toplamkisi_label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.toplamkisi_label.setFont(font)
        self.toplamkisi_label.setObjectName("toplamkisi_label")
        self.horizontalLayout_3.addWidget(self.toplamkisi_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        Gecmis.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Gecmis)
        self.statusbar.setObjectName("statusbar")
        Gecmis.setStatusBar(self.statusbar)

        self.retranslateUi(Gecmis)
        QtCore.QMetaObject.connectSlotsByName(Gecmis)

    def retranslateUi(self, Gecmis):
        _translate = QtCore.QCoreApplication.translate
        Gecmis.setWindowTitle(_translate("Gecmis", "Ge??mi?? Veri"))
        self.label.setText(_translate("Gecmis", "??sim Soyisim : "))
        self.label_2.setText(_translate("Gecmis", "T.C. Numaras?? : "))
        self.garama_pushButton.setText(_translate("Gecmis", "Arama"))
        self.gecmis_cikis_pushButton.setText(_translate("Gecmis", "????k????"))
        self.toplamgelir_lable.setText(_translate("Gecmis", "ff"))
        self.toplamkisi_label.setText(_translate("Gecmis", "ff"))
