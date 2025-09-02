# Serialize and Deserialize Binary Tree Template

## Core Data Structure

```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val, self.left, self.right = val, left, right

from collections import deque

NULL = "null"  # ← 若想用 '#', 改成 NULL = "#"

class Codec:
    def serialize(self, root):
        if not root:            # 1) 空樹
            return "[]"

        q = deque([root])       # 2) 用 deque 當 queue 做層序
        out = []                #    這裡存輸出的字串片段

        while q:                # 3) 標準 BFS
            node = q.popleft()
            if node:            # 4) 有節點：記值、把左右子入隊
                out.append(str(node.val))
                q.append(node.left)     # 即使是 None 也要入隊
                q.append(node.right)    # 目的：保留樹形狀
            else:                       # 5) 空位：用占位符表示
                out.append(NULL)

        # 6) 去掉尾端多餘的 "null"
        while out and out[-1] == NULL:
            out.pop()

        return "[" + ",".join(out) + ']'   # 7) 拼成 LeetCode 風格字串

    def deserialize(self, data):
        data = data.strip()
        if data == "[]":    # 1) 空樹
            return None

        vals = data[1:-1].split(',')   # 2) 去掉 [ ]，切成字串陣列
        root = TreeNode(int(vals[0]))  # 3) 第 1 個值是根
        q = deque([root])              # 4) 佇列保存「待補孩子」的父節點
        i = 1                          # 5) 指向下一個要讀的欄位

        while q and i < len(vals):     # 6) 一次處理一個父節點，消耗最多兩個欄位
            cur = q.popleft()

            # —— 左孩子 ——
            if vals[i] != "null":       # "null"/"#" 代表空位
                cur.left = TreeNode(int(vals[i]))
                q.append(cur.left)      # 新子節點未來也要補它的孩子
            i += 1
            # —— 右孩子 ——
            if i < len(vals) and vals[i] != "null":
                cur.right = TreeNode(int(vals[i]))
                q.append(cur.right)
            i += 1
        return root
```

## Key Patterns to Remember

### Serialize (7 Steps):
1. **空樹檢查** - `if not root: return "[]"`
2. **初始化queue** - `q = deque([root])`
3. **標準BFS** - `while q:`
4. **記錄節點值** - `out.append(str(node.val))`
5. **入隊子節點** - 包括 None 也要入隊保持結構
6. **清理尾端null** - `while out and out[-1] == NULL: out.pop()`
7. **組合字串** - `"[" + ",".join(out) + ']'`

### Deserialize (6 Steps):
1. **空樹檢查** - `if data == "[]": return None`
2. **解析字串** - `vals = data[1:-1].split(',')`
3. **建立根節點** - `root = TreeNode(int(vals[0]))`
4. **初始化queue** - 存放待補孩子的父節點
5. **索引控制** - `i = 1` 指向下個要處理的值
6. **BFS建樹** - 每次處理一個父節點，最多消耗兩個欄位

## Critical Pattern Points

- **NULL佔位符**: 用 "null" 表示空節點，保持樹結構
- **尾端清理**: Serialize時去掉多餘的 null (不一定需要)
- **索引控制**: Deserialize時用 i 追蹤當前處理位置
- **Queue管理**: 只把非空節點加入 deserialize 的 queue

## Review Problems
- **LeetCode 297**: Serialize and Deserialize Binary Tree (exact template match)
