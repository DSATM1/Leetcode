class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primes = [2, 3, 5, 7]
        need = [0, 0, 0, 0]
        x = t
        for i, p in enumerate(primes):
            while x % p == 0:
                need[i] += 1
                x //= p
        if x != 1:
            return "-1"
        A, B, C, D = need

        contrib = {
            0: (0, 0, 0, 0),
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0),
        }

        ab_gains = [(1, 0), (2, 0), (3, 0), (1, 1), (0, 1), (0, 2)]  # digits 2,4,8,6,3,9
        INF = float('inf')
        minAB = [[INF] * (B + 1) for _ in range(A + 1)]
        minAB[0][0] = 0
        for a in range(A + 1):
            for b in range(B + 1):
                if a == 0 and b == 0:
                    continue
                best = INF
                for ga, gb in ab_gains:
                    pa, pb = max(0, a - ga), max(0, b - gb)
                    if minAB[pa][pb] + 1 < best:
                        best = minAB[pa][pb] + 1
                minAB[a][b] = best

        def min_digits(a, b, c, d):
            a = min(max(a, 0), A)
            b = min(max(b, 0), B)
            return minAB[a][b] + max(c, 0) + max(d, 0)

        def feasible(L, a, b, c, d):
            return min_digits(a, b, c, d) <= L

        def build_suffix(L, a, b, c, d):
            res = []
            ra, rb, rc, rd = a, b, c, d
            remaining = L
            for _ in range(L):
                remaining -= 1
                for digit in range(1, 10):
                    ca, cb, cc, cd = contrib[digit]
                    na, nb = max(0, ra - ca), max(0, rb - cb)
                    nc, nd = max(0, rc - cc), max(0, rd - cd)
                    if feasible(remaining, na, nb, nc, nd):
                        res.append(str(digit))
                        ra, rb, rc, rd = na, nb, nc, nd
                        break
            return "".join(res)

        n = len(num)
        digits = [int(ch) for ch in num]

        zero_idx = next((i for i, dg in enumerate(digits) if dg == 0), None)

        if zero_idx is None:
            ta = tb = tc = td = 0
            for dg in digits:
                ca, cb, cc, cd = contrib[dg]
                ta += ca; tb += cb; tc += cc; td += cd
            if ta >= A and tb >= B and tc >= C and td >= D:
                return num

        prefix = [(0, 0, 0, 0)] * (n + 1)
        pa = pb = pc = pd = 0
        for i in range(n):
            prefix[i] = (pa, pb, pc, pd)
            ca, cb, cc, cd = contrib[digits[i]]
            pa += ca; pb += cb; pc += cc; pd += cd
        prefix[n] = (pa, pb, pc, pd)

        start_pos = zero_idx if zero_idx is not None else n - 1
        found = None
        for pos in range(start_pos, -1, -1):
            pa_, pb_, pc_, pd_ = prefix[pos]
            for d_ in range(digits[pos] + 1, 10):
                ca, cb, cc, cd = contrib[d_]
                ra = A - (pa_ + ca)
                rb = B - (pb_ + cb)
                rc = C - (pc_ + cc)
                rd = D - (pd_ + cd)
                Lrem = n - pos - 1
                if feasible(Lrem, ra, rb, rc, rd):
                    suffix = build_suffix(Lrem, ra, rb, rc, rd)
                    found = "".join(str(digits[i]) for i in range(pos)) + str(d_) + suffix
                    break
            if found is not None:
                break

        if found is not None:
            return found

        length = n + 1
        while True:
            if feasible(length, A, B, C, D):
                return build_suffix(length, A, B, C, D)
            length += 1