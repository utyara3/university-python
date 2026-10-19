import re


def parse_line(line: str) -> tuple[str, float] | None:
    pattern = r"^(?! )(.+?)(?<! ) --- (\d+)(?:,(\d{2}))? (?:руб|коп)\.$"

    match = re.match(pattern, line.strip())
    if not match:
        return None

    name, rubles_str, kopecks_str = match.groups()

    price = float(rubles_str)
    if kopecks_str:
        price += int(kopecks_str) / 100.0

    return name, price


def task_a(valid_purchases):
    expensive_purchases = list(filter(lambda item: item[1] >= 1000.0, valid_purchases))
    sorted_expensive = sorted(expensive_purchases, key=lambda x: (-x[1], x[0]))

    output_a = list(map(lambda item: f"{item[0]}: {item[1]:.2f}", sorted_expensive))  # noqa

    return output_a


def task_b(valid_purchases):
    return sum(map(lambda item: item[1], valid_purchases))  # noqa


def process_lab() -> None:
    n_str = input("Enter N: ").strip()

    while not n_str.isdigit():
        print("N must be a non-negative integer.")
        n_str = input("Enter N: ").strip()

    N = int(n_str)

    input_lines = [input(f"Enter line {i + 1}: ") for i in range(N)]
    parsed_results = list(map(parse_line, input_lines))
    incorrect_count = len(list(filter(lambda x: x is None, parsed_results)))
    valid_purchases = list(filter(lambda x: x is not None, parsed_results))

    output_a = task_a(valid_purchases)

    output_b = task_b(valid_purchases)

    print("\nOutput:")
    if output_a:
        print("\n".join(output_a))

    print(f"\nTotal: {output_b:.2f}")
    print(f"Incorrect lines: {incorrect_count}")


if __name__ == "__main__":
    process_lab()
