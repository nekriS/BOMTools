# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableView, QToolBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 754)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 831, 621))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.progressBar = QProgressBar(self.gridLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 180))
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 801, 160))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)

        self.first_file = QLineEdit(self.gridLayoutWidget_2)
        self.first_file.setObjectName(u"first_file")
        self.first_file.setMinimumSize(QSize(0, 30))
        self.first_file.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")
        self.first_file.setReadOnly(True)

        self.gridLayout_4.addWidget(self.first_file, 1, 1, 1, 1)

        self.open_first = QPushButton(self.gridLayoutWidget_2)
        self.open_first.setObjectName(u"open_first")
        self.open_first.setMinimumSize(QSize(176, 30))
        self.open_first.setMaximumSize(QSize(176, 30))
        font = QFont()
        self.open_first.setFont(font)
        self.open_first.setStyleSheet(u"QPushButton {\n"
"	background-color: #EBEBEB;\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #f5f5f5;\n"
"border: 1px solid #f5f5f5;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #3399FF;\n"
"	border: 1px solid #3399FF;\n"
"	color: white;\n"
"}")

        self.gridLayout_4.addWidget(self.open_first, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(278, 0))
        self.label.setMaximumSize(QSize(278, 16777215))
        self.label.setStyleSheet(u"\n"
"	font-size: 14px;\n"
"")

        self.gridLayout_4.addWidget(self.label, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 90))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 771, 61))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(176, 0))
        self.label_10.setMaximumSize(QSize(176, 16777215))

        self.gridLayout_6.addWidget(self.label_10, 0, 2, 1, 1)

        self.first_skip = QSpinBox(self.gridLayoutWidget_4)
        self.first_skip.setObjectName(u"first_skip")
        self.first_skip.setMinimumSize(QSize(176, 30))
        self.first_skip.setMaximumSize(QSize(176, 16777215))
        self.first_skip.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")
        self.first_skip.setValue(8)

        self.gridLayout_6.addWidget(self.first_skip, 1, 2, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(176, 16))
        self.label_9.setMaximumSize(QSize(176, 16))

        self.gridLayout_6.addWidget(self.label_9, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.first_count = QLineEdit(self.gridLayoutWidget_4)
        self.first_count.setObjectName(u"first_count")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_count.sizePolicy().hasHeightForWidth())
        self.first_count.setSizePolicy(sizePolicy)
        self.first_count.setMinimumSize(QSize(176, 30))
        self.first_count.setMaximumSize(QSize(176, 30))
        self.first_count.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")

        self.gridLayout_6.addWidget(self.first_count, 1, 1, 1, 1)

        self.first_pn = QLineEdit(self.gridLayoutWidget_4)
        self.first_pn.setObjectName(u"first_pn")
        sizePolicy.setHeightForWidth(self.first_pn.sizePolicy().hasHeightForWidth())
        self.first_pn.setSizePolicy(sizePolicy)
        self.first_pn.setMinimumSize(QSize(176, 30))
        self.first_pn.setMaximumSize(QSize(176, 30))
        self.first_pn.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")

        self.gridLayout_6.addWidget(self.first_pn, 1, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(176, 16))
        self.label_14.setMaximumSize(QSize(176, 16))

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.compare = QWidget()
        self.compare.setObjectName(u"compare")
        self.gridLayoutWidget_3 = QWidget(self.compare)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 801, 471))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.toolBox = QToolBox(self.gridLayoutWidget_3)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(19)
        font1.setBold(False)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.toolBox.setFont(font1)
        self.toolBox.setTabletTracking(False)
        self.toolBox.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.toolBox.setAcceptDrops(False)
        self.toolBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(u"QToolBox::tab {\n"
"                            background-color: #f5f5f5;\n"
"                            padding: -2px 10px;\n"
"                            font-size: 16px;\n"
"                            border: 1px solid #f5f5f5;\n"
"                            border-radius: 10px;\n"
"                            margin: 0px;\n"
"                        }\n"
"\n"
"                        QToolBox::tab:selected {\n"
"                            background-color: #EBEBEB;\n"
"                            border: 1px solid #CCCCCC;\n"
"                        }\n"
"\n"
"                        QToolBox::tab:hover {\n"
"                            background-color: #3399FF;\n"
"                            border: 1px solid #3399FF;\n"
"                            color: white;\n"
"                        }")
        self.toolBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toolBox.setFrameShadow(QFrame.Shadow.Plain)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 789, 157))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.toolBox.addItem(self.page, icon, u"\u0412\u043a\u043b\u0430\u0434\u043a\u0430 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 789, 157))
        self.toolBox.addItem(self.page_2, u"\u0412\u043a\u043b\u0430\u0434\u043a\u0430 2")

        self.gridLayout_5.addWidget(self.toolBox, 7, 0, 1, 3)

        self.open_second = QPushButton(self.gridLayoutWidget_3)
        self.open_second.setObjectName(u"open_second")
        self.open_second.setMinimumSize(QSize(176, 30))
        self.open_second.setMaximumSize(QSize(176, 30))
        font2 = QFont()
        font2.setBold(False)
        self.open_second.setFont(font2)
        self.open_second.setStyleSheet(u"QPushButton {\n"
"	background-color: #EBEBEB;\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #f5f5f5;\n"
"border: 1px solid #f5f5f5;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #3399FF;\n"
"	border: 1px solid #3399FF;\n"
"	color: white;\n"
"}")

        self.gridLayout_5.addWidget(self.open_second, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 1, 1, 1)

        self.second_file = QLineEdit(self.gridLayoutWidget_3)
        self.second_file.setObjectName(u"second_file")
        self.second_file.setMinimumSize(QSize(0, 30))
        self.second_file.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")
        self.second_file.setReadOnly(True)

        self.gridLayout_5.addWidget(self.second_file, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(278, 0))
        self.label_5.setMaximumSize(QSize(278, 16777215))
        self.label_5.setStyleSheet(u"\n"
"	font-size: 14px;\n"
"")

        self.gridLayout_5.addWidget(self.label_5, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(0, 90))
        self.gridLayoutWidget_5 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 20, 771, 61))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(176, 16))
        self.label_12.setMaximumSize(QSize(176, 16))

        self.gridLayout_7.addWidget(self.label_12, 0, 1, 1, 1)

        self.second_count = QLineEdit(self.gridLayoutWidget_5)
        self.second_count.setObjectName(u"second_count")
        self.second_count.setMinimumSize(QSize(176, 30))
        self.second_count.setMaximumSize(QSize(176, 30))
        self.second_count.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")

        self.gridLayout_7.addWidget(self.second_count, 1, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(176, 0))
        self.label_11.setMaximumSize(QSize(176, 16777215))

        self.gridLayout_7.addWidget(self.label_11, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.second_skip = QSpinBox(self.gridLayoutWidget_5)
        self.second_skip.setObjectName(u"second_skip")
        self.second_skip.setMinimumSize(QSize(176, 30))
        self.second_skip.setMaximumSize(QSize(176, 16777215))
        self.second_skip.setStyleSheet(u"QSpinBox {\n"
"	border: 1px solid #CCCCCC;\n"
"\n"
"	padding: -2px 10px 0px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.second_skip.setValue(8)

        self.gridLayout_7.addWidget(self.second_skip, 1, 2, 1, 1)

        self.second_pn = QLineEdit(self.gridLayoutWidget_5)
        self.second_pn.setObjectName(u"second_pn")
        self.second_pn.setMinimumSize(QSize(176, 30))
        self.second_pn.setMaximumSize(QSize(176, 30))
        self.second_pn.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")

        self.gridLayout_7.addWidget(self.second_pn, 1, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(176, 16))
        self.label_15.setMaximumSize(QSize(176, 16))

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.compareButton = QPushButton(self.gridLayoutWidget_3)
        self.compareButton.setObjectName(u"compareButton")
        self.compareButton.setMinimumSize(QSize(0, 30))
        self.compareButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #EBEBEB;\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #f5f5f5;\n"
"border: 1px solid #f5f5f5;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #3399FF;\n"
"	border: 1px solid #3399FF;\n"
"	color: white;\n"
"}")

        self.gridLayout_5.addWidget(self.compareButton, 3, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 4, 0, 1, 1)

        self.gridLayout_5.setRowMinimumHeight(2, 80)
        self.tabWidget.addTab(self.compare, "")
        self.optimization = QWidget()
        self.optimization.setObjectName(u"optimization")
        self.gridLayoutWidget_6 = QWidget(self.optimization)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 10, 791, 351))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.groupBox_4 = QGroupBox(self.gridLayoutWidget_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 100))
        self.gridLayoutWidget_7 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 10, 771, 61))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.optimizeButton = QPushButton(self.gridLayoutWidget_7)
        self.optimizeButton.setObjectName(u"optimizeButton")
        self.optimizeButton.setMinimumSize(QSize(176, 30))
        self.optimizeButton.setMaximumSize(QSize(176, 30))
        self.optimizeButton.setFont(font)
        self.optimizeButton.setStyleSheet(u"QPushButton {\n"
"	background-color: #EBEBEB;\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #f5f5f5;\n"
"border: 1px solid #f5f5f5;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #3399FF;\n"
"	border: 1px solid #3399FF;\n"
"	color: white;\n"
"}")

        self.gridLayout_8.addWidget(self.optimizeButton, 1, 1, 1, 1)

        self.requestLine = QLineEdit(self.gridLayoutWidget_7)
        self.requestLine.setObjectName(u"requestLine")
        sizePolicy.setHeightForWidth(self.requestLine.sizePolicy().hasHeightForWidth())
        self.requestLine.setSizePolicy(sizePolicy)
        self.requestLine.setMinimumSize(QSize(176, 30))
        self.requestLine.setMaximumSize(QSize(176, 30))
        self.requestLine.setStyleSheet(u"\n"
"	border: 1px solid #CCCCCC;\n"
"	padding: -2px 10px;\n"
"	font-size: 14px;\n"
"	border-radius: 5px;\n"
"")

        self.gridLayout_8.addWidget(self.requestLine, 1, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(176, 16))
        self.label_18.setMaximumSize(QSize(176, 16))

        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.exceptDNP = QCheckBox(self.gridLayoutWidget_7)
        self.exceptDNP.setObjectName(u"exceptDNP")
        self.exceptDNP.setChecked(True)
        self.exceptDNP.setTristate(False)

        self.gridLayout_8.addWidget(self.exceptDNP, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.tableView = QTableView(self.gridLayoutWidget_6)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setDragEnabled(False)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableView, 1, 0, 1, 1)

        self.tabWidget.addTab(self.optimization, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowMinimumHeight(0, 180)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u0444\u0430\u0439\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" \u0424\u0430\u0439\u043b:", None))
        self.first_file.setText("")
        self.open_first.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" \u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430:", None))
        self.first_count.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.first_pn.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u0430\u0434\u043a\u0430 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u0430\u0434\u043a\u0430 2", None))
        self.open_second.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u" \u0424\u0430\u0439\u043b:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" \u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430:", None))
        self.second_count.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a:", None))
        self.second_pn.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u" \u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u043d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b:", None))
        self.compareButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0438\u0442\u044c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.compare), QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.groupBox_4.setTitle("")
        self.optimizeButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c", None))
        self.requestLine.setText(QCoreApplication.translate("MainWindow", u"C-????-", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441:", None))
        self.exceptDNP.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043a\u043b\u044e\u0447\u0438\u0442\u044c DNP/NM", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optimization), QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

