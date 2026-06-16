class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # n=len(board)
        # #row
        # for row in range(9):
        #     seen=set()
        #     for j in range(9):
        #         if board[row][j]=='.':
        #             continue
        #         if board[row][j] in seen:
        #             return False
        #         seen.add(board[row][j])
        # #col
        # for col in range(9):
        #     seen=set()
        #     for i in range(9):                     
        #         if board[i][col]=='.':
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])
        # #sq
        # for sq in range(9):
        #     seen=set()
        #     for i in range(3):        
        #         for j in range(3):
        #             row=(sq//3)*3+i
        #             col=(sq%3)*3+j
        #             if board[row][col]=='.':
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True   

        rowdic=defaultdict(set)         
        coldic=defaultdict(set)         
        sqdic=defaultdict(set)       

        for row in range(9):  
            for col in range(9):
                if board[row][col]=='.':
                    continue
                if (board[row][col] in rowdic[row] or board[row][col] in coldic[col] or board[row][col] in sqdic[(row//3,col//3)]):
                    return False
                rowdic[row].add(board[row][col])
                coldic[col].add(board[row][col])
                sqdic[(row//3,col//3)].add(board[row][col])
        return True  
        
              
                    




