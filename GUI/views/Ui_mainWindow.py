# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1213, 818)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.editDayLabel = QLabel(self.frame_2)
        self.editDayLabel.setObjectName(u"editDayLabel")
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(16)
        self.editDayLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.editDayLabel)

        self.todayDiaryTextBrowser = QTextBrowser(self.frame_2)
        self.todayDiaryTextBrowser.setObjectName(u"todayDiaryTextBrowser")
        font1 = QFont()
        font1.setFamilies([u"\u5047\u7c89\u5713"])
        self.todayDiaryTextBrowser.setFont(font1)
        self.todayDiaryTextBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.todayDiaryTextBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.todayDiaryTextBrowser.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.todayDiaryTextBrowser)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.cmdTipsBtn = QPushButton(self.frame_2)
        self.cmdTipsBtn.setObjectName(u"cmdTipsBtn")

        self.horizontalLayout_5.addWidget(self.cmdTipsBtn)

        self.editTodayDiaryBtn = QPushButton(self.frame_2)
        self.editTodayDiaryBtn.setObjectName(u"editTodayDiaryBtn")

        self.horizontalLayout_5.addWidget(self.editTodayDiaryBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(3)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.editTodayMoney = QPushButton(self.frame)
        self.editTodayMoney.setObjectName(u"editTodayMoney")

        self.horizontalLayout_6.addWidget(self.editTodayMoney)

        self.todayMoneyLabel = QLabel(self.frame)
        self.todayMoneyLabel.setObjectName(u"todayMoneyLabel")
        self.todayMoneyLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.todayMoneyLabel)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.yestMoneyLabel = QLabel(self.frame)
        self.yestMoneyLabel.setObjectName(u"yestMoneyLabel")

        self.verticalLayout_8.addWidget(self.yestMoneyLabel)

        self.todayShouldMoneyLabel = QLabel(self.frame)
        self.todayShouldMoneyLabel.setObjectName(u"todayShouldMoneyLabel")

        self.verticalLayout_8.addWidget(self.todayShouldMoneyLabel)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.todayIncomeLabel = QLabel(self.frame)
        self.todayIncomeLabel.setObjectName(u"todayIncomeLabel")

        self.verticalLayout_7.addWidget(self.todayIncomeLabel)

        self.todayIncomeListview = QListView(self.frame)
        self.todayIncomeListview.setObjectName(u"todayIncomeListview")

        self.verticalLayout_7.addWidget(self.todayIncomeListview)

        self.addIncomeBtn = QPushButton(self.frame)
        self.addIncomeBtn.setObjectName(u"addIncomeBtn")

        self.verticalLayout_7.addWidget(self.addIncomeBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.todayCostLabel = QLabel(self.frame)
        self.todayCostLabel.setObjectName(u"todayCostLabel")

        self.verticalLayout_6.addWidget(self.todayCostLabel)

        self.todayCostListview = QListView(self.frame)
        self.todayCostListview.setObjectName(u"todayCostListview")

        self.verticalLayout_6.addWidget(self.todayCostListview)

        self.addCostBtn = QPushButton(self.frame)
        self.addCostBtn.setObjectName(u"addCostBtn")

        self.verticalLayout_6.addWidget(self.addCostBtn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.editTodaySong = QPushButton(self.frame)
        self.editTodaySong.setObjectName(u"editTodaySong")

        self.horizontalLayout_4.addWidget(self.editTodaySong)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.todaySongLabel = QLabel(self.frame)
        self.todaySongLabel.setObjectName(u"todaySongLabel")
        self.todaySongLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.todaySongLabel)

        self.verticalLayout_2.setStretch(2, 5)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.allDayListview = QListView(self.frame_3)
        self.allDayListview.setObjectName(u"allDayListview")

        self.verticalLayout_5.addWidget(self.allDayListview)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.showVersionLogBtn = QPushButton(self.frame_3)
        self.showVersionLogBtn.setObjectName(u"showVersionLogBtn")

        self.horizontalLayout_2.addWidget(self.showVersionLogBtn)

        self.setPasswordBtn = QPushButton(self.frame_3)
        self.setPasswordBtn.setObjectName(u"setPasswordBtn")

        self.horizontalLayout_2.addWidget(self.setPasswordBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.editTodayDataBtn = QPushButton(self.frame_3)
        self.editTodayDataBtn.setObjectName(u"editTodayDataBtn")

        self.horizontalLayout_2.addWidget(self.editTodayDataBtn)

        self.showMonthlyDataBtn = QPushButton(self.frame_3)
        self.showMonthlyDataBtn.setObjectName(u"showMonthlyDataBtn")

        self.horizontalLayout_2.addWidget(self.showMonthlyDataBtn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalLayout_4.setStretch(0, 2)
        self.verticalLayout_4.setStretch(1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.editDayLabel.setText(QCoreApplication.translate("mainWindow", u"\u7de8\u8f2f\u65e5\u671f\uff1a", None))
        self.cmdTipsBtn.setText(QCoreApplication.translate("mainWindow", u"\u67e5\u770b\u6307\u4ee4\u63d0\u793a", None))
        self.editTodayDiaryBtn.setText(QCoreApplication.translate("mainWindow", u"\u7de8\u8f2f\u65e5\u8a18", None))
        self.editTodayMoney.setText(QCoreApplication.translate("mainWindow", u"\u7de8\u8f2f\u672c\u65e5\u9918\u6b3e", None))
        self.todayMoneyLabel.setText(QCoreApplication.translate("mainWindow", u"\u672c\u65e5\u9918\u6b3e\uff1a", None))
        self.yestMoneyLabel.setText(QCoreApplication.translate("mainWindow", u"\u6628\u65e5\u9918\u6b3e\uff1a", None))
        self.todayShouldMoneyLabel.setText(QCoreApplication.translate("mainWindow", u"\u4eca\u65e5\u61c9\u9918\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u6536\u5165\u9805\u76ee", None))
        self.todayIncomeLabel.setText(QCoreApplication.translate("mainWindow", u"\u672c\u65e5\u6536\u5165\uff1a", None))
        self.addIncomeBtn.setText(QCoreApplication.translate("mainWindow", u"\u65b0\u589e\u672c\u65e5\u6536\u5165", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u82b1\u8cbb\u9805\u76ee", None))
        self.todayCostLabel.setText(QCoreApplication.translate("mainWindow", u"\u672c\u65e5\u82b1\u8cbb\uff1a", None))
        self.addCostBtn.setText(QCoreApplication.translate("mainWindow", u"\u65b0\u589e\u672c\u65e5\u82b1\u8cbb", None))
        self.editTodaySong.setText(QCoreApplication.translate("mainWindow", u"\u7de8\u8f2f\u672c\u65e5\u4e3b\u984c\u6b4c", None))
        self.todaySongLabel.setText(QCoreApplication.translate("mainWindow", u"\u4eca\u65e5\u4e3b\u984c\u6b4c\uff1a", None))
        self.showVersionLogBtn.setText(QCoreApplication.translate("mainWindow", u"\u986f\u793a\u7248\u672c\u7d00\u9304", None))
        self.setPasswordBtn.setText(QCoreApplication.translate("mainWindow", u"\u91cd\u8a2d\u5bc6\u78bc", None))
        self.editTodayDataBtn.setText(QCoreApplication.translate("mainWindow", u"\u7de8\u8f2f\u4eca\u65e5\u8cc7\u6599", None))
        self.showMonthlyDataBtn.setText(QCoreApplication.translate("mainWindow", u"\u986f\u793a\u6bcf\u6708\u7d71\u8a08\u8cc7\u6599", None))
    # retranslateUi

