def is_year_leap(year):
    if year == 1900:
        return False
    elif year == 2000:
        return True
    elif year == 2016:
        return True
    else: 
        year == 1987
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
