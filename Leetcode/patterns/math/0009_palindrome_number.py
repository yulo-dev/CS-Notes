"""
LeetCode 9: Palindrome Number
Difficulty: Easy
Topics: Math

Problem Statement:
Given an integer x, return true if x is a palindrome, and false otherwise.

Examples:
- Input: x = 121, Output: true
- Input: x = -121, Output: false  
- Input: x = 10, Output: false

Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    """
    Three different approaches to solve the palindrome number problem
    """
    
    def isPalindrome_string(self, x: int) -> bool:
        """
        Approach 1: String Conversion (Simple but uses extra space)
        
        Time Complexity: O(log n) - where n is the input number
        Space Complexity: O(log n) - for string storage
        
        Args:
            x: Integer to check
            
        Returns:
            bool: True if x is palindrome, False otherwise
        """
        # Convert to string and compare with reversed string
        s = str(x)
        return s == s[::-1]
    
    
    def isPalindrome_full_reversal(self, x: int) -> bool:
        """
        Approach 2: Full Mathematical Reversal
        
        Time Complexity: O(log n) - process each digit once
        Space Complexity: O(1) - constant extra space
        
        Args:
            x: Integer to check
            
        Returns:
            bool: True if x is palindrome, False otherwise
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Single digits are palindromes
        if x < 10:
            return True
        
        original = x
        reversed_num = 0
        
        # Reverse the entire number
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return original == reversed_num
    
    
    def isPalindrome(self, x: int) -> bool:
        """
        Approach 3: Half Reversal (Most Optimal)
        
        Only reverse half the digits to determine if number is palindrome.
        This saves both time and space compared to full reversal.
        
        Time Complexity: O(log n / 2) - process half the digits
        Space Complexity: O(1) - constant extra space
        
        Args:
            x: Integer to check
            
        Returns:
            bool: True if x is palindrome, False otherwise
        """
        # Negative numbers and numbers ending in 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Only reverse half the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


def test_solution():
    """
    Test function to verify all approaches work correctly
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        (121, True),      # Basic palindrome
        (-121, False),    # Negative number
        (10, False),      # Ends with 0
        (0, True),        # Zero
        (7, True),        # Single digit
        (1221, True),     # Even digits palindrome
        (12321, True),    # Odd digits palindrome
        (123, False),     # Not palindrome
        (1001, True),     # Palindrome with zeros in middle
        (1000021, False)  # Large non-palindrome
    ]
    
    print("Testing all three approaches:")
    print("=" * 50)
    
    for x, expected in test_cases:
        # Test all three approaches
        result1 = solution.isPalindrome_string(x)
        result2 = solution.isPalindrome_full_reversal(x)
        result3 = solution.isPalindrome(x)  # Half reversal (main solution)
        
        # Verify all approaches give same result
        assert result1 == result2 == result3 == expected, f"Test failed for x={x}"
        
        print(f"x = {x:>8} | Expected: {expected:>5} | "
              f"String: {result1:>5} | Full: {result2:>5} | Half: {result3:>5} | ✓")
    
    print("=" * 50)
    print("All tests passed! ")


def demonstrate_half_reversal_logic():
    """
    Demonstrate how the half reversal approach works step by step
    """
    print("\nDemonstrating Half Reversal Logic:")
    print("=" * 40)
    
    def trace_half_reversal(x):
        print(f"\nTracing x = {x}:")
        
        if x < 0 or (x % 10 == 0 and x != 0):
            print(f"  Early return: False (negative or ends with 0)")
            return False
        
        original_x = x
        reversed_half = 0
        step = 1
        
        while x > reversed_half:
            print(f"  Step {step}: x = {x}, reversed_half = {reversed_half}")
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            print(f"    After: x = {x}, reversed_half = {reversed_half}")
            step += 1
        
        result_even = x == reversed_half
        result_odd = x == reversed_half // 10
        final_result = result_even or result_odd
        
        print(f"  Final comparison:")
        print(f"    Even digits check: {x} == {reversed_half} → {result_even}")
        print(f"    Odd digits check: {x} == {reversed_half // 10} → {result_odd}")
        print(f"    Result: {final_result}")
        
        return final_result
    
    # Demonstrate with different examples
    examples = [1221, 12321, 123, 7]
    for example in examples:
        trace_half_reversal(example)


def performance_comparison():
    """
    Compare performance characteristics of different approaches
    """
    print("\nPerformance Comparison:")
    print("=" * 60)
    print("| Approach      | Time     | Space    | Pros                    | Cons           |")
    print("|---------------|----------|----------|-------------------------|----------------|")
    print("| String        | O(log n) | O(log n) | Simple to implement     | Extra space    |")
    print("| Full Reversal | O(log n) | O(1)     | No string conversion    | Overflow risk  |")
    print("| Half Reversal | O(log n) | O(1)     | Most efficient          | Complex logic  |")
    print("=" * 60)
