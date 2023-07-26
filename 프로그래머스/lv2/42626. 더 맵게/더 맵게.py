# 힙(heap) 자료구조 이용, try / except IndexError 이용
# 힙을 사용하는 이유 : 일반적인 리스트와 달리 push(), pop() 이후 자동 정렬

import heapq

def solution(S, K):
    heap = []
    for i in S:
        heapq.heappush(heap, i)

    cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        cnt += 1
    return cnt