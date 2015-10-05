# class way

def leb(term):
    sum=0
    for i in range(0,term+1):
        sum=sum+((1.0/2i+1)*(-1)**i)
    return 4*sum


print leb(3)