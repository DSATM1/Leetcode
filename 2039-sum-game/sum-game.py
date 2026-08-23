class Solution:

  def sumGame(self, num: str) -> bool:
    n = len(num)
    left_sum = 0
    right_sum = 0
    left_q = 0
    right_q = 0

    # Count digits and '?' for both halves
    for i in range(n // 2):
      if num[i] == "?":
        left_q += 1
      else:
        left_sum += int(num[i])

    for i in range(n // 2, n):
      if num[i] == "?":
        right_q += 1
      else:
        right_sum += int(num[i])

    # If the total number of '?' is odd, Alice always wins
    if (left_q + right_q) % 2 != 0:
      return True

    # Bob wins only if the initial sum difference equals the expected '?' offset
    # (left_sum - right_sum) + (left_q - right_q) * 4.5 == 0
    return (left_sum - right_sum) * 2 != (right_q - left_q) * 9