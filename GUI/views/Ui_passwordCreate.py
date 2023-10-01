# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordCreate.ui'
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

class Ui_passwordCreate(object):
    def setupUi(self, passwordCreate):
        if not passwordCreate.objectName():
            passwordCreate.setObjectName(u"passwordCreate")
        passwordCreate.setWindowModality(Qt.NonModal)
        passwordCreate.resize(761, 259)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(passwordCreate.sizePolicy().hasHeightForWidth())
        passwordCreate.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(passwordCreate)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tipsLbl = QLabel(passwordCreate)
        self.tipsLbl.setObjectName(u"tipsLbl")

        self.horizontalLayout_3.addWidget(self.tipsLbl)

        self.tipsLineedit = QLineEdit(passwordCreate)
        self.tipsLineedit.setObjectName(u"tipsLineedit")

        self.horizontalLayout_3.addWidget(self.tipsLineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(passwordCreate)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.passwdLineedit = QLineEdit(passwordCreate)
        self.passwdLineedit.setObjectName(u"passwdLineedit")
        self.passwdLineedit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.passwdLineedit)

        self.showPasswd = QCheckBox(passwordCreate)
        self.showPasswd.setObjectName(u"showPasswd")

        self.horizontalLayout.addWidget(self.showPasswd)

        self.confirmBtn = QPushButton(passwordCreate)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.horizontalLayout.addWidget(self.confirmBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_15.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_15)


        self.retranslateUi(passwordCreate)

        QMetaObject.connectSlotsByName(passwordCreate)
    # setupUi

    def retranslateUi(self, passwordCreate):
        passwordCreate.setWindowTitle(QCoreApplication.translate("passwordCreate", u"Create your password", None))
        self.tipsLbl.setText(QCoreApplication.translate("passwordCreate", u"\u5bc6\u78bc\u63d0\u793a\uff1a", None))
        self.label.setText(QCoreApplication.translate("passwordCreate", u"\u8acb\u8f38\u5165\u5bc6\u78bc\uff1a", None))
        self.passwdLineedit.setText("")
        self.showPasswd.setText(QCoreApplication.translate("passwordCreate", u"\u986f\u793a\u5bc6\u78bc", None))
        self.confirmBtn.setText(QCoreApplication.translate("passwordCreate", u"\u78ba\u8a8d", None))
    # retranslateUi

