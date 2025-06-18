# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(640, 360)
        self.labelLoading = QLabel(Splash)
        self.labelLoading.setObjectName(u"labelLoading")
        self.labelLoading.setGeometry(QRect(220, 50, 191, 151))
        self.progressBar = QProgressBar(Splash)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 242, 571, 41))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background: #f3f3f3\n"
"	padding: 10 px;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #5b29f2\n"
"        );   \n"
"\n"
"}")
        self.progressBar.setValue(24)
        self.getUpdate = QPushButton(Splash)
        self.getUpdate.setObjectName(u"getUpdate")
        self.getUpdate.setGeometry(QRect(120, 180, 391, 61))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.getUpdate.setFont(font)
        self.getUpdate.setStyleSheet(u"QPushButton {\n"
"    color: #eee;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #7612b8\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #954af7\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #5b29f2\n"
"        );\n"
"    }")
        self.rejectUpdate = QPushButton(Splash)
        self.rejectUpdate.setObjectName(u"rejectUpdate")
        self.rejectUpdate.setGeometry(QRect(120, 270, 391, 61))
        self.rejectUpdate.setFont(font)
        self.rejectUpdate.setStyleSheet(u"QPushButton {\n"
"    color: #eee;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(170, 170, 255)\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(211, 203, 255)\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(149, 149, 223)\n"
"        );\n"
"    }")

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"Form", None))
        self.labelLoading.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700; color:#00007f;\">Loading</span></p></body></html>", None))
        self.getUpdate.setText(QCoreApplication.translate("Splash", u"Update app", None))
        self.rejectUpdate.setText(QCoreApplication.translate("Splash", u"Maybe later", None))
    # retranslateUi

