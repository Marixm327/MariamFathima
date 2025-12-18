a = int(input("Enter a number: "))
#The main logic is printing all odd numbers till a if a is an odd number and till a-1 if a is an even number
output = a if a % 2 != 0 else a - 1 
result = []

for i in range(1, output + 1, 2):
    result.append(i)

print(", ".join(map(str, result)))
