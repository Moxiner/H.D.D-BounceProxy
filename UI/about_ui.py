# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 400)
        Form.setMinimumSize(QSize(480, 400))
        Form.setMaximumSize(QSize(700, 600))
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.version_pushButton = QPushButton(Form)
        self.version_pushButton.setObjectName(u"version_pushButton")
        font2 = QFont()
        font2.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        font2.setUnderline(False)
        self.version_pushButton.setFont(font2)
        self.version_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    color:#a6c100;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.version_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.author_pushButton = QPushButton(Form)
        self.author_pushButton.setObjectName(u"author_pushButton")
        font3 = QFont()
        font3.setFamilies([u"\u5370\u54c1\u9e3f\u8499\u4f53\uff08\u975e\u5546\u7528\uff09"])
        font3.setUnderline(True)
        self.author_pushButton.setFont(font3)
        self.author_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    color:#a6c100;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.author_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.PPicku__pushButton = QPushButton(Form)
        self.PPicku__pushButton.setObjectName(u"PPicku__pushButton")
        self.PPicku__pushButton.setFont(font3)
        self.PPicku__pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    color:#a6c100;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.PPicku__pushButton)

        self.xigua__pushButton = QPushButton(Form)
        self.xigua__pushButton.setObjectName(u"xigua__pushButton")
        self.xigua__pushButton.setFont(font3)
        self.xigua__pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    color:#a6c100;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.xigua__pushButton)

        self.ImLaoBJie_pushButton = QPushButton(Form)
        self.ImLaoBJie_pushButton.setObjectName(u"ImLaoBJie_pushButton")
        self.ImLaoBJie_pushButton.setFont(font3)
        self.ImLaoBJie_pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"    color:#a6c100;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.ImLaoBJie_pushButton)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 30, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.openLog_pushButton = QPushButton(Form)
        self.openLog_pushButton.setObjectName(u"openLog_pushButton")
        self.openLog_pushButton.setEnabled(True)
        self.openLog_pushButton.setMinimumSize(QSize(150, 30))
        self.openLog_pushButton.setMaximumSize(QSize(150, 50))
        self.openLog_pushButton.setFont(font1)
        self.openLog_pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_5.addWidget(self.openLog_pushButton)

        self.back_pushButton = QPushButton(Form)
        self.back_pushButton.setObjectName(u"back_pushButton")
        self.back_pushButton.setEnabled(True)
        self.back_pushButton.setMinimumSize(QSize(150, 30))
        self.back_pushButton.setMaximumSize(QSize(150, 50))
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

        self.horizontalLayout_5.addWidget(self.back_pushButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"H.D.D\u95ea\u907f\u4ee3\u7406\u7cfb\u7edf - \u81ea\u52a8\u5f39\u53cd", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u7248\u672c\u53f7", None))
        self.version_pushButton.setText(QCoreApplication.translate("Form", u"v0.01", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4f5c\u8005\uff1a", None))
        self.author_pushButton.setText(QCoreApplication.translate("Form", u"Moxiner", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u611f\u8c22\u4ee5\u4e0b\u5f00\u53d1\u8005\u5bf9\u5f00\u6e90\u793e\u533a\u505a\u51fa\u7684\u8d21\u732e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u672c\u9879\u76ee\u5f15\u7528\u4ee5\u4e0b\u6e90\u4ee3\u7801", None))
        self.PPicku__pushButton.setText(QCoreApplication.translate("Form", u"H.D.D-System    By\uff1aPPicku", None))
        self.xigua__pushButton.setText(QCoreApplication.translate("Form", u"\u57fa\u4e8e\u89c6\u89c9\u68c0\u6d4b\u7684\u81ea\u52a8\u5f39\u53cd    By\uff1a\u897f\u74dc\u52a0\u7cd6\u7cbe", None))
        self.ImLaoBJie_pushButton.setText(QCoreApplication.translate("Form", u"ZZZSoundTrigger    By\uff1aImLaoBJie", None))
        self.openLog_pushButton.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u65e5\u5fd7", None))
        self.back_pushButton.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

