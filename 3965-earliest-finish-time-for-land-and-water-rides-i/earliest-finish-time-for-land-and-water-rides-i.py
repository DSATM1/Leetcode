class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        # 1. Find the earliest time we can finish a single land ride or water ride
        min_land_finish = min(s + d for s, d in zip(landStartTime, landDuration))
        min_water_finish = min(s + d for s, d in zip(waterStartTime, waterDuration))
        
        # 2. Scenario A: Land -> Water
        # After finishing the best land ride, pick the water ride that finishes earliest
        land_then_water = min(
            max(min_land_finish, ws) + wd 
            for ws, wd in zip(waterStartTime, waterDuration)
        )
        
        # 3. Scenario B: Water -> Land
        # After finishing the best water ride, pick the land ride that finishes earliest
        water_then_land = min(
            max(min_water_finish, ls) + ld 
            for ls, ld in zip(landStartTime, landDuration)
        )
        
        return min(land_then_water, water_then_land)