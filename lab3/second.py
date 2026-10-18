import re
from collections import defaultdict

if __name__ == "__main__":
    input_string_regex = r"^([^ ].*?[^ ]) --- (\d+)(?:,(\d{2}))? (?:руб|коп)\.$"

    while True:
        try:
            N = int(input("Enter N: "))
        except ValueError:
            print("N must be integer")
            continue

        products = defaultdict(float)

        for i in range(N):
            name_and_price = input("Enter 'name --- price': ")
            match = re.search(input_string_regex, name_and_price)

            if match is not None:
                name, rubles_str, kopeck_str = match.groups()

                price = float(rubles_str)
                if kopeck_str is not None:
                    price += int(kopeck_str) / 100

                products[name] += price

        products = dict(sorted(products.items(), key=lambda x: (-x[1], x[0])))

        for name, price in products.items():
            print(f"{name}: {price}")
