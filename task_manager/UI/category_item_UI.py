# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_itemcNLRPH.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_categoryItem(object):
    def setupUi(self, categoryItem):
        if not categoryItem.objectName():
            categoryItem.setObjectName(u"categoryItem")
        categoryItem.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(categoryItem.sizePolicy().hasHeightForWidth())
        categoryItem.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(categoryItem)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkbox_category_Filter = QCheckBox(categoryItem)
        self.checkbox_category_Filter.setObjectName(u"checkbox_category_Filter")
        self.checkbox_category_Filter.setMinimumSize(QSize(25, 25))
        self.checkbox_category_Filter.setMaximumSize(QSize(25, 25))
        self.checkbox_category_Filter.setStyleSheet(u"margin: 0px 0px 0px 10px;\n"
"border: 0;\n"
"padding: 0px 0px 0px 16px;")

        self.horizontalLayout.addWidget(self.checkbox_category_Filter)

        self.category_name = QLabel(categoryItem)
        self.category_name.setObjectName(u"category_name")
        self.category_name.setMinimumSize(QSize(0, 25))
        self.category_name.setMaximumSize(QSize(16777215, 25))
        self.category_name.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"border: 0;\n"
"color: black;")
        self.category_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.category_name)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(categoryItem)

        QMetaObject.connectSlotsByName(categoryItem)
    # setupUi

    def retranslateUi(self, categoryItem):
        categoryItem.setWindowTitle(QCoreApplication.translate("categoryItem", u"Form", None))
        self.checkbox_category_Filter.setText("")
        self.category_name.setText(QCoreApplication.translate("categoryItem", u"Category Name", None))
    # retranslateUi

