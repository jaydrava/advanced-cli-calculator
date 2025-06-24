# app/calculator_memento.py

class Memento:
    def __init__(self, state):
        self._state = state.copy()

    def get_state(self):
        return self._state.copy()


class Caretaker:
    def __init__(self):
        self._mementos = []
        self._current = -1

    def save(self, state):
        self._mementos = self._mementos[:self._current + 1]
        self._mementos.append(Memento(state))
        self._current += 1

    def undo(self):
        if self._current > 0:
            self._current -= 1
            return self._mementos[self._current].get_state()
        return None

    def redo(self):
        if self._current + 1 < len(self._mementos):
            self._current += 1
            return self._mementos[self._current].get_state()
        return None
