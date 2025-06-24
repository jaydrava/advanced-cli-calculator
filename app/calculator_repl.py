from logging import config
from app.calculation import CalculationFactory
from app.calculator_memento import Caretaker
from app.history import History
from app.observer import HistoryObserver
from app.calculator_config import CalculatorConfig, ConfigError
from app.history import History


def repl():
    try:
        config = CalculatorConfig()
    except ConfigError as e:
        print(f"Configuration error: {e}")
        return

    history = History(filepath=config.history_file)
    print("Welcome to the Advanced CLI Calculator! (Type 'exit' to quit)")

    caretaker = Caretaker()
    CalculationFactory.register_observer(HistoryObserver(history))
    caretaker.save(history.df)

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'history':
            if history.df.empty:
                print("No history yet.")
            else:
                print(history)
            continue
        elif user_input == 'undo':
            state = caretaker.undo()
            if state is not None:
                history.df = state
                print("Undo successful.")
            else:
                print("Nothing to undo.")
            continue
        elif user_input == 'redo':
            state = caretaker.redo()
            if state is not None:
                history.df = state
                print("Redo successful.")
            else:
                print("Nothing to redo.")
            continue
        elif user_input == 'clear':
            history.clear()
            caretaker.save(history.df)
            print("History cleared.")
            continue
        elif user_input == 'save':
            history.save()
            print("History saved.")
            continue
        elif user_input == 'load':
            history.load()
            caretaker.save(history.df)
            print(f"History loaded. Records: {len(history.df)}")
            print(history)
            continue

        # process normal math expression
        try:
            result = CalculationFactory.process(user_input)
            caretaker.save(history.df)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
