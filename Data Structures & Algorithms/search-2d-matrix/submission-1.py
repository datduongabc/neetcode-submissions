class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array_1D = []

        for row in matrix:
            for column in row:
                array_1D.append(column)

        left, right = 0, len(array_1D) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if array_1D[middle] > target:
                right = middle - 1
            elif array_1D[middle] < target:
                left = middle + 1
            else:
                return True

        return False