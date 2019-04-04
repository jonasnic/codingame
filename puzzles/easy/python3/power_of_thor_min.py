X,Y,x,y=map(int,input().split())
while 1:
 d=""
 if y>Y:d+="N";y-=1
 if y<Y:d+="S";y+=1
 if x>X:d+="W";x-=1
 if x<X:d+="E";x+=1
 print(d)
