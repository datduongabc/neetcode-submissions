class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        for i in range (size // 2 - 1, -1, -1):
            largest = i
            while True:
                current = largest
                left = 2 * current + 1
                right = 2 * current + 2

                if left < size and nums[left] > nums[largest]:
                    largest = left

                if right < size and nums[right] > nums[largest]:
                    largest = right

                if largest == current:
                    break
                else:
                    nums[current], nums[largest] = nums[largest], nums[current]
            
        for _ in range(k):
            ans = nums[0]
            nums[0], nums[size - 1] = nums[size - 1], nums[0]
            size -= 1

            largest = 0
            while True:
                current = largest
                left = 2 * current + 1
                right = 2 * current + 2

                if left < size and nums[left] > nums[largest]:
                    largest = left

                if right < size and nums[right] > nums[largest]:
                    largest = right

                if largest == current:
                    break
                else:
                    nums[current], nums[largest] = nums[largest], nums[current]
        
        return ans