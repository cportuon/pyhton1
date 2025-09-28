def is_year_leap(year):
    if year % 4 != 0:        # Si no es multiplo de 4 --> ¡¡NO ES BISIESTO!!
        return False 
    elif year % 100 != 0:    # Si es multiplo de 4 y no lo es de 100 --> !!SI ES BISIESTO!!
       return True
    elif year % 400 != 0:    # Si es multiplo de 4 y de 100 y no es multiplo de 400 --> ¡¡NO ES BISIESTO!! 
       return False
    else:
       return True           # Si es multiplo de 4, de 100 y de 400 --> ¡¡SI ES BISIESTO!!   

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")