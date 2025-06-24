# app/history.py

import pandas as pd
import os


class History:
    def __init__(self, filepath='calc_history.csv'):
        self.filepath = filepath
        self.df = pd.DataFrame(columns=['expression', 'result'])
        # Set correct dtypes for empty dataframe
        self.df = self.df.astype({'expression': 'string', 'result': 'float64'})
        self.load()

    def add_entry(self, expression, result):
        new_entry = pd.DataFrame(
            [{'expression': str(expression), 'result': float(result)}]
        )
        # Convert dtypes correctly
        new_entry = new_entry.astype({'expression': 'string', 'result': 'float64'})

        self.df = self.df.astype({'expression': 'string', 'result': 'float64'})

        # Drop empty columns if any
        new_entry = new_entry.dropna(axis=1, how='all')
        self.df = self.df.dropna(axis=1, how='all')

        self.df = pd.concat([self.df, new_entry], ignore_index=True)

    def load(self):
        if os.path.exists(self.filepath):
            self.df = pd.read_csv(self.filepath)
        else:
            self.df = pd.DataFrame(columns=['expression', 'result'])

    def save(self):
        self.df.to_csv(self.filepath, index=False)

    def clear(self):
        self.df = pd.DataFrame(columns=['expression', 'result'])
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def __str__(self):
        if self.df.empty:
            return "No history yet."
        return self.df.to_string(index=False)
