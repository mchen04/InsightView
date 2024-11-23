# data_cleaner.py
# This file contains the implementation for data cleaning functions.

import pandas as pd

class DataCleaner:
    def __init__(self):
        pass

    def drop_missing_values(self, data):
        return data.dropna()

    def fill_missing_values(self, data, value=0):
        return data.fillna(value)

    def remove_duplicates(self, data):
        return data.drop_duplicates()
