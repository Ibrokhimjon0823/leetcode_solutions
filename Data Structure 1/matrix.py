class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        a = []
        for i in mat:
            for j in i:
                a.append(j)
        res = [[0 for i in range(c)] for j in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = a[k]
                k += 1
                
        return res
    
   