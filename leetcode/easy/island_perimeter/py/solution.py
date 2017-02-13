class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def countNeighbors(grid, i, j):
            top    = max(0, i - 1)
            bottom = min(len(grid) - 1, i + 1)
            
            left   = max(0, j - 1)
            right  = min(len(grid[0]) - 1, j + 1)

            count  = 0

            for row in range(top, bottom + 1):
                if row != i:
                    if grid[row][j] > 0:
                        count += 1

            for col in range(left, right + 1):
                if col != j:
                    if grid[i][col] > 0:
                        count += 1

            return count

        SIDE_COUNT  = 4
        SIDE_LENGTH = 1        
        perim       = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    perim += SIDE_COUNT * SIDE_LENGTH - countNeighbors(grid, row, col)

        return perim
