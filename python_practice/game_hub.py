# input_list = ["Minecraft", "Roblox", "Minecraft", "FIFA", "Roblox", "Fortnite"]
# convert = set(input_list)
# print(convert)
# clean_libery = list(convert)
# print(clean_libery)

# available_games = "Witcher 3", "Cyberpunk", "GTA V"
# user_game = input("enter your game: ")
# if user_game not in available_games:
#     print("Invalid movie")
# else:
#     print("correct option the film you are looking for it here")

player1_team = {"Halo", "Apex", "Minecraft", "FIFA"}
player2_team = {"Minecraft", "COD", "FIFA", "Zelda"}
mutual_game = player1_team & player2_team
print("they can play together", mutual_game)