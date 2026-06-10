class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]

        suffix = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i+1] * nums[i]

        results = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                results[i] = suffix[i + 1]
                continue
            if i == len(nums) - 1:
                results[i] = prefix[i - 1]
                continue
            else:
                results[i] = suffix[i + 1] * prefix[i - 1]

        return results
        
           

            

        
        