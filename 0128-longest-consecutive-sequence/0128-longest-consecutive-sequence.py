class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)
        ans_list = []
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                ans += 1
            elif nums[i] - nums[i-1] > 1:
                ans_list.append(ans)
                ans = 1

        ans_list.append(ans)

        return max(ans_list)