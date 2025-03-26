from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel
from PySide6.QtCore import QPropertyAnimation,QEasingCurve, QSize, QPoint, Qt, Signal
from task_manager.UI.category_item_CRUD_UI import Ui_category_list_items
from task_manager.UI.category_item_UI import Ui_categoryItem
from task_manager.UI.filter_widgetUI import Ui_filterWidget
from task_manager.UI.main_WindowUI import Ui_MainWindow
from task_manager.UI.donut_chart import DonutChart
from task_manager.SetupTask import taskWidgetItem
from task_manager.models.task import Task
from PySide6.QtGui import QIcon, QPixmap
from pathlib import Path
import sys
import os



class mainWindowWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        
        #Setups
        self.tsk_features = Task()
        self.tsk_features.new_task_table()
        self.tsk_features.new_categorie_table()
        self.tsk_features.new_filtered_task_table()
        self.tsk_features.new_task_categories_table()
        
        self.add_new_item.clicked.connect(self.add_new_task)
        self.searchBar.textChanged.connect(self.load_searchedtasks)
        
        self.button_tasks.clicked.connect(self.load_tasks)
        self.button_tasks.clicked.connect(lambda: self.pages_widget.setCurrentWidget(self.page_task))
        
        self.button_categories.clicked.connect(self.load_categories_CRUD)
        self.button_categories.clicked.connect(lambda: self.pages_widget.setCurrentWidget(self.page_categories))
        
        self.filter_category_widget = filterCategoryWidget(parent=self)
        self.filter_category_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.filter_category_widget.move(self.width() + self.filter_category_widget.width(), 0)
        self.filter_category_widget.apply_filter_btn.clicked.connect(self.toggle_filter)
        self.filter_category_widget.apply_filter_btn.clicked.connect(self.load_filteredtasks)
        self.filter_category_widget.apply_filter_btn.clicked.connect(self.filter_category_widget.selected_category_ids.clear)
        self.filter_btn.clicked.connect(self.filter_category_widget.load_categories)
        self.filter_btn.clicked.connect(self.toggle_filter)
        
        self.category_input.returnPressed.connect(self.set_category_name)
        self.add_category_btn.clicked.connect(self.set_category_name)
        
        self.adjust_fixed_size()
        self.button_tasks.click()
        
        self.donut_chart = DonutChart()
        layout = self.widget_chart_container.layout()
        layout.addWidget(self.donut_chart)
        self.update_chart()
        self.tsk_features.task_updated.connect(self.update_chart)
        
        self.setWindowIcon(QIcon("assets/icon.svg"))
        self.app_icon.setPixmap(QPixmap("assets/icon.svg"))
        self.button_tasks.setIcon(QIcon("assets/task_icon.svg"))
        self.button_categories.setIcon(QIcon("assets/settings_icon.svg"))
        self.add_new_item.setIcon(QIcon("assets/addTask_icon.svg"))
        self.filter_btn.setIcon(QIcon("assets/filter-list-svgrepo-com.svg"))
        
        
#-----------------------------------------------------------------------------------------------------------------------------
# STYLES                                                                                                                     #
#-----------------------------------------------------------------------------------------------------------------------------
        self.scrollArea.setStyleSheet("""
    QScrollBar:vertical {
        background: #F1F1F1;
        width: 12px;
        margin: 0px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::handle:vertical {
        background: #f3d2c1;
        min-height: 20px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        background: none;
    }

    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        background: #F1F1F1;
        height: 12px;
        margin: 0px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::handle:horizontal {
        background: #f3d2c1;
        min-width: 20px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal {
        background: none;
    }

    QScrollBar::add-page:horizontal,
    QScrollBar::sub-page:horizontal {
        background: none;
    }
""")

