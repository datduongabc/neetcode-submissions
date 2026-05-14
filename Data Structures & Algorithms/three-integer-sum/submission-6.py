class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if (len(nums) < 3):
        #     return []
        
        nums.sort()

        # if nums[0] == 0 and nums[-1] == nums[0]:
        #     return [[0, 0, 0]]
        
        # if nums[0] != 0 and nums[-1] == nums[0]:
        #     return []
        
        LIST = []
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
                        LIST.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

        return LIST