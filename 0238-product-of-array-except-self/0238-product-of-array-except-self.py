# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans_list = []

#         for i in range(len(nums)):
#             ans = 1
#             for j in range(len(nums)):
#                 if i != j :
#                     ans *= nums[j]
#             ans_list.append(ans)
#         return ans_list


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans_list = [1] * n
#         nums = nums*2

#         for i in range(n):
#             for j in range(n-1):
#                 ans_list[i] *= nums[i+j+1]
#         return ans_list

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_list = [1] * n
        product = 1

        for i in range(n):
            ans_list[i] *= product
            product *= nums[i]

        product = 1
        for j in range(n-1, -1, -1):
            ans_list[j] *= product
            product *= nums[j]
            
        return ans_list