from PySide6.QtCore import QObject, Signal, QTimer
from functools import wraps
import time
from pathlib import Path
import sqlite3
import sys

class Task(QObject):
    task_updated = Signal()
    def __init__(self):
        super().__init__()
        
        #Connection to DB
        if getattr(sys, 'frozen', False):
            main_directory = Path(sys.executable).parent
        else:
            main_directory = Path(__file__).parent.parent.parent
            
        self.tasks_path = main_directory / "data" / "tasks.sqlite3"
        self.tasks_path.parent.mkdir(parents=True, exist_ok=True)

        
        
    @staticmethod
    def manage_connection(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.conn = sqlite3.connect(self.tasks_path)
            self.cursor = self.conn.cursor()
            
            try:
                result = func(self, *args, **kwargs)
                self.conn.commit()
                return result
            except Exception as e:
                self.conn.rollback()
                raise e
            finally:
                print("Closing DataBase...")
                self.cursor.close()
                self.conn.close()
        return wrapper
        

#-----------------------------------------------------------------------------------------------------------------------------
# TASKS FEATURES                                                                                                             #
#-----------------------------------------------------------------------------------------------------------------------------
    
    @manage_connection
    def new_task(self, title = 'New task', desc = '', status = 0) -> None:
        query = """
        INSERT INTO tasks (title, desc, status) VALUES (?, ?, ?)
        """
        self.cursor.execute(query,(title, desc, status))
        
        print("Task successfully created")
        QTimer.singleShot(0, self.task_updated.emit) 

    @manage_connection
    def get_tasks(self) -> list[dict]:
        self.cursor.execute(
            """
            SELECT * FROM tasks
            """
        )
        tasks = self.cursor.fetchall()
        task_list = []
        for task in tasks:
            task_id, title, desc, status = task
            task_dict = {
                "id": task_id,
                "title": title,
                "desc": desc,
                "status": True if status == 1 else False
            }
            task_list.append(task_dict)
        return task_list

    @manage_connection
    def get_searchtasks(self, search) -> list[dict]:
        query = """
        SELECT * from tasks WHERE title LIKE ?
        """
        self.cursor.execute(query,('%'+ search + '%',))
        tasks = self.cursor.fetchall()
        task_list = []
        for task in tasks:
            task_id, title, desc, status = task
            task_dict = {
                "id": task_id,
                "title": title,
                "desc": desc,
                "status": True if status == 1 else False
            }
            task_list.append(task_dict)
        return task_list

    @manage_connection
    def set_title(self, task_id: int, title: str) -> None:
        query = """
        UPDATE tasks SET title = ?
        WHERE id = ?
        """
        self.cursor.execute(query,(title,task_id))
        
        print('Task Title changed')
        QTimer.singleShot(0, self.task_updated.emit) 
     
    @manage_connection   
    def set_desc(self, task_id: int, desc: str) -> None:
        query = """
        UPDATE tasks SET desc = ?
        WHERE id = ?
        """
        self.cursor.execute(query,(desc,task_id))
        
        print('Task Desc changed')
        QTimer.singleShot(0, self.task_updated.emit) 
        
    @manage_connection
    def do_task(self,task_id: int) -> None:
        query = """
        UPDATE tasks SET status = 1
        WHERE id = ?
        """
        self.cursor.execute(query,(task_id,))
        
        print('Task set to COMPLETED')
        QTimer.singleShot(0, self.task_updated.emit) 

    @manage_connection
    def undo_task(self,task_id: int) -> None:
        query = """
        UPDATE tasks SET status = 0
        WHERE id = ?
        """
        self.cursor.execute(query,(task_id,))
        
        print('Task set to INCOMPLETE')
        QTimer.singleShot(0, self.task_updated.emit) 

    @manage_connection
    def remove_task(self, task_id: int) -> None:
        
        firstQuery = """
        DELETE FROM task_categories WHERE task_id = ?
        """
        secondQuery = """
            DELETE FROM tasks WHERE id = ?
            """
        self.cursor.execute(firstQuery, (task_id,))
        self.cursor.execute(secondQuery, (task_id,))
        
        print('Task deleted successfully')
        QTimer.singleShot(0, self.task_updated.emit) 
        
    @manage_connection
    def count_completed_tasks(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 1")
        return self.cursor.fetchone()[0]
    
    @manage_connection
    def count_pending_tasks(self) -> int:
        self.cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 0")
        return self.cursor.fetchone()[0]
        

#-----------------------------------------------------------------------------------------------------------------------------
# FILTERED TASKS FEATURES                                                                                                    #
#-----------------------------------------------------------------------------------------------------------------------------

    @manage_connection
    def get_filtered_tasks(self) -> list[dict]:
        try:
            self.cursor.execute("SELECT * FROM filtered_tasks")
            tasks = self.cursor.fetchall()
            task_list = []
            for task in tasks:
                task_id, title, desc, status = task
                task_dict = {
                    "id": task_id,
                    "title": title,
                    "desc": desc,
                    "status": True if status == 1 else False
                }
                task_list.append(task_dict)
            return task_list
        except sqlite3.Error as e:
            print(f"Error getting filtered tasks: {e}")
            raise

    @manage_connection
    def update_temp_table(self, category_ids) -> None:
        try:
            self.cursor.execute("DELETE FROM filtered_tasks")
            print("Table filtered_tasks successfully cleared")
            
            if not category_ids:
                return
            
            placeholders = ','.join(['?'] * len(category_ids))
            query = f"""
            INSERT INTO filtered_tasks (id, title, desc, status)
            SELECT t.id, t.title, t.desc, t.status 
            FROM tasks t
            JOIN task_categories tc ON t.id = tc.task_id
            WHERE tc.category_id IN ({placeholders})
            """
            self.cursor.execute(query, category_ids)
            print("Table filtered_tasks updated successfully")
        except sqlite3.Error as e:
            self.conn.rollback()
            print(f"Error updating filtered_tasks table: {e}")
            raise

#-----------------------------------------------------------------------------------------------------------------------------
# CATEGORIES FEATURES                                                                                                        #
#-----------------------------------------------------------------------------------------------------------------------------

    @manage_connection
    def create_and_link_category(self, task_id, category_name):
        self.add_category(category_name)
        self.link_task_to_category(task_id, category_name)
    
    @manage_connection
    def add_category(self, category_name: str):
        try:
            self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
            
            print(f"Category {category_name} added successfully")

        except sqlite3.IntegrityError:
            print(f"Category {category_name} already exists")
    
    @manage_connection
    def if_find_in(self, task_id, category_id) -> bool:
        try:
            self.cursor.execute(
                """
                SELECT 1 FROM task_categories WHERE task_id = ? AND category_id = ? LIMIT 1
                """, (task_id, category_id)
            )
            result = self.cursor.fetchone()
            return result is not None
        
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
    
    @manage_connection           
    def link_task_to_category(self, task_id, category_name) -> None:
        try:
            self.cursor.execute(
                """
                SELECT id FROM categories WHERE name = ?
                """, (category_name,)
            )
            category_id = self.cursor.fetchone()
            
            if category_id:
                self.cursor.execute(
                    """
                    INSERT INTO task_categories (task_id, category_id) VALUES (?,?)
                    """, (task_id, category_id[0])
                )
                print(f"Task {task_id} associated with category {category_name}")
        except sqlite3.IntegrityError:
            print(f"Task already associated with category {category_name}")
    
    @manage_connection
    def unlink_task_from_category(self,task_id, category_id) -> None:
        try:
            self.cursor.execute(
                """
                DELETE FROM task_categories WHERE task_id = ? AND category_id = ?
                """, (task_id, category_id)
            )
            print("Task and category unlinked")
        except sqlite3.IntegrityError:
            print("Error when dissociating task from category")
     
    @manage_connection       
    def delete_category(self, category_id) -> None:
        try:
            self.cursor.execute("DELETE FROM task_categories WHERE category_id = ?", (category_id,))

            self.cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))

            print(f"Category {category_id} and its links have been deleted")
        except sqlite3.Error as e:
            print(f"Error deleting category: {e}")
     
    @manage_connection       
    def get_categories(self) -> list[dict]:
        self.cursor.execute(
            """
            SELECT * FROM categories
            """
        )
        categories = self.cursor.fetchall()
        category_list = []
        for category in categories:
            category_id, name = category
            category_dict = {
                "category_id": category_id,
                "name": name
            }
            category_list.append(category_dict)
        return category_list

                
            
#-----------------------------------------------------------------------------------------------------------------------------
# SQL FEATURES                                                                                                               #
#-----------------------------------------------------------------------------------------------------------------------------

    @manage_connection
    def new_task_table(self) -> None:
        """Will add a new task"""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, desc TEXT, status INTEGER)
            """
        )
        print("The task table has been created or already exists")
    
    @manage_connection
    def new_categorie_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)
            """
        )
        print("The category table has been created or already exists")
     
    @manage_connection   
    def new_task_categories_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS task_categories (
            task_id INTEGER,
            category_id INTEGER,
            PRIMARY KEY (task_id, category_id),
            FOREIGN KEY (task_id) REFERENCES tasks(id),
            FOREIGN KEY(category_id) REFERENCES categories(id))
            """
        )
        print("The relation task_categories table has been created or already exists")
    
    @manage_connection
    def new_filtered_task_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS filtered_tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                desc TEXT,
                status INTEGER
            )
            """
        )
        print("The filtered task table has been created or already exists ")
