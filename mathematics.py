import math
# 1
degree = int(input("Input degree: "))
radian = math.radians(degree)
print(f"Output radian: {radian}")
#####################################################
# 2
height = float(input("Height "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
print(f"Expected Output: {(a+b)*height/2}")
#########################################################
# 3
N = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

my_digree = math.degrees(math.pi)
tan_of_angle = math.tan(my_digree/N)


S =  N*math.pow(a,2)/4/tan_of_angle
print(f"The area of the polygon is: {S}")
###################################################################
# 4
def my_parallelogram(a,h):
    x = float(a*h)
    return x
    pass


my_lengthy = int(input("Length of base: "))
my_heighty = int(input("Height of parallelogram: "))
my_parallelogram(my_lengthy, my_heighty)