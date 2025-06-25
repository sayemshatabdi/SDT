# def sum(num1,num2,num3=0,num4=0,num5=0):
#     return num1 + num2 + num3 + num4 + num5

# total=sum(1,2)
# print(total)
# total=sum(1,2,3)
# print(total)
# total=sum(1,2,3,4)
# print(total)

# args

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

