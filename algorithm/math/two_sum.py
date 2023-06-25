class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            temp = target - nums[i]
            nums.pop(i)
            nums.insert(i, None)
            if temp in nums:
                return [i, nums.index(temp)]
