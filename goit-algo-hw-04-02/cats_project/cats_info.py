def get_cats_info(path):
    """
    Зчитує файл із даними про котів і повертає список словників,
    де кожен словник містить ключі:
    'id', 'name', 'age'.
    """
    cats_info = []  # список для зберігання інформації про котів

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # очищаємо рядок від пробілів і розділяємо за комами
                parts = line.strip().split(",")

                # перевіряємо, чи рядок має правильний формат (3 частини)
                if len(parts) == 3:
                    cat_id, name, age = parts
                    # додаємо інформацію про кота у список як словник
                    cats_info.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })

        # повертаємо список словників
        return cats_info

    except FileNotFoundError:
        print(f"Error: The file {path} was not found")
        return []
