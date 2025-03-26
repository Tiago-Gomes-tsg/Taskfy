# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filter_widgetghTMrE.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_filterWidget(object):
    def setupUi(self, filterWidget):
        if not filterWidget.objectName():
            filterWidget.setObjectName(u"filterWidget")
        filterWidget.resize(400, 300)
        filterWidget.setStyleSheet(u"background: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        self.verticalLayout_2 = QVBoxLayout(filterWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(filterWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background: #f3d2c1;\n"
"padding: 10px;\n"
"")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollWidgetCategory = QWidget()
        self.scrollWidgetCategory.setObjectName(u"scrollWidgetCategory")
        self.scrollWidgetCategory.setGeometry(QRect(0, 0, 356, 214))
        self.scrollWidgetCategory.setStyleSheet(u"border: 0;\n"
"margin: 0;\n"
"padding: 0;")
        self.scroll_categories_layout = QVBoxLayout(self.scrollWidgetCategory)
        self.scroll_categories_layout.setSpacing(0)
        self.scroll_categories_layout.setObjectName(u"scroll_categories_layout")
        self.scroll_categories_layout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea.setWidget(self.scrollWidgetCategory)

        self.verticalLayout.addWidget(self.scrollArea)

        self.apply_filter_btn = QPushButton(filterWidget)
        self.apply_filter_btn.setObjectName(u"apply_filter_btn")
        self.apply_filter_btn.setStyleSheet(u"margin: 5px 0px 5px 0px;\n"
"padding: 2px 0px 2px 5px;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"color: black;\n"
"background: white;\n"
"font: bold;")

        self.verticalLayout.addWidget(self.apply_filter_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(filterWidget)

        QMetaObject.connectSlotsByName(filterWidget)
    # setupUi

    def retranslateUi(self, filterWidget):
        filterWidget.setWindowTitle(QCoreApplication.translate("filterWidget", u"Form", None))
        self.apply_filter_btn.setText(QCoreApplication.translate("filterWidget", u"Apply Filter", None))
    # retranslateUi

