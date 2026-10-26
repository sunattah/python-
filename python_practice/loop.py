# number = int(input("input the number:  " ))
# while number > 40:
#     # for i in number:
#     #     print(i)
#     if number == 30:
#         print("number is 30")


# # else:
# #     print("Number complete")

FRUITS = ["orange", "guava, banana, mango pineapple"]
for fruit in FRUITS:
    if fruit[2] == "banana":
        print("banana is present")
    elif fruit[1] == "guava":
        fruit.replace("banana", "cashew")
        print(fruit)
    else:
        print("fruits are intant")
        break

