class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def get_neighbors(r, c):
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, -1, 0, 1]
            for i in range(len(delta_row)):
                row = r + delta_row[i]
                col = c + delta_col[i]
                if row in range(ROWS) and col in range(COLS):
                    yield (row, col)
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
               heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            for neighbor in get_neighbors(r, c):
                r_neighbor, c_neighbor = neighbor
                dfs(r_neighbor, c_neighbor, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

testcase = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,18],
[63,120,121,122,123,124,125,126,127,128,129,130,131,132,133,80,19],
[62,119,168,169,170,171,172,173,174,175,176,177,178,179,134,81,20],
[61,118,167,208,209,210,211,212,213,214,215,216,217,180,135,82,21],
[60,117,166,207,240,241,242,243,244,245,246,247,218,181,136,83,22],
[59,116,165,206,239,264,265,266,267,268,269,248,219,182,137,84,23],
[58,115,164,205,238,263,280,281,282,283,270,249,220,183,138,85,24],
[57,114,163,204,237,262,279,288,289,284,271,250,221,184,139,86,25],
[56,113,162,203,236,261,278,287,286,285,272,251,222,185,140,87,26],[
    55,112,161,202,235,260,277,276,275,274,273,252,223,186,141,88,27],
    [54,111,160,201,234,259,258,257,256,255,254,253,224,187,142,89,28],
    [53,110,159,200,233,232,231,230,229,228,227,226,225,188,143,90,29],
    [52,109,158,199,198,197,196,195,194,193,192,191,190,189,144,91,30],
    [51,108,157,156,155,154,153,152,151,150,149,148,147,146,145,92,31],
    [50,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,32],
    [49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33]]
