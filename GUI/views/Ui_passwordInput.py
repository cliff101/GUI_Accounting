# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordInput.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_passwordInput(object):
    def setupUi(self, passwordInput):
        if not passwordInput.objectName():
            passwordInput.setObjectName(u"passwordInput")
        passwordInput.setWindowModality(Qt.NonModal)
        passwordInput.resize(761, 259)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(passwordInput.sizePolicy().hasHeightForWidth())
        passwordInput.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(passwordInput)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tipsLbl = QLabel(passwordInput)
        self.tipsLbl.setObjectName(u"tipsLbl")

        self.verticalLayout.addWidget(self.tipsLbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(passwordInput)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.passwdLineedit = QLineEdit(passwordInput)
        self.passwdLineedit.setObjectName(u"passwdLineedit")
        self.passwdLineedit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.passwdLineedit)

        self.showPasswd = QCheckBox(passwordInput)
        self.showPasswd.setObjectName(u"showPasswd")

        self.horizontalLayout.addWidget(self.showPasswd)

        self.confirmBtn = QPushButton(passwordInput)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.horizontalLayout.addWidget(self.confirmBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_15.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_15)


        self.retranslateUi(passwordInput)

        QMetaObject.connectSlotsByName(passwordInput)
    # setupUi

    def retranslateUi(self, passwordInput):
        passwordInput.setWindowTitle(QCoreApplication.translate("passwordInput", u"Input your password", None))
        self.tipsLbl.setText(QCoreApplication.translate("passwordInput", u"\u5bc6\u78bc\u63d0\u793a\uff1a", None))
        self.label.setText(QCoreApplication.translate("passwordInput", u"\u8acb\u8f38\u5165\u5bc6\u78bc\uff1a", None))
        self.passwdLineedit.setText("")
        self.showPasswd.setText(QCoreApplication.translate("passwordInput", u"\u986f\u793a\u5bc6\u78bc", None))
        self.confirmBtn.setText(QCoreApplication.translate("passwordInput", u"\u78ba\u8a8d", None))
    # retranslateUi

