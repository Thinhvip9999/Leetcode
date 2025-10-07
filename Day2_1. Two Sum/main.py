from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # lưu số và chỉ số của nó
        for i, num in enumerate(nums):
            complement = target - num  # số cần tìm để đạt target
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i  # lưu lại số hiện tại với chỉ số của nó

print(Solution().twoSum([2,7,11,15], 9))  # [0, 1]
print(Solution().twoSum([3,2,4], 6))      # [1, 2]
print(Solution().twoSum([3,3], 6))        # [0, 1]
