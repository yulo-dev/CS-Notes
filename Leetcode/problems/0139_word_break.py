class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the word dictionary into a set for faster lookups (O(1))
        word_set = set(wordDict)
        
        # Length of the input string
        n = len(s)
        
        # Initialize a DP array where dp[i] indicates whether s[0:i] can be segmented
        dp = [False] * (n + 1)
        
        # Base case: empty string can always be segmented
        dp[0] = True

        # Iterate over all substring end positions
        for i in range(1, n + 1):
            # For each end position i, check all possible split points j
            for j in range(i):
                # If the substring s[0:j] can be segmented, and s[j:i] is in the dictionary
                if dp[j] and s[j:i] in word_set:
                    # Then s[0:i] can also be segmented
                    dp[i] = True
                    # No need to check further splits for this i
                    break

        # The final result indicates whether the full string can be segmented
        return dp[n]
