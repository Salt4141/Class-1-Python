# function for with if a given year is a leap year
def is_leap_year (year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print (year, " is a leap year")
                return True
            return False
        return True
    else:
        return False