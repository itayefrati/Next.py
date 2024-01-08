def gen_secs():
    for sec in range(0, 60):
        yield sec


def gen_minutes():
    for minute in range(0, 60):
        yield minute


def gen_hours():
    for hour in range(0, 24):
        yield hour


def get_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2024):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        yield 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        yield 30
    elif month == 2:
        if leap_year:
            yield 29
        else:
            yield 28


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month):
                for time in get_time():
                    yield "%02d/%02d/%04d" " %s" % (day, month, year, time)


def main():
    pass


if __name__ == '__main__':
    main()
