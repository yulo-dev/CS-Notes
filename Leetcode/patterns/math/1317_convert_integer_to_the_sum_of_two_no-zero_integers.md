🔗 Link: Convert Integer to the Sum of Two No-Zero Integers
💡 Difficulty: Easy
🛠️ Topics: Math, Brute Force

=======================================================================================
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:
- a and b are No-Zero integers.
- a + b = n

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

Example 1:
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1. Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9. Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

Example 3:
Input: n = 10000
Output: [1,9999]
Explanation: [1,9999] is also valid.

Constraints:
- 2 <= n <= 10^4

=======================================================================================

## UMPIRE Method:

### Understand
Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.

**Key Questions:**
- What defines a "No-Zero integer"? Any positive integer without the digit '0' in its decimal representation
- Can we return any valid solution? Yes, if multiple solutions exist, we can return any of them
- Are both numbers required to be positive? Yes, No-Zero integers are defined as positive
- What's the range of input? n is between 2 and 10,000

**Test Cases:**
- Simple case: n = 2 → [1,1] (only valid solution)
- Multiple solutions: n = 11 → [2,9], [3,8], [4,7], [5,6], [8,3], [9,2] (many valid)
- Contains zero: n = 10 → [1,9], [2,8], [3,7], [4,6] (cannot use 10, 20, 30, etc.)
- Edge case: n = 100 → [1,99], [2,98], etc. (cannot use numbers containing 0)
- Larger number: n = 1111 → [1,1110] is invalid (1110 contains 0), need [1111,0] invalid, try [2,1109], etc.

**Time/Space Requirements:**
- Time: O(n * d) where d is average number of digits (for string conversion and checking)
- Space: O(d) for string conversion during checking
- Can we do better? Since we're guaranteed a solution exists, brute force is acceptable

### Match
See if this problem matches a problem category and strategies or patterns within the category.

**Pattern: Brute Force Search**
- Simple iteration through possible values of first number
- For each candidate a, calculate b = n - a
- Check if both a and b contain no zeros
- Return the first valid pair found

**Key Insight:**
Since we're guaranteed that a solution exists and we can return any valid solution, we can use a simple brute force approach starting from a = 1.

**Alternative Patterns:**
- **Math optimization**: Could try to construct no-zero numbers directly, but more complex
- **Two pointers**: Not applicable here since we're looking for sum, not searching sorted array

### Plan
Sketch visualizations and write pseudocode.

**Visual Example for n = 11:**
```
a = 1, b = 10 → Check: 1 (✓), 10 (✗ contains 0)
a = 2, b = 9  → Check: 2 (✓), 9 (✓) → Return [2,9]
```

**Algorithm:**
1. Create a helper function to check if a number contains zero
2. Start with a = 1
3. While a < n:
   - Calculate b = n - a
   - Check if both a and b are no-zero integers
   - If yes, return [a, b]
   - Otherwise, increment a and continue
4. Since solution is guaranteed, we'll find one before a >= n

**Helper Function (Check No-Zero):**
```
function hasNoZero(num):
    return '0' not in str(num)
```

**Pseudocode:**
```
function getNoZeroIntegers(n):
    for a from 1 to n-1:
        b = n - a
        if hasNoZero(a) and hasNoZero(b):
            return [a, b]
    
    // This should never be reached given problem constraints
    return []
```

### Implement
Implement the solution (make sure to know what level of detail the interviewer wants).

**Approach 1: String-based zero checking**
```python
def getNoZeroIntegers(self, n: int) -> List[int]:
    def hasNoZero(num):
        return '0' not in str(num)
    
    for a in range(1, n):
        b = n - a
        if hasNoZero(a) and hasNoZero(b):
            return [a, b]
    
    # Should never reach here given problem constraints
    return []
```

**Approach 2: Mathematical zero checking (more efficient)**
```python
def getNoZeroIntegers(self, n: int) -> List[int]:
    def hasNoZero(num):
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10
        return True
    
    for a in range(1, n):
        b = n - a
        if hasNoZero(a) and hasNoZero(b):
            return [a, b]
    
    return []
```

