from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QLineEdit
from PySide6.QtGui import QAction
try:
    from .views.Ui_passwordCreate import Ui_passwordCreate
except:
    from views.Ui_passwordCreate import Ui_passwordCreate
from qt_material import apply_stylesheet
import sys


class passwordCreate(QDialog, Ui_passwordCreate):
    def __init__(self):
        super(passwordCreate, self).__init__()

        self.setupUi(self)
        # 按鈕功能
        self.showPasswd.stateChanged.connect(self.showPasswordCheckChanged)
        self.confirmBtn.clicked.connect(self.confirm)

    def showPasswordCheckChanged(self):
        if self.showPasswd.isChecked():
            self.passwdLineedit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwdLineedit.setEchoMode(QLineEdit.Password)

    def confirm(self):
        self.passwordTips = self.tipsLineedit.text()
        self.password = self.passwdLineedit.text()
        self.close()
