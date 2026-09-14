class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Check if either rectangle is actually a line/point (area is 0)
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
            
        # Return False if they do NOT overlap, True otherwise
        return not (rec1[2] <= rec2[0] or  # rec1 is left of rec2
                    rec1[0] >= rec2[2] or  # rec1 is right of rec2
                    rec1[3] <= rec2[1] or  # rec1 is below rec2
                    rec1[1] >= rec2[3])    # rec1 is above rec2