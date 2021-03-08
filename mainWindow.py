from view import Ui_ViewDialog
from menuDialog import Ui_Menu
from PyQt5 import QtCore, QtGui, QtWidgets
from storeDialog import Ui_Store
from transactionDialog import Ui_TransactionDialog
from reportDialog import Ui_Report
from help import Ui_Help

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 345)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.btn_store = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_store.sizePolicy().hasHeightForWidth())
        self.btn_store.setSizePolicy(sizePolicy)
        self.btn_store.setToolTipDuration(-1)
        self.btn_store.setObjectName("btn_store")
        self.verticalLayout.addWidget(self.btn_store)

        self.btn_store.clicked.connect(self.btnStore)

        self.btn_menu = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout.addWidget(self.btn_menu)

        self.btn_menu.clicked.connect(self.btnMenu)

        self.btn_transaction = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_transaction.sizePolicy().hasHeightForWidth())
        self.btn_transaction.setSizePolicy(sizePolicy)
        self.btn_transaction.setObjectName("btn_transaction")
        self.verticalLayout.addWidget(self.btn_transaction)

        self.btn_transaction.clicked.connect(self.btnTransaction)

        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_view.sizePolicy().hasHeightForWidth())
        self.btn_view.setSizePolicy(sizePolicy)
        self.btn_view.setObjectName("btn_view")
        self.verticalLayout.addWidget(self.btn_view)

        self.btn_view.clicked.connect(self.btnView)

        self.btn_report = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy)
        self.btn_report.setObjectName("btn_report")
        self.verticalLayout.addWidget(self.btn_report)

        self.btn_report.clicked.connect(self.btnReport)

        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setObjectName("btn_help")
        self.verticalLayout.addWidget(self.btn_help)

        self.btn_help.clicked.connect(self.btnHelp)

        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fitsa Hats"))
        self.title.setText(_translate("MainWindow", "Fitsa Hats"))
        self.btn_store.setToolTip(_translate("MainWindow", "Register new store"))
        self.btn_store.setStatusTip(_translate("MainWindow", "Register new store"))
        self.btn_store.setText(_translate("MainWindow", "Store"))
        self.btn_menu.setToolTip(_translate("MainWindow", "Register new menu"))
        self.btn_menu.setStatusTip(_translate("MainWindow", "Register new menu"))
        self.btn_menu.setText(_translate("MainWindow", "Menu"))
        self.btn_transaction.setToolTip(_translate("MainWindow", "Make a transaction"))
        self.btn_transaction.setStatusTip(_translate("MainWindow", "Make a transaction"))
        self.btn_transaction.setText(_translate("MainWindow", "Transaction"))
        self.btn_view.setToolTip(_translate("MainWindow", "View stores and menus"))
        self.btn_view.setStatusTip(_translate("MainWindow", "View stores and menus"))
        self.btn_view.setText(_translate("MainWindow", "View"))
        self.btn_report.setToolTip(_translate("MainWindow", "Make a report"))
        self.btn_report.setStatusTip(_translate("MainWindow", "Make a report"))
        self.btn_report.setText(_translate("MainWindow", "Report"))
        self.btn_help.setToolTip(_translate("MainWindow", "Help"))
        self.btn_help.setStatusTip(_translate("MainWindow", "Help"))
        self.btn_help.setText(_translate("MainWindow", "Help"))

    def btnStore(self):
        self.storeDialog = QtWidgets.QDialog()
        self.ui = Ui_Store()
        self.ui.setupUi(self.storeDialog)
        self.storeDialog.show()

    def btnMenu(self):
        self.menuDialog = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.menuDialog)
        self.menuDialog.show()

    def btnView(self):
        self.viewDialog = QtWidgets.QDialog()
        self.ui = Ui_ViewDialog()
        self.ui.setupUi(self.viewDialog)
        self.viewDialog.show()

    def btnTransaction(self):
        self.transactionDialog = QtWidgets.QDialog()
        self.ui = Ui_TransactionDialog()
        self.ui.setupUi(self.transactionDialog)
        self.transactionDialog.show()

    def btnReport(self):
        self.ReportDialog = QtWidgets.QDialog()
        self.ui = Ui_Report()
        self.ui.setupUi(self.ReportDialog)
        self.ReportDialog.show()

    def btnHelp(self):
        self.HelpDialog = QtWidgets.QDialog()
        self.ui = Ui_Help()
        self.ui.setupUi(self.HelpDialog)
        self.HelpDialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
