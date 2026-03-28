class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in ransomNote:
            count[ch] = count.get(ch, 0)+1

        for ch in magazine:
            if ch in count:
                count[ch] -= 1

        for ch in count:
            if count[ch] > 0:
                return False

        return True
