from datetime import date, timedelta

def count_sundays_on_first_of_month(start_year, end_year):
    count_sundays = 0
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if date(year, month, 1).weekday() == 6:  # Sunday is represented as 6
                count_sundays += 1
    return count_sundays

print(count_sundays_on_first_of_month(1901, 2000))

