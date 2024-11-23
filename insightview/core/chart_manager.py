# chart_manager.py
# This file contains the implementation for chart management logic.

class ChartManager:
    def __init__(self, chart_widget):
        self.chart_widget = chart_widget

    def update_chart(self, x, y):
        self.chart_widget.plot_data(x, y)
