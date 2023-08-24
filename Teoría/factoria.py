n=int(input())

for i in range (1,n+1):
    f=f*i
    print(f)

def miFunción (n):
    if (n==1):
        return (1)
    else: f=n*miFunción(n-1)
    return(f)

print(miFunción(5))