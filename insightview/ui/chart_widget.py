from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtChart import QChartView, QChart, QLineSeries, QValueAxis
from PyQt5.QtGui import QPainter
import numpy as np

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.chart_view = QChartView()
        self.chart = QChart()
        self.chart_view.setChart(self.chart)
        self.layout.addWidget(self.chart_view)
        self.setLayout(self.layout)

        # Additional chart widget initialization code here
        self.series = QLineSeries()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Data Visualization Chart")

    def set_data(self, data):
        if data is None or len(data) == 0:
            return

        self.series.clear()
        for i, value in enumerate(data):
            self.series.append(i, value)

        # Adjust axes to fit the data
        x_axis = QValueAxis()
        y_axis = QValueAxis()
        x_axis.setRange(0, len(data) - 1)
        y_axis.setRange(np.min(data), np.max(data))
        self.chart.setAxisX(x_axis, self.series)
        self.chart.setAxisY(y_axis, self.series)
