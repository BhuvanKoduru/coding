def fun(l,string,o,c,n):
    if(o==n and c==n):
        l.append(string)
        return
    else:
        if(o<n):
            fun(l,string+'(',o+1,c,n)


        if(c<o):
            fun(l,string+')',o,c+1,n)
class Solution:
    def AllParenthesis(self,n):
        #code here
        ans=[]
        fun(ans,"",0,0,n)
        return list(set(ans))
