# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 400)
        Form.setMinimumSize(QSize(480, 400))
        Form.setMaximumSize(QSize(700, 600))
        Form.setStyleSheet(u"#Form {\n"
"	background-image: url(./Image/bg.png);         \n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(Form)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.vboxLayout = QVBoxLayout(self.verticalFrame)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.vboxLayout.setContentsMargins(30, -1, -1, -1)
        self.startTitle_QLabel = QLabel(self.verticalFrame)
        self.startTitle_QLabel.setObjectName(u"startTitle_QLabel")
        self.startTitle_QLabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        font.setPointSize(16)
        font.setBold(False)
        self.startTitle_QLabel.setFont(font)
        self.startTitle_QLabel.setStyleSheet(u"QLabel {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.vboxLayout.addWidget(self.startTitle_QLabel)


        self.verticalLayout.addWidget(self.verticalFrame)

        self.verticalFrame_2 = QFrame(Form)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"	border-radius: 14px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.start_pushButton = QPushButton(self.verticalFrame_2)
        self.start_pushButton.setObjectName(u"start_pushButton")
        self.start_pushButton.setMinimumSize(QSize(0, 30))
        self.start_pushButton.setMaximumSize(QSize(200, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        self.start_pushButton.setFont(font1)
        self.start_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid  #a6c100;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"	border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.start_pushButton)

        self.stop_pushButton = QPushButton(self.verticalFrame_2)
        self.stop_pushButton.setObjectName(u"stop_pushButton")
        self.stop_pushButton.setMinimumSize(QSize(0, 30))
        self.stop_pushButton.setMaximumSize(QSize(200, 50))
        self.stop_pushButton.setFont(font1)
        self.stop_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid  #f48322;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #f48322;\n"
"    color: black;\n"
"    border: 5px solid #f48322;\n"
"	border-radius: 14px;\n"
"}")
        self.stop_pushButton.setProperty("hidden", True)

        self.verticalLayout_2.addWidget(self.stop_pushButton)

        self.setting_pushButton = QPushButton(self.verticalFrame_2)
        self.setting_pushButton.setObjectName(u"setting_pushButton")
        self.setting_pushButton.setMinimumSize(QSize(0, 30))
        self.setting_pushButton.setMaximumSize(QSize(200, 50))
        self.setting_pushButton.setFont(font1)
        self.setting_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid  #0078d4;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0078d4;\n"
"    color: black;\n"
"    border: 5px solid #0078d4;\n"
"	border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.setting_pushButton)

        self.about_pushButton = QPushButton(self.verticalFrame_2)
        self.about_pushButton.setObjectName(u"about_pushButton")
        self.about_pushButton.setMinimumSize(QSize(0, 30))
        self.about_pushButton.setMaximumSize(QSize(200, 50))
        self.about_pushButton.setFont(font1)
        self.about_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid  #ffdb29;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ffdb29;\n"
"    color: black;\n"
"    border: 5px solid #ffdb29;\n"
"	border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.about_pushButton)

        self.exit_pushButton = QPushButton(self.verticalFrame_2)
        self.exit_pushButton.setObjectName(u"exit_pushButton")
        self.exit_pushButton.setEnabled(True)
        self.exit_pushButton.setMinimumSize(QSize(0, 30))
        self.exit_pushButton.setMaximumSize(QSize(200, 50))
        self.exit_pushButton.setFont(font1)
        self.exit_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 2px solid  #aa0000;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #aa0000;\n"
"    color: black;\n"
"    border: 5px solid #aa0000;\n"
"	border-radius: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.exit_pushButton)


        self.verticalLayout.addWidget(self.verticalFrame_2)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        QWidget.setTabOrder(self.start_pushButton, self.setting_pushButton)
        QWidget.setTabOrder(self.setting_pushButton, self.about_pushButton)
        QWidget.setTabOrder(self.about_pushButton, self.exit_pushButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.startTitle_QLabel.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u4f7f\u7528 H.D.D \u95ea\u907f\u4ee3\u7406\u7cfb\u7edf", None))
        self.start_pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u4ee3\u7406\uff08F8\uff09", None))
        self.stop_pushButton.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u4ee3\u7406\uff08F9\uff09", None))
        self.setting_pushButton.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.about_pushButton.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e\u7cfb\u7edf", None))
        self.exit_pushButton.setText(QCoreApplication.translate("Form", u"\u9000\u51fa\u7cfb\u7edf", None))
    # retranslateUi

