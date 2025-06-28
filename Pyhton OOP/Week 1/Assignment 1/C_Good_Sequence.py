size=int(input())
nums=list()

for x in input().split():
    nums.append(int(x))

# dic={item:nums.count(item) for item in nums}

# result=0

# for key,value in dic.items():
#     if(key>value):
#         result+=value
#     else:           
#         result+=value-key
    

# print(result)
freq = dict()
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

result = 0
for num, count in freq.items():
    if num > count:
        result += count
    else:
        result += count - num

print(result)

