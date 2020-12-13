# Solution to Session 10 Problem 9
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 4, 2020

# Problems 9 and 10 are designed to be complementary. While Problem 10 focuses on BFS,
#     Problem 9 can be solved via DFS.
def num_contiguous(board, i, j, color):
    if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == color:
        # 'V' stands for "visited"
        board[i][j] = 'V'
        return 1 + num_contiguous(board, i + 1, j, color) + num_contiguous(board, i - 1, j, color) + \
               num_contiguous(board, i, j + 1, color) + num_contiguous(board, i, j - 1, color)

    return 0


def max_num_contiguous(board, color):
    ret_val = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == color:
                ret_val = max(ret_val, num_contiguous(board, i, j, color))
                
    return ret_val


input_file = open("blockd-input.txt", "r")
output_file = open("blockd-output.txt", "w")

color = str(input_file.readline().rstrip())
dimensions = input_file.readline()

board = [input_file.readline().split() for _ in range(int(dimensions[0]))]
output_file.write(str(max_num_contiguous(board, color)))

output_file.close()
input_file.close()
