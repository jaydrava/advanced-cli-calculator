import os
import pytest
from app.calculator_config import CalculatorConfig, ConfigError


def test_valid_config(monkeypatch):
    # Patch HISTORY_FILE to a valid string
    monkeypatch.setenv("HISTORY_FILE", "history.csv")
    config = CalculatorConfig()
    assert config.history_file == "history.csv"


def test_invalid_config(monkeypatch):
    # Patch HISTORY_FILE to None or empty to cause error
    # Remove env var if present
    monkeypatch.delenv("HISTORY_FILE", raising=False)
    with pytest.raises(ConfigError):
        CalculatorConfig()
