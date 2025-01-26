class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones ]
        heapq.heapify(maxHeap)
        # print(maxHeap)
        
        while len(maxHeap) > 1:
            a = -heapq.heappop(maxHeap)
            b = -heapq.heappop(maxHeap)
            # print(maxHeap)
            diff = a - b
            heapq.heappush(maxHeap, -diff)
            # if len(maxHeap) >= 1:
            #     # b = -heapq.heappop(maxHeap)
            #     print(-abs(a+maxHeap[0]))
            #     if a != -maxHeap[0]:
                    
            #         heapq.heappush(maxHeap, )
            #         heapq.heappop(maxHeap)
        
        return -maxHeap[0]

        

            