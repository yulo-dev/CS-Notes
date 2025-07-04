# Leetcode 0139 - Word Break

## ☀️ UMPIRE

- **Understand**: Given a string `s` and a list of words `wordDict`, determine if `s` can be segmented into a sequence of dictionary words. Each word in the dictionary can be reused any number of times. Return True if possible, otherwise False.
- **Match**: Input is a string + dictionary list → suitable for dynamic programming.
- **Plan**: Use a DP array `dp` where `dp[i]` means `s[0:i]` can be segmented. Iterate `i` from 1 to `n`, and for each `i`, check all `j < i`. If `dp[j]` is True and `s[j:i]` in wordDict, then set `dp[i] = True`.
- **Implement**: See below
- **Review**: Check if all substrings `s[j:i]` are valid dictionary words and if their prefix has been successfully segmented.
- **Evaluate**: Time O(n^2), Space O(n), where n is the length of input string s. For each `i`, we check up to `i` possible splits. Set lookup is O(1).

## ☀️ Metadata

- **Appears In**: Grind75
- **Pattern**: Dynamic Programming
- **Data Structure**: Array
- **Algorithm**: Bottom-up DP
- **Tags**: DP, String, HashSet, Prefix Validation


## ☀️ Solution Code

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the word dictionary into a set for faster lookups (O(1))
        word_set = set(wordDict)
        
        # Length of the input string
        n = len(s)

        # Initialize a DP array where dp[i] indicates whether s[0:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can always be segmented

        # Iterate over all substring end positions
        for i in range(1, n + 1):
            # For each end position i, check all possible split points j
            for j in range(i):
                # If the substring s[0:j] can be segmented, and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    # Then s[0:i] can also be segmented
                    dp[i] = True
                    break  # No need to check further splits for this i

        # The final result indicates whether the full string can be segmented
        return dp[n]
```

## ☀️ Trace

```
s = "applepenapple"
wordDict = ["apple", "pen"]

DP Trace:
dp[0] = True  (base case)
i = 5: j = 0 → s[0:5] = "apple" ✔️ dp[5] = True
i = 8: j = 5 → s[5:8] = "pen"   ✔️ dp[8] = True
i = 13: j = 8 → s[8:13] = "apple" ✔️ dp[13] = True

Final dp = [True, False, ..., True]  ✔️ return True
```

## ☀️ Line-by-line Typing Script

- I’m defining the wordBreak function, which takes in a string and a word dictionary.
- I’m converting the wordDict to a set for fast O(1) lookups.
- I define `n` as the length of the input string.
- I create a dp array of size n+1, initialized to False.
- I mark dp[0] = True as the base case, meaning an empty string is always valid.
- For each i from 1 to n, I try all previous split points j.
- If dp[j] is True and s[j\:i] is in the word set, it means s[0\:i] can be built.
- So I mark dp[i] = True and break out of the inner loop.
- After checking all positions, I return dp[n] as the final result.

