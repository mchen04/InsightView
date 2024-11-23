# file_handler.py
# This file contains the implementation for file upload and parsing.

import pandas as pd

class FileHandler:
    def __init__(self):
        pass

    def load_csv(self, file_path):
        return pd.read_csv(file_path)

    def load_excel(self, file_path):
        return pd.read_excel(file_path)
