def validate_and_calc_average(student: tuple[str, list[int]]) -> tuple[str, float]:
    name, marks = student

    if not isinstance(marks, list) or not marks:
        raise ValueError(f"Student {name} has no marks.")

    if not all(map(lambda x: isinstance(x, int) and 2 <= x <= 5, marks)):  # noqa
        raise ValueError(
            f"Student {name} has incorrect marks: {marks}. Only integers from 2 to 5 allowed"
        )

    average = round(sum(marks) / len(marks), 2)
    return name, average


if __name__ == "__main__":
    students = {
        "Даша": [5, 4, 3, 2, 5, 4],
        "Маша": [2, 2, 3, 2, 4, 3],
        "Паша": [5, 5, 4, 5, 5, 5],
        "Гриша": [5, 4, 5, 2, 3, 2],
    }
    try:
        # a. dict with average marks
        res_average = dict(map(validate_and_calc_average, students.items()))

        print("a. dict with average marks")
        print(res_average)

        # b. calc total number of ratings for entire group
        total_marks_count = sum(map(len, students.values()))

        print(f"\nb. Total marks: {total_marks_count}")

    except ValueError as e:
        print(f"Ошибка валидации данных: {e}")
