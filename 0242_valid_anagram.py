class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=s.lower()
        s2=t.lower()
        hashmap={}
        for c in s1:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1

        for c in s2:
            if c not in hashmap:
                return False
            else:
                hashmap[c]-=1
        for c in hashmap:
            if hashmap[c]!=0:
                return False

        return True