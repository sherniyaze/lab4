# 1 
def my_squares(N):
    for i in range(1,N+1):
        yield i**2

N = int(input())
for squared_num in my_squares(N):
    print(squared_num)

# 2
n = int(input())
def my_evens(n):
    for i in range(0,n+1):
        if i%2==0:
            yield str(i)

print(",".join(my_evens(n)))

# 3
number = int(input())
def divisible_for_3_4(number):
    for i in range(0,number+1):
        if i==0:
            continue
        elif (i%3==0 or i%4==0):
            yield i
for i in divisible_for_3_4(number):
    print(i)

def divisible_for_3_AND_4(number):
    for i in range(1,number+1,12):
        if (i%3==0 and i%4==0):
            yield i
for i in divisible_for_3_AND_4(number):
    print(i)

# 4
def again_my_lovely_squares(a,b):
    for i in range(a, b+1):
        yield i**2

first_endpoint = int(input())
second_endpoint = int(input())

for i in again_my_lovely_squares(first_endpoint,second_endpoint):
    print(i)

# 5
def oh_we_are_going_down(num):
    for i in range(0,num+1):
        yield num-i

numbik = int(input())
for i in oh_we_are_going_down(numbik):
    print(i)