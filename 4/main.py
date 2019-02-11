for num in range(0, 13):
    print(num, end="\t")
print("\n")

for first in range(1, 13):
    print("{0}".format(first), end="\t")
    for second in range(1, 13):
        print("{0}".format(first * second), end="\t")
    print("\n")
