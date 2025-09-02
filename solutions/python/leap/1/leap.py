def leap_year(year):
    str_year = str(year)

    if str_year[-2:] == "00" and year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False