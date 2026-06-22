from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        verdict = True

        for i in range(9):
            row = []
            for j in range(9):
                row.append(board[i][j])
            count = 0
            nums = set()

            for k in range(len(row)):
                if row[k] != ".":
                    nums.add(row[k])
                    count += 1

            if count > len(nums):
                verdict = False

        for i in range(9):
            row = []
            for j in range(9):
                row.append(board[j][i])

            count = 0
            nums = set()

            for k in range(len(row)):
                if row[k] != ".":
                    nums.add(row[k])
                    count += 1

            if count > len(nums):
                verdict = False 


        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                box_id = (r//3, c//3)

                curr_val = board[r][c]
                if curr_val != ".":
                    if curr_val in boxes[box_id]:
                        verdict = False
                        return False
                    boxes[box_id].add(curr_val)
        return verdict


