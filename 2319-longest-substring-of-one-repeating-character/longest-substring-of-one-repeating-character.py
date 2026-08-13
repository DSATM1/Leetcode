class SegmentTree:

  def __init__(self, s: str):
    self.n = len(s)
    self.s = list(s)

    # Segment tree arrays
    self.max_len = [0] * (4 * self.n)
    self.prefix_len = [0] * (4 * self.n)
    self.suffix_len = [0] * (4 * self.n)
    self.left_char = [''] * (4 * self.n)
    self.right_char = [''] * (4 * self.n)

    self._build(1, 0, self.n - 1)

  def _merge(self, node: int, l: int, mid: int, r: int):
    left_child = 2 * node
    right_child = 2 * node + 1

    left_size = mid - l + 1
    right_size = r - mid

    self.left_char[node] = self.left_char[left_child]
    self.right_char[node] = self.right_char[right_child]

    # Base max length from children
    self.max_len[node] = max(
        self.max_len[left_child], self.max_len[right_child]
    )

    # Base prefix/suffix lengths
    self.prefix_len[node] = self.prefix_len[left_child]
    self.suffix_len[node] = self.suffix_len[right_child]

    # If middle characters match, cross-boundary substrings can form
    if self.right_char[left_child] == self.left_char[right_child]:
      cross_len = self.suffix_len[left_child] + self.prefix_len[right_child]
      self.max_len[node] = max(self.max_len[node], cross_len)

      # Extend prefix length if entire left child segment is uniform
      if self.prefix_len[left_child] == left_size:
        self.prefix_len[node] = (
            left_size + self.prefix_len[right_child]
        )

      # Extend suffix length if entire right child segment is uniform
      if self.suffix_len[right_child] == right_size:
        self.suffix_len[node] = (
            right_size + self.suffix_len[left_child]
        )

  def _build(self, node: int, l: int, r: int):
    if l == r:
      c = self.s[l]
      self.max_len[node] = 1
      self.prefix_len[node] = 1
      self.suffix_len[node] = 1
      self.left_char[node] = c
      self.right_char[node] = c
      return

    mid = (l + r) // 2
    self._build(2 * node, l, mid)
    self._build(2 * node + 1, mid + 1, r)
    self._merge(node, l, mid, r)

  def update(self, node: int, l: int, r: int, idx: int, char: str):
    if l == r:
      self.s[idx] = char
      self.left_char[node] = char
      self.right_char[node] = char
      return

    mid = (l + r) // 2
    if idx <= mid:
      self.update(2 * node, l, mid, idx, char)
    else:
      self.update(2 * node + 1, mid + 1, r, idx, char)

    self._merge(node, l, mid, r)


class Solution:

  def longestRepeating(
      self, s: str, queryCharacters: str, queryIndices: list[int]
  ) -> list[int]:
    st = SegmentTree(s)
    ans = []

    for char, idx in zip(queryCharacters, queryIndices):
      st.update(1, 0, st.n - 1, idx, char)
      ans.append(st.max_len[1])

    return ans