class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        current_mass = mass
        for ast in asteroids:
            if current_mass >= ast:
                current_mass += ast
            else:
                return False
        return True