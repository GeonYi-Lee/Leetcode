class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            num_list = []
            for j in board[i]:
                if j != '.':
                    if j in num_list:
                        return False
                        break
                    else:
                        num_list.append(j)
                else:
                    continue
        
        
        for i in range(9):
            num_list = []
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in num_list:
                        return False
                        break
                    else:
                        num_list.append(board[j][i])
                else:
                    continue
        

        for a in range(3):
            for b in range(3):
                num_list = []
                for i in range(3):
                    for j in range(3):
                        if board[3*a+i][3*b+j] != '.':
                            if board[3*a+i][3*b+j] in num_list:
                                return False
                                break
                            else:
                                num_list.append(board[3*a+i][3*b+j])
                        else:
                            continue

        return True



        