class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        # hash_map {1:1, 2:2, 3:3}

        LIST = []
        for _ in range (k):
            max_key = max(hash_map, key=hash_map.get)
            LIST.append(max_key)
            del hash_map[max_key]

        return LIST
