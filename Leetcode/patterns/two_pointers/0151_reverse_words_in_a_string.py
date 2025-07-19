# version 1 (built-in):

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by whitespace, filter out empty strings
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join them back with a single space
        return ' '.join(reversed_words)


# version 2 (Reverse Two-Pointer Scan (Manual Split, Backward)):

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []  # This will store words in reverse order
        i = len(s) - 1  # Start from the end of the string

        while i >= 0:
            # Skip any trailing spaces
            while i >= 0 and s[i] == ' ':
                i -= 1

            if i < 0:
                break  # No more words

            j = i  # j marks the end of the current word

            # Move i to the beginning of the word
            while i >= 0 and s[i] != ' ':
                i -= 1

            # Extract the word and append to result
            # Note: i+1 to j+1 because i has moved past the first character
            result.append(s[i + 1 : j + 1])

        # Join the collected words with a single space
        return ' '.join(result)


# version 3 (Full Character List Reverse (Trim + Reverse + Reverse Words)):

class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Trim spaces (leading, trailing, and multiple spaces)
        def trim_spaces(s):
            left, right = 0, len(s) - 1
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1

            output = []
            while left <= right:
                if s[left] != ' ':
                    output.append(s[left])
                elif output and output[-1] != ' ':
                    output.append(' ')
                left += 1
            return output  # returns list of chars

        # Step 2: Reverse a portion of the list from left to right (inclusive)
        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        # Step 3: Reverse each word in the list
        def reverse_each_word(l):
            n = len(l)
            start = 0
            while start < n:
                end = start
                while end < n and l[end] != ' ':
                    end += 1
                reverse(l, start, end - 1)
                start = end + 1

        # Run the steps
        char_list = trim_spaces(s)               # Clean and convert to list
        reverse(char_list, 0, len(char_list)-1)  # Reverse the entire list
        reverse_each_word(char_list)             # Reverse each individual word

        return ''.join(char_list)                # Join and return final string

