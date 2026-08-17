class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the angle of the minute hand from 12:00
        minute_angle = minutes * 6
        
        # Calculate the angle of the hour hand from 12:00
        # (hour % 12) maps 12 to 0 to align with the starting point
        hour_angle = (hour % 12) * 30 + (minutes * 0.5)
        
        # Find the absolute difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller of the two possible angles
        return min(angle, 360 - angle)
        