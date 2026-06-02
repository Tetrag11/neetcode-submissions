class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []; 
        differenceHashmap = {}
        for i, val in enumerate(nums):
            difference = target - val
            if(difference in differenceHashmap):
                  answer.append(differenceHashmap[difference])
                  answer.append(i)
                  
                  return answer
            else:
                  differenceHashmap[nums[i]] = i
        return answer

