# tests/test_calculator_memento.py

import pandas as pd
from app.calculator_memento import Caretaker


def test_save_and_undo_redo():
    caretaker = Caretaker()
    df1 = pd.DataFrame([{'expression': '2+2', 'result': 4.0}])
    df2 = pd.DataFrame([{'expression': '3+3', 'result': 6.0}])
    df3 = pd.DataFrame([{'expression': '4+4', 'result': 8.0}])

    caretaker.save(df1)
    caretaker.save(df2)
    caretaker.save(df3)

    assert caretaker.undo().equals(df2)
    assert caretaker.undo().equals(df1)
    assert caretaker.undo() is None

    assert caretaker.redo().equals(df2)
    assert caretaker.redo().equals(df3)
    assert caretaker.redo() is None
