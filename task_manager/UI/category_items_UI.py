# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_list_item_widgetaGGJZS.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_cateogry_list_items(object):
    def setupUi(self, cateogry_list_items):
        if not cateogry_list_items.objectName():
            cateogry_list_items.setObjectName(u"cateogry_list_items")
        cateogry_list_items.resize(496, 38)
        cateogry_list_items.setStyleSheet(u"margin: 0;\n"
"padding:0;\n"
"border: 0")
        self.horizontalLayout_2 = QHBoxLayout(cateogry_list_items)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_category = QCheckBox(cateogry_list_items)
        self.checkBox_category.setObjectName(u"checkBox_category")
        self.checkBox_category.setStyleSheet(u"margin: 0;\n"
"border: 0;\n"
"padding: 0px 0px 0px 0px;")

        self.horizontalLayout.addWidget(self.checkBox_category, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.category_name = QLabel(cateogry_list_items)
        self.category_name.setObjectName(u"category_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category_name.sizePolicy().hasHeightForWidth())
        self.category_name.setSizePolicy(sizePolicy)
        self.category_name.setMinimumSize(QSize(400, 0))
        self.category_name.setMaximumSize(QSize(500, 60))
        self.category_name.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"border: 0;")

        self.horizontalLayout.addWidget(self.category_name, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.delete_category_btn = QPushButton(cateogry_list_items)
        self.delete_category_btn.setObjectName(u"delete_category_btn")
        self.delete_category_btn.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"border: 0;")

        self.horizontalLayout.addWidget(self.delete_category_btn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(cateogry_list_items)

        QMetaObject.connectSlotsByName(cateogry_list_items)
    # setupUi

    def retranslateUi(self, cateogry_list_items):
        cateogry_list_items.setWindowTitle(QCoreApplication.translate("cateogry_list_items", u"Form", None))
        self.checkBox_category.setText("")
        self.category_name.setText(QCoreApplication.translate("cateogry_list_items", u"TextLabel", None))
        self.delete_category_btn.setText(QCoreApplication.translate("cateogry_list_items", u"delete", None))
    # retranslateUi

