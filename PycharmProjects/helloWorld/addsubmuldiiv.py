def cal(*x):
    #addition
   return x[0]+x[1]+x[2]

def sub(x, y):
    #substraction
    c=x-y
    return c

def mul(x, y):
    #multiplication
    c=x*y
    return c

def div(x, y):
    #division
    c=x/y
    return c

def main():
    a=10
    b=5
    c=20

    c=cal(a,b,c)
    d=sub(a,b)
    e=mul(a,b)
    f=div(a,b)

    print(" sum: {0}\n sub: {1}\n mul: {2}\n div: {3}".format(c,d,e,f))

if __name__ == '__main__':
    main()