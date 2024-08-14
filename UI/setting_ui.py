# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 400)
        Form.setMinimumSize(QSize(480, 400))
        Form.setMaximumSize(QSize(700, 600))
        Form.setStyleSheet(u"#Form {\n"
"	background-image: url(./Image/bg.png);         \n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalFrame = QFrame(Form)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setMaximumSize(QSize(16777215, 60))
        self.verticalFrame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.verticalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(15, -1, -1, 9)
        self.startTitle_QLabel = QLabel(self.verticalFrame)
        self.startTitle_QLabel.setObjectName(u"startTitle_QLabel")
        self.startTitle_QLabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        font.setPointSize(16)
        font.setBold(True)
        self.startTitle_QLabel.setFont(font)
        self.startTitle_QLabel.setStyleSheet(u"QLabel {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.startTitle_QLabel)

        self.back_pushButton = QPushButton(self.verticalFrame)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setEnabled(True)
        self.back_pushButton.setMinimumSize(QSize(0, 30))
        self.back_pushButton.setMaximumSize(QSize(100, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        self.back_pushButton.setFont(font1)
        self.back_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.back_pushButton)


        self.verticalLayout.addWidget(self.verticalFrame)

        self.verticalFrame_2 = QFrame(Form)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMinimumSize(QSize(0, 280))
        self.verticalFrame_2.setMaximumSize(QSize(16777215, 280))
        self.verticalFrame_2.setStyleSheet(u".QFrame{\n"
"	border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"	background-color: #000000;\n"
"}\n"
".QWidget{\n"
"    background-color: #222222;\n"
"    color: white;\n"
"    border: 2px solid #262626;\n"
"    border-radius: 14px;\n"
"}\n"
"\n"
"\n"
".QLabel {\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	border-radius:14px;\n"
"	background-color:#000000;\n"
"    color:rgb(255,255,255);\n"
"    border:2px solid #323232;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:disabled\n"
"{\n"
"	background-color:rgba(50,50,50,200);\n"
"    color:rgb(160,160,160);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color:#000000;\n"
"	border:2px solid #a6c100 ;\n"
"}\n"
"/*\u70b9\u51fbcombox\u7684\u6837\u5f0f*/\n"
"QComboBox:on\n"
"{\n"
"	border-radius:14px;\n"
"	background-color:#000000;\n"
"    color:#ffffff;\n"
"    border:2px solid #a6c100  ;\n"
"}\n"
"\n"
"\n"
"\n"
"/*\u4e0b\u62c9\u6846\u7684\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView \n"
"{\n"
"    outline: 0px solid g"
                        "ray;  /*\u53d6\u6d88\u9009\u4e2d\u865a\u7ebf*/\n"
"    border: 0px solid rgb(31,156,220);  \n"
"    color: #ffffff;\n"
"    background-color: #222222;   \n"
"    selection-background-color: #a6c100;   \n"
"	border-radius:14px;\n"
"\n"
"}\n"
" /*\u9009\u4e2d\u6bcf\u4e00\u9879\u9ad8\u5ea6*/\n"
"QComboBox QAbstractItemView::item\n"
" { \n"
"	\n"
"	height: 30px;\n"
"	 border-radius: 8px;\n"
"    min-height:30px;\n"
"\n"
" }\n"
"/*\u9009\u4e2d\u6bcf\u4e00\u9879\u7684\u5b57\u4f53\u989c\u8272\u548c\u80cc\u666f\u989c\u8272*/\n"
"QComboBox QAbstractItemView::item:selected \n"
"{\n"
"    color: #000000;\n"
"	background-color: #a6c100 ; \n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"	border:none;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.Evasion_setting = QWidget(self.verticalFrame_2)
        self.Evasion_setting.setObjectName(u"Evasion_setting")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Evasion_setting.sizePolicy().hasHeightForWidth())
        self.Evasion_setting.setSizePolicy(sizePolicy)
        self.Evasion_setting.setMaximumSize(QSize(16777215, 40))
        self.Evasion_setting.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.Evasion_setting)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.Evasion_label = QLabel(self.Evasion_setting)
        self.Evasion_label.setObjectName(u"Evasion_label")
        self.Evasion_label.setMinimumSize(QSize(0, 40))
        self.Evasion_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.Evasion_label)

        self.Evasion_comBox = QComboBox(self.Evasion_setting)
        self.Evasion_comBox.addItem("")
        self.Evasion_comBox.addItem("")
        self.Evasion_comBox.addItem("")
        self.Evasion_comBox.setObjectName(u"Evasion_comBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.Evasion_comBox.sizePolicy().hasHeightForWidth())
        self.Evasion_comBox.setSizePolicy(sizePolicy1)
        self.Evasion_comBox.setMinimumSize(QSize(0, 30))
        self.Evasion_comBox.setMaximumSize(QSize(120, 30))
        self.Evasion_comBox.setSizeIncrement(QSize(0, 30))
        self.Evasion_comBox.setFont(font1)

        self.horizontalLayout_3.addWidget(self.Evasion_comBox)


        self.verticalLayout_2.addWidget(self.Evasion_setting)

        self.bounce_Setting = QWidget(self.verticalFrame_2)
        self.bounce_Setting.setObjectName(u"bounce_Setting")
        self.bounce_Setting.setMinimumSize(QSize(0, 40))
        self.bounce_Setting.setMaximumSize(QSize(16777215, 40))
        self.bounce_Setting.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.bounce_Setting)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.bounce_label = QLabel(self.bounce_Setting)
        self.bounce_label.setObjectName(u"bounce_label")
        self.bounce_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.bounce_label)

        self.bounce_comboBox = QComboBox(self.bounce_Setting)
        self.bounce_comboBox.addItem("")
        self.bounce_comboBox.addItem("")
        self.bounce_comboBox.addItem("")
        self.bounce_comboBox.setObjectName(u"bounce_comboBox")
        self.bounce_comboBox.setMinimumSize(QSize(0, 30))
        self.bounce_comboBox.setMaximumSize(QSize(120, 30))
        self.bounce_comboBox.setFont(font1)

        self.horizontalLayout_4.addWidget(self.bounce_comboBox)


        self.verticalLayout_2.addWidget(self.bounce_Setting)

        self.determineMode_Setting = QWidget(self.verticalFrame_2)
        self.determineMode_Setting.setObjectName(u"determineMode_Setting")
        self.determineMode_Setting.setMinimumSize(QSize(0, 40))
        self.determineMode_Setting.setMaximumSize(QSize(16777215, 40))
        self.determineMode_Setting.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.determineMode_Setting)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.determineMode_label = QLabel(self.determineMode_Setting)
        self.determineMode_label.setObjectName(u"determineMode_label")
        self.determineMode_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.determineMode_label)

        self.determineMode_comboBox = QComboBox(self.determineMode_Setting)
        self.determineMode_comboBox.addItem("")
        self.determineMode_comboBox.addItem("")
        self.determineMode_comboBox.setObjectName(u"determineMode_comboBox")
        self.determineMode_comboBox.setMinimumSize(QSize(120, 30))
        self.determineMode_comboBox.setMaximumSize(QSize(120, 30))
        self.determineMode_comboBox.setSizeIncrement(QSize(0, 0))
        self.determineMode_comboBox.setFont(font1)

        self.horizontalLayout_6.addWidget(self.determineMode_comboBox)


        self.verticalLayout_2.addWidget(self.determineMode_Setting)

        self.operationMode_setting = QWidget(self.verticalFrame_2)
        self.operationMode_setting.setObjectName(u"operationMode_setting")
        self.operationMode_setting.setMinimumSize(QSize(0, 40))
        self.operationMode_setting.setMaximumSize(QSize(16777215, 40))
        self.operationMode_setting.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.operationMode_setting)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.operationMode_label = QLabel(self.operationMode_setting)
        self.operationMode_label.setObjectName(u"operationMode_label")
        self.operationMode_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.operationMode_label)

        self.operationMode_comboBox = QComboBox(self.operationMode_setting)
        self.operationMode_comboBox.addItem("")
        self.operationMode_comboBox.addItem("")
        self.operationMode_comboBox.addItem("")
        self.operationMode_comboBox.setObjectName(u"operationMode_comboBox")
        self.operationMode_comboBox.setMinimumSize(QSize(120, 30))
        self.operationMode_comboBox.setMaximumSize(QSize(120, 30))
        self.operationMode_comboBox.setFont(font1)

        self.horizontalLayout_5.addWidget(self.operationMode_comboBox)


        self.verticalLayout_2.addWidget(self.operationMode_setting)

        self.outTone_Setting = QWidget(self.verticalFrame_2)
        self.outTone_Setting.setObjectName(u"outTone_Setting")
        self.outTone_Setting.setMinimumSize(QSize(0, 40))
        self.outTone_Setting.setMaximumSize(QSize(16777215, 40))
        self.outTone_Setting.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.outTone_Setting)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.outTone_label = QLabel(self.outTone_Setting)
        self.outTone_label.setObjectName(u"outTone_label")
        self.outTone_label.setFont(font1)

        self.horizontalLayout.addWidget(self.outTone_label)

        self.outTone_comboBox = QComboBox(self.outTone_Setting)
        self.outTone_comboBox.addItem("")
        self.outTone_comboBox.addItem("")
        self.outTone_comboBox.setObjectName(u"outTone_comboBox")
        self.outTone_comboBox.setMinimumSize(QSize(120, 30))
        self.outTone_comboBox.setMaximumSize(QSize(120, 30))
        self.outTone_comboBox.setFont(font1)

        self.horizontalLayout.addWidget(self.outTone_comboBox)


        self.verticalLayout_2.addWidget(self.outTone_Setting)

        self.inTone_Setting = QWidget(self.verticalFrame_2)
        self.inTone_Setting.setObjectName(u"inTone_Setting")
        self.inTone_Setting.setMinimumSize(QSize(0, 40))
        self.inTone_Setting.setMaximumSize(QSize(16777215, 40))
        self.inTone_Setting.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.inTone_Setting)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.inTone_label = QLabel(self.inTone_Setting)
        self.inTone_label.setObjectName(u"inTone_label")
        self.inTone_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.inTone_label)

        self.inTone_comboBox = QComboBox(self.inTone_Setting)
        self.inTone_comboBox.addItem("")
        self.inTone_comboBox.addItem("")
        self.inTone_comboBox.setObjectName(u"inTone_comboBox")
        self.inTone_comboBox.setMinimumSize(QSize(120, 30))
        self.inTone_comboBox.setMaximumSize(QSize(120, 30))
        self.inTone_comboBox.setFont(font1)

        self.horizontalLayout_9.addWidget(self.inTone_comboBox)


        self.verticalLayout_2.addWidget(self.inTone_Setting)


        self.verticalLayout.addWidget(self.verticalFrame_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.startTitle_QLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.back_pushButton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de/\u4fdd\u5b58", None))
        self.Evasion_label.setText(QCoreApplication.translate("Form", u"\u95ea\u907f", None))
        self.Evasion_comBox.setItemText(0, QCoreApplication.translate("Form", u"\u6781\u9650\u5f39\u95ea", None))
        self.Evasion_comBox.setItemText(1, QCoreApplication.translate("Form", u"\u6781\u9650\u652f\u63f4", None))
        self.Evasion_comBox.setItemText(2, QCoreApplication.translate("Form", u"\u6781\u9650\u95ea\u907f", None))

        self.bounce_label.setText(QCoreApplication.translate("Form", u"\u5f39\u53cd", None))
        self.bounce_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u540c\u8f74\u95ea\u907f", None))
        self.bounce_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6781\u9650\u53cc\u95ea", None))
        self.bounce_comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u6781\u9650\u95ea\u907f", None))

        self.determineMode_label.setText(QCoreApplication.translate("Form", u"\u5224\u65ad\u65b9\u5f0f", None))
        self.determineMode_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u89c6\u89c9", None))
        self.determineMode_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u97f3\u9891", None))

        self.operationMode_label.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u65b9\u5f0f", None))
        self.operationMode_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u81ea\u52a8", None))
        self.operationMode_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u952e\u9f20", None))
        self.operationMode_comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u624b\u67c4", None))

        self.outTone_label.setText(QCoreApplication.translate("Form", u"\u5c40\u5916\u63d0\u793a\u8bed\u97f3", None))
        self.outTone_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.outTone_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u5173\u95ed", None))

        self.inTone_label.setText(QCoreApplication.translate("Form", u"\u5c40\u5185\u63d0\u793a\u8bed\u97f3", None))
        self.inTone_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u5f00\u542f", None))
        self.inTone_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u5173\u95ed", None))

    # retranslateUi

