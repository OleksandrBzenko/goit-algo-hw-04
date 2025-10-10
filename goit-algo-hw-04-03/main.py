import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізуємо colorama (щоб кольори працювали в Windows)
init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
    """
    Рекурсивно виводить структуру директорії з кольорами.
    path: шлях до поточної директорії (об’єкт Path)
    indent: відступ для візуальної ієрархії
    """
    for item in path.iterdir():
        if item.is_dir():
            # Виводимо директорії синім кольором
            print(f"{indent}{Fore.BLUE} {item.name}{Style.RESET_ALL}")
            # викликаємо функцію для піддиректорії
            print_directory_structure(item, indent + "    ")
        else:
            # Виводимо файли зеленим кольором
            print(f"{indent}{Fore.GREEN} {item.name}{Style.RESET_ALL}")


def main():
    # Перевіряємо чи передано аргумент шляху
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Error: Please specify the path to the directory.{Style.RESET_ALL}")
        print("Example:")
        print(r"  python main.py C:\Users\aleks\Desktop\picture")
        sys.exit(1)

    # Отримуємо шлях з аргументу
    directory_path = Path(sys.argv[1])

    # Перевірка, чи існує шлях
    if not directory_path.exists():
        print(f"{Fore.RED}Error: The specified path does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    # Перевірка, чи це директорія
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: The specified path is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}Directory structure for: {directory_path}{Style.RESET_ALL}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()