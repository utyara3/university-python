from random import randint

MIN_VALUE = -100
MAX_VALUE = 100


def print_matrix(matrix: list[list[int]]) -> None:
    for row in matrix:
        print("".join(f"{num:5}" for num in row))


def generate_random_matrix(m: int) -> list[list[int]]:
    return [[randint(MIN_VALUE, MAX_VALUE) for _ in range(m)] for _ in range(m)]


def find_saddle_points(matrix: list[list[int]]) -> list[list[int]] | None:
    M = len(matrix)

    min_in_rows: list[int] = [min(row) for row in matrix]
    max_in_cols: list[int] = [max(col) for col in zip(*matrix)]

    saddle_points = []

    for i in range(M):
        for j in range(M):
            elem: int = matrix[i][j]
            if elem == min_in_rows[i] and elem == max_in_cols[j]:
                saddle_points.append([i, j, elem])

    return saddle_points or None


if __name__ == "__main__":
    while True:
        try:
            M = int(input("Enter matrix size: "))

            if M <= 0:
                raise ValueError("Size must be greater than zero")
            break
        except ValueError as e:
            print(f"Invalid input! Please enter a valid positive integer.\nError: {e}")

    matrix = generate_random_matrix(M)
    print("Generated matrix: ")
    print_matrix(matrix)
    print()

    saddle_points = find_saddle_points(matrix)
    if saddle_points:
        for point in saddle_points:
            print(f"Row: {point[0]}, Column: {point[1]}, Value: {point[2]}")
    else:
        print("There are no saddle points in matrix")
