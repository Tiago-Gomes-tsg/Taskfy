# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_list_item_widgetjzPLEr.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_category_list_items(object):
    def setupUi(self, category_list_items):
        if not category_list_items.objectName():
            category_list_items.setObjectName(u"category_list_items")
        category_list_items.resize(496, 38)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(category_list_items.sizePolicy().hasHeightForWidth())
        category_list_items.setSizePolicy(sizePolicy)
        category_list_items.setStyleSheet(u"margin: 0;\n"
"padding:0;\n"
"border: 0;\n"
"background: white;")
        self.horizontalLayout_2 = QHBoxLayout(category_list_items)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category_name = QLabel(category_list_items)
        self.category_name.setObjectName(u"category_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.category_name.sizePolicy().hasHeightForWidth())
        self.category_name.setSizePolicy(sizePolicy1)
        self.category_name.setMinimumSize(QSize(400, 0))
        self.category_name.setMaximumSize(QSize(500, 60))
        self.category_name.setStyleSheet(u"margin: 0;\n"
"border: 2px solid black;\n"
"border-right: none;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"padding: 0px 0px 0px 16px;\n"
"color: black;")

        self.horizontalLayout.addWidget(self.category_name, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.delete_category_btn = QPushButton(category_list_items)
        self.delete_category_btn.setObjectName(u"delete_category_btn")
        self.delete_category_btn.setMaximumSize(QSize(16777215, 20))
        self.delete_category_btn.setStyleSheet(u"margin: 0;;\n"
"border: 2px solid black;\n"
"border-left: none;\n"
"border-radius: 10px;\n"
"border-top-left-radius: none;\n"
"border-bottom-left-radius: none;\n"
"color: black;")
        icon = QIcon()
        icon.addFile(u"assets/trash_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_category_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.delete_category_btn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(category_list_items)

        QMetaObject.connectSlotsByName(category_list_items)
    # setupUi

    def retranslateUi(self, category_list_items):
        category_list_items.setWindowTitle(QCoreApplication.translate("category_list_items", u"Form", None))
        self.category_name.setText(QCoreApplication.translate("category_list_items", u"TextLabel", None))
        self.delete_category_btn.setText("")
    # retranslateUi

