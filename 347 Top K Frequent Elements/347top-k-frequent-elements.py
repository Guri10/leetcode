class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for ele in nums:
            dic[ele] += 1
        
        # print(dic)
        # sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_dict)
    
        # for key,value in sorted_dict.items():
        # top_elements_dic = dict(heapq.nlargest(k, dic.items(), key=lambda item: item[1]))
        
        # lis = top_elements_dic.keys()

        sorted_lis = sorted(dic.items(), key=lambda item: item[1])
        # print(sorted_lis)

        lis = []
        for _ in sorted_lis:
            while len(lis)<k:
                a = sorted_lis.pop()
                lis.append(a[0])
                
        # lis2 = []
        # for num, cnt in lis:
        #     lis2.append(num)

        return lis
