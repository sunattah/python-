my_list = ("student", "teachers", "staffs", "gateman", "security", "field keeper")
my_set = set(my_list)
my_listy = list(my_set)
print(sorted(my_listy))
print(my_listy)
print(my_set)

player1_library = {"Halo", "Apex", "Minecraft", "FIFA"}
player2_library = {"Minecraft", "COD", "FIFA", "Zelda"}

gift_ideas = player2_library - player1_library 

print("Great gift ideas for Player 1:", gift_ideas)


borrow_ideas = player1_library - player2_library

print("Games Player 2 could borrow:", borrow_ideas)
