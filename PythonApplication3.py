numbers = input().split(" ")
number_set = set()

for number in numbers:
    print(number, end = " ")

    if number in number_set:
        print("YES")
    else:
        print("NO")

    number_set.add(number)