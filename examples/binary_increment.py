"""Пример: инкремент бинарного числа на ленте.

Алгоритм: идём вправо до конца числа, затем идём влево:
- 0 -> пишем 1, идём к началу и стоп
- 1 -> пишем 0, перенос, дальше влево
- # (начало) -> пишем 1 (переполнение), стоп
"""

from turing_machine import Tape, TuringMachine
from parser import parse_transitions


BINARY_INCREMENT_RAW = {
    'q0 0': 'q0 0 R',
    'q0 1': 'q0 1 R',
    'q0 #': 'q1 # L',
    'q1 0': 'q2 1 L',
    'q1 1': 'q1 0 L',
    'q1 #': 'qf 1 N',
    'q2 0': 'q2 0 L',
    'q2 1': 'q2 1 L',
    'q2 #': 'qf # N',
}


def get_binary_increment_machine(initial_binary):
    """
    initial_binary: строка из '0' и '1', например '110' для числа 6.
    Возвращает машину, которая по завершении оставит на ленте initial_binary + 1.
    """
    tape = Tape(list(initial_binary) if initial_binary else ['0'])
    transitions = parse_transitions(BINARY_INCREMENT_RAW)
    return TuringMachine(
        transitions,
        start_state='q0',
        final_state='qf',
        tape=tape,
    )
