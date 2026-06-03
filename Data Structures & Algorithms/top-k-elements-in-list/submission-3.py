class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        bucket_count = len(nums)
        buckets = [[] for _ in range(bucket_count + 1)]

        for i in hashmap:
            buckets[hashmap[i]].append(i)

        results = []
        for bucket in buckets:
            results.extend(bucket)

        actual_result = []
        for i in range(k):
            actual_result.append(results.pop())

        return actual_result