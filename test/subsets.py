import datetime

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    
    def subsets(self, S):
        def dfs(depth, start, valuelist):
            print "===" * (depth), "DFS ===>: ", depth, start, valuelist
            res.append(valuelist)
            #print "==="*(depth), "update res: ", res
            if depth == len(S): return
            for i in range(start, len(S)):
                #print "===" * (depth), "Loop: ", i, start, len(S)

                dfs(depth+1, i+1, valuelist+[S[i]])
                #print "==="*(depth+1), "DFS <===: ", depth+1, i+1, valuelist+[S[i]]
        S.sort()
        res = []
        dfs(0, 0, [])
        return res



    def subsets1(self, S):
        """
        LL version
        """

        def dfs1(depth, start, valuelist):
            print "===" * (depth), "DFS ===>: ", depth, start, valuelist
            if depth == len(S):
                res.append(valuelist)
                return
            if start < len(S):
                dfs1(depth+1,start+1,valuelist+[S[start]])
                dfs1(depth+1,start+1,valuelist)

        S.sort()
        res = []
        dfs1(0, 0, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    li = [1,2,3,4]
    t1 = datetime.datetime.now()
    a = sol.subsets(li)
    t2 = datetime.datetime.now()
    print "=================================="
    t3 = datetime.datetime.now()
    b = sol.subsets1(li)
    t4 = datetime.datetime.now()
    print "=================================="
    print a
    print len(a), t2-t1
    print "=================================="
    print b
    print len(b), t4-t3