m1, d1, m2, d2 = map(int, input().split())
d = input()



def get_days(m1, d1, m2, d2, d):
    num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    index_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    month = m1
    date = d1
    day = 1
    cnt = 0

    while True:
        if month == m2 and date == d2:
            break

        day = (day + 1) % 7
        date += 1

        if index_days[day] == d:
            cnt += 1

        if date > num_of_days[month]:
            month += 1
            date = 1

        
        
    return cnt
    
print(get_days(m1, d1, m2, d2, d))