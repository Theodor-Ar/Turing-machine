"""Парсинг входного формата переходов в удобный вид."""

# Входной формат:  'q0 1': 'q1 0 R'
# Выходной формат: ('q0', '1') -> ('q1', '0', 'R')


def parse_transitions(raw_transitions):
    """
    Преобразует словарь вида:
        {'q0 1': 'q1 0 R', 'q1 #': 'qf 1 N'}
    в словарь:
        {('q0', '1'): ('q1', '0', 'R'), ('q1', '#'): ('qf', '1', 'N')}
    """
    result = {}
    for key_str, value_str in raw_transitions.items():
        key_parts = key_str.split()
        if len(key_parts) != 2:
            raise ValueError(f"Ключ перехода должен быть 'state symbol': {key_str!r}")
        state, symbol = key_parts[0], key_parts[1]

        value_parts = value_str.split()
        if len(value_parts) != 3:
            raise ValueError(
                f"Значение перехода должно быть 'new_state write direction': {value_str!r}"
            )
        new_state, write_sym, direction = value_parts[0], value_parts[1], value_parts[2]
        if direction not in ('L', 'R', 'N'):
            raise ValueError(f"Направление должно быть L, R или N: {direction!r}")

        result[(state, symbol)] = (new_state, write_sym, direction)
    return result
