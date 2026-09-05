# 🔢 Two Sum

[![LeetCode](https://img.shields.io/badge/LeetCode-1-orange?logo=leetcode)](https://leetcode.com/problems/two-sum/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)](https://leetcode.com/problems/two-sum/)
[![Language](https://img.shields.io/badge/Language-Python-blue?logo=python)](https://www.python.org/)

## 📌 Problem

Given an integer array `nums` and an integer `target`, return the **indices of the two numbers** whose sum equals `target`.

### Example

```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

Because `nums[0] + nums[1] = 2 + 7 = 9`.

### Constraints

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Exactly one valid answer exists.
- The same element cannot be used twice.

---

## 💡 Approach: Hash Map

A brute-force solution checks every possible pair, which takes **O(n²)** time.

Instead, this solution uses a **dictionary (hash map)** to remember numbers that have already been visited.

For every element:

1. Calculate the required number:
   `remainder = target - nums[i]`
2. Check whether that remainder already exists in the dictionary.
3. If it exists, we have found the required pair and return their indices.
4. Otherwise, store the current number and its index in the dictionary.

### 🔍 Quick Trace

For `nums = [2, 7, 11, 15]` and `target = 9`:

| Index | Value | Required (`target - value`) | Dictionary | Result |
|---:|---:|---:|---|---|
| 0 | 2 | 7 | `{}` | Store `2: 0` |
| 1 | 7 | 2 | `{2: 0}` | Found `2` → `[0, 1]` |

The key idea is that instead of searching the array again for the required number, the dictionary lets us check for it efficiently.

---

## 🧑‍💻 Solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}

        for i in range(n):
            rem = target - nums[i]

            if rem in dict1:
                return [dict1[rem], i]

            dict1[nums[i]] = i
```

---

## ⏱️ Complexity

| Complexity | Analysis |
|---|---|
| **Time** | `O(n)` — one pass through the array |
| **Space** | `O(n)` — dictionary stores visited elements |

---

## 🧠 What I Learned

- Array traversal using a `for` loop
- Using a **Hash Map / Dictionary** for fast lookup
- Finding a complement using `target - current_value`
- Returning indices instead of values
- Improving a brute-force `O(n²)` approach to `O(n)`
- Understanding the **time vs. space trade-off** in DSA

---

## 🔗 Resources

- [LeetCode — Two Sum](https://leetcode.com/problems/two-sum/)
- [Solution Code](./two-sum.py)

> 🚀 Part of my ongoing **DSA learning and LeetCode practice**. Solving problems consistently to strengthen problem-solving skills and build a strong foundation for Software Engineering.