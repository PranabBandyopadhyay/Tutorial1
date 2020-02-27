import random

def array(p):
    q=[]
    for i in range(1, p):
        q.append(random.randint(1,99))
    return q

x=array(random.randint(1,99))
y=array(random.randint(1,99))
c=[]

print(x)
print(y)

for i in x:
    if i in y:
        if i not in c:
            c.append(i)


print(c)