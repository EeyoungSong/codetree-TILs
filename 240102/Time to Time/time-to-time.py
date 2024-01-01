a, b, c, d = map(int, input().split())

def calc_minutes(a, b, c, d):
    elapsed_time = 0
    hour = a
    mins = b
    while True:
        if hour == c and mins == d:
            break
        
        elapsed_time += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0
    return elapsed_time


print(calc_minutes(a, b, c, d))