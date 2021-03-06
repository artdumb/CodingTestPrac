# 내 풀이 리스트 del을 이용하여 삭제
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

count = 0
while True:
    if len(a) == 0:
        break
    if a[0] <= len(a):
        del a[:a[0]]
        count += 1
    else:
        break
print(count)

# 정답풀이
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 현재그룹의 수
group = 0
# 현재 그룹에 포함된 모험가의 수
count = 0

for i in a:
    count += 1
    # 현재 그룹의 인원이 공포도 이상이라면 그룹결성
    if count >= i:
        # 그룹으로 만들기
        group += 1
        # 현재인원 초기화
        count = 0


# 정답풀이
# 아이디어 : 오름차순 정렬 후 밑에서 부터 비교
n = int(input())
a = list(map(int, input().split()))
# 정렬
a.sort()

# 현재그룹인원
count = 0
group = 0
# 작은 수부터 확인한다.
for i in a:
    count += 1
    # 현재인원수가 현재 공포도 이상이라면 그룹결성
    if count >= i:
        count = 0
        group += 1
group = 0
