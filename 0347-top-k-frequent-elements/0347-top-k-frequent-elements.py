class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        num_dict = sorted(num_dict.items(), key = lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(num_dict[i][0])
        return ans
