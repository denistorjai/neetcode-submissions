class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        STrackedLetters = {}
        for i in s:
            if i not in STrackedLetters:
                STrackedLetters[i] = 1
            if i in STrackedLetters:
                STrackedLetters[i] += 1
    
        TTrackedLetters = {}
        for i in t:
            if i not in TTrackedLetters:
                TTrackedLetters[i] = 1
            if i in TTrackedLetters:
                TTrackedLetters[i] += 1

        if STrackedLetters == TTrackedLetters:
            return True

        return False