class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            current = nums[0]
        checker = []
        for num in nums:
            if num not in checker:
                checker.append(num)
            else:
                return True
        return False

                