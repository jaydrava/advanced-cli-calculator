# tests/test_history.py

import os
import pandas as pd
import pytest
from app.history import History

TEST_FILE = "test_calc_history.csv"


@pytest.fixture
def history():
    # Ensure test file is removed before each test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    hist = History(filepath=TEST_FILE)
    yield hist
    # Cleanup
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_add_entry(history):
    history.add_entry("2 + 2", 4.0)
    assert len(history.df) == 1
    assert history.df.iloc[0]['expression'] == "2 + 2"
    assert history.df.iloc[0]['result'] == 4.0


def test_save_and_load(history):
    history.add_entry("3 * 3", 9.0)
    history.save()

    # Reload new history instance
    new_history = History(filepath=TEST_FILE)
    assert len(new_history.df) == 1
    assert new_history.df.iloc[0]['expression'] == "3 * 3"
    assert new_history.df.iloc[0]['result'] == 9.0


def test_clear(history):
    history.add_entry("4 - 1", 3.0)
    history.save()
    history.clear()
    assert history.df.empty
    assert not os.path.exists(TEST_FILE)


def test_str(history):
    assert str(history) == "No history yet."
    history.add_entry("1 + 1", 2.0)
    assert "1 + 1" in str(history) 