#-----------------------------------------------------------------------------------------------------------------------------
# FEATURES                                                                                                                   #
#-----------------------------------------------------------------------------------------------------------------------------

    def update_chart(self):
        completed = self.tsk_features.count_completed_tasks()
        pending = self.tsk_features.count_pending_tasks()
        self.donut_chart_container.update_data(completed, pending)

    def load_tasks(self):
        self.clear_tasks()
        tasks = self.tsk_features.get_tasks()
        for task in tasks:
            task_widget = taskWidgetItem(task.get('id'))
            task_widget.title_task.setText(task.get('title'))
            task_widget.task_desc_edit.setText(task.get('desc'))
            task_widget.complete_taskcheckbox.setChecked(task.get('status'))
            task_widget.task_updated.connect(self.update_chart)
            self.scroll_layout.addWidget(task_widget)
    
    def load_searchedtasks(self):
        self.clear_tasks()
        tasks = self.tsk_features.get_searchtasks(self.searchBar.text().strip())
        for task in tasks:
            task_widget = taskWidgetItem(task.get('id'))
            task_widget.title_task.setText(task.get('title'))
            task_widget.task_desc_edit.setText(task.get('desc'))
            task_widget.complete_taskcheckbox.setChecked(task.get('status'))
            task_widget.task_updated.connect(self.update_chart)
            self.scroll_layout.addWidget(task_widget)
        self.update_chart()
            
    def load_filteredtasks(self):
        selected_categories = self.filter_category_widget.get_selected_category_ids()
        if selected_categories:
            self.tsk_features.update_temp_table(selected_categories)
            self.clear_tasks()
            tasks = self.tsk_features.get_filtered_tasks()
            for task in tasks:
                task_widget = taskWidgetItem(task.get('id'))
                task_widget.title_task.setText(task.get('title'))
                task_widget.task_desc_edit.setText(task.get('desc'))
                task_widget.complete_taskcheckbox.setChecked(task.get('status'))
                task_widget.task_updated.connect(self.update_chart)
                self.scroll_layout.addWidget(task_widget)
        else:
            self.load_tasks()
        self.update_chart()
    
    def clear_tasks(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def add_new_task(self):
        self.tsk_features.new_task()
        self.load_tasks()
    
    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(1110, 750)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setMaximumSize(1110, 750)
        self.setMinimumSize(1110, 750)
        self.show()
    
    def toggle_filter(self):
        if self.filter_category_widget.x() > self.width():
            self.animate_filter_widget(self.width() - self.filter_category_widget.width())
        else:
            self.animate_filter_widget(self.width() + self.filter_category_widget.width())
    
    def animate_filter_widget(self, target_x):
        self.animation = QPropertyAnimation(self.filter_category_widget, b"pos")
        self.animation.setDuration(200)
        self.animation.setStartValue(self.filter_category_widget.pos())
        self.animation.setEndValue(QPoint(target_x, self.filter_category_widget.y()))
        self.animation.start()

    def update_chart(self):
        completed = self.tsk_features.count_completed_tasks()
        pending = self.tsk_features.count_pending_tasks()
        self.donut_chart.update_data(completed, pending)
        
    def load_categories_CRUD(self):
        self.clear_categories()
        categories = self.tsk_features.get_categories()
        for category in categories:
            category_widget = categoryCrudItems(category.get('category_id'))
            category_widget.category_name.setText(category.get('name'))
            self.scroll_edit_category_layout.addWidget(category_widget)
            
    def set_category_name(self):
        if self.category_input.text().strip() == '':
            self.category_input.setText('New Category')
        self.tsk_features.add_category(self.category_input.text().strip())
        self.load_categories_CRUD()
            
    def clear_categories(self):
        while self.scroll_edit_category_layout.count():
            item = self.scroll_edit_category_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
            
class filterCategoryWidget(Ui_filterWidget, QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.tsk_features = Task()
        self.setFixedWidth(400)
        
        self.selected_category_ids = set()

        self.load_categories()
        
        self.scrollArea.setStyleSheet("""
    QScrollBar:vertical {
        background: #F1F1F1;
        width: 12px;
        margin: 0px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::handle:vertical {
        background: #f3d2c1;
        min-height: 20px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        background: none;
    }

    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        background: #F1F1F1;
        height: 12px;
        margin: 0px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::handle:horizontal {
        background: #f3d2c1;
        min-width: 20px;
        border: 1 solid black;
        border-radius: 6px;
    }

    QScrollBar::add-line:horizontal,
    QScrollBar::sub-line:horizontal {
        background: none;
    }

    QScrollBar::add-page:horizontal,
    QScrollBar::sub-page:horizontal {
        background: none;
    }
""")
       
    def load_categories(self):
        self.clear_categories()
        categories = self.tsk_features.get_categories()
        for category in categories:
            category_widget = categoryItemWidget()
            category_widget.category_name.setText(category.get("name"))
            category_widget.category_id = category.get("category_id")
            category_widget.name = category.get("name")
            
            category_widget.checkbox_state_changed.connect(self.update_selected_categories)
            
            self.scroll_categories_layout.addWidget(category_widget)
            
    def update_selected_categories(self, category_id, is_checked):
        if is_checked:
            self.selected_category_ids.add(category_id)
        else:
            self.selected_category_ids.discard(category_id)
        
        print(f"Categories checked: {self.selected_category_ids}")
        
    def get_selected_category_ids(self):
        return list(self.selected_category_ids)
    
    def clear_categories(self):
        while self.scroll_categories_layout.count():
            item = self.scroll_categories_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
                
    

class categoryItemWidget(Ui_categoryItem, QWidget):
    
    checkbox_state_changed = Signal(int, bool)
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.category_id = None
        self.name = None
        
        self.checkbox_category_Filter.stateChanged.connect(self.on_checkbox_state_changed)
        
        #style for checkbox
        self.checkbox_category_Filter.setStyleSheet("""
                                  
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
    
    def on_checkbox_state_changed(self, state):
        is_checked = state == 2
        self.checkbox_state_changed.emit(self.category_id, is_checked)
    
class categoryCrudItems(QWidget, Ui_category_list_items):
    def __init__(self, category_id, parent= None):
        super().__init__(parent)
        self.setupUi(self)
        self.tsk_features = Task()
        self.category_id = category_id
        self.delete_category_btn.clicked.connect(self.remove_category)

        self.animation_delete = QPropertyAnimation(self, b'maximumSize')
        self.animation_delete.setDuration(300)
        self.animation_delete.setEasingCurve(QEasingCurve.InOutQuad)
        
    def remove_category(self):
        self.tsk_features.delete_category(self.category_id)
        self.animation_delete.setStartValue(self.size())
        self.animation_delete.setEndValue(QSize(0, 0))
        self.animation_delete.finished.connect(self.delete_widget)
        self.animation_delete.start()
    
    def delete_widget(self):
        self.deleteLater()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = mainWindowWidget()
    window.adjust_fixed_size()
    window.show()
    app.exec()