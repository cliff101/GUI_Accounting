# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aDayItemEdit.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_aDayItemEdit(object):
    def setupUi(self, aDayItemEdit):
        if not aDayItemEdit.objectName():
            aDayItemEdit.setObjectName(u"aDayItemEdit")
        aDayItemEdit.setWindowModality(Qt.NonModal)
        aDayItemEdit.resize(327, 128)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aDayItemEdit.sizePolicy().hasHeightForWidth())
        aDayItemEdit.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(aDayItemEdit)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tipsLbl = QLabel(aDayItemEdit)
        self.tipsLbl.setObjectName(u"tipsLbl")

        self.horizontalLayout_3.addWidget(self.tipsLbl)

        self.itemNameLineedit = QLineEdit(aDayItemEdit)
        self.itemNameLineedit.setObjectName(u"itemNameLineedit")

        self.horizontalLayout_3.addWidget(self.itemNameLineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itemCostIncomeLbl = QLabel(aDayItemEdit)
        self.itemCostIncomeLbl.setObjectName(u"itemCostIncomeLbl")

        self.horizontalLayout.addWidget(self.itemCostIncomeLbl)

        self.itemCostIncomeLineedit = QLineEdit(aDayItemEdit)
        self.itemCostIncomeLineedit.setObjectName(u"itemCostIncomeLineedit")
        self.itemCostIncomeLineedit.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout.addWidget(self.itemCostIncomeLineedit)

        self.confirmBtn = QPushButton(aDayItemEdit)
        self.confirmBtn.setObjectName(u"confirmBtn")

        self.horizontalLayout.addWidget(self.confirmBtn)

        self.cancelBtn = QPushButton(aDayItemEdit)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_15.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_15)


        self.retranslateUi(aDayItemEdit)

        QMetaObject.connectSlotsByName(aDayItemEdit)
    # setupUi

    def retranslateUi(self, aDayItemEdit):
        aDayItemEdit.setWindowTitle(QCoreApplication.translate("aDayItemEdit", u"Edit Item", None))
        self.tipsLbl.setText(QCoreApplication.translate("aDayItemEdit", u"\u9805\u76ee\u540d\u7a31\uff1a", None))
        self.itemCostIncomeLbl.setText(QCoreApplication.translate("aDayItemEdit", u"\u9805\u76ee\uff1a", None))
        self.itemCostIncomeLineedit.setText("")
        self.confirmBtn.setText(QCoreApplication.translate("aDayItemEdit", u"\u78ba\u8a8d", None))
        self.cancelBtn.setText(QCoreApplication.translate("aDayItemEdit", u"\u53d6\u6d88", None))
    # retranslateUi

