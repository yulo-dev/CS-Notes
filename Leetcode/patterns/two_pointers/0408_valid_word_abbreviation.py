class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0  # i for word, j for abbr

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # Leading zero is invalid (e.g., "02" is not a valid abbreviation)
                if abbr[j] == '0':
                    return False

                # Parse the full number (e.g., "12" → skip 12 characters)
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                # Skip `num` characters in the original word
                i += num
            else:
                # Characters must match exactly
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # Both pointers must reach the end for a valid abbreviation
        return i == len(word) and j == len(abbr)
