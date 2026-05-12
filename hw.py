nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

def sq(n):
    return n * n

square = list(map(sq, nums))

even = []
odd = []

for i in square:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Square of numbers in this list")
print(square)

print("Even square numbers")
print(even)

print("Odd square numbers")
print(odd)