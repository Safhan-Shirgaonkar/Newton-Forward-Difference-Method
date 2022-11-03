

'''NEWTON FORWARD DIFFERENCE'''

n=5   #value of number of Data points
print("The number of data points are", n)

#List Creating
m=[]
l=[]
s=[]
v=[]
w=[]
e=[]

#taking Values of x from user as input
i=0
for i in range(5):
    a=float(input("enter value of x{p} : ".format(p=i) ))
    i=i+1
    m.append(a)

#taking value of y from user as input  
i=0
for i in range(5):
    b=float(input("enter value of y{p}: ".format(p=i)))  
    i=i+1 
    l.append(b)

#value of X at which the value of function is to be calculated
X=float(input("enter value of Xy: "))
h=m[1]-m[0]
q=X-m[0]
u=q/h
print("The value of U is",u)

#value of deltaY
j=0
for j in range(4):
    deltaY= l[j+1]-l[j]
    j=j+1
    s.append(deltaY)
print("value of deltay is",s)

#calculating value of deltasquareY
k=0
for k in range(3):
    deltasquareY=s[k+1]-s[k]
    k=k+1
    v.append(deltasquareY)
print("value of deltasquarey is",v)

#calculating value of deltacubey
z=0
for z in range(2):
    deltacubeY=v[z+1]-v[z]
    z=z+1
    w.append(deltacubeY)
print("value of deltacubey is", w)

#calculating value of deltaquady
c=0
for c in range(1):
    deltaquady=w[c+1]-w[c]
    e.append(deltaquady)
print("value of deltaquady is",e)


first=u*(u-1)/2
second=u*(u-1)*(u-2)/6
third=u*(u-1)*(u-2)*(u-3)/24

#calculating value of y at  point X
y=l[0]+u*s[0]+first*v[0]+second*w[0]+third*e[0]

print("The value of y at X=",X ,"is", y)   #Final solution  






    









 


