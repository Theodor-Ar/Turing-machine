"""Логика машины Тьюринга: лента и сама машина."""

BLANK = '#'


class Tape:
    """Лента с динамическим расширением. Не знает алфавит заранее."""

    def __init__(self, initial_content=None):
        if initial_content is None:
            initial_content = []
        self._cells = list(initial_content) if initial_content else [BLANK]
        self._head = 0

    def read(self):
        """Прочитать символ под головкой."""
        self._ensure_bounds()
        return self._cells[self._head]

    def write(self, symbol):
        """Записать символ под головкой."""
        self._ensure_bounds()
        self._cells[self._head] = symbol

    def move(self, direction):
        """Сдвинуть головку: 'L', 'R' или 'N'."""
        if direction == 'L':
            self._head -= 1
        elif direction == 'R':
            self._head += 1
        # 'N' — не двигаем

    def _ensure_bounds(self):
        """Расширить ленту при выходе головки за границы."""
        while self._head < 0:
            self._cells.insert(0, BLANK)
            self._head += 1
        while self._head >= len(self._cells):
            self._cells.append(BLANK)

    def get_visible_range(self, padding=2):
        """Диапазон индексов для отображения (с небольшим отступом)."""
        self._ensure_bounds()
        start = max(0, self._head - padding)
        end = min(len(self._cells), self._head + padding + 1)
        return start, end

    def get_cells(self):
        return self._cells

    def get_head(self):
        return self._head


class NoTransitionError(Exception):
    """Нет перехода для текущего состояния и символа."""

    def __init__(self, state, symbol):
        self.state = state
        self.symbol = symbol
        super().__init__(f"Нет перехода для (state={state!r}, symbol={symbol!r})")


class TuringMachine:
    """
    Машина Тьюринга.
    transitions: словарь (state, symbol) -> (new_state, write_symbol, direction)
    """

    def __init__(self, transitions, start_state, final_state, tape):
        self.transitions = dict(transitions)
        self.start_state = start_state
        self.final_state = final_state
        self.tape = tape
        self.current_state = start_state
        self._finished = False

    def step(self):
        """
        Выполнить один шаг. Возвращает True, если шаг выполнен; False если уже в финале.
        Выбрасывает NoTransitionError при отсутствии перехода.
        """
        if self._finished:
            return False

        symbol = self.tape.read()
        key = (self.current_state, symbol)
        if key not in self.transitions:
            raise NoTransitionError(self.current_state, symbol)

        new_state, write_sym, direction = self.transitions[key]
        self.tape.write(write_sym)
        self.tape.move(direction)
        self.current_state = new_state

        if self.current_state == self.final_state:
            self._finished = True
        return True

    def run(self, max_steps=None):
        """
        Выполнять шаги до финального состояния или до max_steps.
        Возвращает число выполненных шагов.
        """
        steps = 0
        while self.step():
            steps += 1
            if max_steps is not None and steps >= max_steps:
                break
        return steps

    @property
    def is_finished(self):
        return self._finished
