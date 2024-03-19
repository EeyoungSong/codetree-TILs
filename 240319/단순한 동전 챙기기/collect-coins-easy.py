import sys
# 입력 및 변수 선언
n = int(input())
grid = [list(input()) for _ in range(n)]
pos_dic = {}
num_arr = []
s = ('', '')
e = ('', '')

# 자료 정리
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            s = (i, j)
        elif grid[i][j] == 'E':
            e = (i, j)
        elif grid[i][j] != '.':
            num_arr.append(grid[i][j])
            pos_dic[grid[i][j]] = (i, j)

#print(pos_dic)


# 조합 리스트 만드는 함수
choosed = []
chooesd_list = []

def print_ans():
    l = []
    for i in range(len(choosed)):
        if choosed[i] == 1:
            l.append(num_arr[i])
    chooesd_list.append(l)


def choose(curr_num, cnt):
    if curr_num > m:
        if cnt == p:
            print_ans()
        return
    choosed.append(1)
    choose(curr_num+1, cnt+1)
    choosed.pop()

    choosed.append(0)
    choose(curr_num+1, cnt)
    choosed.pop()

# 조합에 따른 거리 구하는 함수
def cal_distance(arr):
    s2f = abs(pos_dic[arr[0]][0] - s[0]) + abs(pos_dic[arr[0]][1] - s[1])
    l2e = abs(pos_dic[arr[-1]][0] - e[0]) + abs(pos_dic[arr[-1]][1] - e[1])

    t_dis = s2f + l2e

    for i in range(1, len(arr)):
    #print(str(arr[i-1]))
        r1, c1 = pos_dic[str(arr[i-1])]
        r2, c2 = pos_dic[str(arr[i])]
        d = abs(r1 - r2) + abs(c1 - c2)
        t_dis += d
    return t_dis


# 3 ~ m 까지 p를 바꿔가면서 최솟값 구해야함
answer = -1
m = len(num_arr)
num_arr.sort()
for i in range(3, m+1):
    p = i
    choose(1, 0)
#print(chooesd_list)


# 조합에 대해서 거리 계산
if len(chooesd_list) > 0:
    min_dis = sys.maxsize
    for c in chooesd_list:
        d = cal_distance(c)
        #print(d)
        min_dis = min(d, min_dis)

if len(chooesd_list) != 0:
    answer = min_dis

print(answer)