
from datetime import date, datetime


def calculate_age(birth_date):
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

    today = date.today()

    if birth_date > today:
        raise ValueError("Birth date cannot be in the future")

    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def days_between(date1, date2):
    if isinstance(date1, str):
        date1 = datetime.strptime(date1, "%Y-%m-%d").date()

    if isinstance(date2, str):
        date2 = datetime.strptime(date2, "%Y-%m-%d").date()

    return abs((date2 - date1).days)


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def format_date(date_string, output_format="%d-%m-%Y"):
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
    return parsed_date.strftime(output_format)


def current_date():
    return date.today()


def days_until(target_date):
    if isinstance(target_date, str):
        target_date = datetime.strptime(target_date, "%Y-%m-%d").date()

    return (target_date - date.today()).days


def get_weekday(date_string):
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
    return parsed_date.strftime("%A")
