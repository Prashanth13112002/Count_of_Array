class solutions:
    def countof_even(self,array,l,r):
        b=[]
        c=0
        for i in a:
            if i%2==0:
               c+=1
               b.append(c)
            else:
               b.append(c)
        for i in b:
            if l==0:
               return b[r]
            else:
               return b[r]-b[l-1]
a=list(map(int,input("ENTER THE ARRAY : ").split()))
q=int(input("ENTER THE Q : "))
b1=[]
for i in range (q):
    a1=solutions ()
    b=int(input("ENTER LEFT INDEX: "))
    c=int(input("ENTER RIGHT INDEX: "))
    b1.append(a1.countof_even(a,b,c))
print(b1)