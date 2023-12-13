len_a, len_b = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 'No'
for i in range(len_a):
    if a[i] == b[0] and i + len_b < len_a:
        check = True
        for j in range(len_b):
            if a[i+j] != b[j]:
                check = False
                break
        if check == True:
            print('Yes')
            answer = 'Yes'
            break

if answer == 'No':
    print(answer)