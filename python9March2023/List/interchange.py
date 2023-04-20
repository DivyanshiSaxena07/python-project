def change():
    n=[1,2,3,8]
    temp=n[0]
    n[0]=n[len(n)-1]
    n[len(n)-1]=temp

    print(n)
    
def swapList():
    n=[23, 65, 19, 90]
    pos1=int(input("ENter element u want to set"))
    pos2=int(input("ENter position u want to set"))
    # temp=n[pos1-1]
    # n[pos1-1]=n[pos2-1]
    # n[pos2-1]=temp
    print(n)
    
    # simple form
    n[pos2-1],n[pos1-1]=n[pos1-1],n[pos2-1]
    print(n)

# swapList()


def max():
    a,b=2,4
    if a>b:print(a,"is maximum")
    else: print(b,"is maximum")
# max()

def tupel():
    a=("apple","banana","mango","grapesS","cherry")
    print(a)
    print(a[:3])
    
    (b,c,d,*e)=a
    print(b)
    print(c)
    print(d)
    print(e)
    
tupel()