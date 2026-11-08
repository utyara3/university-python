import logging
import random


def configure_logger():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s || %(message)s", datefmt="%H:%M:%S"
    )


def run():
    random_numbers = [random.randint(-100, 100) for _ in range(10)]

    for x in random_numbers:
        try:
            if 42 % x == 0:
                result = 42 // x
                logging.info(  # noqa
                    f"42 divides by {x} without remainder with result: {result}"
                )
            else:
                result = round(42 / x, 4)
                logging.warning(  # noqa
                    f"42 divides by {x} with remainder with result: {result}"
                )

        except ZeroDivisionError:
            logging.error("zero was encountered among the divisors")  # noqa


if __name__ == "__main__":
    configure_logger()
    run()
