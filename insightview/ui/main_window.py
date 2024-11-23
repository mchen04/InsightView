from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from .table_widget import TableWidget
from .chart_widget import ChartWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InsightView: Local Data Visualization Tool")
        self.setGeometry(100, 100, 800, 600)

        # Initialize UI components
        self.table_widget = TableWidget()
        self.chart_widget = ChartWidget()

        # Set the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.chart_widget)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
