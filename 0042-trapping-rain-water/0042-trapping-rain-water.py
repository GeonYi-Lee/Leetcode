class Solution:
    def trap(self, height: List[int]) -> int:
        front = 1
        back = len(height) - 1
        fmax = height[0]
        bmax = height[-1]
        water = 0

        while front <= back:
            if height[front] > fmax:
                fmax = height[front]
            if height[back] > bmax:
                bmax = height[back]

            if fmax <= bmax:
                water += fmax - height[front]
                front += 1
            else:
                water += bmax - height[back]
                back -= 1
        
        return water



