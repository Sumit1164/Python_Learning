def patt(n):
    if (n ==0):
        return ""
    print("*"*n)
    patt(n-1)

patt(3)