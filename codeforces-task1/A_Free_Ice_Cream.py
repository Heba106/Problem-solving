if __name__ == "__main__":
    n,x= list(map(int,input().split()))
    distress=0
    for i in range(n):
        sign ,d= list(input().split())
        d=int(d)
        if sign=='+':
            x+=d
        else:
            if x<d :
                distress+=1 
            else: 
                x=x-d
    print(x,distress)


