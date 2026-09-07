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
