__author__ = 'shankar'

# simple dynamic programming - a,b - print a,b - swap - b,a
def getPermutations(a,k=0):
   if(k==len(a)):
      print ''.join(a)
   else:
      for i in xrange(k,len(a)):
         a[k],a[i] = a[i],a[k]
         getPermutations(a, k+1)
         a[k],a[i] = a[i],a[k]

if __name__ == "__main__":
    t = raw_input("Enter text for getting permutations out: ")
    getPermutations([s for s in t])


