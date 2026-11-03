#!/usr/bin/env python3
"""Day 5 code-along: Recall & Practice. Run: python3 <file> or ./<file>"""

grid = [[1,2],[3,4],[5,6]]
total = 0 
#print(grid)
for row in grid 
    for value in row 
            if value % 2 == 0:
                  total += value
print(total)
# ===== 1. Loop + Conditional + Function, Together =====

# Count how many scores pass a threshold of 70. Here the answer is 3.
print('----- 1. Loop + Conditional + Function, Together -----')
# TODO: define count_passing(scores, threshold)
# TODO: return how many scores are >= threshold
# scores are >= threshold

def count_passing(scores, threshold):
      count = 0 
      for val in scores:
            if val >= threshold
            count += 1


# TODO: call it with [55, 82, 91, 40, 76] and 70; print the result
# print the result
print(count_passing([55, 82, 91, 40, 76])