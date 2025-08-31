# BFS vs DFS Decision Guide for Tree Problems

## ☀️ Opening Statement 

*"If the tree can be very deep or skewed, I'll choose iterative BFS to avoid recursion depth issues. If depth is bounded or the tree is roughly balanced, a concise recursive DFS is fine. Both give O(n) time; BFS uses O(w) space, DFS uses O(h) space."*

## ☀️ Algorithm Selection Questions for Interviewer

### 🎯 Tree Shape & Structural Concerns

**1. Tree Depth & Skewness**
- **Question:** *"Could the tree be highly skewed or very deep? If so I'll avoid recursion and use BFS."*
- **Follow-up:** *"That prevents stack-overflow risk while keeping O(n) time, O(w) space."*

**2. Constraints Clarification**
- **Question:** *"What are the upper bounds on node count and height?"*
- **Follow-up:** *"If height ≪ 1000 recursion is fine; otherwise I'll go iterative."*

**3. Worst-Case Optimization**
- **Question:** *"Should I optimize for worst-case skewed trees or typical balanced cases?"*
- **Follow-up:** *"Worst-case → BFS; balanced → recursive DFS is clean."*

### 🎯 Implementation Preferences

**4. Method Preference**
- **Question:** *"Do you prefer a recursive DFS or an iterative approach?"*
- **Follow-up:** *"I can implement both; DFS is concise, BFS is safest for depth."*

**5. Space Complexity Target**
- **Question:** *"Is O(w) auxiliary space acceptable, where w is the maximum level width?"*
- **Follow-up:** *"BFS uses O(w); recursive DFS uses O(h)."*

**6. Time/Space Trade-off**
- **Question:** *"Is O(n) time with O(h) or O(w) space the target?"*
- **Follow-up:** *"I'll justify the pick based on these bounds."*

### 🎯 Problem Requirements Analysis

**7. Level-Based Processing**
- **Question:** *"Do we need per-level stats (e.g., averages or grouping by level)?"*
- **Follow-up:** *"If yes, BFS with level-size tracking is straightforward."*

**8. Output Granularity**
- **Question:** *"Is the output purely the final result, or do we need level-by-level information?"*
- **Follow-up:** *"Pure result → DFS/BFS both fine; per-level → BFS fits better."*

### 🎯 Runtime Environment Considerations

**9. Recursion Limits**
- **Question:** *"Are there recursion depth limits in the runtime environment we should consider?"*
- **Follow-up:** *"If limits are tight, I'll do iterative BFS/DFS."*

**10. Numerical Constraints (if applicable)**
- **Question:** *"Any constraints on node values if we accumulate sums? I'll use 64-bit or Python int accordingly."*

## ☀️ Decision Matrix

| Factor | Favors BFS | Favors DFS | Notes |
|--------|------------|------------|--------|
| Tree Shape | Deep/Skewed trees | Balanced trees | Stack overflow risk |
| Problem Type | Level-order requirements | Structure comparison | Natural fit |
| Space Priority | O(w) acceptable | Need O(h) optimization | Width vs height |
| Implementation | Iterative preferred | Recursive preferred | Code style choice |
| Early Termination | Shortest path problems | Deep search problems | Algorithm efficiency |
