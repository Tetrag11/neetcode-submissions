class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i, val in enumerate(nums):
            if(val in hashmap):
                return True
            hashmap[val] = True;
        return False
        
        
        
        