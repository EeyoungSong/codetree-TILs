m1, d1, m2, d2 = map(int, input().split())

def calc_date(m1, d1, m2, d2):
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = m1
    date = d1
    elapsed_time = 1
    while True:
        if month == m2 and date == d2:
            break
        #print(month, date, elapsed_time)
        elapsed_time += 1
        date += 1

        if date > num_of_days[month]:
            month += 1
            date = 1
    
    return elapsed_time

print(calc_date(m1, d1, m2, d2))