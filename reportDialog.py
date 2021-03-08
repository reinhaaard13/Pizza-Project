from PyQt5 import QtCore, QtGui, QtWidgets
from store import Store
from datetime import datetime
import csv

class Ui_Report(object):
    def setupUi(self, ReportDialog):
        ReportDialog.setObjectName("ReportDialog")
        ReportDialog.resize(412, 150)
        self.gridLayout = QtWidgets.QGridLayout(ReportDialog)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(ReportDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_2 = QtWidgets.QLabel(ReportDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QtWidgets.QLabel(ReportDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.dateEdit = QtWidgets.QDateEdit(ReportDialog)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.storeComboBox = QtWidgets.QComboBox(ReportDialog)
        self.storeComboBox.setObjectName("storeComboBox")
        self.addItemStoreComboBox()
        self.horizontalLayout_2.addWidget(self.storeComboBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.btnPreview = QtWidgets.QPushButton(ReportDialog)
        self.btnPreview.setObjectName("btnPreview")
        self.horizontalLayout_3.addWidget(self.btnPreview)

        self.btnPreview.clicked.connect(self.previewClicked)

        self.btnCancel = QtWidgets.QPushButton(ReportDialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.btnCancel.clicked.connect(ReportDialog.reject)

        self.retranslateUi(ReportDialog)
        QtCore.QMetaObject.connectSlotsByName(ReportDialog)

    def retranslateUi(self, ReportDialog):
        _translate = QtCore.QCoreApplication.translate
        ReportDialog.setWindowTitle(_translate("ReportDialog", "ReportDialog"))
        self.label.setText(_translate("ReportDialog", "Report"))
        self.label_2.setText(_translate("ReportDialog", "Date"))
        self.label_3.setText(_translate("ReportDialog", "Store"))
        self.btnPreview.setText(_translate("ReportDialog", "Preview"))
        self.btnCancel.setText(_translate("ReportDialog", "Cancel"))

    def previewClicked(self):
        date = self.getDate()
        transactionCounter = 0
        totalTransaction = 0
        with open('./csv/transactions.csv','r') as input:
            csv_reader = csv.DictReader(input)
            for row in csv_reader:
                if date == row['transactionDate'] and str(self.storeComboBox.currentData()) == row['storeId']:
                    transactionCounter += 1
                    totalTransaction += int(row['grandTotal'])
        print(transactionCounter)
        print(totalTransaction)
        self.previewDialog(date,transactionCounter,totalTransaction)
    
    def previewDialog(self,date,count,total):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText('Transaction Report (Press <Show Details...> to show report)')
        msg.setWindowTitle('Report')
        msg.setInformativeText("")
        msg.setDetailedText(f"At {date}, there is {count} transaction(s) with total price amount {total}")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        msg.exec_()

    def getDate(self):
        temp_date = self.dateEdit.date()
        date = str(temp_date.toPyDate())
        date = datetime.strptime(date,"%Y-%m-%d").strftime('%m/%d/%y')
        return date

    def getStore(self):
        store = Store.loadStore()
        return store

    def addItemStoreComboBox(self):
        stores = self.getStore()
        for store in stores:
            self.storeComboBox.addItem(store.name,store.id)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportDialog = QtWidgets.QDialog()
    ui = Ui_Report()
    ui.setupUi(ReportDialog)
    ReportDialog.show()
    sys.exit(app.exec_())
