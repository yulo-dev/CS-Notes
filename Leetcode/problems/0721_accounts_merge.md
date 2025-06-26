## ☀️ Leetcode 721 - Accounts Merge

### ✨ Problem Summary:

Merge multiple accounts that may share common email addresses. Each account has a name and a list of emails. If two accounts share any email, they belong to the same person and should be merged.


### ☀️ Key Ideas:

- Use **Union Find** to group emails that belong to the same person
- Each email initially points to itself (self-parent)
- Perform `union` to group emails within the same account
- Use `find` with **path compression** to locate representative parent of each group
- Group all emails by their root, then format the output by retrieving names and sorting emails


### ☀️ Code with Comments:

```python
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}  # Union-Find parent
        email_to_name = {}  # Email to username mapping

        def find(x):
            # Path compression: make each node point directly to root
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # Connect x's root to y's root
            parent[find(x)] = find(y)

        # ☀️ Step 1: Initialize parent and perform unions
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        # ☀️ Step 2: Group emails by their root
        unions = defaultdict(list)
        for email in parent:
            root = find(email)
            unions[root].append(email)

        # ☀️ Step 3: Format output with name and sorted emails
        result = []
        for root, emails in unions.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result
```


### ☀️ Time Complexity:

- Step 1: Union operations for each email: **O(E \* α(E))** where α is inverse Ackermann
- Step 2: Grouping by root: **O(E \* α(E))**
- Step 3: Sorting emails in each group: **O(E log E)**
- ✨ Final: **O(E log E)** (dominated by sorting)

### ☀️ Space Complexity:

- **O(E)** for parent, email\_to\_name, unions


### ☀️ Notes to Remember:

- Step 1: Initialize parent = self; then union each email to first\_email in account
- Step 1: Path compression hasn't really occurred yet (only shallow linking)
- Step 2: Real path compression happens here when we group by root using `find`
- Step 3: Sort and format each group


### ☀️ Pattern:

- Union-Find (Disjoint Set Union)
- Graph Component Merging


### ☀️ 14 Patterns:

- ✅ Union-Find Pattern (Pattern 14)

