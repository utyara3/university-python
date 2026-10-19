import re
from string import ascii_letters

ENCODE_REGEX = r"([a-zA-Z])\1*"
DECODE_REGEX = r"([a-zA-Z])(\d+)"


def encode_string(input_string: str) -> str:
    return re.sub(
        ENCODE_REGEX, lambda m: f"{m.group(1)}{len(m.group(0))}", input_string
    )


def decode_string(encoded_string: str) -> str:
    return re.sub(DECODE_REGEX, lambda m: m.group(1) * int(m.group(2)), encoded_string)


def validate_input(user_str: str) -> None:
    if not user_str or not all(map(lambda char: char in ascii_letters, user_str)):  # noqa
        raise ValueError(
            "The string must contain ONLY Latin letters (no spaces, numbers, or symbols)."
        )


def process_user_input() -> str:
    while True:
        try:
            input_string = input("Enter a string: ").strip()
            validate_input(input_string)
            return input_string
        except ValueError as e:
            print(f"Validation Error: {e}")


if __name__ == "__main__":
    input_string = process_user_input()

    encoded_string = encode_string(input_string)
    decoded_string = decode_string(encoded_string)

    is_correct = input_string == decoded_string

    print("\nOutput:")
    print(f"Encoded string : {encoded_string}")
    print(f"Decoded string : {decoded_string}")
    print(f"Original string: {input_string}")
    print(f"Verification   : {is_correct}")
