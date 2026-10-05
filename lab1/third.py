from datetime import date, datetime, timedelta
from random import randint

DATE_FORMAT = "%d.%m.%Y"


def generate_random_dates(num: int = 10) -> list[str]:
    """Формат дат - ДД.ММ.ГГГГ"""
    dates = []

    for _ in range(num):
        is_valid = randint(0, 1)

        if is_valid:  # генерим валидную дату
            initial_date = date(2000, 1, 1)  # 1 января 2000 года
            days_delta = randint(1, 365 * 50)  # сдвиг по дате

            ret_date = initial_date + timedelta(days=days_delta)

            dates.append(ret_date.strftime(DATE_FORMAT))

        else:
            day = randint(32, 60)
            month = randint(12, 20)
            year = randint(2000, 2100)

            dates.append(".".join(map(str, [day, month, year])))

    return dates


def validate_date(date: str) -> bool:
    try:
        datetime.strptime(date, DATE_FORMAT)  # noqa
    except ValueError:
        return False

    return True


def check_dates(*dates: str) -> None:
    valid_dates = []
    for gen_date in dates:
        if validate_date(gen_date):
            valid_dates.append(gen_date)

    if not valid_dates:
        print("Валидных дат не найдено")
        return

    earliest = min(valid_dates, key=lambda x: datetime.strptime(x, DATE_FORMAT))  # noqa
    latest = max(valid_dates, key=lambda x: datetime.strptime(x, DATE_FORMAT))  # noqa

    today = datetime.today()  # noqa
    future_dates = [d for d in valid_dates if datetime.strptime(d, DATE_FORMAT) > today]  # noqa

    print(f"Валидные даты:\n{valid_dates}")
    print(f"Самая ранняя и поздняя даты: {earliest}, {latest}")
    print(f"Будущие даты относительно сегодня ({today}): {future_dates}")


if __name__ == "__main__":
    try:
        dates_num = int(input("Enter num of dates: "))

        dates = generate_random_dates(dates_num)

        check_dates(*dates)
    except ValueError:
        print("Количество дат невалидно.")
