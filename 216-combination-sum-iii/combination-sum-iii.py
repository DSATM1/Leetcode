class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, target: int, path: list):
            # Base case: valid combination found
            if len(path) == k:
                if target == 0:
                    res.append(path[:])
                return

            # Explore numbers from 'start' to 9
            for i in range(start, 10):
                # Pruning: if current number exceeds target, larger numbers will too
                if i > target:
                    break
                
                path.append(i)
                backtrack(i + 1, target - i, path)
                path.pop()

        backtrack(1, n, [])
        return res