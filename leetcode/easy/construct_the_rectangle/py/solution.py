class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        minDiff = -1
        rect    = [0, 0]
        
        for length in xrange(int(area ** 0.5), area + 1):
            width = area // length
            
            if length * width == area and length >= width:
                curDiff = abs(length - width)
                
                if minDiff < 0 or curDiff < minDiff:
                    minDiff = curDiff
                    rect    = [length, width]
                    break
            
        return rect
