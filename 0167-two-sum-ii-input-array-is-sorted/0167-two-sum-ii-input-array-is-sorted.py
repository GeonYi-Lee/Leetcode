class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = 0, len(numbers) - 1

        while True:
            if numbers[front] + numbers[back] == target:
                return [front +1, back + 1]
                break
            elif numbers[front] + numbers[back] < target:
                front += 1
            else:
                back -= 1
        
            

        