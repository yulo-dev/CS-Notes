from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}  # Union-Find parent pointer for each email
        email_to_name = {}  # Map each email to the corresponding user's name

        # Find operation with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Compress the path while finding the root
            return parent[x]

        # Union operation: connect the root of x to the root of y
        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Build Union-Find structure
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email  # Initialize parent
                union(first_email, email)  # Union all emails in the same account
                email_to_name[email] = name  # Save the name for each email

        # Step 2: Group emails by their root parent
        unions = defaultdict(list)
        for email in parent:
            root = find(email)  # Find the ultimate root of this email
            unions[root].append(email)

        # Step 3: Build the final result
        result = []
        for root, emails in unions.items():
            # Get the user's name from any email in the group
            name = email_to_name[root]  
            result.append([name] + sorted(emails))  # Sort emails for consistent output

        return result
