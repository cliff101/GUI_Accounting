from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QLineEdit
from PySide6.QtGui import QAction
try:
    from .views.Ui_passwordInput import Ui_passwordInput
except:
    from views.Ui_passwordInput import Ui_passwordInput
from qt_material import apply_stylesheet
import sys


class passwordInput(QDialog, Ui_passwordInput):
    def __init__(self, tips):
        super(passwordInput, self).__init__()

        self.setupUi(self)
        # 按鈕功能
        self.tipsLbl.setText("密碼提示： {}".format(tips))
        self.showPasswd.stateChanged.connect(self.showPasswordCheckChanged)
        self.confirmBtn.clicked.connect(self.confirm)

    def showPasswordCheckChanged(self):
        if self.showPasswd.isChecked():
            self.passwdLineedit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwdLineedit.setEchoMode(QLineEdit.Password)

    def confirm(self):
        self.password = self.passwdLineedit.text()
        self.close()
