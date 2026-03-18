"""Точка входа: пошаговый запуск машины Тьюринга с визуализацией."""

import time
from turing_machine import NoTransitionError
from visualization import show_tape

from examples.binary_increment import get_binary_increment_machine


def run_interactive(machine, step_delay=0.5):
    """Пошаговое выполнение с выводом ленты после каждого шага."""
    print("--- Старт ---")
    show_tape(machine.tape, machine.current_state)
    print()

    step_num = 0
    while True:
        try:
            if not machine.step():
                print("--- Финал ---")
                show_tape(machine.tape, machine.current_state)
                print(f"Выполнено шагов: {step_num}")
                break
        except NoTransitionError as e:
            print(f"Ошибка: {e}")
            show_tape(machine.tape, machine.current_state)
            break

        step_num += 1
        print(f"--- Шаг {step_num} ---")
        show_tape(machine.tape, machine.current_state)
        print()

        if step_delay > 0:
            time.sleep(step_delay)


def main():
    machine = get_binary_increment_machine("110")  # 6 в двоичном → 111 (7)
    run_interactive(machine, step_delay=0.7)


if __name__ == "__main__":
    main()
