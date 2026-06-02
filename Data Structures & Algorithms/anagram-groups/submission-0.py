import json
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainhashmap = {}
        outputarray = []

        def stringToHashMap(string: str):
            hashmap = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
            for i in string:
                if i in hashmap:
                    hashmap[i] += 1
            return hashmap

        for val in strs:
            key = json.dumps(stringToHashMap(val))
            if key in mainhashmap:
                mainhashmap[key].append(val)
            else:
                mainhashmap[key] = [val]

        for i in mainhashmap:
            outputarray.append(mainhashmap[i])

        return outputarray
        