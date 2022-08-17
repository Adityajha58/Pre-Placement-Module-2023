class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        top = -1
        bottom = len(board)
        rowstart = -1
        rowend = len(board[0])
        def traverse(a, b, index, visited):
            if index == len(word):
                return True
            if a == top or a == bottom or b == rowstart or b == rowend:
                return False
            if board[a][b] != word[index]:
                return False
            if [a,b] in visited:
                return False
            visited.append([a,b])
            if (
                traverse(a+1, b, index+1, visited)
                or
                traverse(a, b+1, index+1, visited)
                or
                traverse(a-1, b, index+1, visited)
                or
                traverse(a, b-1, index+1, visited)
            ):
                return True
            else:
                visited.pop()
                return False
        for c in range(0, len(board)):
            for d in range(0, len(board[0])):
                if board[c][d] == word[0]:
                    if traverse(c,d,0,[]) == True:
                        return True
        return False