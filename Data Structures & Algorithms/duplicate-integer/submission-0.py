class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i, val in enumerate(nums):
            hashmap[val] = 0
        for num in nums:
            if(num in hashmap):
                hashmap[num] += 1
                if (hashmap[num]>1):
                    return True
        return False
        
        
        