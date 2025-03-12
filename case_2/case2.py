import numpy as np  #work with massive
import matplotlib.pyplot as plt  # graph
import re

import ru
def find_cb(func):
    # Search for coefficients c and b
    pattern = re.match(r"Q=([+-]?\d*\.?\d+)?([+-]?\d*\.?\d*)p?", func)

    if pattern:
        c_str, b_str = pattern.groups()
        # Convert the coefficient c (if absent, take 0)
        if c_str:
            c = float(c_str)
        else:
            c = 0.0

        # Convert the coefficient b (if absent, take 0)
        if not b_str or b_str in ('+', '-'):
            if b_str:
                b = float(b_str + '1')
            else:
                b = 0.0  # Turn '+' to 1.0, '-' to -1.0, empty to 0.0.

        else:
            b = float(b_str)

        return c, b
    else:
        raise ValueError(ru.DEF_TYPE_ERR)

def main():
    # Request equation input
    str_def = input(ru.INPUT_TEXT)
    c, b = find_cb(str_def)  # Take the equation apart and get c and b
    # Choose what's known
    choise = int(input(ru.CHOISE_VALUE))

    if choise == 1:
        q = float(input(ru.Q_INPUT))
        p = (c - q) / b
        e = b * (p / q)
    elif choise == 2:
        p = float(input(ru.P_INPUT))
        q = c - b * p
        e = b * (p / q)
    else:
        print(ru.WRONG_VALUE)  # Stop on incorrect entry

    # Create an array of p values from -10 to 10 with 400 points
    p_values = np.linspace(-100, 100, 400)
    Q_values = c - b * p_values  # find Q

    # make graph
    plt.figure(figsize=(8, 6))
    plt.plot(Q_values, p_values, label=f'{ru.E} = {e:.2f}', color='b')

    # Add coordinate axes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Axis captions and title
    plt.xlabel(f'{ru.Q} (Q)')
    plt.ylabel(f'{ru.P} (p)')
    plt.title(f'{ru.E} = {e:.2f}')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
