def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        total = 0
        count = 0
        for line in lines[1:]:
            clean_line = line.strip()
            if not clean_line:
                continue
            try:
                name, salary = clean_line.split(',')
                total += int(salary)
                count += 1
            except ValueError:
                print(f"Missing line: {line.strip()}")
        if count == 0:
            return (0.0, 0.0)
        average = total / count
        return (total, average)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return (0.0, 0.0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0.0, 0.0)