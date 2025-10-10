from data import total_salary



def main():
    path = 'salaries.txt'
    total, average = total_salary(path)
    print(f"Total Salary: {total}")
    print(f"Average Salary: {average:.0f}")


if __name__ == "__main__":
    main()