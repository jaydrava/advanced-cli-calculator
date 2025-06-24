import pytest
from app.observer import Observer, HistoryObserver
from unittest.mock import MagicMock


def test_observer_update_not_implemented():
    obs = Observer()
    with pytest.raises(NotImplementedError):
        obs.update("2 + 2", 4)


def test_history_observer_update_calls_history_methods():
    mock_history = MagicMock()
    observer = HistoryObserver(mock_history)

    observer.update("2 + 2", 4)

    mock_history.add_entry.assert_called_once_with("2 + 2", 4)
    mock_history.save.assert_called_once()
