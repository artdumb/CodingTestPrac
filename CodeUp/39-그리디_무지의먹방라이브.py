import heapq
food_times = [3, 1, 2]
k = 5
# 인덱스
iter = 0
count = 0
while True:

    if food_times[iter] != 0:
        food_times[iter] -= 1
        print(food_times)
        count += 1
        if count == k:
            break

    if iter == len(food_times)-1:
        iter = 0
    else:
        iter += 1

if sum(food_times) == 0:
    print(-1)
else:

    print(iter+1)

# 답안
# 음식을 음식종류, 걸리는시간을 작은순서로 정렬한뒤 하나씩 없애며
# 남는 시간을 계산한다.
food_times = [3, 1, 2]
k = 5
q = []
# if sum(food_times) <k:
#     return -1
# 우선순위 힙에 데이터 넣기(걸리는 시간, 음식번호)
for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i], i+1))


k2 = k
sum = 0
turn = 0
while k2 > 0:
    now = heapq.heappop(q)
    print(q)
    turn = (len(q)+1)*(now[0]-turn)
    k2 = k2 - turn
    sum = sum + now[0]

result = []
result.append(now[1])
for i in q:
    result.append(i[1])
result.sort()
print(result[turn % (len(q)+1)])



import heapq
def solution(food_times, k):

    #아이디어 : 가장 시간이 빨리 걸리는 음식부터 소거하며 계산한다.
    
    if sum(food_times)<=k:
        return -1
    food = []
    for i in range(len(food_times)):
        food.append((food_times[i],i))
    now_food_count = len(food_times)
    food.sort()
    prev=0
    for i in range(len(food_times)):
        duration = (food[i][0]-prev)*now_food_count
        if k>= duration:
            k-=duration
            now_food_count -=1
            prev = food[i][0]
        else:
            break

    #남은시간 k, 현재음식개수
    result = sorted(food,key=lambda x:x[1])[:now_food_count]
    answer = result[k%now_food_count][1]+1
    return answer
solution([8,6,4],15)