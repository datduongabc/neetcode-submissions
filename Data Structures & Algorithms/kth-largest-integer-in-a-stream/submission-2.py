class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        size = len(self.nums)

        def heapify(nums: List[int], i: int, size: int) -> None:
            largest = i
            left = 2 * largest + 1
            right = 2 * largest + 2

            if left < size and nums[left] > nums[largest]:
                largest = left

            if right < size and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                heapify(nums, largest, size)

        def buildmaxheap(nums: List[int], size: int) -> None:
            for i in range((size // 2) - 1, -1, -1):
                heapify(nums, i, size)

        buildmaxheap(self.nums, size)

        for _ in range(self.k - 1):
            self.nums[0], self.nums[size - 1] = self.nums[size - 1], self.nums[0]
            size -= 1
            heapify(self.nums, 0, size)
        
        return self.nums[0]