guess = "the number is"

def  add(number1, number2):
    global guess

    return number1 + number2

# guess = "the sum is"
add_num = add(22, 23)
print(guess, add_num)

def string():
    str_int = int("334")
    g = str(str_int)
    g_type = type(g)
    print(g)
string()


def numbers(**numbers):
    return numbers
print(numbers())
numbers()