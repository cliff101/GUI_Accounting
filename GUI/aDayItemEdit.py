from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QLineEdit
from PySide6.QtGui import QAction
try:
    from .views.Ui_aDayItemEdit import Ui_aDayItemEdit
except:
    from views.Ui_aDayItemEdit import Ui_aDayItemEdit
from qt_material import apply_stylesheet
import sys


class aDayItemEdit(QDialog, Ui_aDayItemEdit):
    def __init__(self, isCost, name="", value=""):
        super(aDayItemEdit, self).__init__()

        self.setupUi(self)

        self.itemName = name
        self.value = str(value)
        self.OK = False

        self.itemNameLineedit.setText(self.itemName)
        self.itemCostIncomeLineedit.setText(self.value)

        # 按鈕功能
        if not self.value.isnumeric():
            self.itemCostIncomeLineedit.setStyleSheet(
                "color: red;  background-color: black")
            self.confirmBtn.setEnabled(False)
        self.confirmBtn.clicked.connect(self.confirm)
        self.cancelBtn.clicked.connect(self.cancel)

        if isCost:
            self.itemCostIncomeLbl.setText("項目花費：")
        else:
            self.itemCostIncomeLbl.setText("項目收入：")
        self.itemCostIncomeLineedit.textChanged.connect(
            self.itemCostIncomeLineeditValueChanged)

    def confirm(self):
        self.itemName = self.itemNameLineedit.text()
        self.value = self.itemCostIncomeLineedit.text()
        self.OK = True
        self.close()

    def itemCostIncomeLineeditValueChanged(self, value):
        if not value.isnumeric():
            self.itemCostIncomeLineedit.setStyleSheet(
                "color: red;  background-color: black")
            self.confirmBtn.setEnabled(False)
            return
        self.itemCostIncomeLineedit.setStyleSheet("dark_teal.xml")
        self.confirmBtn.setEnabled(True)

    def cancel(self):
        self.OK = False
        self.close()
