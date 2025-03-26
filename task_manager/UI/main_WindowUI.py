# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_widgetvNWPIs.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(906, 693)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: #fef6e4;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sideBar = QFrame(self.centralwidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setEnabled(True)
        self.sideBar.setMinimumSize(QSize(200, 200))
        self.sideBar.setMaximumSize(QSize(200, 16777215))
        self.sideBar.setStyleSheet(u"background: #f3d2c1;\n"
"padding: 5px;\n"
"border: 1.5px solid black;\n"
"border-radius: 15px;")
        self.sideBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sideBar.setFrameShadow(QFrame.Shadow.Raised)
        self.sideBar.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.sideBar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.banner = QWidget(self.sideBar)
        self.banner.setObjectName(u"banner")
        self.banner.setMaximumSize(QSize(16777215, 50))
        self.banner.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"background: white;\n"
"border-radius: 10px;")
        self.horizontalLayout_3 = QHBoxLayout(self.banner)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.app_icon = QLabel(self.banner)
        self.app_icon.setObjectName(u"app_icon")
        self.app_icon.setMaximumSize(QSize(35, 50))
        font = QFont()
        font.setPointSize(11)
        self.app_icon.setFont(font)
        self.app_icon.setAutoFillBackground(False)
        self.app_icon.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"border: none;")
        self.app_icon.setPixmap(QPixmap(u"assets/icon.svg"))
        self.app_icon.setScaledContents(True)
        self.app_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.app_icon)

        self.app_name = QLabel(self.banner)
        self.app_name.setObjectName(u"app_name")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.app_name.setFont(font1)
        self.app_name.setStyleSheet(u"color: black")
        self.app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.app_name)


        self.verticalLayout_2.addWidget(self.banner, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.widget_chart_container = QWidget(self.sideBar)
        self.widget_chart_container.setObjectName(u"widget_chart_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_chart_container.sizePolicy().hasHeightForWidth())
        self.widget_chart_container.setSizePolicy(sizePolicy)
        self.widget_chart_container.setStyleSheet(u"border: 0;\n"
"padding: 0;\n"
"margin: 0;\n"
"")
        self.donut_chart_container = QVBoxLayout(self.widget_chart_container)
        self.donut_chart_container.setObjectName(u"donut_chart_container")

        self.verticalLayout_2.addWidget(self.widget_chart_container)

        self.button_tasks = QPushButton(self.sideBar)
        self.button_tasks.setObjectName(u"button_tasks")
        self.button_tasks.setStyleSheet(u"margin: 0px 0px 0px 10px;\n"
"padding: 0;\n"
"border: 0;\n"
"border-radius: 0;\n"
"color: black;")
        icon = QIcon()
        icon.addFile(u"assets/task_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_tasks.setIcon(icon)
        self.button_tasks.setIconSize(QSize(18, 18))

        self.verticalLayout_2.addWidget(self.button_tasks, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_categories = QPushButton(self.sideBar)
        self.button_categories.setObjectName(u"button_categories")
        self.button_categories.setStyleSheet(u"color: black;\n"
"margin: 0px 0px 10px 5px;\n"
"border: 0;")
        icon1 = QIcon()
        icon1.addFile(u"assets/settings_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_categories.setIcon(icon1)
        self.button_categories.setIconSize(QSize(18, 18))

        self.verticalLayout_2.addWidget(self.button_categories, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.sideBar, 0, Qt.AlignmentFlag.AlignLeft)

        self.pages_widget = QStackedWidget(self.centralwidget)
        self.pages_widget.setObjectName(u"pages_widget")
        self.pages_widget.setStyleSheet(u"margin: 0;\n"
"padding: 0;")
        self.page_categories = QWidget()
        self.page_categories.setObjectName(u"page_categories")
        self.page_categories.setStyleSheet(u"margin: 0;\n"
"padding:5px;\n"
"background: #f3d2c1;\n"
"border: 1.5 solid black;\n"
"border-radius: 15px;")
        self.verticalLayout_4 = QVBoxLayout(self.page_categories)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_2 = QScrollArea(self.page_categories)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"margin: 0;\n"
"padding: 45;\n"
"background: transparent;\n"
"border: 0;\n"
"border-radius: 0;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollEditCategories = QWidget()
        self.scrollEditCategories.setObjectName(u"scrollEditCategories")
        self.scrollEditCategories.setGeometry(QRect(0, 0, 86, 16))
        self.scroll_edit_category_layout = QVBoxLayout(self.scrollEditCategories)
        self.scroll_edit_category_layout.setSpacing(5)
        self.scroll_edit_category_layout.setObjectName(u"scroll_edit_category_layout")
        self.scroll_edit_category_layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.scroll_edit_category_layout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea_2.setWidget(self.scrollEditCategories)

        self.verticalLayout_3.addWidget(self.scrollArea_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.category_input = QLineEdit(self.page_categories)
        self.category_input.setObjectName(u"category_input")
        self.category_input.setStyleSheet(u"margin: 0 10px 25px 10px;\n"
"background: white;\n"
"color: black;")

        self.horizontalLayout_6.addWidget(self.category_input)

        self.add_category_btn = QPushButton(self.page_categories)
        self.add_category_btn.setObjectName(u"add_category_btn")
        self.add_category_btn.setStyleSheet(u"margin: 0 10px 25px 10px;\n"
"background: white;\n"
"color: black;")

        self.horizontalLayout_6.addWidget(self.add_category_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.pages_widget.addWidget(self.page_categories)
        self.page_task = QWidget()
        self.page_task.setObjectName(u"page_task")
        self.page_task.setStyleSheet(u"margin: 0;\n"
"padding: 0;")
        self.gridLayout_2 = QGridLayout(self.page_task)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.page_task)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"margin: 0;\n"
"padding:5px;\n"
"background: white;\n"
"border: 1.5 solid black;\n"
"border-radius: 15px;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.scrollWidget = QWidget()
        self.scrollWidget.setObjectName(u"scrollWidget")
        self.scrollWidget.setGeometry(QRect(0, 0, 598, 554))
        self.scrollWidget.setStyleSheet(u"border: 0;\n"
"border-radius: 0;")
        self.scroll_layout = QVBoxLayout(self.scrollWidget)
        self.scroll_layout.setSpacing(0)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollWidget)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add_new_item = QPushButton(self.page_task)
        self.add_new_item.setObjectName(u"add_new_item")
        self.add_new_item.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;\n"
"margin: 10px 0px 15px 0px;\n"
"color: black;")
        icon2 = QIcon()
        icon2.addFile(u"assets/addTask_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_new_item.setIcon(icon2)
        self.add_new_item.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.add_new_item)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.searchBar = QLineEdit(self.page_task)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setStyleSheet(u"margin: 5px 0px 5px 0px;\n"
"padding: 2px 0px 2px 5px;\n"
"border: 2px solid black;\n"
"border-right: none;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"color: black;\n"
"background: white;")

        self.horizontalLayout_4.addWidget(self.searchBar)

        self.filter_btn = QPushButton(self.page_task)
        self.filter_btn.setObjectName(u"filter_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filter_btn.sizePolicy().hasHeightForWidth())
        self.filter_btn.setSizePolicy(sizePolicy1)
        self.filter_btn.setMaximumSize(QSize(70, 28))
        self.filter_btn.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"background: white;\n"
"color: black;\n"
"border: 2px solid black;\n"
"border-left: none;\n"
"border-radius: 10px;\n"
"border-top-left-radius: none;\n"
"border-bottom-left-radius: none;")
        icon3 = QIcon()
        icon3.addFile(u"assets/filter-list-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filter_btn.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.filter_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.pages_widget.addWidget(self.page_task)

        self.horizontalLayout.addWidget(self.pages_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_icon.setText("")
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"Taskfy", None))
        self.button_tasks.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.button_categories.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.category_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Create a category...", None))
        self.add_category_btn.setText(QCoreApplication.translate("MainWindow", u"Add Category", None))
        self.add_new_item.setText(QCoreApplication.translate("MainWindow", u" New Task", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search task...", None))
        self.filter_btn.setText("")
    # retranslateUi

