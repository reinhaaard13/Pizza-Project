from store import Store
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle

class Ui_Store(object):
    def setupUi(self, StoreDialog):
        StoreDialog.setObjectName("StoreDialog")
        StoreDialog.resize(346, 316)
        self.gridLayout = QtWidgets.QGridLayout(StoreDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(StoreDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")


        self.namaLabel = QtWidgets.QLabel(StoreDialog)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.namaLabel)


        self.namaLineEdit = QtWidgets.QLineEdit(StoreDialog)
        self.namaLineEdit.setObjectName("namaLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.namaLineEdit)


        self.alamatLabel = QtWidgets.QLabel(StoreDialog)
        self.alamatLabel.setObjectName("alamatLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.alamatLabel)


        self.alamatLineEdit = QtWidgets.QLineEdit(StoreDialog)
        self.alamatLineEdit.setObjectName("alamatLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.alamatLineEdit)


        self.kotaLabel = QtWidgets.QLabel(StoreDialog)
        self.kotaLabel.setObjectName("kotaLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.kotaLabel)


        self.kotaComboBox = QtWidgets.QComboBox(StoreDialog)
        self.kotaComboBox.setObjectName("kotaComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kotaComboBox)
        kota = ['Jakarta','Bogor','Depok','Tangerang','Bekasi']
        for i in kota:
            self.kotaComboBox.addItem(i)


        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.saveButton = QtWidgets.QPushButton(StoreDialog)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)

        self.saveButton.clicked.connect(self.saveStore)

        self.cancelButton = QtWidgets.QPushButton(StoreDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)

        self.cancelButton.clicked.connect(StoreDialog.reject)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(StoreDialog)
        QtCore.QMetaObject.connectSlotsByName(StoreDialog)

    def retranslateUi(self, StoreDialog):
        _translate = QtCore.QCoreApplication.translate
        StoreDialog.setWindowTitle(_translate("StoreDialog", "Store Form"))
        self.label.setText(_translate("StoreDialog", "Store"))
        self.namaLabel.setText(_translate("StoreDialog", "Nama : "))
        self.alamatLabel.setText(_translate("StoreDialog", "Alamat : "))
        self.kotaLabel.setText(_translate("StoreDialog", "Kota : "))
        self.saveButton.setText(_translate("StoreDialog", "Save"))
        self.cancelButton.setText(_translate("StoreDialog", "Cancel"))

    def saveStore(self):
        nama =  self.namaLineEdit.text()
        alamat = self.alamatLineEdit.text()
        kota = self.kotaComboBox.currentText()

        newStore = Store(nama,alamat,kota)
        newStore.saveStore()

        print('saved!')
        self.successStoreDialog()
    
    def successStoreDialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText('Save Successful!')
        msg.setWindowTitle('Save')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StoreDialog = QtWidgets.QDialog()
    ui = Ui_Store()
    ui.setupUi(StoreDialog)
    StoreDialog.show()
    sys.exit(app.exec_())
