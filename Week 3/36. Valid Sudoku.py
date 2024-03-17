class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        We solve the sudoku by checking the neccessary rules
            1. Check the elemnt with row index. 
            2. Check the element with col index.
            3. Check the subgrid.
        
        If the set length is same as original length, ie, we have no duplicates hence the Sudoku is valid.
        
        '''
        store=[]

        for i in range(9):
            for j in range(9):
                ele=board[i][j]
                if ele.isdigit():
                    store+=[(i,ele),(ele,j),(i//3,j//3,ele)] # [row check,column check,3x3 grid check]

        return len(store)==len(set(store)) # Check for possible duplicates.
