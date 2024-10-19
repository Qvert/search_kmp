"""Utils"""
from typing import Dict, Tuple
import time


def color_output(string: str, matches: Dict[str, Tuple[int, ...]]):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset_color = '\033[0m'
    colored_string = string

    for i, (sub_string, positions) in enumerate(matches.items()):
        color = colors[i % len(colors)]
        for pos in positions:
            colored_string = (colored_string[:pos] + color + sub_string + reset_color
                              + colored_string[pos + len(sub_string):])

    print(colored_string[:min(len(colored_string), 500)])

def time_loger(func):
    """Декоратор для логирования времени выполнения"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {func.__name__}: {end_time - start_time:.4f} секунд")
        return result
    return wrapper