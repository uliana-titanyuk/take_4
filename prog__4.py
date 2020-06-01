def Sequence(filename):
    n = 0
    m = 0
    l = 0
    res = 0
    x = 0
  filename = 'data.dat' 
  try:
        f=open(filename, "r")
  except:
      print('cant open file')
        for (x in f for  [s5 for s1 in f for s2 in s1.split(' ') ): 
            try:
                if (l == 0):
                m=x
                l+=1
                elif(l == 1):
                n=x
                l+=1
            except:
                print('not enough numbers')
                elif(x in [min(m,n),max(n,m)]:
                res+=1
            return res
        f.close()