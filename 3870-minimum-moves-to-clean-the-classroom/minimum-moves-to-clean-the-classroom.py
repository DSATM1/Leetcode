from typing import List
import heapq

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start = None
        litters = []
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        num_litters = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        full_mask = (1 << num_litters) - 1
        
        start_mask = 0
        if start in litter_map:
            start_mask |= (1 << litter_map[start])
            
        # (steps, r, c, mask, current_energy)
        pq = [(0, start[0], start[1], start_mask, energy)]
        best_energy = {}
        
        while pq:
            steps, r, c, mask, e = heapq.heappop(pq)
            
            if mask == full_mask:
                return steps
                
            state_key = (r, c, mask)
            if best_energy.get(state_key, -1) >= e:
                continue
            best_energy[state_key] = e
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    if e <= 0:
                        continue
                        
                    ne = e - 1
                    
                    # If energy is 0 and it's not a reset cell, we can't step here
                    if ne == 0 and classroom[nr][nc] != 'R' and mask != full_mask:
                        # Wait, we can still step on it if it collects the last litter and completes the task!
                        # Let's check mask condition properly.
                        pass
                        
                    nmask = mask
                    if (nr, nc) in litter_map:
                        nmask |= (1 << litter_map[(nr, nc)])
                        
                    # If energy drops to 0, we can only survive if we land on 'R' or we just completed all litters
                    if ne < 0:
                        continue
                    if ne == 0 and classroom[nr][nc] != 'R' and nmask != full_mask:
                        continue
                        
                    next_energy = energy if classroom[nr][nc] == 'R' else ne
                    
                    next_state_key = (nr, nc, nmask)
                    if next_energy > best_energy.get(next_state_key, -1):
                        heapq.heappush(pq, (steps + 1, nr, nc, nmask, next_energy))
                        
        return -1