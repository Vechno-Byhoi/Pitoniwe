
print("Lacit")

i = 0
while i<=5:
 print("0"*i)
 i+=1

print("*"' '"*"' '"*")
print(" ""*"" ""*"" ""*"" ""*")
print(" ""*"" ""*"" ""*"" ""*")
print(" ""*"" ""*")

print('-------------------------------------------------\n|\t4\t|\t9\t|\t2\t|\n\
-------------------------------------------------\n|\t3\t|\t5\t|\t7\t|\n\
-------------------------------------------------\n|\t8\t|\t1\t|\t6\t|\n\
-------------------------------------------------')

print(0.25+0.5)

from math import *

print((2+4*3)*(2-3*3)+2**2)

a = -2
print(fabs(a)+ a**5)

x = 1.7
print((x+1)**2 + 3*(x+1))

x = -2.34
print(((fabs(x-5)-sin(x))/3)+((((x**2+2014)**0.5))*cos(2*x))-3)

z = 3.6

print(exp(z-2)+fabs(sin(z))-(z**4*cos(1/z)))

a = 0.1
b = 0.2
q = 1

print(((q**2+b)**0.2)-((b**2*(sin(q+a)**3))/q))









d = dict(

[(n,'Zima')
for n in [12,0,1]]+
[(n,'Vesna')
for n in range(3,6)]+
[(n,'Leto')
for n in range(6,9)]+
[(n,'Osen')
for n in range(9,12)]



)



I = [2,-2,'a',43]
print(list(filter(lambda x:type(x)==int and x%2==0,I)))



Q = ['a',1,-2,1.2]
print(Q[::2])



l = ['a',1,-2,1.2]

print(list(filter(lambda x: (type(x) == int or type(x) == float) and x >= 0 , l)))


l = [1, 3, 4, 7, 9, 11]
m = 3

def f(lst, m):
 tmp, res = [], []
 for x in lst:
     rem = x % m
     for y in lst:
            if (y % m == rem):
             tmp.append(y)
     res.append(tmp[:])
     tmp.clear()

 for x in res:
     if x not in tmp:
         tmp.append(x)
 return tmp

print(f(l,m))







d = {1:2, 'a':3, -1:1, 3:'a'}
print(d)
def f(dic):
 sum = [0,0]
 for x in dic:
     if((type(dic.get(x)) == int or type(dic.get(x)) == float) and (type(x) == int or type(x) == float)):
            sum[0] += dic.get(x)
            sum[1] += x
 return sum

print(f(d))








d = [3, 4.1, 2]

def check(lst):
 l = []
 for x in lst:
     for y in lst: 
        if((type(x) == int or type(x) == float) and (type(y) == int or type(y) == float) and  x < y): l.append((x, y))        
 return l

print(check(d))







l = ['a',1,-2,1.2]

def f(lst):
 keys = lst[::2]
 val = lst[1::2]

 for x in val:
     d = dict.fromkeys(keys, x)

 return d

print(f(l))



