n = ""
while n == "":
    n = input("Enter size or arr : ")

n = int(n)

arr = []
for i in range(0, n):
    element = int(input(f"Enter the {i+1}th Element : "))
    arr.append(element)

newList = list(set(arr))
print(newList)