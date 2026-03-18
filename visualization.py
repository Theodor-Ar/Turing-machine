"""Простая консольная визуализация ленты и состояния."""


def show_tape(tape, state, padding=3):
    """
    Выводит ленту и текущую позицию головки.
    Пример:
        1 1 [0] 1 #
              ↑ головка
        Состояние: q1
    """
    cells = tape.get_cells()
    head = tape.get_head()
    start, end = tape.get_visible_range(padding)

    # Строка символов
    visible = cells[start:end]
    line_parts = []
    for i, sym in enumerate(visible):
        idx = start + i
        if idx == head:
            line_parts.append(f"[{sym}]")
        else:
            line_parts.append(f" {sym} ")
    line = " ".join(line_parts)

    # Указатель под головкой (центр текущей ячейки)
    pos = 0
    for i, p in enumerate(line_parts):
        if start + i == head:
            pos += len(p) // 2
            break
        pos += len(p) + 1
    pointer = " " * pos + "↑"

    print(line)
    print(pointer, "головка")
    print(f"Состояние: {state}")
