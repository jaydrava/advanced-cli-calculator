# app/observer.py

class Observer:
    def update(self, expression, result):
        raise NotImplementedError("Subclasses must implement this method.")


class HistoryObserver(Observer):
    def __init__(self, history):
        self.history = history

    def update(self, expression, result):
        # 🔧 DEBUG: print to verify observer update is called
        print(f"[DEBUG] Adding to history: {expression} = {result}")
        self.history.add_entry(expression, result)
        self.history.save()
