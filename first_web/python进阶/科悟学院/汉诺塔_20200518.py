
def hanio(n,a,b,c):
    if n >0:
        hanio(n-1,a,c,b)
        print(f"{a}移动到{c}")
        hanio(n-1,b,a,c)


hanio(3,"A","B","C")