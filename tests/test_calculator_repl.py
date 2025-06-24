import pytest
from unittest.mock import patch, PropertyMock, MagicMock
from app.calculator_repl import repl
from app.calculator_config import ConfigError


def test_config_error():
    # Patch CalculatorConfig where it is used, i.e. in calculator_repl module
    with patch("app.calculator_repl.CalculatorConfig", side_effect=ConfigError("Invalid config")):
        with patch("builtins.print") as mock_print:
            repl()
        mock_print.assert_any_call("Configuration error: Invalid config")


def test_undo_redo_nothing_to_do():
    user_inputs = ['undo', 'redo', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("Nothing to undo." in s for s in printed)
            assert any("Nothing to redo." in s for s in printed)


def test_history_load_and_error_output():
    user_inputs = ['2 + 2', 'load', 'invalid_expr', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("History loaded. Records:" in s for s in printed)
            assert any("Error:" in s for s in printed)


def test_undo_redo_success():
    user_inputs = [
        '2 + 2',    # calculate so history has something
        'undo',     # undo should succeed now
        'redo',     # redo should succeed now
        'exit'
    ]
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("Undo successful." in s for s in printed)
            assert any("Redo successful." in s for s in printed)


def test_clear_command():
    user_inputs = ['clear', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("History cleared." in s for s in printed)


def test_save_command():
    user_inputs = ['save', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("History saved." in s for s in printed)


def test_load_command():
    user_inputs = ['load', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("History loaded. Records:" in s for s in printed)
            # Optional: check print(history) output as well


def test_invalid_expression_error():
    user_inputs = ['invalid_expression_###', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("Error:" in s for s in printed)


def test_invalid_expression_raises_value_error():
    # Provide an input which will cause CalculationFactory.process to raise ValueError
    user_inputs = ['invalid_expression', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("Error:" in s for s in printed)


def test_history_command():
    user_inputs = ['2 + 2', 'history', 'exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any("Welcome to the Advanced CLI Calculator! (Type 'exit' to quit)" in s for s in printed)


def test_welcome_message_printed():
    user_inputs = ['exit']
    with patch('builtins.input', side_effect=user_inputs):
        with patch('builtins.print') as mock_print:
            repl()
            printed = [str(args[0]) for args, _ in mock_print.call_args_list]
            assert any(
                "Welcome to the Advanced CLI Calculator! (Type 'exit' to quit)" in s
                for s in printed
            )


def test_history_command_when_empty():
    user_inputs = ['history', 'exit']

    # Patch CalculatorConfig to use a dummy empty history file path
    class DummyConfig:
        # file does not exist, so history is empty
        history_file = "non_existent_file.csv"

    with patch('builtins.input', side_effect=user_inputs), \
            patch('builtins.print') as mock_print, \
            patch('app.calculator_repl.CalculatorConfig', return_value=DummyConfig()):

        from app.calculator_repl import repl
        repl()

        printed = [str(args[0]) for args, _ in mock_print.call_args_list]
        assert any("No history yet." in s for s in printed)
