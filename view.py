from menu import Menu
from PyQt5 import QtCore, QtGui, QtWidgets
from store import Store

class Ui_ViewDialog(object):
    def setupUi(self, ViewDialog):
        ViewDialog.setObjectName("ViewDialog")
        ViewDialog.resize(490, 439)
        self.gridLayout = QtWidgets.QGridLayout(ViewDialog)
        self.gridLayout.setObjectName("gridLayout")

        self.label = QtWidgets.QLabel(ViewDialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.tableStores = QtWidgets.QTableWidget(ViewDialog)
        self.tableStores.setColumnCount(4)
        self.tableStores.setObjectName("tableStores")
        self.tableStores.setRowCount(0)
        self.tableStores.horizontalHeader().setVisible(True)
        self.tableStores.horizontalHeader().setCascadingSectionResizes(False)
        self.tableStores.horizontalHeader().setHighlightSections(True)
        self.tableStores.horizontalHeader().setSortIndicatorShown(False)
        self.tableStores.verticalHeader().setVisible(False)

        self.tableStores.setHorizontalHeaderLabels(("Id;Name;Address;City").split(';'))
        self.tableStores.resizeColumnToContents(0)

        # Load store data
        self.getStoreData()

        self.gridLayout.addWidget(self.tableStores, 1, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(ViewDialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)


        self.tableMenus = QtWidgets.QTableWidget(ViewDialog)
        self.tableMenus.setColumnCount(5)
        self.tableMenus.setObjectName("tableMenus")
        self.tableMenus.setRowCount(0)
        self.tableMenus.verticalHeader().setVisible(False)
        
        self.tableMenus.setHorizontalHeaderLabels(("Id;Category;Name;Price;Info").split(';'))
        self.tableMenus.resizeColumnToContents(0)

        self.getMenuData()

        self.gridLayout.addWidget(self.tableMenus, 3, 0, 1, 1)


        self.retranslateUi(ViewDialog)
        QtCore.QMetaObject.connectSlotsByName(ViewDialog)

    def retranslateUi(self, ViewDialog):
        _translate = QtCore.QCoreApplication.translate
        ViewDialog.setWindowTitle(_translate("ViewDialog", "View Store and Menu"))
        self.label.setText(_translate("ViewDialog", "Stores"))
        self.label_2.setText(_translate("ViewDialog", "Menus"))

    def getStoreData(self):
        loadedStore = Store.loadStore()
        for store in loadedStore :
            rowPosition = self.tableStores.rowCount()
            self.tableStores.insertRow(rowPosition)
            self.tableStores.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(store.id)))
            self.tableStores.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(store.name))
            self.tableStores.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(store.address))
            self.tableStores.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(store.city))

    def getMenuData(self):
        loadedMenu = Menu.loadMenu()
        for menu in loadedMenu:
            rowPosition = self.tableMenus.rowCount()
            self.tableMenus.insertRow(rowPosition)
            self.tableMenus.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(menu.id)))
            self.tableMenus.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(menu.category))
            self.tableMenus.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(menu.name))
            self.tableMenus.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem("Rp " + menu.price))
            self.tableMenus.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(menu.info))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ViewDialog = QtWidgets.QDialog()
    ui = Ui_ViewDialog()
    ui.setupUi(ViewDialog)
    ViewDialog.show()
    sys.exit(app.exec_())
