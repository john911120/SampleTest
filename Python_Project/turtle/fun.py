"""
a = 20

def func(b) :
    a = b
func(0)

print(a)

def add(a, b) :
    return a+b
print(add(add(2,2), 4))

def func(num, *args) :
    print(num)
    print(args)

func(2,4,6,8,10)

tup = (10, 30, 50, 70, 90)
print(tup[2])
for num in tup:
    print(num)

lst = [1, 3, 5, 7, 9]
def func(l):
    l[3] = 5

func(lst)
print(lst)

"""
def checkPrime(num):

    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, num) :
        if num%i == 0:
            return False
        return True


for num in range(1, 20001) :
    if checkPrime (num) :
        print(num)