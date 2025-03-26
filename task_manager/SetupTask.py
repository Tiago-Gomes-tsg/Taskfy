from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize, QObject,Signal
from task_manager.SetupCategory import categoryWidgetItems
from task_manager.UI.task_itemsUI import Ui_task_Title
from PySide6.QtWidgets import QWidget, QApplication
from task_manager.models.task import Task
import sys

class taskWidgetItem(QWidget, Ui_task_Title, QObject):
    """
    It is a widget with title, description and standard animations to contain tasks and be used with QListWidget
    """
    task_updated = Signal()
    def __init__(self, task_id ,parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.tsk_features = Task()
        self.task_id = task_id
        self.load_categories()
        
#-----------------------------------------------------------------------------------------------------------------------------
# BUTTONS                                                                                                                    #
#-----------------------------------------------------------------------------------------------------------------------------

        self.arrow_down_btn.clicked.connect(self.toggle_desc)     #animation
        self.edit_taskbtn.clicked.connect(self.toggle_title_edit) #animation
        self.category_btn.clicked.connect(self.toggle_categories) #animation
        
        self.delete_btn.clicked.connect(self.remove_task)
        self.edit_taskbtn.clicked.connect(self.edit_desc)
        self.title_task_edit.returnPressed.connect(self.edit_title)
        self.complete_taskcheckbox.stateChanged.connect(self.on_checkbox_state_changed)
        

#-----------------------------------------------------------------------------------------------------------------------------
# ANIMATION AND STYLES                                                                                                       #
#-----------------------------------------------------------------------------------------------------------------------------

        #animation toggle title edit
        self.animation_toggle_title_edit = QPropertyAnimation(self.title_task_edit, b'maximumHeight')
        self.animation_toggle_title_edit.setDuration(150)
        self.animation_toggle_title_edit.setEasingCurve(QEasingCurve.InOutQuad)

        #animation toggle desc
        self.animation_toggle_desc_edit = QPropertyAnimation(self.task_desc_edit, b'maximumHeight')
        self.animation_toggle_desc_edit.setDuration(150)
        self.animation_toggle_desc_edit.setEasingCurve(QEasingCurve.InOutQuad)
        
        #animation toggle categories
        self.animation_toggle_categories = QPropertyAnimation(self.scroll_area_categories, b'maximumHeight')
        self.animation_toggle_categories.setDuration(150)
        self.animation_toggle_categories.setEasingCurve(QEasingCurve.InOutQuad)
        
        #animation to delete
        self.animation_delete = QPropertyAnimation(self, b'maximumSize')
        self.animation_delete.setDuration(300)
        self.animation_delete.setEasingCurve(QEasingCurve.InOutQuad)

        #style for checkbox
        self.complete_taskcheckbox.setStyleSheet("""
                                  
    QCheckBox {
        margin: 0;
        border: 2px solid black;
        border-right: none;
        border-top-left-radius: 10px;
        border-bottom-left-radius: 10px;
        padding: 0px 0px 0px 16px;
    }

    QCheckBox::indicator {
        width: 18px;
        height: 18px;
        border: 2px solid black;
        border-radius: 10px;
        background-color: transparent;
    }

    QCheckBox::indicator:checked {
        background-color: #4CAF50;
        border: 2px solid black;
        border-radius: 10px;
    }

    QCheckBox::indicator:checked:hover {
        background-color: #66BB6A;
    }

    QCheckBox::indicator:hover {
        border: 2px solid #808080;
        border-radius: 10px;
    }

    QCheckBox::indicator:pressed {
        background-color: #808080;
    }
""")

#-----------------------------------------------------------------------------------------------------------------------------
# FEATURES                                                                                                                   #
#-----------------------------------------------------------------------------------------------------------------------------

    
    def edit_title(self):
        new_title = self.title_task_edit.text()
        if new_title == '':
            new_title = self.title_task.text()
        else:
            self.title_task.setText(new_title)
        self.tsk_features.set_title(self.task_id, new_title)


    def edit_desc(self):
        if self.task_desc_edit.isReadOnly():
            self.task_desc_edit.setReadOnly(False)
            self.edit_taskbtn.setText('Save')
        else:
            self.task_desc_edit.setReadOnly(True)
            desc = self.task_desc_edit.toPlainText()
            
            self.edit_title()
            self.tsk_features.set_desc(self.task_id, desc)
            self.edit_taskbtn.setText('Edit')


    #animation toggle title edit
    def toggle_title_edit(self):
        if self.task_desc_edit.maximumHeight() == 0:
            self.arrow_down_btn.click()
            
        if self.title_task_edit.maximumHeight() == 0:
            if self.scroll_area_categories.maximumHeight() == 225:
                self.scroll_area_categories.setMaximumHeight(0)
            
            self.animation_toggle_title_edit.setStartValue(0)
            self.animation_toggle_title_edit.setEndValue(60)
            self.title_task_edit.setText(self.title_task.text())
        else:
            self.animation_toggle_title_edit.setStartValue(60)
            self.animation_toggle_title_edit.setEndValue(0)

        self.animation_toggle_title_edit.start()

    #animation toggle desc
    def toggle_desc(self):
        if self.scroll_area_categories.maximumHeight() == 225:
            self.scroll_area_categories.setMaximumHeight(0)
            
        if self.task_desc_edit.maximumHeight() == 0:
            self.animation_toggle_desc_edit.setStartValue(0)
            self.animation_toggle_desc_edit.setEndValue(250)
        else:
            if self.title_task_edit.maximumHeight() == 60 and self.task_desc_edit.maximumHeight() == 250:
                self.edit_taskbtn.click()
                
            self.animation_toggle_desc_edit.setStartValue(250)
            self.animation_toggle_desc_edit.setEndValue(0)

        self.animation_toggle_desc_edit.start()
    
    #animation toggle categories
    def toggle_categories(self):
        if self.title_task_edit.maximumHeight() == 60 and self.scroll_area_categories.maximumHeight() == 0:
            self.edit_taskbtn.click()
        
        if self.task_desc_edit.maximumHeight() == 250 and self.scroll_area_categories.maximumHeight() == 0:
            self.arrow_down_btn.click()
            
        if self.scroll_area_categories.maximumHeight() == 0:
            self.animation_toggle_categories.setStartValue(0)
            self.animation_toggle_categories.setEndValue(225)
        else:
            self.animation_toggle_categories.setStartValue(225)
            self.animation_toggle_categories.setEndValue(0)

        self.animation_toggle_categories.start()
        
    def on_checkbox_state_changed(self, state):
        if state == 2:
            self.tsk_features.do_task(self.task_id)
        if state == 0:
            self.tsk_features.undo_task(self.task_id)
        self.task_updated.emit()

    #animation to delete
    def remove_task(self):
        self.tsk_features.remove_task(self.task_id)
        self.task_updated.emit()
        self.animation_delete.setStartValue(self.size())
        self.animation_delete.setEndValue(QSize(0, 0))
        self.animation_delete.finished.connect(self.delete_widget)
        self.animation_delete.start()

    def delete_widget(self):
        self.deleteLater()

    def load_categories(self):
        self.clear_categories()
        categories = self.tsk_features.get_categories()
        for category in categories:
            category_name = category.get('name')
            category_id = category.get('category_id')
            
            category_widget = categoryWidgetItems(self.task_id, category_id, category_name )
            category_widget.category_name.setText(category_name)
            category_widget.checkBox_category.setChecked(self.tsk_features.if_find_in(self.task_id, category_id))
            self.scroll_layout_categories.addWidget(category_widget)
    
    def clear_categories(self):
        while self.scroll_layout_categories.count():
            item = self.scroll_layout_categories.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    taskwidget = taskWidgetItem()
    taskwidget.show()
    app.exec()