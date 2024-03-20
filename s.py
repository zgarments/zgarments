N = int(input()) # input 4
str = input()  # input 1010
substr = str * 2 
distinct_rotations = set()
for i in range(len(str)):
    rotation = substr[i:i+N]
    distinct_rotations.add(rotation)
    
print(len(distinct_rotations)) #output 2