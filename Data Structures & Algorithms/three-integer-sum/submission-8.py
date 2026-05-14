class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()

        for i in range (len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    TUPLE = tuple([nums[i], nums[j], nums[k]])
                    if TUPLE not in seen:
                        seen.add(TUPLE)

                    j += 1
                    k -= 1

        return [list(i) for i in seen]