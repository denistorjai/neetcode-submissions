class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # O(n + m)
        TrackedLettersT = {}
        TrackedLettersS = {}

        # O(n) complexity
        for i in s:
            # dictionary.get(i,0) # defaults the i to 0, and adds an addiitonal 1
            TrackedLettersS[i] = TrackedLettersS.get(i,0) + 1

        # O(m) complexity
        for i in t:
            TrackedLettersT[i] = TrackedLettersT.get(i,0) + 1

        # O(k) = O(1) 
        if TrackedLettersT == TrackedLettersS:
            return True

        return False