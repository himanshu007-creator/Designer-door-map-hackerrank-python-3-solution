def fun(p,q):
  x='.|.'
  a=int((p+1)/2-1)
  b=int((p+1)/2)
  c=int(p)
  
  for i in range(1,a+1):
    u=i+(i-1)
    v=x*u
    print(v.center(q,'-'))
  print('WELCOME'.center(q,'-'))
  
  for i in range(b+1,c+1):
    r=((p+1)/2)+1
    d=int(p-(2*(i-r+1)))
    e=d*x
    print(e.center(q,'-'))
x=list(i for i in input().split(' '))
n=int(x[0])
m=int(x[1])
fun(n,m)
