# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_item_widgetwkgKLx.ui'
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
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_task_Title(object):
    def setupUi(self, task_Title):
        if not task_Title.objectName():
            task_Title.setObjectName(u"task_Title")
        task_Title.resize(854, 116)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(task_Title.sizePolicy().hasHeightForWidth())
        task_Title.setSizePolicy(sizePolicy)
        task_Title.setStyleSheet(u"background: #ff8ba7;\n"
"border: 0;\n"
"border-radius: 0;\n"
"color: black;\n"
"margin: 0;\n"
"padding: 0;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(task_Title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.layout_task = QVBoxLayout()
        self.layout_task.setSpacing(0)
        self.layout_task.setObjectName(u"layout_task")
        self.title_task_layout = QHBoxLayout()
        self.title_task_layout.setSpacing(0)
        self.title_task_layout.setObjectName(u"title_task_layout")
        self.title_task_layout.setContentsMargins(-1, 0, -1, 0)
        self.complete_taskcheckbox = QCheckBox(task_Title)
        self.complete_taskcheckbox.setObjectName(u"complete_taskcheckbox")
        self.complete_taskcheckbox.setMinimumSize(QSize(50, 0))
        self.complete_taskcheckbox.setMaximumSize(QSize(50, 40))
        self.complete_taskcheckbox.setStyleSheet(u"margin: 0;\n"
"border: 2px solid black;\n"
"border-right: none;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"padding: 0px 0px 0px 16px;")

        self.title_task_layout.addWidget(self.complete_taskcheckbox)

        self.title_task = QLabel(task_Title)
        self.title_task.setObjectName(u"title_task")
        self.title_task.setMinimumSize(QSize(600, 40))
        self.title_task.setMaximumSize(QSize(600, 40))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.title_task.setFont(font)
        self.title_task.setStyleSheet(u"border: 2px solid black;\n"
"border-left: none;\n"
"border-right:none;\n"
"padding: 0px 5px;\n"
"font: bold;")

        self.title_task_layout.addWidget(self.title_task)

        self.edit_taskbtn = QPushButton(task_Title)
        self.edit_taskbtn.setObjectName(u"edit_taskbtn")
        self.edit_taskbtn.setMinimumSize(QSize(50, 0))
        self.edit_taskbtn.setMaximumSize(QSize(50, 40))
        self.edit_taskbtn.setStyleSheet(u"margin: 0;\n"
"border: 2px solid black;\n"
"border-left: none;\n"
"border-right: none;")
        icon = QIcon()
        icon.addFile(u"assets/edit_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_taskbtn.setIcon(icon)

        self.title_task_layout.addWidget(self.edit_taskbtn)

        self.arrow_down_btn = QPushButton(task_Title)
        self.arrow_down_btn.setObjectName(u"arrow_down_btn")
        self.arrow_down_btn.setMinimumSize(QSize(50, 0))
        self.arrow_down_btn.setMaximumSize(QSize(50, 40))
        self.arrow_down_btn.setStyleSheet(u"margin: 0;\n"
"border: 2px solid black;\n"
"border-left: none;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"assets/arrow_down_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.arrow_down_btn.setIcon(icon1)

        self.title_task_layout.addWidget(self.arrow_down_btn)

        self.delete_btn = QPushButton(task_Title)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setMinimumSize(QSize(50, 0))
        self.delete_btn.setMaximumSize(QSize(50, 40))
        self.delete_btn.setStyleSheet(u"margin: 0;;\n"
"border: 2px solid black;\n"
"border-left: none;\n"
"border-right: none;\n"
"border-radius: 0px;\n"
"border-top-left-radius: none;\n"
"border-bottom-left-radius: none;")
        icon2 = QIcon()
        icon2.addFile(u"assets/trash_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon2)

        self.title_task_layout.addWidget(self.delete_btn)

        self.category_btn = QPushButton(task_Title)
        self.category_btn.setObjectName(u"category_btn")
        self.category_btn.setMinimumSize(QSize(50, 40))
        self.category_btn.setMaximumSize(QSize(50, 40))
        self.category_btn.setStyleSheet(u"margin: 0;;\n"
"border: 2px solid black;\n"
"border-left: none;\n"
"border-radius: 10px;\n"
"border-top-left-radius: none;\n"
"border-bottom-left-radius: none;")
        icon3 = QIcon()
        icon3.addFile(u"assets/three-dots-vertical-svgrepo-com.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.category_btn.setIcon(icon3)

        self.title_task_layout.addWidget(self.category_btn)


        self.layout_task.addLayout(self.title_task_layout)

        self.title_task_edit = QLineEdit(task_Title)
        self.title_task_edit.setObjectName(u"title_task_edit")
        self.title_task_edit.setMaximumSize(QSize(16777215, 0))
        font1 = QFont()
        font1.setPointSize(13)
        self.title_task_edit.setFont(font1)
        self.title_task_edit.setStyleSheet(u"padding: 0px 0px 0px 25px;\n"
"border: 2px solid black;\n"
"border-radius: 10px")
        self.title_task_edit.setMaxLength(60)

        self.layout_task.addWidget(self.title_task_edit)

        self.task_desc_edit = QTextEdit(task_Title)
        self.task_desc_edit.setObjectName(u"task_desc_edit")
        self.task_desc_edit.setMaximumSize(QSize(16777215, 0))
        font2 = QFont()
        font2.setPointSize(11)
        self.task_desc_edit.setFont(font2)
        self.task_desc_edit.setStyleSheet(u"padding: 0px 0px 0px 5px;\n"
"border: 2px solid black;\n"
"border-radius: 10px")
        self.task_desc_edit.setReadOnly(True)

        self.layout_task.addWidget(self.task_desc_edit)

        self.scroll_area_categories = QScrollArea(task_Title)
        self.scroll_area_categories.setObjectName(u"scroll_area_categories")
        self.scroll_area_categories.setMaximumSize(QSize(16777215, 0))
        self.scroll_area_categories.setStyleSheet(u"background: transparent;")
        self.scroll_area_categories.setWidgetResizable(True)
        self.scrollWidgetCategories = QWidget()
        self.scrollWidgetCategories.setObjectName(u"scrollWidgetCategories")
        self.scrollWidgetCategories.setGeometry(QRect(0, 0, 500, 18))
        self.scrollWidgetCategories.setMaximumSize(QSize(500, 16777215))
        self.scrollWidgetCategories.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background: #f3d2c1;")
        self.scroll_layout_categories = QVBoxLayout(self.scrollWidgetCategories)
        self.scroll_layout_categories.setObjectName(u"scroll_layout_categories")
        self.scroll_area_categories.setWidget(self.scrollWidgetCategories)

        self.layout_task.addWidget(self.scroll_area_categories)


        self.verticalLayout_2.addLayout(self.layout_task)


        self.retranslateUi(task_Title)

        QMetaObject.connectSlotsByName(task_Title)
    # setupUi

    def retranslateUi(self, task_Title):
        task_Title.setWindowTitle(QCoreApplication.translate("task_Title", u"Form", None))
        self.complete_taskcheckbox.setText("")
        self.title_task.setText(QCoreApplication.translate("task_Title", u"TextLabel", None))
        self.edit_taskbtn.setText(QCoreApplication.translate("task_Title", u"Edit", None))
        self.arrow_down_btn.setText("")
        self.delete_btn.setText("")
        self.category_btn.setText("")
        self.title_task_edit.setPlaceholderText(QCoreApplication.translate("task_Title", u"Title task...", None))
        self.task_desc_edit.setMarkdown(QCoreApplication.translate("task_Title", u"`Lorem ipsum dolor sit amet. Ut voluptatum molestiae qui odio repudiandae et\n"
"harum quisquam. Ad adipisci omnis qui adipisci error eum beatae molestiae? Est\n"
"mollitia consequatur non facere voluptatem ut dolorem necessitatibus.   Id\n"
"necessitatibus error ea voluptates eligendi non molestiae ipsam aut quasi\n"
"cumque in ullam possimus. Sit vero voluptatem At facere praesentium qui dicta\n"
"tempore aut laborum odit et odit aliquam ut neque modi. Ea beatae tempore qui\n"
"repudiandae quaerat a incidunt sint.   Qui libero Quis aut dolore autem et\n"
"deserunt velit qui laboriosam asperiores et enim architecto et voluptas\n"
"praesentium et ipsum perferendis. Non voluptatum sint sit inventore ducimus ut\n"
"sunt ratione qui voluptas impedit ea quia obcaecati. Sed laudantium alias est\n"
"minima eveniet aut enim beatae qui incidunt possimus quo nulla voluptatibus eum\n"
"enim nulla.`\n"
"\n"
"", None))
        self.task_desc_edit.setPlaceholderText(QCoreApplication.translate("task_Title", u"Description...", None))
    # retranslateUi

