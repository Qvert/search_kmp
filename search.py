import os
from typing import Union, Optional, List, Tuple, Dict

from utils import time_loger


def search_in_file(file_path: str, sub_string: Union[str, List[str]], case_sensitivity: bool = False,
                   method: str = 'first', count: Optional[int] = None) -> \
        Optional[Union[Tuple[int, ...], Dict[str, Tuple[int, ...]]]]:

    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return None

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    return search(content, sub_string, case_sensitivity, method, count)

@time_loger
def search(string: str, sub_string: Union[str, List[str]],
           case_sensitivity: bool = False,
           method: str = 'first', count: Optional[int] = None) -> (
           Optional)[Union[Tuple[int, ...], Dict[str, Tuple[int, ...]]]]:
    """Функция для поиска всех вхождений подстрок"""
    if isinstance(sub_string, str):
        sub_string = [sub_string]

    if not case_sensitivity:
        string = string.lower()
        sub_string = [s.lower() for s in sub_string]

    return kmp_search(string, sub_string, method, count)

def kmp_search(string: str, sub_strings: List[str], method: str = 'first', count: Optional[int] = None) -> \
        tuple[int, ...] | dict[str, tuple[int, ...]] | None:
    results = {}
    for sub_string in sub_strings:
        lps = build_kmp_table(sub_string)
        positions = kmp_search_in_string(string, sub_string, lps, method, count)
        if positions:
            results[sub_string] = tuple(positions)
    if len(results) == 1:
        return results[sub_strings[0]] if results else None
    return results if results else None

def kmp_search_in_string(string: str, pattern: str, lps: List[int], method: str, count: Optional[int]) -> List[int]:
    positions = []
    i = 0
    j = 0

    if method == 'last':
        string = string[::-1]
        pattern = pattern[::-1]

    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                positions.append(i - j)
                if count and len(positions) >= count:
                    break
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if method == 'last':
        positions = [len(string) - pos - len(pattern) for pos in positions]

    return positions

def build_kmp_table(pattern: str) -> List[int]:
    lps = [0] * len(pattern)  # LPS - longest proper prefix which is suffix
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps
