# LeetCode Solutions
🔥 22 Days Streak | 44 Problems Solved

## 📊 About
Migrating from Java to Python. Focused on consistency.

## ✅ Day 22 - Latest

### 22. Generate Parentheses (Medium)
- **Approach:** Backtracking
- **Condition 1:** `open < n` → add `(`
- **Condition 2:** `close < open` → add `)`
- **Code:** `Python/022_Generate_Parentheses.py`

```python
class Solution:
    def generateParenthesis(self, n):
        res = []
        def backtrack(curr, open_c, close_c):
            if len(curr) == 2 * n:
                res.append(curr)
                return
            if open_c < n:
                backtrack(curr + "(", open_c + 1, close_c)
            if close_c < open_c:
                backtrack(curr + ")", open_c, close_c + 1)
        backtrack("", 0, 0)
        return res

# LeetCode - 140 Solved | Day 22 Streak

Python migration from Java.

### Day 22: 22. Generate Parentheses
- Backtracking: `open < n` and `close < open`
- File: `Python/022_Generate_Parentheses.py`

Total: 140 Problems
Streak: 22 Days 🔥

### LeetCode Profile
https://leetcode.com/u/Pavithra4341/

