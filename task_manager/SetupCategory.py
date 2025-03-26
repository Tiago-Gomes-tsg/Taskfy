from task_manager.UI.category_items_UI import Ui_cateogry_list_items
from PySide6.QtWidgets import QApplication, QWidget
from task_manager.models.task import Task
from PySide6.QtCore import Signal
import sys


class categoryWidgetItems(Ui_cateogry_list_items, QWidget):
    def __init__(self, task_id, category_id, category_Name, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.tsk_features = Task()
        
        self.task_id = task_id
        self.category_id = category_id
        self.category_Name = category_Name
        self.delete_category_btn.setText("")

        self.checkBox_category.stateChanged.connect(self.on_checkbox_category_state_changed)
        
    
    #style for checkbox
        self.checkBox_category.setStyleSheet("""
                                  
    QCheckBox {
        margin: 0;
        border: 0;
        padding: 0px 0px 0px 0px;
    }

    QCheckBox::indicator {
        width: 12px;
        height: 12px;
        border: 2px solid black;
        border-radius: 5px;
        background-color: transparent;
    }

    QCheckBox::indicator:checked {
        background-color: #4CAF50;
        border: 2px solid black;
        border-radius: 5px;
    }

    QCheckBox::indicator:checked:hover {
        background-color: #66BB6A;
    }

    QCheckBox::indicator:hover {
        border: 2px solid #808080;
        border-radius: 5px;
    }

    QCheckBox::indicator:pressed {
        background-color: #808080;
    }
""")

    def on_checkbox_category_state_changed(self, state):
        if state == 2:
            self.tsk_features.link_task_to_category(self.task_id, self.category_Name)
        if state == 0:
            self.tsk_features.unlink_task_from_category(self.task_id, self.category_id)
        print(self.task_id, self.category_Name)
        
                