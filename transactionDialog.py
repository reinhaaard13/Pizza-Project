from PyQt5 import QtCore, QtGui, QtWidgets
from store import Store
from datetime import datetime
from menu import Menu
import csv

class Ui_TransactionDialog(object):

    def setupUi(self, transactionDialog):
        self.transactionDialog = transactionDialog
        transactionDialog.setObjectName("transactionDialog")
        transactionDialog.resize(465, 478)
        self.gridLayout = QtWidgets.QGridLayout(transactionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_49 = QtWidgets.QLabel(transactionDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.horizontalLayout_14.addWidget(self.label_49)

        # Combo box Store
        self.storeComboBox_4 = QtWidgets.QComboBox(transactionDialog)
        self.storeComboBox_4.setObjectName("storeComboBox_4")
        self.addItemStoreComboBox()
        self.horizontalLayout_14.addWidget(self.storeComboBox_4)
        self.gridLayout.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        # Tanggal Transaksi
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_50 = QtWidgets.QLabel(transactionDialog)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_15.addWidget(self.label_50)
        self.tanggalTransaksi_4 = QtWidgets.QLabel(transactionDialog)
        self.tanggalTransaksi_4.setText(self.setTime())
        self.tanggalTransaksi_4.setObjectName("tanggalTransaksi_4")
        self.horizontalLayout_15.addWidget(self.tanggalTransaksi_4)

        # Nomor Order
        self.label_51 = QtWidgets.QLabel(transactionDialog)
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_15.addWidget(self.label_51)
        self.nomorOrder_4 = QtWidgets.QLabel(transactionDialog)
        self.nomorOrder_4.setText(str(self.getOrderNo()))
        self.nomorOrder_4.setObjectName("nomorOrder_4")
        self.horizontalLayout_15.addWidget(self.nomorOrder_4)
        self.gridLayout.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)


        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_78 = QtWidgets.QVBoxLayout()
        self.verticalLayout_78.setObjectName("verticalLayout_78")
        self.label_52 = QtWidgets.QLabel(transactionDialog)
        self.label_52.setObjectName("label_52")
        self.verticalLayout_78.addWidget(self.label_52)
        self.gridLayout_11.addLayout(self.verticalLayout_78, 0, 1, 1, 1)


        self.verticalLayout_79 = QtWidgets.QVBoxLayout()
        self.verticalLayout_79.setObjectName("verticalLayout_79")
        self.label_53 = QtWidgets.QLabel(transactionDialog)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_79.addWidget(self.label_53)
        self.gridLayout_11.addLayout(self.verticalLayout_79, 0, 2, 1, 1)


        self.verticalLayout_80 = QtWidgets.QVBoxLayout()
        self.verticalLayout_80.setObjectName("verticalLayout_80")
        self.label_54 = QtWidgets.QLabel(transactionDialog)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_80.addWidget(self.label_54)
        self.gridLayout_11.addLayout(self.verticalLayout_80, 0, 0, 1, 1)


        self.verticalLayout_81 = QtWidgets.QVBoxLayout()
        self.verticalLayout_81.setObjectName("verticalLayout_81")
        self.label_55 = QtWidgets.QLabel(transactionDialog)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_81.addWidget(self.label_55)
        self.gridLayout_11.addLayout(self.verticalLayout_81, 0, 3, 1, 1)

        # Pizza Check Box
        self.pizzaLayout = QtWidgets.QVBoxLayout()
        self.pizzaLayout.setObjectName("pizzaLayout")
        
        # Jumlah Pizza
        self.jumlahPizzaLayout = QtWidgets.QVBoxLayout()
        self.jumlahPizzaLayout.setObjectName("jumlahPizzaLayout")
        
        # Harga Pizza
        self.hargaPizzaLayout = QtWidgets.QVBoxLayout()
        self.hargaPizzaLayout.setObjectName("hargaPizzaLayout")
       

        # Total harga pizza
        self.totalHargaPizzaLayout = QtWidgets.QVBoxLayout()
        self.totalHargaPizzaLayout.setObjectName("totalHargaPizzaLayout")

        # unite layouts
        self.gridLayout_11.addLayout(self.pizzaLayout, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.jumlahPizzaLayout, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.hargaPizzaLayout, 1, 2, 1, 1)
        self.gridLayout_11.addLayout(self.totalHargaPizzaLayout, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_11, 2, 0, 1, 1)


        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_86 = QtWidgets.QVBoxLayout()
        self.verticalLayout_86.setObjectName("verticalLayout_86")
        self.label_56 = QtWidgets.QLabel(transactionDialog)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_86.addWidget(self.label_56)
        self.gridLayout_12.addLayout(self.verticalLayout_86, 0, 1, 1, 1)


        self.verticalLayout_87 = QtWidgets.QVBoxLayout()
        self.verticalLayout_87.setObjectName("verticalLayout_87")
        self.label_57 = QtWidgets.QLabel(transactionDialog)
        self.label_57.setObjectName("label_57")
        self.verticalLayout_87.addWidget(self.label_57)
        self.gridLayout_12.addLayout(self.verticalLayout_87, 0, 2, 1, 1)


        self.verticalLayout_88 = QtWidgets.QVBoxLayout()
        self.verticalLayout_88.setObjectName("verticalLayout_88")
        self.label_58 = QtWidgets.QLabel(transactionDialog)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_88.addWidget(self.label_58)
        self.gridLayout_12.addLayout(self.verticalLayout_88, 0, 0, 1, 1)


        self.verticalLayout_89 = QtWidgets.QVBoxLayout()
        self.verticalLayout_89.setObjectName("verticalLayout_89")
        self.label_59 = QtWidgets.QLabel(transactionDialog)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_89.addWidget(self.label_59)
        self.gridLayout_12.addLayout(self.verticalLayout_89, 0, 3, 1, 1)

        # ++++ TOPPING ++++
        # Topping Checkbox
        self.toppingLayout = QtWidgets.QVBoxLayout()
        self.toppingLayout.setObjectName("toppingLayout")

        # Topping Jumlah
        self.toppingJumlahLayout = QtWidgets.QVBoxLayout()
        self.toppingJumlahLayout.setObjectName("toppingJumlahLayout")

        # Topping Harga
        self.toppingHargaLayout = QtWidgets.QVBoxLayout()
        self.toppingHargaLayout.setObjectName("toppingHargaLayout")

        # Topping Total Harga
        self.toppingTotalHargaLayout = QtWidgets.QVBoxLayout()
        self.toppingTotalHargaLayout.setObjectName("toppingTotalHargaLayout")

        # Unite topping layout
        self.gridLayout_12.addLayout(self.toppingLayout, 1, 0, 1, 1)
        self.gridLayout_12.addLayout(self.toppingJumlahLayout, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.toppingHargaLayout, 1, 2, 1, 1)
        self.gridLayout_12.addLayout(self.toppingTotalHargaLayout, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_12, 3, 0, 1, 1)


        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_94 = QtWidgets.QVBoxLayout()
        self.verticalLayout_94.setObjectName("verticalLayout_94")
        self.label_60 = QtWidgets.QLabel(transactionDialog)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_94.addWidget(self.label_60)
        self.gridLayout_13.addLayout(self.verticalLayout_94, 0, 1, 1, 1)


        self.verticalLayout_95 = QtWidgets.QVBoxLayout()
        self.verticalLayout_95.setObjectName("verticalLayout_95")
        self.label_61 = QtWidgets.QLabel(transactionDialog)
        self.label_61.setObjectName("label_61")
        self.verticalLayout_95.addWidget(self.label_61)
        self.gridLayout_13.addLayout(self.verticalLayout_95, 0, 2, 1, 1)


        self.verticalLayout_96 = QtWidgets.QVBoxLayout()
        self.verticalLayout_96.setObjectName("verticalLayout_96")
        self.label_62 = QtWidgets.QLabel(transactionDialog)
        self.label_62.setObjectName("label_62")
        self.verticalLayout_96.addWidget(self.label_62)
        self.gridLayout_13.addLayout(self.verticalLayout_96, 0, 0, 1, 1)


        self.verticalLayout_97 = QtWidgets.QVBoxLayout()
        self.verticalLayout_97.setObjectName("verticalLayout_97")
        self.label_63 = QtWidgets.QLabel(transactionDialog)
        self.label_63.setObjectName("label_63")
        self.verticalLayout_97.addWidget(self.label_63)
        self.gridLayout_13.addLayout(self.verticalLayout_97, 0, 3, 1, 1)

        # Check Box Minuman
        self.drinkLayout = QtWidgets.QVBoxLayout()
        self.drinkLayout.setObjectName("drinkLayout")

        # Jumlah Minuman
        self.drinkJumlahLayout = QtWidgets.QVBoxLayout()
        self.drinkJumlahLayout.setObjectName("drinkJumlahLayout")

        # Harga Minuman
        self.drinkHargaLayout = QtWidgets.QVBoxLayout()
        self.drinkHargaLayout.setObjectName("drinkHargaLayout")

        # Total Harga Minuman
        self.drinkTotalHargaLayout = QtWidgets.QVBoxLayout()
        self.drinkTotalHargaLayout.setObjectName("drinkTotalHargaLayout")

        # Get data of the menus
        self.getMenu(transactionDialog)
        # self.countTotal()

        # unite drinks layout
        self.gridLayout_13.addLayout(self.drinkLayout, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.drinkJumlahLayout, 1, 1, 1, 1)
        self.gridLayout_13.addLayout(self.drinkHargaLayout, 1, 2, 1, 1)
        self.gridLayout_13.addLayout(self.drinkTotalHargaLayout, 1, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_13, 4, 0, 1, 1)


        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.label_64 = QtWidgets.QLabel(transactionDialog)
        self.label_64.setObjectName("label_64")
        self.horizontalLayout_16.addWidget(self.label_64)
        self.grandTotal_4 = QtWidgets.QLabel(transactionDialog)
        self.grandTotal_4.setObjectName("grandTotal_4")
        self.grandTotal_4.setText('0')
        self.horizontalLayout_16.addWidget(self.grandTotal_4)
        self.gridLayout.addLayout(self.horizontalLayout_16, 5, 0, 1, 1)


        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)

        # ==== BUTTON ====
        self.pushButton_8 = QtWidgets.QPushButton(transactionDialog)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_17.addWidget(self.pushButton_8)

        self.pushButton_8.clicked.connect(self.makeOrder)

        self.pushButton_7 = QtWidgets.QPushButton(transactionDialog)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_17.addWidget(self.pushButton_7)

        self.pushButton_7.clicked.connect(transactionDialog.reject)

        self.gridLayout.addLayout(self.horizontalLayout_17, 6, 0, 1, 1)


        self.retranslateUi(transactionDialog)
        QtCore.QMetaObject.connectSlotsByName(transactionDialog)
        

    def retranslateUi(self, transactionDialog):
        _translate = QtCore.QCoreApplication.translate
        transactionDialog.setWindowTitle(_translate("transactionDialog", "Make a Transaction"))
        self.label_49.setText(_translate("transactionDialog", "Store : "))
        self.label_50.setText(_translate("transactionDialog", "Tgl Transaksi"))
        self.label_51.setText(_translate("transactionDialog", "Order No."))
        self.label_52.setText(_translate("transactionDialog", "Jumlah"))
        self.label_53.setText(_translate("transactionDialog", "Harga"))
        self.label_54.setText(_translate("transactionDialog", "Pizza"))
        self.label_55.setText(_translate("transactionDialog", "Total Harga"))
        self.label_56.setText(_translate("transactionDialog", "Jumlah"))
        self.label_57.setText(_translate("transactionDialog", "Harga"))
        self.label_58.setText(_translate("transactionDialog", "Topping"))
        self.label_59.setText(_translate("transactionDialog", "Total Harga"))
        self.label_60.setText(_translate("transactionDialog", "Jumlah"))
        self.label_61.setText(_translate("transactionDialog", "Harga"))
        self.label_62.setText(_translate("transactionDialog", "Minuman"))
        self.label_63.setText(_translate("transactionDialog", "Total Harga"))
        self.label_64.setText(_translate("transactionDialog", "Grand Total:"))
        self.pushButton_7.setText(_translate("transactionDialog", "Cancel"))
        self.pushButton_8.setText(_translate("transactionDialog", "Order"))


    def setTime(self):
        self.time = datetime.now().strftime("%x")
        return self.time

    def getStore(self):
        store = Store.loadStore()
        return store

    def addItemStoreComboBox(self):
        stores = self.getStore()
        for store in stores:
            self.storeComboBox_4.addItem(store.name,store.id)

    def getMenu(self,transactionDialog):
        menus = Menu.loadMenu()
        self.listPizza = []
        self.listTopping = []
        self.listDrink = []
        for menu in menus:
            if menu.category == 'Pizza':
                self.listPizza.append(menu)
                # self.addPizza(menu)
            elif menu.category == 'Topping':
                self.listTopping.append(menu)
                # self.addTopping(menu)
            elif menu.category == 'Drink':
                self.listDrink.append(menu)
                # self.addDrink(menu)

        self.addPizza(transactionDialog, self.listPizza)
        self.addTopping(transactionDialog, self.listTopping)
        self.addDrink(transactionDialog, self.listDrink)


    def addPizza(self, transactionDialog, menus):
        self.pizzaCheckBoxes = []
        self.jumlahPizzas = []
        self.hargaPizzas = []
        self.totalHargaPizzas = []

        for menu in menus:
            self.pizzaCheckBox = QtWidgets.QCheckBox(transactionDialog)
            self.pizzaCheckBox.setObjectName("pizzaCheckBox")
            self.pizzaCheckBox.setText(menu.name)
            
            self.pizzaCheckBoxes.append(self.pizzaCheckBox)

            self.pizzaCheckBox.stateChanged.connect(lambda: self.checkboxStateChange('p'))

            self.jumlahPizza = QtWidgets.QLineEdit(transactionDialog)
            self.jumlahPizza.setObjectName("jumlahPizza")
            self.jumlahPizza.textChanged.connect(lambda: self.checkboxStateChange('p'))

            self.jumlahPizzas.append(self.jumlahPizza)

            self.hargaPizza_4 = QtWidgets.QLabel(transactionDialog)
            self.hargaPizza_4.setObjectName("hargaPizza_4")
            self.hargaPizza_4.setText(menu.price)

            self.hargaPizzas.append(self.hargaPizza_4)

            self.totalHargaPizza_4 = QtWidgets.QLabel(transactionDialog)
            self.totalHargaPizza_4.setObjectName("totalHargaPizza_4")
            self.totalHargaPizza_4.setText('0')

            self.totalHargaPizzas.append(self.totalHargaPizza_4)

        for checkbox in self.pizzaCheckBoxes : self.pizzaLayout.addWidget(checkbox)
        for jumlahPizza in self.jumlahPizzas : self.jumlahPizzaLayout.addWidget(jumlahPizza)
        for hargaPizza in self.hargaPizzas : self.hargaPizzaLayout.addWidget(hargaPizza)
        for totalHargaPizza in self.totalHargaPizzas : self.totalHargaPizzaLayout.addWidget(totalHargaPizza)

    def addTopping(self, transactionDialog, menus):
        self.toppingCheckBoxes = []
        self.jumlahToppings = []
        self.hargaToppings = []
        self.totalHargaToppings = []

        for menu in menus:
            self.toppingCheckBox_4 = QtWidgets.QCheckBox(transactionDialog)
            self.toppingCheckBox_4.setObjectName("toppingCheckBox_4")
            self.toppingCheckBox_4.setText(menu.name)

            self.toppingCheckBoxes.append(self.toppingCheckBox_4)

            self.toppingCheckBox_4.stateChanged.connect(lambda: self.checkboxStateChange('t'))

            self.jumlahTopping_4 = QtWidgets.QLineEdit(transactionDialog)
            self.jumlahTopping_4.setObjectName("jumlahTopping_4")
            self.jumlahTopping_4.textChanged.connect(lambda: self.checkboxStateChange('t'))

            self.jumlahToppings.append(self.jumlahTopping_4)

            self.hargaTopping_4 = QtWidgets.QLabel(transactionDialog)
            self.hargaTopping_4.setObjectName("hargaTopping_4")
            self.hargaTopping_4.setText(menu.price)

            self.hargaToppings.append(self.hargaTopping_4)

            self.totalHargaTopping_4 = QtWidgets.QLabel(transactionDialog)
            self.totalHargaTopping_4.setObjectName("totalHargaTopping_4")
            self.totalHargaTopping_4.setText('0')

            self.totalHargaToppings.append(self.totalHargaTopping_4)


        for checkbox in self.toppingCheckBoxes : self.toppingLayout.addWidget(checkbox)
        for jumlahTopping in self.jumlahToppings : self.toppingJumlahLayout.addWidget(jumlahTopping)
        for hargaTopping in self.hargaToppings : self.toppingHargaLayout.addWidget(hargaTopping)
        for totalHargaTopping in self.totalHargaToppings : self.toppingTotalHargaLayout.addWidget(totalHargaTopping)

    def addDrink(self, transactionDialog, menus):
        self.drinkCheckBoxes = []
        self.jumlahDrinks = []
        self.hargaDrinks = []
        self.totalHargaDrinks = []

        for menu in menus:
            self.minumanCheckBox_4 = QtWidgets.QCheckBox(transactionDialog)
            self.minumanCheckBox_4.setObjectName("minumanCheckBox_4")
            self.minumanCheckBox_4.setText(menu.name)

            self.drinkCheckBoxes.append(self.minumanCheckBox_4)

            self.minumanCheckBox_4.stateChanged.connect(lambda: self.checkboxStateChange('d'))

            self.jumlahMinuman_4 = QtWidgets.QLineEdit(transactionDialog)
            self.jumlahMinuman_4.setObjectName("jumlahMinuman_4")
            self.jumlahMinuman_4.textChanged.connect(lambda: self.checkboxStateChange('d'))

            self.jumlahDrinks.append(self.jumlahMinuman_4)

            self.hargaMinuman_4 = QtWidgets.QLabel(transactionDialog)
            self.hargaMinuman_4.setObjectName("hargaMinuman_4")
            self.hargaMinuman_4.setText(menu.price)

            self.hargaDrinks.append(self.hargaMinuman_4)

            self.totalHargaMinuman_4 = QtWidgets.QLabel(transactionDialog)
            self.totalHargaMinuman_4.setObjectName("totalHargaMinuman_4")
            self.totalHargaMinuman_4.setText('0')

            self.totalHargaDrinks.append(self.totalHargaMinuman_4)

        for checkbox in self.drinkCheckBoxes : self.drinkLayout.addWidget(checkbox)
        for jumlahDrink in self.jumlahDrinks : self.drinkJumlahLayout.addWidget(jumlahDrink)
        for hargaDrink in self.hargaDrinks : self.drinkHargaLayout.addWidget(hargaDrink)
        for totalHargaDrink in self.totalHargaDrinks : self.drinkTotalHargaLayout.addWidget(totalHargaDrink)

    def checkboxStateChange(self,cat):
        i = 0
        if cat == 'p':
            for checkbox in self.pizzaCheckBoxes:
                if checkbox.isChecked():
                    text = self.countPrice(self.jumlahPizzas[i].text(),self.hargaPizzas[i].text())
                    self.totalHargaPizzas[i].setText(text)
                if not checkbox.isChecked():
                    self.totalHargaPizzas[i].setText('0')
                i += 1
        elif cat == 't':
            for checkbox in self.toppingCheckBoxes:
                if checkbox.isChecked():
                    text = self.countPrice(self.jumlahToppings[i].text(),self.hargaToppings[i].text())
                    self.totalHargaToppings[i].setText(text)
                if not checkbox.isChecked():
                    self.totalHargaToppings[i].setText('0')
                i += 1
        elif cat == 'd':
            for checkbox in self.drinkCheckBoxes:
                if checkbox.isChecked():
                    text = self.countPrice(self.jumlahDrinks[i].text(),self.hargaDrinks[i].text())
                    self.totalHargaDrinks[i].setText(text)
                if not checkbox.isChecked():
                    self.totalHargaDrinks[i].setText('0')
                i += 1
        
        self.countTotal()
        # print(f'{menu} checked!')

    def countPrice(self,jumlah,harga):
        try:
            jumlah = int(jumlah)
            harga = int(harga)
            total = jumlah*harga
            return str(total)
        except ValueError:
            return '0'

    def countTotal(self):
        total = 0
        index = 0
        
        for pizza in self.totalHargaPizzas:
            total += int(pizza.text())
            index += 1

            # count total of listTopping
        index = 0
        for topping in self.totalHargaToppings:
            total += int(topping.text())
            index += 1

            # count total of listDrink
        index = 0
        for drink in self.totalHargaDrinks:
            total += int(drink.text())
            index += 1

        self.grandTotal_4.setText(str(total))
        
    def makeOrder(self):
        # get all the data
        transactionDate = self.time
        orderNo = self.getOrderNo()
        storeId = str(self.storeComboBox_4.currentData())
        mainBuy = []
        toppingBuy = []
        drinkBuy = []

        i = 0
        for pizza in self.listPizza:
            main = []
            main.append(pizza.id)
            main.append('0' if self.jumlahPizzas[i].text() == '' else self.jumlahPizzas[i].text())
            main.append(self.totalHargaPizzas[i].text())
            mainBuy.append(main)
            i += 1
        
        i = 0
        for topping in self.listTopping:
            toppings = []
            toppings.append(topping.id)
            toppings.append('0' if self.jumlahToppings[i].text() == '' else self.jumlahToppings[i].text())
            toppings.append(self.totalHargaToppings[i].text())
            toppingBuy.append(toppings)
            i += 1

        i = 0
        for drink in self.listDrink:
            drinks = []
            drinks.append(drink.id)
            drinks.append('0' if self.jumlahDrinks[i].text() == '' else self.jumlahDrinks[i].text())
            drinks.append(self.totalHargaDrinks[i].text())
            drinkBuy.append(drinks)
            i += 1

        grandTotal = self.grandTotal_4.text()

        self.saveToCsv(transactionDate,orderNo,storeId,mainBuy,toppingBuy,drinkBuy,grandTotal)
        # print(main)
        # print(mainBuy)
        # print(toppingBuy)
        # print(drinkBuy)

    def saveToCsv(self, date, orderNo, id, mainBuy, toppingBuy, drinkBuy, grandTotal):
        newData = []
        newData.append(date)
        newData.append(orderNo)
        newData.append(id)

        for main in mainBuy:
            for mainAtr in main[1:]:
                newData.append(mainAtr)
        
        for topBuy in toppingBuy:
            for topAtr in topBuy[1:]:
                newData.append(topAtr)
        
        for driBuy in drinkBuy:
            for driAtr in driBuy[1:]:
                newData.append(driAtr)
        newData.append(grandTotal)
        # print(newData)
        
        with open('./csv/transactions.csv','a',newline='') as output:
            csv_writer = csv.writer(output)
            csv_writer.writerow(newData)
        
        self.successStoreDialog()

    def getOrderNo(self):
        with open('./csv/transactions.csv','r') as input:
            csv_reader = csv.reader(input)
            row_count = sum(1 for row in csv_reader)
            return row_count


    def successStoreDialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText('Transaction Succeed!')
        msg.setWindowTitle('Transaction')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.transactionDialog.reject()

        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transactionDialog = QtWidgets.QDialog()
    ui = Ui_TransactionDialog()
    ui.setupUi(transactionDialog)
    transactionDialog.show()
    sys.exit(app.exec_())
