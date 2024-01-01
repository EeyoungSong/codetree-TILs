a, b, c = map(int, input().split())

def calc_mins(a, b, c):
    date = 11
    hours = 11
    mins = 11
    elapsed_time = 0

    if a < 11 or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
        return -1
    else:
        while True:
            if date == a and hours == b and mins == c:
                break
            
            elapsed_time += 1
            mins += 1

            if mins == 60:
                hours += 1
                mins = 0
            
            if hours == 24:
                date += 1
                hours = 0

        return elapsed_time

print(calc_mins(a, b, c))