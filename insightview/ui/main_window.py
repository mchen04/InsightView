from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLabel
from .table_widget import TableWidget
from .chart_widget import ChartWidget
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InsightView: Local Data Visualization Tool")
        self.setGeometry(100, 100, 800, 600)

        # Initialize UI components
        self.table_widget = TableWidget()
        self.chart_widget = ChartWidget()
        self.file_details_label = QLabel("File Details: None", self)

        # Set the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.file_details_label)
        layout.addWidget(self.chart_widget)

        # Add a button for file upload
        self.upload_button = QPushButton("Upload File", self)
        self.upload_button.clicked.connect(self.upload_file)
        layout.addWidget(self.upload_button)

    def upload_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;CSV Files (*.csv);;Excel Files (*.xlsx);;JSON Files (*.json)", options=options)
        if file_path:
            print(f"File selected: {file_path}")
            self.display_file_details(file_path)
            data = self.load_data(file_path)
            self.chart_widget.set_data(data)

    def display_file_details(self, file_path):
        try:
            if file_path.endswith('.csv'):
                data = pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            elif file_path.endswith('.json'):
                data = pd.read_json(file_path)
            else:
                self.file_details_label.setText("Unsupported file type")
                return

            details = f"File Details:\nPath: {file_path}\nSize: {data.size}\nNumber of Columns: {data.shape[1]}\nNumber of Rows: {data.shape[0]}"
            self.file_details_label.setText(details)
        except Exception as e:
            self.file_details_label.setText(f"Error reading file: {str(e)}")

    def load_data(self, file_path):
        try:
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path).values
            elif file_path.endswith('.xlsx'):
                return pd.read_excel(file_path).values
            elif file_path.endswith('.json'):
                return pd.read_json(file_path).values
            else:
                return None
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return None

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
