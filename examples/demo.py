
from pyhelper.date_utils import (
    calculate_age,
    days_between,
    is_leap_year,
    format_date,
    current_date,
    days_until,
    get_weekday
)

print("===== PyHelper Date Utilities =====")

print("Age:", calculate_age("2005-06-15"))
print("Days Between:", days_between("2026-01-01", "2026-11-18"))
print("Leap Year:", is_leap_year(2024))
print("Formatted Date:", format_date("2026-11-18"))
print("Current Date:", current_date())
print("Days Until:", days_until("2026-12-31"))
print("Weekday:", get_weekday("2026-11-18"))
