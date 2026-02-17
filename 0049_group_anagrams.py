class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in hashmap:
                hashmap[s_sorted] = [s]
            else:
                hashmap[s_sorted].append(s)
        result = []
        for s in hashmap:
            result.append(hashmap[s])
        return result
