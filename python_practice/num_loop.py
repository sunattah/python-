'''
number =  [9,0,8,7,6,6,5,2,5,1]
print(sorted(number))

balance = 5000
print("balance before withdrawal", balance)
after_withdrawal = balance - 1000
print("after withdrawal", after_withdrawal)
for num in [1,2,4,5,6,78,9]:
    print(num)
'''
def know():
    y = "positive"
    x = "Negative"
    user_number = int(input("enter a number: ")) 
    if user_number < 0:
        print(f"The number is {x}, it should be {y}")
    elif user_number > 0:
        print("The number is positive")
    else:
        print("The number is zero")
know()

def loop():
     market_list = ["apple", "creyfish", "yam", "potatoes", "fish", "meat"]
     for main_thing in market_list:
         favorite = main_thing
         if favorite == main_thing.split():
             print("It is splited")
loop()