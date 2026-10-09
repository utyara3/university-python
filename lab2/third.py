from itertools import combinations


def process_user_input() -> dict[str, set[str]]:
    students_data = {}

    while True:
        name = input("Enter student name: ").strip()
        if name == "!!!":
            break

        if not name:
            continue

        skills = set()
        print(f"Enter {name}'s skills:")
        while True:
            skill = input().strip()
            if not skill:
                break
            skills.add(skill)

        students_data[name] = skills

    return students_data


def calc_jaccard(set_a: set, set_b: set) -> float:
    if not set_a and not set_b:
        return 1.0
    return round(len(set_a & set_b) / len(set_a | set_b), 2)


def analyze_students(students_data: dict[str, set[str]]):
    names = list(students_data.keys())

    same_skills = []
    supersets = set()

    # base jaccard matrix (1.0 on the main diagonal)
    matrix = {n1: {n2: 1.0 if n1 == n2 else 0.0 for n2 in names} for n1 in names}

    # compare pairs
    for name1, name2 in combinations(names, 2):
        skills1 = students_data[name1]
        skills2 = students_data[name2]

        # set comparison
        if skills1 == skills2:
            same_skills.append((name1, name2))
        elif skills1 > skills2:
            supersets.add(name1)
        elif skills2 > skills1:
            supersets.add(name2)

        # jaccard coefficient
        j_score = calc_jaccard(skills1, skills2)
        matrix[name1][name2] = j_score
        matrix[name2][name1] = j_score

    # all students with the maximum number of skills
    if students_data:
        max_len = max(len(skills) for skills in students_data.values())
        top_students = [
            name for name, skills in students_data.items() if len(skills) == max_len
        ]
    else:
        top_students = []

    return same_skills, list(supersets), top_students, matrix


def print_matrix(matrix: dict, names: list):
    if not names:
        return

    # calc column width based on the longest name
    col_width = max(max(len(name) for name in names), 6) + 2

    # matrix header
    print(f"{'':<{col_width}}", "".join(f"{name:>{col_width}}" for name in names))

    # table rows
    for n1 in names:
        row = "".join(f"{matrix[n1][n2]:>{col_width}.2f}" for n2 in names)
        print(f"{n1:<{col_width}} {row}")


if __name__ == "__main__":
    # data collection
    data = process_user_input()

    # data analysis
    same_sk, super_sk, top_st, sim_matrix = analyze_students(data)

    print(f"""
a. Students with completely identical skill sets: {same_sk}
b. Students whose skill set is a strict superset: {super_sk}
c. Top students with the most skills (max: {len(data[top_st[0]]) if top_st else 0}): {top_st}

d. Jaccard Similarity Matrix:
    """)
    print_matrix(sim_matrix, list(data.keys()))
