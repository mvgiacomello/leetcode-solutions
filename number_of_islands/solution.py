from typing import List


class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    """
    tags: dict
    count: int

    def num_islands(self, grid: List[List[str]]) -> int:
        """
        Solves the problem
        :param grid: a grid of representing a map
        :return: the amount of islands
        """
        # Edge case
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        # Clear
        self.tags = {}
        self.count = 0

        self.grid = grid
        self.max_line = len(grid)
        self.max_row = len(grid[0])

        # Rest
        for line in range(self.max_line):
            for row in range(self.max_row):
                if grid[line][row] == '1' and (line, row) not in self.tags:
                    self.count += 1
                    self.flag_island(line, row)
        return self.count

    def flag_island(self, line, row):
        """
        Walks through the island and marks it in the dictionary
        :param line: start node line
        :param row: start node row
        """
        # Center
        self.tags[(line, row)] = True
        # Left
        if line - 1 >= 0 and self.grid[line - 1][row] == '1' and (line - 1, row) not in self.tags:
            self.flag_island(line - 1, row)
        # Right
        if line + 1 < self.max_line and self.grid[line + 1][row] == '1' and (line + 1, row) not in self.tags:
            self.flag_island(line + 1, row)
        # Down
        if row - 1 >= 0 and self.grid[line][row - 1] == '1' and (line, row - 1) not in self.tags:
            self.flag_island(line, row - 1)
        # Up
        if row + 1 < self.max_row and self.grid[line][row + 1] == '1' and (line, row + 1) not in self.tags:
            self.flag_island(line, row + 1)
