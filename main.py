"""Main module"""
import argparse
from search import search, search_in_file
from utils import color_output


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Утилита поиска подстрок в строке/файле")
    parser.add_argument('--string', type=str, help='Строка для поиска')
    parser.add_argument('--substrings', type=str, nargs='+', required=True, help='Подстрока которую нужно найти')
    parser.add_argument('--case-sensitive', action='store_true', help='Чувствительность к регистру.')
    parser.add_argument('--file', type=str, help="Путь до файла для поиска.")
    parser.add_argument('--count', type=int, help="Количество первых вхождений для поиска.")
    parser.add_argument('--color', action='store_true', help="Включить цветовой вывод.")
    parser.add_argument('--method', type=str, choices=['first', 'last'], default='first',
                        help="Метод поиска ('first' или 'last').")
    args = parser.parse_args()

    if args.string:
        result = search(args.string, args.substrings, args.case_sensitive, args.method, args.count)
    elif args.file:
        result = search_in_file(args.file, args.substrings, args.case_sensitive, args.method, args.count)
    else:
        print("Необходимо указать либо строку (--string), либо файл (--file).")
        exit(1)

    if result:
        if args.color:
            color_output(args.string, result)
        else:
            print(result)
    else:
        print("Совпадений не найдено.")

if __name__ == '__main__':
    main()