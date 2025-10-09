from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        for i in range(n - 2):
            # Bỏ qua phần tử i trùng để không tạo triplet trùng
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Nếu số hiện tại > 0 thì không thể có tổng 0 (vì mảng đã sort)
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            target = -nums[i]

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # Dịch l và r bỏ qua các giá trị trùng lặp
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res
