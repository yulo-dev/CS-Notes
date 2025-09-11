class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i, ch in enumerate(s):
            if (i + 1) < len(s) and val[ch] < val[s[i + 1]]:
                ans -= val[ch]
            else:
                ans += val[ch]
        return ans
