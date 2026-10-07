class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(i, j, word, visited):
            #check indices or if not visited
            if len(word) == 0:
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and [i,j] not in visited and board[i][j] == word[0]:
                visited.append([i,j])
                word = word[1:]
                chud= check(i+1, j, word, visited) or check(i, j+1, word, visited) or check(i, j-1, word, visited) or check(i-1, j, word, visited) 
                visited.remove([i,j])
                return chud
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if check(i, j, word, []):
                    return True
        return False

        


    #             if board[i][j] == word[0]:
    #                 c = board[i][j]
    #                 board[i][j] = ""
    #                 if self.check(board, i, j, word[1:]):
    #                     return True
                    
    #                 board[i][j] = c
    #     return False

    # def check(self, board, i, j, word):
    #     print(board, i, j, word)
    #     if len(word) == 0:
    #         return True
    #     if i-1 >= 0 and board[i-1][j] == word[0]:
    #         board[i-1][j] = ""
    #         if self.check(board, i-1, j, word[1:]):
    #             return True
    #     if j-1 >= 0 and board[i][j-1] == word[0]:
    #         board[i][j-1] = ""
    #         if self.check(board, i, j-1, word[1:]):
    #             return True
    #     if i+1 < len(board) and board[i+1][j] == word[0]:
    #         board[i+1][j] = ""
    #         if self.check(board, i+1, j, word[1:]):
    #             return True
    #     if j+1 < len(board[0]) and board[i][j+1] == word[0]:
    #         board[i][j+1] = ""
    #         if self.check(board, i, j+1, word[1:]):
    #             return True
    #     return False
    

        