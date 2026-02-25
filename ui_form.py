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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 681)
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
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 801, 151))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(176, 0))
        self.pushButton.setMaximumSize(QSize(176, 24))

        self.gridLayout_4.addWidget(self.pushButton, 1, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(278, 0))
        self.label.setMaximumSize(QSize(278, 16777215))

        self.gridLayout_4.addWidget(self.label, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
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

        self.gridLayout_6.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(176, 16))
        self.label_9.setMaximumSize(QSize(176, 16))

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(176, 0))
        self.spinBox.setMaximumSize(QSize(176, 16777215))
        self.spinBox.setValue(8)

        self.gridLayout_6.addWidget(self.spinBox, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(176, 0))
        self.lineEdit_3.setMaximumSize(QSize(176, 24))

        self.gridLayout_6.addWidget(self.lineEdit_3, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.compare = QWidget()
        self.compare.setObjectName(u"compare")
        self.gridLayoutWidget_3 = QWidget(self.compare)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 801, 311))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(176, 0))
        self.pushButton_2.setMaximumSize(QSize(176, 24))

        self.gridLayout_5.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.gridLayoutWidget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayoutWidget_5 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 20, 771, 61))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.gridLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(176, 0))
        self.label_11.setMaximumSize(QSize(176, 16777215))

        self.gridLayout_7.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(176, 16))
        self.label_12.setMaximumSize(QSize(176, 16))

        self.gridLayout_7.addWidget(self.label_12, 0, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(176, 0))
        self.spinBox_2.setMaximumSize(QSize(176, 16777215))
        self.spinBox_2.setValue(8)

        self.gridLayout_7.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(176, 0))
        self.lineEdit_4.setMaximumSize(QSize(176, 24))

        self.gridLayout_7.addWidget(self.lineEdit_4, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 16))

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(278, 0))
        self.label_5.setMaximumSize(QSize(278, 16777215))

        self.gridLayout_5.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 1, 1, 1)

        self.tableView = QTableView(self.gridLayoutWidget_3)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_5.addWidget(self.tableView, 3, 0, 1, 3)

        self.gridLayout_5.setRowStretch(3, 1)
        self.gridLayout_5.setRowMinimumHeight(2, 100)
        self.tabWidget.addTab(self.compare, "")
        self.optimization = QWidget()
        self.optimization.setObjectName(u"optimization")
        self.tabWidget.addTab(self.optimization, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowMinimumHeight(0, 180)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u043e\u0439 \u0444\u0430\u0439\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0442\u0440\u043e\u043a:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u043e\u0442\u043a\u0440\u044b\u0442", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.compare), QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optimization), QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

