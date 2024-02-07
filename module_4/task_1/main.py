from salary import total_salary


def main():
    if total_salary("module_4/task_1/salary/salaries.txt") == "File not found":
        print("File not found")
    else:
        total, average = total_salary("module_4/task_1/salary/salaries.txt")
        print(f"Загальна сума заробітної плати: {total},"
              f"Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()
