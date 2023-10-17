class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans_list = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            front, back = i+1, len(nums)-1
            while True:
                if front >= back :
                    break
                s = nums[i] + nums[front] + nums[back]
                if s > 0 :
                    back -= 1
                elif s < 0:
                    front += 1
                else:
                    ans_list.append([nums[i], nums[front], nums[back]])
                    front += 1
                    while nums[front-1] == nums[front] and front < back:
                        front += 1
        return ans_list


        