from collections import defaultdict
from pprint import pprint


def pair_persons(
    relationships: defaultdict[str, set[str]], person1: str, person2: str
) -> None:
    """Establishing a connection between two people"""
    relationships[person1].add(person2)
    relationships[person2].add(person1)


def parse_and_validate_user_input(input_data: str) -> tuple[str, str] | None:
    parts = [name.strip() for name in input_data.split("---")]

    if len(parts) != 2:
        print("The string must contain exactly one '---' separator!")
        return None

    p1, p2 = parts

    if not p1 or not p2:
        print("People's names cannot be empty!")
        return None

    if p1 == p2:
        print("A person cannot be friends with themselves!")
        return None

    return p1, p2


def print_people_with_shared_connections(relationships: defaultdict[str, set[str]]):
    # Creating a list of unique people
    persons = list(relationships.keys())
    for i in range(len(persons)):
        for j in range(i + 1, len(persons)):
            # Go through each pair
            person1 = persons[i]
            person2 = persons[j]

            rels1 = relationships[person1]
            rels2 = relationships[person2]

            # Intersect sets
            intersection = rels1 & rels2

            if len(intersection) >= 2:
                print(f"{person1} and {person2} have mutual friends: {intersection}")


if __name__ == "__main__":
    relationships = defaultdict(set)
    input_string = "Enter relationship: "

    # Processing user input
    while True:
        input_data = input(input_string)
        if input_data == "!!!":
            break

        pair = parse_and_validate_user_input(input_data)
        if pair is None:
            # Skip processing if the input is invalid.
            continue

        person1, person2 = pair
        pair_persons(relationships, person1, person2)

    # Listing all relationships
    pprint(relationships)

    print_people_with_shared_connections(relationships)
