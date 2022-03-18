'''
    https://codeforces.com/contest/152/problem/B
'''
import sys
n,m = list(map(int,input().split()))
x,y = list(map(int,input().split()))

k=int(input())
totalSteps=0
for i in range (k):
    steps=sys.maxsize
    dx,dy = list(map(int,input().split()))
    if dx>0:
        steps=int(min(steps,(n-x)/dx))
    if dx<0:
        steps=int(min(steps,((x-1)/-dx)))
    if dy>0:
        steps=int(min(steps,(m-y)/dy))
    if dy<0:
        steps=int(min(steps,((y-1)/-dy)))
    x+=dx*steps 
    y+=dy*steps
    totalSteps+=steps
print (totalSteps)
