def total_salary(path):

    with open(path, "r", encoding="utf-8") as file:
        people = [i.strip().split(",") for i in file.readlines()]
        n = len(people)
        total = 0
        for sal in people:
            total += int(sal[1])
        average = total / n
        return total, average
