from functools import cmp_to_key

def compare(x, y):
    if len(x) == 1:
        # print(x)
        # print(x+y, y+x)
        if x + y > y + x:
            return -1
        else:
            return 1
    # x가 y보다 크다면
    # 우리가 원하는 방향입니다.
    elif x > y:
        return -1
    # y가 x보다 크다면
    # 우리가 원하지 않는 방향입니다.
    elif y > x:
        return 1
    # 우선 순위가 동일한 경우입니다.
    return 0


# 내림차순 정렬
#arr.sort(key=cmp_to_key(compare))

# for elem in arr: # 정렬 이후의 결과 출력
#     print(elem, end=" ")


n = int(input())
arr = [input() for _ in range(n)]
arr.sort(reverse=True)
arr.sort(key=cmp_to_key(compare))


for elem in arr:
    print(elem, end="")