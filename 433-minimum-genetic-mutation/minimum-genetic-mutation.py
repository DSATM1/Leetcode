from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        
        # If the end gene is not in the bank, it's impossible to reach
        if endGene not in bank_set:
            return -1
            
        # Queue stores tuples of (current_gene, number_of_mutations)
        queue = deque([(startGene, 0)])
        
        while queue:
            curr_gene, mutations = queue.popleft()
            
            # If we reach the target, return the number of steps taken
            if curr_gene == endGene:
                return mutations
            
            # Check all possible single-character mutations
            for i in range(8):
                for char in 'ACGT':
                    if char != curr_gene[i]:
                        next_gene = curr_gene[:i] + char + curr_gene[i+1:]
                        
                        # If the valid mutation is in the bank, add it to the queue
                        if next_gene in bank_set:
                            queue.append((next_gene, mutations + 1))
                            # Remove from the set to avoid revisiting (acts as a visited set)
                            bank_set.remove(next_gene)
                            
        # If the queue empties and we never hit endGene, it's unreachable
        return -1