**Approach 3: Optimized with early termination**
```python
def getNoZeroIntegers(self, n: int) -> List[int]:
    def hasNoZero(num):
        return '0' not in str(num)
    
    # Start from 1 and go up to n//2 + 1 for slight optimization
    for a in range(1, n // 2 + 2):
        b = n - a
        if hasNoZero(a) and hasNoZero(b):
            return [a, b]
    
    return []
```

**Java Implementation:**
```java
public int[] getNoZeroIntegers(int n) {
    for (int a = 1; a < n; a++) {
        int b = n - a;
        if (hasNoZero(a) && hasNoZero(b)) {
            return new int[]{a, b};
        }
    }
    return new int[0]; // Should never reach here
}

private boolean hasNoZero(int num) {
    while (num > 0) {
        if (num % 10 == 0) {
            return false;
        }
        num /= 10;
    }
    return true;
}
```

### Review
Re-check that your algorithm solves the problem by running through important examples.

**Trace through n = 11:**
- a=1, b=10: hasNoZero(1)=true, hasNoZero(10)=false → continue
- a=2, b=9: hasNoZero(2)=true, hasNoZero(9)=true → return [2,9] ✓

**Trace through n = 10:**
- a=1, b=9: hasNoZero(1)=true, hasNoZero(9)=true → return [1,9] ✓

**Trace through n = 100:**
- a=1, b=99: hasNoZero(1)=true, hasNoZero(99)=true → return [1,99] ✓

**Edge Cases:**
- n=2: a=1, b=1 → both valid → return [1,1] ✓
- n=1001: Need to check systematically, but guaranteed solution exists ✓

**hasNoZero Function Test:**
- hasNoZero(123) = true ✓
- hasNoZero(102) = false ✓
- hasNoZero(1000) = false ✓
- hasNoZero(9999) = true ✓

### Evaluate
Finish by giving space and run-time complexity.

**Time Complexity: O(n * d)**
- Where n is the input number and d is the average number of digits
- In the worst case, we might iterate through all values from 1 to n-1
- For each iteration, we check if both numbers contain zero, which takes O(d) time
- Since d ≤ log₁₀(n), this is effectively O(n * log n)
- In practice, most test cases will find a solution very quickly

**Space Complexity:**
- **String approach**: O(d) for string conversion during zero checking
- **Mathematical approach**: O(1) constant space
- Overall: O(1) if we use mathematical approach, O(log n) for string approach

**Performance Analysis:**
- **Best case**: O(1) - when n = 2, immediately return [1,1]
- **Average case**: O(1) to O(log n) - most inputs have solutions with small values of a
- **Worst case**: O(n * log n) - though this is rare given problem constraints

**Pros:**
- Simple and intuitive algorithm
- Easy to understand and implement
- Guaranteed to find a solution (problem constraint)
- Multiple valid implementations (string vs mathematical)

**Cons:**
- Brute force approach, not the most efficient theoretically
- Could be slow for very large inputs (though constraints limit this)

**Optimization Opportunities:**
1. **Early termination**: Stop at n//2 + 1 since we only need one solution
2. **Mathematical checking**: Avoid string conversion overhead
3. **Smart starting point**: Could analyze patterns in no-zero numbers

**Key Insights:**
- The problem guarantees a solution exists, making brute force viable
- String-based zero checking is more readable but slightly less efficient
- Mathematical zero checking avoids string conversion overhead
- Most real inputs will have solutions with small values, making average case very fast
- The constraint n ≤ 10⁴ makes even worst-case performance acceptable

**Interview Tips:**
- Start with the string-based approach for clarity
- Mention the mathematical alternative for efficiency
- Explain why brute force is acceptable here (guaranteed solution + small constraints)
- Consider discussing the early termination optimization
- Test with edge cases like n=2 and numbers containing zeros
