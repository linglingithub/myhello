class Solution:
    # @return a string
    def count(self,s):
        t=''; count=0; curr='#'
        for i in s:
            if i!=curr:
                if curr!='#':
                    t+=str(count)+curr
                curr=i
                count=1
            else:
                count+=1
        t+=str(count)+curr
        return t
    def countAndSay(self, n):
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s

if __name__ == "__main__":
    mps = Solution()
    for i in range(0,10):
        print "[",i,"]",mps.countAndSay(i)
