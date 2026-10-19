from collections.abc import Callable


def calc_average_mark(student: tuple[str, list[int]]) -> tuple[str, float]:
    student_name, student_marks = student

    if not student_marks:
        return student_name, 0.0

    average: float = round(sum(student_marks) / len(student_marks), 2)
    return student_name, average


def print_marks(
    calc_func: Callable[[tuple[str, list[int]]], tuple[str, float]],
    students: dict[str, list[int]],
):
    """Применяем calc_func к каждому student"""
    print(dict(map(calc_func, students.items())))


if __name__ == "__main__":
    students = {
        "Даша": [5, 4, 3, 2, 5, 4],
        "Маша": [2, 2, 3, 2, 4, 3],
        "Паша": [5, 5, 4, 5, 5, 5],
        "Гриша": [5, 4, 5, 2, 3, 2],
    }

    # a.
    print("a.")
    print_marks(calc_average_mark, students)

    # b.
    print("b.")
    print(sum(map(len, students.values())))
