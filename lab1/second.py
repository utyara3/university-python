import statistics as st
from random import randint


def stats_calculator(*args, mode: str = "basic") -> dict[str, int]:
    print(f"Usermode: {mode}")
    nums = list(args)

    min_stat = min(nums)
    max_stat = max(nums)
    mean = st.mean(nums)

    base_ret = {"min": min_stat, "max": max_stat, "mean": mean}

    match mode:
        case "advanced":
            base_ret["median"] = st.median(nums)
            base_ret["mode"] = st.mode(nums)

        case "scientific":
            base_ret["median"] = st.median(nums)
            base_ret["mode"] = st.mode(nums)
            base_ret["geometric_mean"] = st.geometric_mean(nums)
            base_ret["harmonic_mean"] = st.harmonic_mean(nums)

    return base_ret


if __name__ == "__main__":
    user_input_mode = input("Enter mode: ")

    nums = [randint(1, 100) for _ in range(randint(5, 10))]
    print(f"{nums = }")
    print(stats_calculator(*nums, mode=user_input_mode))
