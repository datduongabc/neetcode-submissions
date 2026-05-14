class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index_1 in range (len(numbers)):
            remain_value = target - numbers[index_1]
            for index_2 in range (index_1 + 1, len(numbers)):
                if numbers[index_2] == remain_value:
                    return [index_1 + 1, index_2 + 1]

        return []

    # [1, 2, 3, 4]
    # index_1 0
    # num_1   1