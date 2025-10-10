from cats_info import get_cats_info

def main():
    path = "cats.txt"  # шлях до файлу
    cats_info = get_cats_info(path)  # отримуємо список словників

    print(cats_info)  # просто виводимо результат

if __name__ == "__main__":
    main()