from salary import total_salary


def main():
    total, average = total_salary("module_4/task_1/salary/salaries.txt")
    print(f"Загальна сума заробітної плати: {total},"
          f"Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()
