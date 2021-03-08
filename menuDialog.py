import csv
from drink import Drink
from extra_topping import Topping
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Menu

class Ui_Menu(object):
    def setupUi(self, MenuDialog):
        MenuDialog.setObjectName("MenuDialog")
        MenuDialog.resize(349, 286)
        self.gridLayout = QtWidgets.QGridLayout(MenuDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(MenuDialog)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.kategoriLabel = QtWidgets.QLabel(MenuDialog)
        self.kategoriLabel.setObjectName("kategoriLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kategoriLabel)


        self.kategoriComboBox = QtWidgets.QComboBox(MenuDialog)
        self.kategoriComboBox.setObjectName("kategoriComboBox")
        self.kategoriComboBox.addItems(['Pizza','Topping','Drink'])
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kategoriComboBox)

        
        self.namaLabel = QtWidgets.QLabel(MenuDialog)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.namaLabel)


        self.namaLineEdit = QtWidgets.QLineEdit(MenuDialog)
        self.namaLineEdit.setObjectName("namaLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.namaLineEdit)


        self.hargaLabel = QtWidgets.QLabel(MenuDialog)
        self.hargaLabel.setObjectName("hargaLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.hargaLabel)


        self.hargaLineEdit = QtWidgets.QLineEdit(MenuDialog)
        self.hargaLineEdit.setObjectName("hargaLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.hargaLineEdit)


        self.infoLabel = QtWidgets.QLabel(MenuDialog)
        self.infoLabel.setObjectName("infoLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.infoLabel)


        self.infoLineEdit = QtWidgets.QLineEdit(MenuDialog)
        self.infoLineEdit.setObjectName("infoLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.infoLineEdit)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")


        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.updateCsv()


        self.saveButton = QtWidgets.QPushButton(MenuDialog)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)

        self.saveButton.clicked.connect(self.saveMenu)

        self.cancelButton = QtWidgets.QPushButton(MenuDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.cancelButton.clicked.connect(MenuDialog.reject)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(MenuDialog)
        QtCore.QMetaObject.connectSlotsByName(MenuDialog)

    def retranslateUi(self, MenuDialog):
        _translate = QtCore.QCoreApplication.translate
        MenuDialog.setWindowTitle(_translate("MenuDialog", "Create Menu Form"))
        self.label.setText(_translate("MenuDialog", "Menu"))
        self.kategoriLabel.setText(_translate("MenuDialog", "Kategori : "))
        self.namaLabel.setText(_translate("MenuDialog", "Nama : "))
        self.hargaLabel.setText(_translate("MenuDialog", "Harga : "))
        self.infoLabel.setText(_translate("MenuDialog", "Info : "))
        self.saveButton.setText(_translate("MenuDialog", "Save"))
        self.cancelButton.setText(_translate("MenuDialog", "Cancel"))

    def saveMenu(self):
        name = self.namaLineEdit.text()
        price = self.hargaLineEdit.text()
        info = self.infoLineEdit.text()
        category = self.kategoriComboBox.currentText()

        if category == "Pizza":
            newMenu = Menu(name,price,info)
            newMenu.saveMenu()
        elif category == "Topping":
            newTopping = Topping(name,price,info)
            newTopping.saveTopping()
        elif category == "Drink":
            newDrink = Drink(name,price,info)
            newDrink.saveDrink()
        
        self.successDialog()
    
    # def updateCsv(self):
    #     newHeader = []
    #     with open('transactions.csv','r') as output:
    #         csv_reader = csv.DictReader(output)

    #         with open('temp_transactions.csv','w') as input:
    #             fieldnames = newHeader
    #             csv_writer = csv.DictWriter(input,fieldnames=fieldnames)

    #             csv_writer.writeheader()
    #             for row in csv_reader:
    #                 csv_writer.writerow(row)

    def successDialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText('Save Successful!')
        msg.setWindowTitle('Save')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg.exec_()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuDialog = QtWidgets.QDialog()
    ui = Ui_Menu()
    ui.setupUi(MenuDialog)
    MenuDialog.show()
    sys.exit(app.exec_())
