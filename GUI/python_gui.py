# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_SEEnglish(object):
    def setupUi(self, SEEnglish):
        if not SEEnglish.objectName():
            SEEnglish.setObjectName(u"SEEnglish")
        SEEnglish.resize(1280, 720)
        SEEnglish.setMinimumSize(QSize(1280, 0))
        SEEnglish.setMaximumSize(QSize(1280, 720))
        icon = QIcon()
        icon.addFile(u"assets/images/output-onlinepngtools.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SEEnglish.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(SEEnglish)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-10, 0, 1301, 771))
        self.Base_Layout = QVBoxLayout(self.verticalLayoutWidget)
        self.Base_Layout.setSpacing(9)
        self.Base_Layout.setObjectName(u"Base_Layout")
        self.Base_Layout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.verticalLayoutWidget)
        self.pages.setObjectName(u"pages")
        self.pages.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.pages.setAutoFillBackground(False)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.MistakesLabel = QLabel(self.page_3)
        self.MistakesLabel.setObjectName(u"MistakesLabel")
        self.MistakesLabel.setGeometry(QRect(110, 200, 271, 121))
        self.MistakesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Grade3 = QLabel(self.page_3)
        self.Grade3.setObjectName(u"Grade3")
        self.Grade3.setGeometry(QRect(1000, 220, 71, 71))
        self.Grade3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Grade4 = QLabel(self.page_3)
        self.Grade4.setObjectName(u"Grade4")
        self.Grade4.setGeometry(QRect(1080, 220, 71, 71))
        self.Grade4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.GradesLabel = QLabel(self.page_3)
        self.GradesLabel.setObjectName(u"GradesLabel")
        self.GradesLabel.setGeometry(QRect(360, 220, 581, 71))
        self.GradesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(130, 310, 1061, 271))
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 1059, 269))
        self.scrollAreaWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollAreaWidget.setAutoFillBackground(True)
        self.scrollGrid = QGridLayout(self.scrollAreaWidget)
        self.scrollGrid.setObjectName(u"scrollGrid")
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.ResultsLabel = QLabel(self.page_3)
        self.ResultsLabel.setObjectName(u"ResultsLabel")
        self.ResultsLabel.setGeometry(QRect(470, 50, 361, 91))
        self.ResultsLabel.setStyleSheet(u"font-size: 24px; color: #810031;")
        self.ResultsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Grade1 = QLabel(self.page_3)
        self.Grade1.setObjectName(u"Grade1")
        self.Grade1.setGeometry(QRect(840, 220, 71, 71))
        self.Grade1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Grade5 = QLabel(self.page_3)
        self.Grade5.setObjectName(u"Grade5")
        self.Grade5.setGeometry(QRect(1160, 220, 71, 71))
        self.Grade5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget = QWidget(self.page_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 600, 1151, 80))
        self.ButtonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.ButtonsLayout.setObjectName(u"ButtonsLayout")
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.SaveAndExit = QPushButton(self.horizontalLayoutWidget)
        self.SaveAndExit.setObjectName(u"SaveAndExit")
        self.SaveAndExit.setMinimumSize(QSize(500, 70))
        self.SaveAndExit.setMaximumSize(QSize(500, 70))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setKerning(False)
        self.SaveAndExit.setFont(font)
        self.SaveAndExit.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.SaveAndExit.setStyleSheet(u"QPushButton {\n"
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

        self.ButtonsLayout.addWidget(self.SaveAndExit)

        self.Repeat = QPushButton(self.horizontalLayoutWidget)
        self.Repeat.setObjectName(u"Repeat")
        self.Repeat.setMinimumSize(QSize(500, 70))
        self.Repeat.setMaximumSize(QSize(500, 70))
        self.Repeat.setFont(font)
        self.Repeat.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.Repeat.setStyleSheet(u"QPushButton {\n"
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
"    }\n"
"")

        self.ButtonsLayout.addWidget(self.Repeat)

        self.AnswersLabel = QLabel(self.page_3)
        self.AnswersLabel.setObjectName(u"AnswersLabel")
        self.AnswersLabel.setGeometry(QRect(350, 140, 601, 81))
        self.AnswersLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Grade2 = QLabel(self.page_3)
        self.Grade2.setObjectName(u"Grade2")
        self.Grade2.setGeometry(QRect(920, 220, 71, 71))
        self.Grade2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pages.addWidget(self.page_3)
        self.Lesson_screen = QWidget()
        self.Lesson_screen.setObjectName(u"Lesson_screen")
        self.verticalLayoutWidget_2 = QWidget(self.Lesson_screen)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 1447, 625))
        self.Main_Study_Layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.Main_Study_Layout.setSpacing(0)
        self.Main_Study_Layout.setObjectName(u"Main_Study_Layout")
        self.Main_Study_Layout.setContentsMargins(0, 0, 0, 0)
        self.word_centering2 = QSpacerItem(20, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Main_Study_Layout.addItem(self.word_centering2)

        self.Center_widget = QWidget(self.verticalLayoutWidget_2)
        self.Center_widget.setObjectName(u"Center_widget")
        self.Center_widget.setMinimumSize(QSize(0, 300))
        self.Center_widget.setMaximumSize(QSize(16777215, 260))
        self.The_word = QLabel(self.Center_widget)
        self.The_word.setObjectName(u"The_word")
        self.The_word.setGeometry(QRect(10, 40, 1271, 110))
        self.The_word.setMaximumSize(QSize(16777215, 110))
        font1 = QFont()
        font1.setPointSize(48)
        font1.setBold(True)
        self.The_word.setFont(font1)
        self.The_word.setStyleSheet(u"")
        self.The_word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.repeat_audio = QPushButton(self.Center_widget)
        self.repeat_audio.setObjectName(u"repeat_audio")
        self.repeat_audio.setGeometry(QRect(210, 150, 100, 100))
        self.repeat_audio.setMinimumSize(QSize(100, 100))
        self.repeat_audio.setMaximumSize(QSize(100, 100))
        self.repeat_audio.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.repeat_audio.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: none;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ccc\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #aaa\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../.designer/images/audio.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.repeat_audio.setIcon(icon1)
        self.repeat_audio.setIconSize(QSize(60, 60))
        self.restart_lesson = QPushButton(self.Center_widget)
        self.restart_lesson.setObjectName(u"restart_lesson")
        self.restart_lesson.setEnabled(True)
        self.restart_lesson.setGeometry(QRect(980, 150, 100, 100))
        self.restart_lesson.setMinimumSize(QSize(100, 100))
        self.restart_lesson.setMaximumSize(QSize(100, 100))
        self.restart_lesson.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.restart_lesson.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: none;\n"
"    border-radius: 50px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ccc\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #aaa\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../.designer/images/restart.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.restart_lesson.setIcon(icon2)
        self.restart_lesson.setIconSize(QSize(60, 60))
        self.word_translation = QLabel(self.Center_widget)
        self.word_translation.setObjectName(u"word_translation")
        self.word_translation.setGeometry(QRect(10, 130, 1271, 70))
        self.word_translation.setMinimumSize(QSize(0, 70))
        self.word_translation.setMaximumSize(QSize(16777215, 70))
        font2 = QFont()
        font2.setPointSize(32)
        self.word_translation.setFont(font2)
        self.word_translation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_transcription = QLabel(self.Center_widget)
        self.word_transcription.setObjectName(u"word_transcription")
        self.word_transcription.setGeometry(QRect(10, 20, 1271, 50))
        self.word_transcription.setMinimumSize(QSize(0, 50))
        self.word_transcription.setMaximumSize(QSize(16777215, 50))
        self.word_transcription.setFont(font2)
        self.word_transcription.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.checkBox = QCheckBox(self.Center_widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(690, 240, 181, 31))
        font3 = QFont()
        font3.setPointSize(15)
        self.checkBox.setFont(font3)
        self.Layout_type = QCheckBox(self.Center_widget)
        self.Layout_type.setObjectName(u"Layout_type")
        self.Layout_type.setEnabled(True)
        self.Layout_type.setGeometry(QRect(400, 240, 181, 31))
        self.Layout_type.setFont(font3)
        self.Layout_type.setChecked(False)

        self.Main_Study_Layout.addWidget(self.Center_widget)

        self.W_L_button_layout = QHBoxLayout()
        self.W_L_button_layout.setSpacing(0)
        self.W_L_button_layout.setObjectName(u"W_L_button_layout")
        self.W_L_button_layout.setContentsMargins(320, -1, 480, -1)
        self.button_spaceholder2_2 = QSpacerItem(5, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.W_L_button_layout.addItem(self.button_spaceholder2_2)

        self.L_answer = QPushButton(self.verticalLayoutWidget_2)
        self.L_answer.setObjectName(u"L_answer")
        self.L_answer.setMinimumSize(QSize(240, 70))
        self.L_answer.setMaximumSize(QSize(240, 70))
        self.L_answer.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.L_answer.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #c71050\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #e0487d\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #e86413\n"
"        );\n"
"    }")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../.designer/images/cross.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.L_answer.setIcon(icon3)
        self.L_answer.setIconSize(QSize(64, 64))

        self.W_L_button_layout.addWidget(self.L_answer)

        self.W_answer = QPushButton(self.verticalLayoutWidget_2)
        self.W_answer.setObjectName(u"W_answer")
        self.W_answer.setMinimumSize(QSize(240, 70))
        self.W_answer.setMaximumSize(QSize(240, 70))
        self.W_answer.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.W_answer.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #10a350\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #3cd665\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #28d413\n"
"        );\n"
"    }")
        icon4 = QIcon()
        icon4.addFile(u"../../../../../.designer/images/checked.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.W_answer.setIcon(icon4)
        self.W_answer.setIconSize(QSize(64, 64))

        self.W_L_button_layout.addWidget(self.W_answer)

        self.button_spaceholder2_3 = QSpacerItem(5, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.W_L_button_layout.addItem(self.button_spaceholder2_3)


        self.Main_Study_Layout.addLayout(self.W_L_button_layout)

        self.translation_layout = QHBoxLayout()
        self.translation_layout.setSpacing(0)
        self.translation_layout.setObjectName(u"translation_layout")
        self.translation_layout.setContentsMargins(83, 10, 237, 0)
        self.button_spaceholder2 = QSpacerItem(5, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.translation_layout.addItem(self.button_spaceholder2)

        self.translation = QPushButton(self.verticalLayoutWidget_2)
        self.translation.setObjectName(u"translation")
        self.translation.setEnabled(True)
        self.translation.setMinimumSize(QSize(500, 70))
        self.translation.setMaximumSize(QSize(520, 70))
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        self.translation.setFont(font4)
        self.translation.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.translation.setStyleSheet(u"QPushButton {\n"
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
"    }\n"
"")

        self.translation_layout.addWidget(self.translation)

        self.button_spaceholder1 = QSpacerItem(5, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.translation_layout.addItem(self.button_spaceholder1)


        self.Main_Study_Layout.addLayout(self.translation_layout)

        self.Back_widget = QWidget(self.Lesson_screen)
        self.Back_widget.setObjectName(u"Back_widget")
        self.Back_widget.setGeometry(QRect(10, 1, 1280, 120))
        self.Back_widget.setMinimumSize(QSize(1280, 120))
        self.Back_widget.setMaximumSize(QSize(1280, 16777215))
        self.prev_page = QPushButton(self.Back_widget)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setGeometry(QRect(280, 40, 100, 70))
        self.prev_page.setMinimumSize(QSize(100, 70))
        self.prev_page.setMaximumSize(QSize(100, 70))
        font5 = QFont()
        font5.setPointSize(9)
        self.prev_page.setFont(font5)
        self.prev_page.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.prev_page.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(199, 20, 47)\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(224, 53, 78)\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(232, 0, 0)\n"
"        );\n"
"    }")
        icon5 = QIcon()
        icon5.addFile(u"../../../../../.designer/images/return.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.prev_page.setIcon(icon5)
        self.prev_page.setIconSize(QSize(80, 60))
        self.prev_page.setAutoDefault(False)
        self.points_display = QLabel(self.Back_widget)
        self.points_display.setObjectName(u"points_display")
        self.points_display.setGeometry(QRect(650, 70, 341, 31))
        font6 = QFont()
        font6.setPointSize(20)
        self.points_display.setFont(font6)
        self.points_display.setStyleSheet(u"\n"
"    QLabel {\n"
"        padding: 10px;            /* Padding around the text */\n"
"        border-radius: 15px;      /* Rounded corners */\n"
"\n"
"    }\n"
"\n"
"")
        self.points_display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.pages.addWidget(self.Lesson_screen)
        self.Mode_Choose_screen = QWidget()
        self.Mode_Choose_screen.setObjectName(u"Mode_Choose_screen")
        self.verticalLayoutWidget_3 = QWidget(self.Mode_Choose_screen)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 1291, 721))
        self.Main_Mode_Layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.Main_Mode_Layout.setSpacing(9)
        self.Main_Mode_Layout.setObjectName(u"Main_Mode_Layout")
        self.Main_Mode_Layout.setContentsMargins(0, 0, 0, 0)
        self.Back_widget_2 = QWidget(self.verticalLayoutWidget_3)
        self.Back_widget_2.setObjectName(u"Back_widget_2")
        self.Back_widget_2.setMinimumSize(QSize(1280, 120))
        self.Back_widget_2.setMaximumSize(QSize(1280, 120))
        self.prev_page_2 = QPushButton(self.Back_widget_2)
        self.prev_page_2.setObjectName(u"prev_page_2")
        self.prev_page_2.setGeometry(QRect(280, 40, 100, 70))
        self.prev_page_2.setMinimumSize(QSize(100, 70))
        self.prev_page_2.setMaximumSize(QSize(100, 70))
        self.prev_page_2.setFont(font5)
        self.prev_page_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.prev_page_2.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(199, 20, 47)\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(224, 53, 78)\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 rgb(232, 0, 0)\n"
"        );\n"
"    }\n"
"")
        self.prev_page_2.setIcon(icon5)
        self.prev_page_2.setIconSize(QSize(80, 60))

        self.Main_Mode_Layout.addWidget(self.Back_widget_2)

        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.Main_Mode_Layout.addItem(self.verticalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.mode2stud = QPushButton(self.verticalLayoutWidget_3)
        self.mode2stud.setObjectName(u"mode2stud")
        self.mode2stud.setMinimumSize(QSize(700, 70))
        self.mode2stud.setMaximumSize(QSize(700, 16777215))
        self.mode2stud.setFont(font2)
        self.mode2stud.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.gridLayout.addWidget(self.mode2stud, 5, 0, 1, 1)

        self.mode3ex = QPushButton(self.verticalLayoutWidget_3)
        self.mode3ex.setObjectName(u"mode3ex")
        self.mode3ex.setMinimumSize(QSize(700, 70))
        self.mode3ex.setMaximumSize(QSize(700, 16777215))
        self.mode3ex.setFont(font2)
        self.mode3ex.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.gridLayout.addWidget(self.mode3ex, 6, 0, 1, 1)

        self.mode1intro = QPushButton(self.verticalLayoutWidget_3)
        self.mode1intro.setObjectName(u"mode1intro")
        self.mode1intro.setMinimumSize(QSize(700, 70))
        self.mode1intro.setMaximumSize(QSize(700, 16777215))
        self.mode1intro.setFont(font2)
        self.mode1intro.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.mode1intro.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.mode1intro, 2, 0, 1, 1)

        self.mode_choose = QLabel(self.verticalLayoutWidget_3)
        self.mode_choose.setObjectName(u"mode_choose")
        self.mode_choose.setEnabled(True)
        self.mode_choose.setMaximumSize(QSize(700, 70))
        font7 = QFont()
        font7.setPointSize(44)
        font7.setBold(True)
        self.mode_choose.setFont(font7)
        self.mode_choose.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.mode_choose, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)


        self.Main_Mode_Layout.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.Main_Mode_Layout.addItem(self.verticalSpacer)

        self.pages.addWidget(self.Mode_Choose_screen)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.scrollArea_2 = QScrollArea(self.page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-10, 0, 1300, 720))
        self.scrollArea_2.setMaximumSize(QSize(1300, 720))
        self.scrollArea_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidget_2 = QWidget()
        self.scrollAreaWidget_2.setObjectName(u"scrollAreaWidget_2")
        self.scrollAreaWidget_2.setGeometry(QRect(0, 0, 1298, 718))
        self.scrollAreaWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollAreaWidget_2.setAutoFillBackground(True)
        self.groupGrid = QGridLayout(self.scrollAreaWidget_2)
        self.groupGrid.setSpacing(6)
        self.groupGrid.setObjectName(u"groupGrid")
        self.groupGrid.setContentsMargins(9, 9, 9, 9)
        self.scrollArea_2.setWidget(self.scrollAreaWidget_2)
        self.pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.scrollArea_3 = QScrollArea(self.page_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setGeometry(QRect(-10, 0, 1300, 720))
        self.scrollArea_3.setMaximumSize(QSize(1300, 720))
        self.scrollArea_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidget_5 = QWidget()
        self.scrollAreaWidget_5.setObjectName(u"scrollAreaWidget_5")
        self.scrollAreaWidget_5.setGeometry(QRect(0, 0, 1298, 718))
        self.scrollAreaWidget_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollAreaWidget_5.setAutoFillBackground(True)
        self.groupGrid_2 = QGridLayout(self.scrollAreaWidget_5)
        self.groupGrid_2.setSpacing(6)
        self.groupGrid_2.setObjectName(u"groupGrid_2")
        self.groupGrid_2.setContentsMargins(9, 9, 9, 9)
        self.scrollArea_3.setWidget(self.scrollAreaWidget_5)
        self.pages.addWidget(self.page_2)

        self.Base_Layout.addWidget(self.pages)

        self.verticalSpacer_2 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.Base_Layout.addItem(self.verticalSpacer_2)


        self.retranslateUi(SEEnglish)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SEEnglish)
    # setupUi

    def retranslateUi(self, SEEnglish):
        SEEnglish.setWindowTitle(QCoreApplication.translate("SEEnglish", u"Shark's Empire: English", None))
        self.MistakesLabel.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700; color:#00007f;\">Mistakes:</span></p></body></html>", None))
        self.Grade3.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><br/></p></body></html>", None))
        self.Grade4.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><br/></p></body></html>", None))
        self.GradesLabel.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700; color:#00007f;\">Recent grades:</span></p></body></html>", None))
        self.ResultsLabel.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:700; color:#810031;\">Results</span></p></body></html>", None))
        self.Grade1.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><br/></p></body></html>", None))
        self.Grade5.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><br/></p></body></html>", None))
        self.SaveAndExit.setText(QCoreApplication.translate("SEEnglish", u"Save and switch Lesson", None))
        self.Repeat.setText(QCoreApplication.translate("SEEnglish", u"Next lesson", None))
        self.AnswersLabel.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:700; color:#00007f;\">Correct answers: </span></p></body></html>", None))
        self.Grade2.setText(QCoreApplication.translate("SEEnglish", u"<html><head/><body><p><br/></p></body></html>", None))
        self.The_word.setText(QCoreApplication.translate("SEEnglish", u"WordLabel", None))
        self.repeat_audio.setText("")
        self.restart_lesson.setText("")
        self.word_translation.setText(QCoreApplication.translate("SEEnglish", u"Translation", None))
        self.word_transcription.setText(QCoreApplication.translate("SEEnglish", u"Transcription", None))
        self.checkBox.setText(QCoreApplication.translate("SEEnglish", u"Show mistakes", None))
        self.Layout_type.setText(QCoreApplication.translate("SEEnglish", u"Buttons layout ", None))
        self.L_answer.setText("")
        self.W_answer.setText("")
        self.translation.setText(QCoreApplication.translate("SEEnglish", u"Reveal Translation", None))
        self.prev_page.setText("")
        self.points_display.setText("")
        self.prev_page_2.setText("")
        self.mode2stud.setText(QCoreApplication.translate("SEEnglish", u"\u0418\u0437\u0443\u0447\u0435\u043d\u0438\u0435 \u0441\u043b\u043e\u0432", None))
        self.mode3ex.setText(QCoreApplication.translate("SEEnglish", u"\u0415\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.mode1intro.setText(QCoreApplication.translate("SEEnglish", u"\u0421\u043b\u043e\u0432\u0430 \u0432 \u044d\u0442\u043e\u043c \u0443\u0440\u043e\u043a\u0435", None))
        self.mode_choose.setText(QCoreApplication.translate("SEEnglish", u"\u0412\u044b\u0431\u043e\u0440 \u0440\u0435\u0436\u0438\u043c\u0430", None))
    # retranslateUi

