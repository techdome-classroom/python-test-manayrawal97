import unittest
from program1 import Solution

def count_islands(grid):
  rows, cols = len(grid), len(grid[0])
  islands = 0

  def dfs(row, col):
    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 'L':
      grid[row][col] = 'V' 
      for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
        dfs(row + dr, col + dc)
  
  for row in range(rows):
    for col in range(cols):
      if grid[row][col] == 'L':
        islands += 1
        dfs(row, col)
  
  return islands

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        result = self.solution.getTotalIsles([["L","L","L","L","W"],["L","L","W","L","W"],["L","L","W","W","W"],["W","W","W","W","W"]])
        self.assertEqual(result, 1)

    def test_case2(self):
        result = self.solution.getTotalIsles([["L","L","W","W","W"],["L","L","W","W","W"],["W","W","L","W","W"],["W","W","W","L","L"]])
        self.assertEqual(result, 3)

    def test_case3(self):
        result = self.solution.getTotalIsles([["W", "W", "W", "W"], ["W", "L", "L", "W"], ["W", "L", "L", "W"], ["W", "W", "W", "W"]])
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
