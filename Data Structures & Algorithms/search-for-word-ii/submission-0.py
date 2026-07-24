class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        res = set()

        def dfs(r,c,node, wordsofar):
            ## Base case:
            

            if (r < 0 or c < 0 or c >=COLS or r >= ROWS or board[r][c] not in node.children or (r,c) in visit):
                return 
        
            visit.add((r,c))
            node = node.children[board[r][c]]
            wordsofar += board[r][c]
            if node.endOfWord:
                res.append(wordsofar)

            dfs(r+1,c,node,wordsofar) 
            dfs(r-1,c,node,wordsofar)
            dfs(r,c+1,node,wordsofar)
            dfs(r,c-1,node,wordsofar)
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root, "")
        return list(res)
            




        
