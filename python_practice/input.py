def add(number1, number2):
   
   return number1 + number2
enter_number = int(input("enter your specific number: "))
if enter_number is not int(input("enter your specific number: ")):
   print("input the valid number not letters")
print(add(enter_number, 4 ))
