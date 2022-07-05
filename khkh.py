class Solution:
    def twoSum( nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for s in range(len(nums)):
                if nums[s] + nums[x] == target:
                    return [x, s]


s = Solution
nums = [2,3,4]
target = 6
print(s.twoSum(nums=nums, target=target))
