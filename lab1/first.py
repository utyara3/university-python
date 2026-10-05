def solve_equation(a: float, b: float, c: float) -> list[float] | None:
    D = b**2 - 4 * a * c

    if D < 0:
        return None

    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)

    return [x1, x2]


if __name__ == "__main__":
    a, b, c = [float(input(f"Enter {i}: ")) for i in ["a", "b", "c"]]

    if a == 0:
        exit("Введенное уравнение не является квадратным")

    res = solve_equation(a, b, c)
    print(
        "Действительных корней нет." if res is None else f"x1 = {res[0]}\nx2 = {res[1]}"
    )
