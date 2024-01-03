m1, d1, m2, d2 = map(int, input().split())

def get_days(m1, d1, m2, d2):
    num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    index_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    month = m1
    date = d1
    day = 1

    if (m1 == m2 and d1 > d2) or (m1 > m2):
        while True:
            if month == m2 and date == d2:
                break
        
            day = (day - 1) % 7
            date -= 1

            if date < 1:
                month -= 1
                date = num_of_days[month]
    else:
        while True:
            if month == m2 and date == d2:
                break
            
            day = (day + 1) % 7
            date += 1

            if date > num_of_days[month]:
                month += 1
                date = 1
        
    return index_days[day]
    
print(get_days(m1, d1, m2, d2))