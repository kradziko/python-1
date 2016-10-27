def NWD(a,b):
    while(a!=b):
        if a > b:
            a-=b
        else:
            b-=a
    return a

def NWW(a,b):
    return a*b / NWD(a,b)

print NWD(1,3)
print NWW(4,5)