from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import numpy as np

class DonutChart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.figure = Figure(figsize=(3, 3), dpi=100, facecolor='none')
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        self.completed = 0
        self.pending = 0
        self.anim = None
        
        self._draw_chart()
        
    def update_data(self, completed, pending):
        self.old_completed = self.completed
        self.old_pending = self.pending
        self.completed = max(0, completed)
        self.pending = max(0, pending)
        self._start_animation()
        
    def _draw_chart(self, values=None):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        total = self.completed + self.pending
        if total == 0:
            ax.text(0, 0, 'No Tasks', ha='center', va='center', fontsize=12, color='black')
        else:
            sizes = values if values else [self.completed, self.pending]
            sizes = [max(0.01, s) for s in sizes]
            colors = ['#ff8ba7', '#f3d2c1']

            ax.pie(
                sizes,
                colors=colors,
                startangle=90,
                wedgeprops=dict(width=0.4, edgecolor='white'),
                counterclock=False
            )

            percent = (self.completed / total) * 100
            ax.text(0, 0, f'{percent:.0f}%', ha='center', va='center', fontsize=20, fontweight='bold', color='black')

        ax.set_aspect('equal')
        self.canvas.draw_idle()

    def _start_animation(self):
        steps = 40
        
        def update(frame):
            alpha = frame / steps
            new_completed = self.old_completed * (1 - alpha) + self.completed * alpha
            new_pending = self.old_pending * (1 - alpha) + self.pending * alpha

            new_completed = max(0, new_completed)
            new_pending = max(0, new_pending)

            self._draw_chart([new_completed, new_pending])

        self.anim = FuncAnimation(self.figure, update, frames=steps, interval=5, repeat=False)

        self.canvas.draw_idle()