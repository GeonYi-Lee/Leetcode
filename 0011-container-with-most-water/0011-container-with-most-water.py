class Solution:
    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        most = 0

        while front < back:
            sub = min(height[front], height[back]) * (back - front)
            most = max(most, sub)

            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
                
        return most


