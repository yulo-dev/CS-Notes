🔗 Link: Excel Sheet Column Number
💡 Difficulty: Easy
🛠️ Topics: Math, String

=======================================================================================
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].

=======================================================================================

## UMPIRE Method:

### Understand
Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.

**Key Questions:**
- Is this essentially a base-26 numbering system? Yes, but with a twist - there's no zero digit (A=1, not A=0)
- Should we handle lowercase letters? No, constraints specify only uppercase
- What's the maximum column we need to handle? Up to "FXSHRXW" (which is column 2^31 - 1)

**Test Cases:**
- Happy path: "AB" → 28 (A=1×26¹ + B=2×26⁰ = 26 + 2 = 28)
- Edge case: "A" → 1 (single character)
- Edge case: "Z" → 26 (last single character)
- Edge case: "AA" → 27 (first double character)
- Complex case: "ZY" → 701 (Z=26×26¹ + Y=25×26⁰ = 676 + 25 = 701)

**Time/Space Requirements:**
- Time: O(N) where N is the length of the string
- Space: O(1) constant extra space

### Match
See if this problem matches a problem category and strategies or patterns within the category.

**Pattern: Base Conversion / Number System**
- This is a modified base-26 number system where digits go from 1-26 instead of 0-25
- Similar to converting from any base to decimal, but with offset
- Pattern: Each position has a weight of 26^position, and each character has value (char - 'A' + 1)

**Key Insight:**
Unlike standard base-26, Excel columns don't have a "zero" digit. A=1, B=2, ..., Z=26. This means:
- Single chars: A=1, B=2, ..., Z=26
- Double chars: AA=27 (not 26), AB=28, ..., AZ=52, BA=53, etc.

### Plan
Sketch visualizations and write pseudocode.

**Visual Example for "AB":**
```
Position weights: [26¹, 26⁰] = [26, 1]
Characters:       ['A', 'B']  = [1,  2] (after conversion)
Calculation:      1×26 + 2×1  = 26 + 2 = 28
```

**Algorithm:**
1. Initialize result = 0
2. For each character in the string (left to right):
   - Convert character to its numeric value: char - 'A' + 1
   - Update result: result = result × 26 + char_value
3. Return result

**Pseudocode:**
```
function titleToNumber(columnTitle):
    result = 0
    for each char in columnTitle:
        char_value = char - 'A' + 1
        result = result * 26 + char_value
    return result
```

### Implement
Implement the solution (make sure to know what level of detail the interviewer wants).

**Python Solution:**
```python
def titleToNumber(self, columnTitle: str) -> int:
    result = 0
    for char in columnTitle:
        # Convert character to number (A=1, B=2, ..., Z=26)
        char_value = ord(char) - ord('A') + 1
        # Update result using base-26 logic
        result = result * 26 + char_value
    return result
```

**Alternative Implementation with explicit power calculation:**
```python
def titleToNumber(self, columnTitle: str) -> int:
    result = 0
    n = len(columnTitle)
    
    for i, char in enumerate(columnTitle):
        char_value = ord(char) - ord('A') + 1
        power = n - i - 1
        result += char_value * (26 ** power)
    
    return result
```

**Java Solution:**
```java
public int titleToNumber(String columnTitle) {
    int result = 0;
    for (char c : columnTitle.toCharArray()) {
        int charValue = c - 'A' + 1;
        result = result * 26 + charValue;
    }
    return result;
}
```

### Review
Re-check that your algorithm solves the problem by running through important examples.

**Trace through "AB":**
- Start: result = 0
- First char 'A': char_value = 1, result = 0 × 26 + 1 = 1
- Second char 'B': char_value = 2, result = 1 × 26 + 2 = 28
- Return 28 ✓

**Trace through "ZY":**
- Start: result = 0
- First char 'Z': char_value = 26, result = 0 × 26 + 26 = 26
- Second char 'Y': char_value = 25, result = 26 × 26 + 25 = 676 + 25 = 701
- Return 701 ✓

**Edge Cases:**
- "A": result = 0 × 26 + 1 = 1 ✓
- "Z": result = 0 × 26 + 26 = 26 ✓
- "AA": result = (0 × 26 + 1) × 26 + 1 = 26 + 1 = 27 ✓

### Evaluate
Finish by giving space and run-time complexity.

**Time Complexity: O(N)**
- Where N is the length of the input string
- We iterate through each character exactly once
- Each operation (character conversion and arithmetic) takes O(1) time

**Space Complexity: O(1)**
- We only use a constant amount of extra space for variables
- No additional data structures that grow with input size

**Pros:**
- Simple and intuitive algorithm
- Efficient single-pass solution
- Easy to understand and implement
- Handles all edge cases naturally

**Cons:**
- Requires understanding of the Excel column numbering system
- Potential integer overflow for very long strings (though constraints prevent this)

**Alternative Approaches:**
1. **Right-to-left with explicit powers:** More intuitive but requires calculating powers
2. **Recursive approach:** More complex, not recommended for this problem

**Key Insights:**
- This is essentially base-26 conversion with 1-indexing instead of 0-indexing
- The mathematical formula: each character contributes (char_value) × 26^(position_from_right)
- Left-to-right processing with `result = result × 26 + char_value` is the most elegant approach
