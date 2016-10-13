# fibonacci python
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    e1 = 1
    e2 = 1
    print 0,
    for x in range(1,n+1):
        if x < 3:
            print 1,
        else:
            pom = e1+e2
            e1=e2
            e2=pom
            print e2,
    print "\n"
#print fib(100)
fib2(10)
fib2(9)
fib2(0)
