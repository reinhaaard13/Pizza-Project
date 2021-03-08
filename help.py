from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName("HelpDialog")
        HelpDialog.resize(411, 292)
        self.gridLayout_2 = QtWidgets.QGridLayout(HelpDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(HelpDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(HelpDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(HelpDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(HelpDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(HelpDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(HelpDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(HelpDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(HelpDialog)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(HelpDialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 1, 1, 1)

        self.label_10 = QtWidgets.QLabel(HelpDialog)
        self.label_10.setObjectName("label_10")
        self.label_10.setText("View :")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(HelpDialog)
        self.label_11.setObjectName("label_11")
        self.label_11.setText("View table of registered stores and menus")
        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.pushButton = QtWidgets.QPushButton(HelpDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)

        self.pushButton.clicked.connect(HelpDialog.reject)

        self.retranslateUi(HelpDialog)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        _translate = QtCore.QCoreApplication.translate
        HelpDialog.setWindowTitle(_translate("HelpDialog", "HelpDialog"))
        self.label.setText(_translate("HelpDialog", "Help"))
        self.label_4.setText(_translate("HelpDialog", "Menu :"))
        self.label_2.setText(_translate("HelpDialog", "Store :"))
        self.label_3.setText(_translate("HelpDialog", "Register new store"))
        self.label_6.setText(_translate("HelpDialog", "Transaction :"))
        self.label_5.setText(_translate("HelpDialog", "Register new menu (pizza, topping, drinks)"))
        self.label_7.setText(_translate("HelpDialog", "Make a transaction"))
        self.label_8.setText(_translate("HelpDialog", "Report :"))
        self.label_9.setText(_translate("HelpDialog", "View cumulative transaction record in selected date and store"))
        self.pushButton.setText(_translate("HelpDialog", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpDialog = QtWidgets.QDialog()
    ui = Ui_Help()
    ui.setupUi(HelpDialog)
    HelpDialog.show()
    sys.exit(app.exec_())
