class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # Get the length of the input string
        n = len(word)

        # Special case: if only one segment is allowed, 
        # we just take the whole word (no splitting)
        if numFriends == 1:
            return word
            
        # Maximum substring length allowed from one split
        maxLength = n - numFriends + 1

        # Step 1: Find the lexicographically largest character in the string
        max_char = max(word)

        # Step 2: Initialize the best substring as empty
        best = ""

        # Step 3: Iterate through all characters in the string
        for i, ch in enumerate(word):
            # Only consider substrings starting with the maximum character
            if ch == max_char:
                # Slice the substring with the allowed max length
                candidate = word[i:i + maxLength]
                # Update the best substring if the current candidate is greater
                if candidate > best:
                    best = candidate

        # Step 4: Return the lexicographically largest valid substring
        return best
