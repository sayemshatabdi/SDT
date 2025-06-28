size=input()
nums=list()
for x in input().split():
    nums.append(int(x))

# flag=True
# for num in nums:
#     if num%2 !=0:
#         flag=False
#         break

# count=0

# if flag:
#     print(0)
# else:
#     while True:
#        diveded = [num for num in nums if num % 2 == 0]
#        count+=1
#        for nums in diveded:
#            if( nums % 2 != 0):
#                break
#         nums = diveded

count = 0

while True:
    # check if all numbers are even
    all_even = True

    for num in nums:
        if num % 2 != 0:
            all_even = False
            break

    if not all_even:
        break
    
    # divide every number by 2
    nums = [num / 2 for num in nums]
    count += 1

print(count)