🔗 Link: Roman to Integer
💡 Difficulty: Easy
🛠️ Topics: Hash Table, Math, String

=======================================================================================
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Valuea
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

=======================================================================================

## UMPIRE Method:

### Understand
Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.

**Key Questions:**
- How do we handle the subtraction cases (IV, IX, XL, XC, CD, CM)? We need to recognize when a smaller numeral precedes a larger one
- Are there any invalid inputs to handle? No, the problem guarantees valid roman numerals
- What's the maximum value we need to handle? Up to 3999 (MMMCMXCIX)
- Should we consider case sensitivity? No, problem specifies only uppercase letters

**Test Cases:**
- Happy path: "LVIII" → 58 (L=50, V=5, III=3)
- Subtraction cases: "IV" → 4, "IX" → 9, "XL" → 40, "XC" → 90, "CD" → 400, "CM" → 900
- Complex case: "MCMXCIV" → 1994 (M=1000, CM=900, XC=90, IV=4)
- Single character: "V" → 5
- Repeated characters: "III" → 3

**Time/Space Requirements:**
- Time: O(N) where N is the length of the string
- Space: O(1) constant space for the symbol mapping

**Key Insight:**
The main challenge is recognizing when to subtract vs add. If a smaller value appears before a larger value, we subtract; otherwise, we add.

### Match
See if this problem matches a problem category and strategies or patterns within the category.

**Pattern: Hash Table + String Processing**
- Use a hash table/dictionary to map Roman symbols to their integer values
- Process the string character by character
- Apply the subtraction rule when current character value < next character value

**Two Main Approaches:**
1. **Left-to-right with lookahead**: Check if current character should be subtracted
2. **Right-to-left processing**: Add if current >= previous, subtract if current < previous
3. **Substring matching**: Match 2-character substrings first, then single characters

### Plan
Sketch visualizations and write pseudocode.

**Visual Example for "MCMXCIV":**
```
M  C  M  X  C  I  V
↓  ↓  ↓  ↓  ↓  ↓  ↓
1000 + 900 + 90 + 4 = 1994
     CM    XC    IV
   (subtract) (subtract) (subtract)
```

**Algorithm (Left-to-right approach):**
1. Create a hash map for symbol values
2. Initialize result = 0
3. For each character from left to right:
   - If current value < next value: subtract current from result
   - Otherwise: add current to result
4. Return result

**Pseudocode:**
```
function romanToInt(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i from 0 to length(s) - 1:
        current_val = values[s[i]]
        
        if i < length(s) - 1 and current_val < values[s[i + 1]]:
            result -= current_val  // Subtraction case
        else:
            result += current_val  // Addition case
    
    return result
```

### Implement
Implement the solution (make sure to know what level of detail the interviewer wants).

**Approach 1: Left-to-right with lookahead**
```python
def romanToInt(self, s: str) -> int:
    # Create mapping of roman symbols to integers
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    n = len(s)
    
    for i in range(n):
        current_val = roman_map[s[i]]
        
        # Check if we need to subtract (current < next)
        if i < n - 1 and current_val < roman_map[s[i + 1]]:
            result -= current_val
        else:
            result += current_val
    
    return result
```

**Approach 2: Right-to-left processing**
```python
def romanToInt(self, s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    result = 0
    prev_val = 0
    
    # Process from right to left
    for i in range(len(s) - 1, -1, -1):
        current_val = roman_map[s[i]]
        
        if current_val < prev_val:
            result -= current_val  # Subtraction case
        else:
            result += current_val  # Addition case
            
        prev_val = current_val
    
    return result
```

**Approach 3: Substring matching (most explicit)**
```python
def romanToInt(self, s: str) -> int:
    # Include both single and double character mappings
    roman_map = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }
    
    result = 0
    i = 0
    
    while i < len(s):
        # Try to match 2-character substring first
        if i + 1 < len(s) and s[i:i+2] in roman_map:
            result += roman_map[s[i:i+2]]
            i += 2
        else:
            # Match single character
            result += roman_map[s[i]]
            i += 1
    
    return result
```

### Review
Re-check that your algorithm solves the problem by running through important examples.

**Trace through "MCMXCIV" (Approach 1):**
- i=0: M(1000), next=C(100), 1000 >= 100 → result = 1000
- i=1: C(100), next=M(1000), 100 < 1000 → result = 1000 - 100 = 900
- i=2: M(1000), next=X(10), 1000 >= 10 → result = 900 + 1000 = 1900
- i=3: X(10), next=C(100), 10 < 100 → result = 1900 - 10 = 1890
- i=4: C(100), next=I(1), 100 >= 1 → result = 1890 + 100 = 1990
- i=5: I(1), next=V(5), 1 < 5 → result = 1990 - 1 = 1989
- i=6: V(5), no next → result = 1989 + 5 = 1994 ✓

**Trace through "IV" (Approach 1):**
- i=0: I(1), next=V(5), 1 < 5 → result = -1
- i=1: V(5), no next → result = -1 + 5 = 4 ✓

**Edge Cases:**
- "III": 1 + 1 + 1 = 3 ✓
- "V": 5 ✓
- "LVIII": 50 + 5 + 1 + 1 + 1 = 58 ✓

### Evaluate
Finish by giving space and run-time complexity.

**Time Complexity: O(N)**
- Where N is the length of the input string
- We process each character exactly once
- Hash map lookups are O(1)

**Space Complexity: O(1)**
- We use a fixed-size hash map (7 or 13 entries depending on approach)
- No additional data structures that grow with input size

**Approach Comparison:**

| Approach | Pros | Cons |
|----------|------|------|
| Left-to-right | Intuitive, single pass | Requires lookahead logic |
| Right-to-left | Clean logic, no boundary checks | Less intuitive direction |
| Substring matching | Most explicit about rules | Slightly more complex implementation |

**Pros:**
- Simple and efficient algorithm
- Easy to understand and implement
- Handles all Roman numeral rules correctly
- Single pass through the string

**Cons:**
- Requires knowledge of Roman numeral rules
- Hash map approach uses extra space (though constant)

**Key Insights:**
- The core insight is recognizing when to subtract vs add based on character comparison
- All three approaches have the same time complexity but different code clarity
- The substring matching approach is most explicit about the Roman numeral rules
- Left-to-right approach is most commonly used in interviews due to its intuitive nature

**Interview Tips:**
- Start with the left-to-right approach as it's most intuitive
- Explain the subtraction rule clearly before coding
- Consider asking which approach the interviewer prefers
- Test with both simple (IV) and complex (MCMXCIV) examples
