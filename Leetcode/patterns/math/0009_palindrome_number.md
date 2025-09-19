🔗 Link: Palindrome Number
💡 Difficulty: Easy
🛠️ Topics: Math

=======================================================================================
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
- -2³¹ <= x <= 2³¹ - 1

Follow up: Could you solve it without converting the integer to a string?

=======================================================================================

## UMPIRE Method:

### Understand
Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.

**Key Questions:**
- What is a palindrome? A number that reads the same forward and backward
- Are negative numbers palindromes? No, because of the negative sign (e.g., -121 becomes 121- when reversed)
- What about numbers ending in 0? Only 0 itself can be a palindrome ending in 0 (e.g., 10 → 01 is not valid)
- Should we avoid string conversion? The follow-up asks for a mathematical solution

**Test Cases:**
- Positive palindrome: 121 → true
- Single digit: 7 → true (all single digits are palindromes)
- Negative number: -121 → false
- Ends with 0: 10 → false, but 0 → true
- Non-palindrome: 123 → false
- Large palindrome: 1221 → true
- Edge cases: 0 → true, 1 → true

**Time/Space Requirements:**
- String approach: O(log n) time, O(log n) space
- Mathematical approach: O(log n) time, O(1) space

### Match
See if this problem matches a problem category and strategies or patterns within the category.

**Pattern: Number Manipulation**
- **String conversion approach**: Convert to string, compare with reversed string
- **Mathematical reversal**: Reverse the number mathematically and compare
- **Half reversal optimization**: Only reverse half the digits to save time/space

**Key Insights:**
1. Negative numbers are never palindromes
2. Numbers ending in 0 (except 0 itself) are never palindromes
3. We can optimize by reversing only half the number

### Plan
Sketch visualizations and write pseudocode.

**Visual Example for x = 1221:**
```
Original: 1221
Reverse:  1221
Compare: 1221 == 1221 → true
```

**Visual Example for x = 123:**
```
Original: 123
Reverse:  321
Compare: 123 == 321 → false
```

**Approach 1: String Conversion**
```
function isPalindrome(x):
    if x < 0: return false
    s = toString(x)
    return s == reverse(s)
```

**Approach 2: Full Mathematical Reversal**
```
function isPalindrome(x):
    if x < 0: return false
    if x < 10: return true
    
    original = x
    reversed = 0
    
    while x > 0:
        reversed = reversed * 10 + x % 10
        x = x // 10
    
    return original == reversed
```

**Approach 3: Half Reversal (Optimal)**
```
function isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return false
    
    reversedHalf = 0
    while x > reversedHalf:
        reversedHalf = reversedHalf * 10 + x % 10
        x = x // 10
    
    // For odd digits: x == reversedHalf // 10
    // For even digits: x == reversedHalf
    return x == reversedHalf or x == reversedHalf // 10
```

### Implement
Implement the solution (make sure to know what level of detail the interviewer wants).

**Approach 1: String Conversion (Simple)**
```python
def isPalindrome(self, x: int) -> bool:
    # Convert to string and compare with reversed
    s = str(x)
    return s == s[::-1]
```

**Approach 2: Full Mathematical Reversal**
```python
def isPalindrome(self, x: int) -> bool:
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
```

**Approach 3: Half Reversal (Most Optimal)**
```python
def isPalindrome(self, x: int) -> bool:
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
```

**Java Implementation (Approach 3):**
```java
public boolean isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) {
        return false;
    }
    
    int reversedHalf = 0;
    while (x > reversedHalf) {
        reversedHalf = reversedHalf * 10 + x % 10;
        x /= 10;
    }
    
    return x == reversedHalf || x == reversedHalf / 10;
}
```

### Review
Re-check that your algorithm solves the problem by running through important examples.

**Trace through x = 1221 (Half Reversal):**
- Initial: x = 1221, reversedHalf = 0
- Iteration 1: reversedHalf = 0 * 10 + 1 = 1, x = 122
- Iteration 2: reversedHalf = 1 * 10 + 2 = 12, x = 12
- Loop ends since x == reversedHalf (both are 12)
- Return x == reversedHalf → true ✓

**Trace through x = 12321 (Half Reversal):**
- Initial: x = 12321, reversedHalf = 0
- Iteration 1: reversedHalf = 0 * 10 + 1 = 1, x = 1232
- Iteration 2: reversedHalf = 1 * 10 + 2 = 12, x = 123
- Iteration 3: reversedHalf = 12 * 10 + 3 = 123, x = 12
- Loop ends since x < reversedHalf
- Return x == reversedHalf // 10 → 12 == 123 // 10 → 12 == 12 → true ✓

**Trace through x = 123:**
- Initial: x = 123, reversedHalf = 0
- Iteration 1: reversedHalf = 0 * 10 + 3 = 3, x = 12
- Iteration 2: reversedHalf = 3 * 10 + 2 = 32, x = 1
- Loop ends since x < reversedHalf
- Return x == reversedHalf or x == reversedHalf // 10 → 1 == 32 or 1 == 3 → false ✓

**Edge Cases:**
- x = -121: Return false (negative) ✓
- x = 0: Skip condition, return true ✓
- x = 10: Return false (ends with 0 and != 0) ✓
- x = 7: Never enters loop, return true ✓

### Evaluate
Finish by giving space and run-time complexity.

**Time Complexity Analysis:**
- **String approach**: O(log n) - where n is the input number (converting to string and reversing)
- **Full reversal**: O(log n) - process each digit once
- **Half reversal**: O(log n) - but approximately half the iterations

**Space Complexity Analysis:**
- **String approach**: O(log n) - storing the string representation
- **Mathematical approaches**: O(1) - only using constant extra variables

**Approach Comparison:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| String | O(log n) | O(log n) | Simple to implement | Uses extra space |
| Full Reversal | O(log n) | O(1) | No string conversion | Risk of overflow |
| Half Reversal | O(log n/2) | O(1) | Most efficient | Slightly complex logic |

**Pros:**
- Multiple valid solutions with different trade-offs
- Clear problem with straightforward logic
- Good for demonstrating optimization thinking

**Cons:**
- Full reversal approach might cause integer overflow for large numbers
- Half reversal requires careful handling of odd/even digit cases

**Key Insights:**
- **Early termination conditions**: Negative numbers and numbers ending in 0 (except 0) can be eliminated immediately
- **Half reversal optimization**: We only need to reverse half the digits to determine if it's a palindrome
- **Overflow consideration**: While the problem constraints fit in 32-bit integers, the reversal might cause overflow

**Interview Tips:**
1. Start with the simple string approach to show you understand the problem
2. Mention the mathematical approach as an optimization
3. Discuss the half-reversal optimization if time permits
4. Always handle edge cases (negative numbers, numbers ending in 0)
5. Consider discussing integer overflow if using full reversal approach

**Follow-up Discussion:**
The mathematical approach (especially half reversal) demonstrates:
- Understanding of number manipulation
- Optimization thinking
- Careful handling of edge cases
- Space complexity awareness
